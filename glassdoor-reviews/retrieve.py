'''Scrapes reviews data from Glassdoor and imports it into MongoDB'''
from bs4 import BeautifulSoup
import csv
import datetime
from datetime import date
from datetime import timedelta
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium.webdriver.chrome.options import Options

import urls

ALL_LINKS = urls.links
# dictionary of month abbreviations and corresponding month numbers
MONTHS = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
SORT = '.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng&filter.employmentStatus=REGULAR'

# request users MongoDB database credentials
def GetCredentials():
    username = input("Enter your MongoDB Database username:").strip()
    password = input("Enter your MongoDB Database password:").strip()
    print("Does this look right?")
    print(f"username: {username}, password: {password}")
    confirm = input("y/n:")
    if confirm.lower() == "y":
        return username, password
    else:
        return GetCredentials()

# request which collection the user would like to import the data into
def GetTargetCollection():
    print("Would you like to import the data into the Test collection (TEST)")
    print("Or import the data into the intended collection? (REAL)")
    target = input("TEST/REAL:").strip()
    if target.lower() == "test":
        return True
    elif target.lower() == "real":
        return False
    else:
        return GetTargetCollection()

# attempt to navigate to link with webdriver
def TryGetLink(driver, link):
    try:
        driver.get(link)
    except:
        try:
            driver.get(link)
        except:
            time.sleep(1)
            try:
                driver.get(link)
            except:
                time.sleep(3)
                try:
                    driver.get(link)
                except:
                    time.sleep(5)
                    try:
                        driver.get(link)
                    except:
                        print("Failed to get link 5 times, moving on...")
    return driver

