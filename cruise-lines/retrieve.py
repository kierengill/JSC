'''Runs the scripts to retrieve and import cruise line pricing data'''

from bs4 import BeautifulSoup
import sys
import csv
import datetime
import os
import requests
import threading
import time
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib
import links

CRUISE_LINES_DICT = links.cruise_lines_dict
CRUISE_LINES_LINKS = links.cruise_line_links
CRUISE_LINES_LIST = links.cruise_lines_list

# dictionary of month abbreviations and corresponding month numbers
MONTHS = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

# return html data ready to be parsed
def GetPageHTML(url):
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    #r = requests.get(url, headers=req_headers)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

# request users MongoDB database credentials
def GetCredentials():
    #username = input("Enter your MongoDB Database username:").strip()
    #password = input("Enter your MongoDB Database username:").strip()
    username = sys.argv[2]
    password = sys.argv[3]
    print("Does this look right?")
    print(f"username: {username}, password: {password}")
    #confirm = input("y/n:")
    confirm = sys.argv[4]
    if confirm.lower() == "y":
        return username, password
    else:
        return GetCredentials()

# request which collection the user would like to import the data into
def GetTargetCollection():
    print("Would you like to import the data into the Test collection (TEST)")
    print("Or import the data into the intended collection? (REAL)")
    #target = input("TEST/REAL:").strip()
    target = sys.argv[1]
    if target.lower() == "test":
        return True
    elif target.lower() == "real":
        return False
    else:
        return GetTargetCollection()

# get ship data for the given listing 
def GetShipData(listings, j):
    title = listings[j].find('h2', {'class': 'heading-sm heading-secondary card-title'})
    title = title.text.strip()
    ship_name = listings[j].find('span', {'title': "Ship's name"})
    ship_name = ship_name.text.strip()

    rating = listings[j].find('div', {'class': 'search-result rating-result d-flex'})
    try:
        rating = float(rating.text.strip()[:3].strip())
        opinion = listings[j].find('div', {'class': 'search-result rating-result d-flex'})
        opinion = opinion.text.strip()[3:].strip().replace('"', "")
    except:
        opinion = rating.text.strip()[:3].strip()
        if 'ok' in opinion.lower():
            opinion = 'Ok'
        rating = None
    dates_container = listings[j].find('div', {'class': 'tabs'})
    dates = dates_container.find('p', {'class': 'small-label'})
    dates = dates.text.strip().split("-")

    start_date = dates[0].replace("\n", "").replace("\xa0", "")
    start_date = start_date.replace("SAIL DATE:", "").strip()
    day = int(start_date.split(" ")[1].split(",")[0])
    month = int(MONTHS[start_date.split(" ")[0]])
    year = int(start_date.split(" ")[2][0:4])
    start_date = datetime.date(year, month, day)

    end_date = dates[1].replace("\n", "").replace("\xa0", "")
    end_date = end_date.replace("SAIL DATE:", "").strip().split("$")[0]
    end_date = end_date.replace("Interior", "")
    day = int(end_date.split(" ")[1].split(",")[0])
    month = int(MONTHS[end_date.split(" ")[0]])
    year = int(end_date.split(" ")[2][0:4])
    end_date = datetime.date(year, month, day)

    ship_data = [title, ship_name, rating, opinion, start_date, end_date]
    return ship_data

# get price data for the given listing
def GetPriceData(listings, j):
    prices = listings[j].find_all('div', {'class': 'block-price'})
    for price in prices:
        price_level = price.find('h4', {'class': 'small-label'}).text
        price_level = price_level.lower().strip()
        if price_level == 'interior':
            try:
                interior_price = price.find('span', {'class': 'price'})
                interior_price = interior_price.text
                interior_cost = price.find('span', {'class': 'cost'})
                interior_cost = interior_cost.text
            except:
                interior_price = None
                interior_cost = None
        elif price_level == 'oceanview':
            try:
                oceanview_price = price.find('span', {'class': 'price'})
                oceanview_price = oceanview_price.text
                oceanview_cost = price.find('span', {'class': 'cost'})
                oceanview_cost = oceanview_cost.text
            except:
                oceanview_price = None
                oceanview_cost = None
        elif price_level == 'balcony':
            try:
                balcony_price = price.find('span', {'class': 'price'})
                balcony_price = balcony_price.text
                balcony_cost = price.find('span', {'class': 'cost'})
                balcony_cost = balcony_cost.text
            except:
                balcony_price = None
                balcony_cost = None
        elif price_level == 'suite':
            try:
                suite_price = price.find('span', {'class': 'price'})
                suite_price = suite_price.text
                suite_cost = price.find('span', {'class': 'cost'}).text
            except:
                suite_price = None
                suite_cost = None

    price_data = [interior_price, interior_cost, oceanview_price,
        oceanview_cost, balcony_price, balcony_cost, suite_price, suite_cost]
    return price_data

