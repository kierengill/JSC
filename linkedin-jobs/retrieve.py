'''Scrapes company data from LinkedIn and imports it into MongoDB'''

from bs4 import BeautifulSoup
import csv
import datetime
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import companies

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

# returns the number of job postings from company's LinkedIn page
def GetNumJobPostings(soup):
    try:
        job_board = soup.find('p', {'class': 't-18 pt2'})
        if job_board != None:
            no_jobs = job_board.text.strip().replace(' ', '').lower()

        if (job_board != None) and (no_jobs == 'therearenojobsrightnow.'):
            num_job_postings = 0
        else:
            postings_info = soup.find('h4', {'class': 'org-jobs-job-search-form-module__headline'})

            num_job_postings = postings_info.text.strip()
            num_job_postings = num_job_postings.split('has ')[1]
            num_job_postings = num_job_postings.split(' ')[0]
            num_job_postings = num_job_postings.replace(',', '')
        return num_job_postings
    except:
         return None

# returns the number of employees from company's LinkedIn page
def GetNumEmployees(soup):
    try:
        employees_info = soup.find('span', {'class': 't-normal t-black--light link-without-visited-state link-without-hover-state'})
        # employees_info = soup.find('span', {'class': 'org-top-card-secondary-content__see-all t-normal t-black--light link-without-visited-state link-without-hover-state'})
        employees_info_2 = soup.find('span', {'class': 'link-without-visited-state t-bold t-black--light'})
        if employees_info != None:
            num_employees = employees_info.text.strip()
            num_employees = num_employees.split(' ')
            if len(num_employees) == 2:
                num_employees = num_employees[0]
            elif len(num_employees) == 6:
                num_employees = num_employees[2]
            num_employees = num_employees.replace(',', '')
        elif employees_info_2 != None:
            num_employees = employees_info_2.text.strip()
            num_employees = num_employees.split(' ')
            if len(num_employees) == 2:
                num_employees = num_employees[0]
            elif len(num_employees) == 6:
                num_employees = num_employees[2]
            num_employees = num_employees.replace(',', '')
        else:
            print("possible error")
            num_employees = 0
        print(num_employees)
        return num_employees
    except:
        return None

# returns the number of followers from company's LinkedIn page
def GetNumFollowers(soup):
    try:
        followers_info = soup.find_all('div', {'class': 'org-top-card-summary-info-list__info-item'})[-1]
        num_followers = followers_info.text.strip().split(' ')[0]
        num_followers = num_followers.replace(',', '')
        return num_followers
    except:
        return None

# returns company's stats to be appended to the list of all companies
def GetCompanyStats(driver, soup, company, category):
    num_job_postings = GetNumJobPostings(soup)
    if num_job_postings == None:
        print("Trying again")
        time.sleep(3)
    
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        num_job_postings = GetNumJobPostings(soup)

    num_employees = GetNumEmployees(soup)
    if num_employees == None:
        print("Trying again")
        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        num_employees = GetNumEmployees(soup)
        
    num_followers = GetNumFollowers(soup)
    if num_followers == None:
        print("Trying again")
        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        num_followers = GetNumFollowers(soup)

    company_entry = {
        'company': str(company),
        'category': str(category),
        'numJobPostings': int(num_job_postings),
        'numEmployees': int(num_employees),
        'numFollowers': int(num_followers),
        'date': datetime.date.today()
    }
    
    return company_entry

# scrapes all companies tracked and imports the data into MongoDB
def RunScript():
    # initiate driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    link = "https://www.linkedin.com/"

    driver.get(link)
    time.sleep(10)

    username = driver.find_element(By.XPATH , "//input[@name='session_key']")
    password = driver.find_element(By.XPATH , "//input[@name='session_password']")

    username.send_keys('georgeomalley42069@gmail.com')
    password.send_keys('Georgina12345!')
    time.sleep(2)

    submit = driver.find_element(By.XPATH , "//button[@type='submit']").click()
    time.sleep(10)

    confirm = input("Press Enter after confirming code:")
    
    company_list = []
    for category in companies.category_list:
        for company in companies.category_list[category]:
            myUrl = (f'https://www.linkedin.com/company/{companies.category_list[category][company]}/jobs/')
            try:
                driver.get(myUrl)

                time.sleep(random.uniform(1.5, 2.5))

                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                company_entry = GetCompanyStats(driver, soup, company, category)
                company_list.append(company_entry)
            except:
                print(f"Trying {company} again")
                time.sleep(3)

                driver.get(myUrl)
                time.sleep(3)

                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                company_entry = GetCompanyStats(driver, soup, company, category)
                company_list.append(company_entry)

    fields = ['company', 'category', 'numJobPostings', 'numEmployees',
        'numFollowers', 'date']
    
    with open('jobs.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(company_list)
        
    driver.quit()

    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: LinkedIn-Jobs, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/LinkedIn-Jobs --collection Test --type csv --file jobs.csv --headerline')
    else:
        print("Importing data into database: LinkedIn-Jobs, collection: Companies")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/LinkedIn-Jobs --collection Companies --type csv --file jobs.csv --headerline')
    os.system('rm jobs.csv')


RunScript()