# gets the reviews for the given company
def GetData(driver, reviews_link, company, yesterday):
    link = reviews_link + ".htm"
    driver = TryGetLink(driver, link)

    pros = ['''''']
    cons = ['''''']
    all_data = []
    i = 0
    while i < 10000:
        i += 1

        link = f'{reviews_link}_P{i}{SORT}'
        driver = TryGetLink(driver, link)
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        outer_box = soup.find('div', {'id': 'ReviewsRef'})
        success = False
        while not success:
            try:
                reviews = outer_box.find_all('div', {'class': 'gdReview'})
                success = True
            except:
                print("Waiting a couple of seconds to try again")
                time.sleep(2.5)
                driver = TryGetLink(driver, link)       
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                outer_box = soup.find('div', {'id': 'ReviewsRef'})

        if len(reviews) == 0:
            i = 99999
        for review in reviews:
            rating = review.find('span', {'class': 'ratingNumber mr-xsm'}).text
            info = review.find('div', {'class': 'mx-0'})
            author = info.find('span', {'class': 'common__EiReviewDetailsStyle__newUiJobLine'}).text
            author = author.split(" - ")

            date = author[0].split(" ")
            month = int(MONTHS[date[0].replace(",", "").replace(" ", "")])
            if month < 4:
                quarter = 1
            elif month < 7:
                quarter = 2
            elif month < 10:
                quarter = 3
            else:
                quarter = 4

            day = int(date[1].replace(",", "").replace(" ", ""))
            year = int(date[2].replace(",", "").replace(" ", ""))
            if year >= 2010:
                converted_date = datetime.date(year, month, day)
                if yesterday == "" or str(converted_date) == yesterday:
                    job = author[1].replace("\n", "").strip()

                    pro = review.find('span', {'data-test': 'pros'}).text
                    pro = pro.strip().replace("\n", " ").splitlines()
                    pro = ''.join(pro)
                    pros[0] = pros[0] + " " + pro

                    con = review.find('span', {'data-test': 'cons'}).text
                    con = con.strip().replace("\n", " ").splitlines()
                    con = ''.join(con)
                    cons[0] = cons[0] + " " + con
                    
                    data = {
                        'company': str(company),
                        'date': converted_date,
                        'year': int(year),
                        'quarter': int(quarter),
                        'jobTitle': str(job),
                        'rating': int(float(rating)),
                        'proReview': str(pro),
                        'conReview': str(con),
                    }
                    all_data.append(data)
                else:
                    i = 99999
            else:
                i = 99999

    fields = ['company', 'date', 'year', 'quarter', 'jobTitle', 'rating',
        'proReview', 'conReview']
    with open(f'{company}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)
        print(company + " reviews finished!")

# scrapes all companies tracked
def GetAllCompanies(yesterday):
    # initiate driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    link = 'https://www.glassdoor.com/member/home/index.htm'
    driver = TryGetLink(driver, link)
    time.sleep(10)

    username = driver.find_element(By.XPATH , "//input[@name='username']")
    username.send_keys('georgeomalley42069@gmail.com')
    time.sleep(2)

    submit = driver.find_element(By.XPATH , "//button[@type='submit']").click()
    time.sleep(10)

    password = driver.find_element(By.XPATH , "//input[@name='password']")
    password.send_keys('Georgina12345!')
    time.sleep(2)

    submit = driver.find_element(By.XPATH , "//button[@type='submit']").click()
    time.sleep(10)

    # login = input("Login to Glassdoor... Input 'y' once completed:")
    # while login.lower() != 'y':
    #     login = input("Login to Glassdoor... Input 'y' once completed:")

    for comp in ALL_LINKS:
        GetData(driver, ALL_LINKS[comp], comp, yesterday)
    driver.quit()

# writes the data taken from Glassdoor into a CSV file
def WriteData():
    all_data = []
    for comp in ALL_LINKS:
        csvfile = f'{comp}.csv'
        df = pd.read_csv(csvfile)
        for i in range(len(df)):
            stat = {
                'company': str(df.iloc[i][0]),
                'date': df.iloc[i][1],
                'year': int(df.iloc[i][2]),
                'quarter': int(df.iloc[i][3]),
                'jobTitle': str(df.iloc[i][4]),
                'rating': int(df.iloc[i][5]),
                'proReview': str(df.iloc[i][6]),
                'conReview': str(df.iloc[i][7]),
            }
            all_data.append(stat)
        
        os.system(f'rm "{csvfile}"')

    fields = ['company', 'date', 'year', 'quarter', 'jobTitle', 'rating',
        'proReview', 'conReview']
    with open('all.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# returns the job category for the given reviewer
def GetJobCategory(job):
    if 'intern' in job and 'internal' not in job:
        job_category = 'Intern'
    elif 'sales' in job or 'account' in job or 'business' in job:
        job_category = 'Sales'
    elif 'marketing' in job:
        job_category = 'Marketing'
    elif 'engineer' in job or 'software' in job or 'develop' in job:
        job_category = 'Engineer'
    elif 'customer' in job:
        job_category = 'Customer Support'
    elif 'product' in job or 'program' in job:
        job_category = 'Product'
    elif 'data' in job or 'tech' in job:
        job_category = 'Information Systems'
    else:
        job_category = 'Other'

    return job_category

# generates a csv file with all sentiment and reviews statistics
def GenerateFullCSV(csvfile):
    df = pd.read_csv(csvfile)
    all_reviews = []
    analyzer = SentimentIntensityAnalyzer()
    for i in range(len(df)):
        pro = str(df.iloc[i][6])
        pro_vs = analyzer.polarity_scores(pro)
        con = str(df.iloc[i][7])
        con_vs = analyzer.polarity_scores(con)

        pro_neg = pro_vs['neg']
        pro_neu = pro_vs['neu']
        pro_pos = pro_vs['pos']
        pro_comp = pro_vs['compound']

        con_neg = con_vs['neg']
        con_neu = con_vs['neu']
        con_pos = con_vs['pos']
        con_comp = con_vs['compound']

        pro_str = pro.lower().replace("â€™", "'")
        if 'manage' in pro_str or 'leader' in pro_str or 'boss' in pro_str:
            pro_management = 1
        else:
            pro_management = 0
        if ('compensation' in pro_str or 'pay' in pro_str or 'salary' in pro_str
                or 'benefits' in pro_str):
            pro_compensation = 1
        else:
            pro_compensation = 0
        if ('cultur' in pro_str or 'balance' in pro_str or 'values' in pro_str
                or 'environment' in pro_str or 'mission' in pro_str or
                'wlb' in pro_str):
            pro_culture = 1
        else:
            pro_culture = 0
        if ('product' in pro_str or 'service' in pro_str or
                'offering' in pro_str):
            pro_product = 1
        else:
            pro_product = 0
        if ('competit' in pro_str or 'outlook' in pro_str or
                'positioning' in pro_str or 'market' in pro_str):
            pro_outlook = 1
        else:
            pro_outlook = 0
        if 'divers' in pro_str or 'inclus' in pro_str:
            pro_diversity = 1
        else:
            pro_diversity = 0
        if ('career' in pro_str or 'opportunit' in pro_str or
                'progression' in pro_str or 'learn' in pro_str):
            pro_opportunity = 1
        else:
            pro_opportunity = 0

        con_str = con.lower().replace("â€™", "'")
        if 'manage' in con_str or 'leader' in con_str or 'boss' in con_str:
            con_management = 1
        else:
            con_management = 0
        if ('compensation' in con_str or 'pay' in con_str or 'salary' in con_str
                or 'benefits' in con_str):
            con_compensation = 1
        else:
            con_compensation = 0
        if ('cultur' in con_str or 'balance' in con_str or 'values' in con_str
                or 'environment' in con_str or 'mission' in con_str or
                'wlb' in con_str):
            con_culture = 1
        else:
            con_culture = 0
        if ('product' in con_str or 'service' in con_str or
                'offering' in con_str):
            con_product = 1
        else:
            con_product = 0
        if ('competit' in con_str or 'outlook' in con_str or
                'positioning' in con_str or 'market' in con_str):
            con_outlook = 1
        else:
            con_outlook = 0
        if 'divers' in con_str or 'inclus' in con_str:
            con_diversity = 1
        else:
            con_diversity = 0
        if ('career' in con_str or 'opportunit' in con_str or
                'progression' in con_str or 'learn' in con_str):
            con_opportunity = 1
        else:
            con_opportunity = 0

        job = str(df.iloc[i][4]).lower()
        job_category = GetJobCategory(job)

        point = {
            'company': str(df.iloc[i][0]),
            'date': df.iloc[i][1],
            'year': int(df.iloc[i][2]),
            'quarter': int(df.iloc[i][3]),
            'jobTitle': str(df.iloc[i][4]),
            'jobCategory': str(job_category),
            'rating': int(df.iloc[i][5]),
            'proReview': str(df.iloc[i][6]).replace("â€™", "'"),
            'conReview': str(df.iloc[i][7]).replace("â€™", "'"),
            'proNegSentiment': float(pro_neg),
            'proNeuSentiment': float(pro_neu),
            'proPosSentiment': float(pro_pos),
            'proCompoundSentiment': float(pro_comp),
            'conNegSentiment': float(con_neg),
            'conNeuSentiment': float(con_neu),
            'conPosSentiment': float(con_pos),
            'conCompoundSentiment': float(con_comp),
            'proManagement': int(pro_management),
            'proCompensation': int(pro_compensation),
            'proCulture': int(pro_culture),
            'proProduct': int(pro_product),
            'proOutlook': int(pro_outlook),
            'proDiversity': int(pro_diversity),
            'proOpportunity': int(pro_opportunity),
            'conManagement': int(con_management),
            'conCompensation': int(con_compensation),
            'conCulture': int(con_culture),
            'conProduct': int(con_product),
            'conOutlook': int(con_outlook),
            'conDiversity': int(con_diversity),
            'conOpportunity': int(con_opportunity)
        }
        all_reviews.append(point)

    fields = ['date', 'year', 'quarter', 'company', 'jobTitle', 'jobCategory',
        'rating', 'proReview', 'conReview', 'proNegSentiment',
        'proNeuSentiment', 'proPosSentiment', 'proCompoundSentiment',
        'conNegSentiment', 'conNeuSentiment', 'conPosSentiment',
        'conCompoundSentiment', 'proManagement', 'proCompensation',
        'proCulture', 'proProduct', 'proOutlook', 'proDiversity',
        'proOpportunity', 'conManagement', 'conCompensation', 'conCulture',
        'conProduct', 'conOutlook', 'conDiversity', 'conOpportunity']

    with open(f'full.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_reviews)

# runs the scripts to scrape Glassdoor, analyze the reviews, and import the data
def Automate(yesterday):
    GetAllCompanies(yesterday)
    WriteData()
    GenerateFullCSV('all.csv')

    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: Glassdoor, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Glassdoor --collection Test --type csv --file full.csv --headerline')
    else:
        print("Importing data into database: Glassdoor, collection: Reviews")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Glassdoor --collection Reviews --type csv --file full.csv --headerline')
    
    SendEmail()

def SendEmail():
    df = pd.read_csv("full.csv")
    df = df[["company", "rating", "conReview"]]
    df = df[df["rating"]<=2]
    html = df.to_html(justify = "left", index=False, border = 1)
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.table
    table["style"] = "border: 1px solid black; border-collapse: collapse;"

    tags = ["th","td"]
    for tag in soup.find_all(tags):
        tag["style"] = "padding: 5px 5px 5px 5px;"

    if len(df) != 0:
        final = str(soup.prettify())
        text = "Hello! <br> Below are the negative Glassdoor reviews from yesterday: <br><br>"
        body = text + final
    else:
        body = "Hello! There were no negative Glassdoor reviews from yesterday."

    email_sender = "ksg7699@nyu.edu"
    email_receiver = ["twestcott@jsoros.com", "jlobel@jsoros.com", "ksehgal@jsoros.com", "kgill@jsoros.com"]
    email_password = "zovrtywzgxvxpkqb"

    yesterday = date.today() - timedelta(days = 1)
    formatted_date = date.strftime(yesterday, "%m/%d/%Y")
    subject = "Glassdoor Reviews " + formatted_date

    em = MIMEMultipart('alternative')
    em['From'] = email_sender
    em['To'] = ", ".join(email_receiver)
    em['Subject'] = subject

    em.attach(MIMEText(body, 'html'))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        for receiver in email_receiver:
            smtp.sendmail(email_sender, receiver, em.as_string())

    os.system('rm full.csv')
    os.system('rm all.csv')     

yesterday = str(date.today() - timedelta(days = 1))
Automate(yesterday)