# clean price data and convert to floats
def CleanPriceData(price_data):
    try:
        interior_price = price_data[0].replace("$", "")
        interior_price = float(interior_price.replace(",", "").strip())
        interior_cost = price_data[1].replace("$", "").replace(",", "")
        interior_cost = interior_cost.replace("/night", "")
        interior_cost = float(interior_cost.strip())
    except:
        interior_price = None
        interior_cost = None
    try:
        oceanview_price = price_data[2].replace("$", "")
        oceanview_price = oceanview_price.replace(",", "")
        oceanview_price = float(oceanview_price.strip())
        oceanview_cost = price_data[3].replace("$", "")
        oceanview_cost = oceanview_cost.replace(",", "")
        oceanview_cost = oceanview_cost.replace("/night", "").strip()
        oceanview_cost = float(oceanview_cost)
    except:
        oceanview_price = None
        oceanview_cost = None
    try:
        balcony_price = price_data[4].replace("$", "").replace(",", "")
        balcony_price = float(balcony_price.strip())
        balcony_cost = price_data[5].replace("$", "").replace(",", "")
        balcony_cost = float(balcony_cost.replace("/night", "").strip())
    except:
        balcony_price = None
        balcony_cost = None
    try:
        suite_price = price_data[6].replace("$", "").replace(",", "")
        suite_price = float(suite_price.strip())
        suite_cost = price_data[7].replace("$", "").replace(",", "")
        suite_cost = float(suite_cost.replace("/night", "").strip())
    except:
        suite_price = None
        suite_cost = None

    cleaned_price_data = [interior_price, interior_cost, oceanview_price,
        oceanview_cost, balcony_price, balcony_cost, suite_price, suite_cost]
    return cleaned_price_data

# generate CSV of all cruises for the given cruise line link
def GetData(company, cruise_line, link):
    soup = GetPageHTML(link)
    container = soup.find('aside', {'class': 'sidebar order-first'})
    header = container.find('div', {'class': 'section-head'}).text.strip()

    num_results = header.replace("Find your cruise", "").split(" ")[0]
        
    num_pages = 5 + int(num_results)//10
    print(f"There are {num_pages} pages for {cruise_line}")
    start_time = time.time()
    all_data = []

    for i in range(0, num_pages + 1):
        link = f'{link}&offset={(i-1)*10}&page={i}'
        soup = GetPageHTML(link)

        listings = soup.find_all('div', {'class': 'card-body'})
        for j in range(len(listings)):
            ship_data = GetShipData(listings, j)
            price_data = GetPriceData(listings, j)
            cleaned_price_data = CleanPriceData(price_data)

            ship = {
                'date': datetime.date.today(),
                'company': str(company),
                'cruiseLine': str(cruise_line),
                'title': str(ship_data[0]),
                'shipName': str(ship_data[1]),
                'rating': ship_data[2],
                'opinion': str(ship_data[3]),
                'startDate': ship_data[4],
                'endDate': ship_data[5],
                'interiorPrice': cleaned_price_data[0],
                'interiorCost': cleaned_price_data[1],
                'oceanviewPrice': cleaned_price_data[2],
                'oceanviewCost': cleaned_price_data[3],
                'balconyPrice': cleaned_price_data[4],
                'balconyCost': cleaned_price_data[5],
                'suitePrice': cleaned_price_data[6],
                'suiteCost': cleaned_price_data[7]
            }
            all_data.append(ship)

    fields = ['date', 'company', 'cruiseLine', 'title', 'shipName', 'rating',
        'opinion', 'startDate', 'endDate', 'interiorPrice', 'interiorCost',
        'oceanviewPrice', 'oceanviewCost', 'balconyPrice', 'balconyCost',
        'suitePrice', 'suiteCost']
    with open(f'{cruise_line}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

    print(f"Finished {cruise_line}!")
    print(f"That took {round(time.time() - start_time, 0)} seconds")

# thread calls to GetData and import data into MongoDB
def ThreadAll():
    for i in range(len(CRUISE_LINES_LIST)):
        threads = []
        for j in range(len(CRUISE_LINES_LIST[i])):
            for company in CRUISE_LINES_DICT:
                cruise = CRUISE_LINES_LIST[i][j]
                if cruise in CRUISE_LINES_DICT[company]:
                    request_thread = threading.Thread(target=GetData, args=(company, cruise, CRUISE_LINES_LINKS[cruise]))
                    request_thread.start()
                    threads.append(request_thread)

        for thread in threads:
            thread.join()
    
    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: Travel, collection: Test")
        for cruise in CRUISE_LINES_LINKS:
            csvfile = f'"{cruise}.csv"'
            os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Travel --collection Test --type csv --file {csvfile} --headerline')
    else:
        print("Importing data into database: Travel, collection: Cruise-Lines")
        for cruise in CRUISE_LINES_LINKS:
            csvfile = f'"{cruise}.csv"'
            os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Travel --collection Cruise-Lines --type csv --file {csvfile} --headerline')

    for cruise in CRUISE_LINES_LINKS:
        csvfile = f'"{cruise}.csv"'
        os.system(f'rm {csvfile}')

try:
    ThreadAll()
except:
    email_sender = "ksg7699@nyu.edu"
    email_receiver = ["ksg7699@nyu.edu", "kgill@jsoros.com"]
    email_password = "zovrtywzgxvxpkqb"
    subject = "Error with Cruise Lines Script"
    em = MIMEMultipart('alternative')
    em['From'] = email_sender
    em['To'] = ", ".join(email_receiver)
    em['Subject'] = subject
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        for receiver in email_receiver:
            smtp.sendmail(email_sender, receiver, em.as_string())