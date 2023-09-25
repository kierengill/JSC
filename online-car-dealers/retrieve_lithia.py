'''Runs the scripts to retrieve and import Lithia car listings data'''

from bs4 import BeautifulSoup
import csv
import datetime
import os
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

NEW_LINK = 'https://www.lithia.com/new-inventory/index.htm'
PREOWONED_LINK = 'https://www.lithia.com/used-inventory/index.htm?compositeType=used'
CERTIFIED_LINK = 'https://www.lithia.com/used-inventory/index.htm?compositeType=certified'

# request users MongoDB database credentials
def GetCredentials():
    username = input("Enter your MongoDB Database username:").strip()
    password = input("Enter your MongoDB Database username:").strip()
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

# return car listing info from text
def CreateListing(info, condition):
    if condition == 'New':
        name = info.split("$")[0]
        if 'InfoPricing' in name:
            name = name.split('InfoPricing')[0]
        if 'InfoSpecials':
            name = name.split('InfoSpecials')[0]

        try:
            year = int(name.split(" ")[0])
        except:
            year = -1
        make = name.split(" ")[1]
        
        try:
            price = float(info.split("$")[1].replace(",", "")[0:7])
        except:
            try:
                price = float(info.split("$")[1].replace(",", "")[0:6])
            except:
                try:
                    price = float(info.split("$")[1].replace(",", "")[0:5])
                except:
                    try:
                        price = float(info.split("$")[1].replace(",", "")[0:4])
                    except:
                        price = -1

        try:
            stock_number = info.split("Stock #: ")[1].split(" ")[0]
        except:
            stock_number = -1

        car = {
            'date': datetime.date.today(),
            'condition': str(condition),
            'name': str(name),
            'year': int(year),
            'make': str(make),
            'price': float(price),
            'mileage': 0,
            'stockNumber': str(stock_number),
            'dealer': 'Lithia'
        }
        return car

    elif condition == 'Pre-Owned' or condition == 'Certified':
        name = info.split("$")[0]
        if 'InfoPricing' in name:
            name = name.split('InfoPricing')[0]

        try:
            year = int(name.split(" ")[0])
        except:
            year = -1
        make = name.split(" ")[1]
        
        try:
            price = info.split("mpg City/HwyPrice$")[1]
            price = price.split("Confirm Availability")[0].replace(",", "")
            price = float(price.replace(" ", "").strip())
        except:
            price = -1
        try:
            mileage = info.split(" milesStock #")[0].split(" Engine")[-1]
            mileage = int(mileage.replace(",", "").replace(" ", "").strip())
        except:
            mileage = -1

        try:
            stock_number = info.split("Stock #: ")[1].split(" ")[0]
        except:
            stock_number = -1

        car = {
            'date': datetime.date.today(),
            'condition': str(condition),
            'name': str(name),
            'year': int(year),
            'make': str(make),
            'price': float(price),
            'mileage': int(mileage),
            'stockNumber': str(stock_number),
            'dealer': 'Lithia'
        }
        return car
    else:
        print("Incorrect condition input")

# get Lithia car listings data
def GetData(condition, link):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get(link)

    try:
        num_pages = int(input("How many pages are there?").strip())
    except:
        print("Please input an integer value")
        num_pages = int(input("How many pages are there?").strip())
    confirm = input(f"Type 'y' to confirm and anything else to try again:")
    confirm = confirm.strip()

    while confirm.lower() != 'y':
        try:
            num_pages = int(input("How many pages are there?").strip())
        except:
            print("Please input an integer value")
            num_pages = int(input("How many pages are there?").strip())
        confirm = input(f"Type 'y' to confirm and anything else to try again:")
        confirm = confirm.strip()

    all_data = []
    all_listings_set = set()
    for i in range(num_pages):

        time.sleep(1)
        for j in range(1, 15):
            driver.execute_script(f"window.scrollTo(0, {600*j});")
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        listings = soup.find_all('li', {'class': 'box box-border vehicle-card vehicle-card-detailed'})
        if len(listings) != 18:
            print(f'Number of Listings = {len(listings)}')

        for k in range(len(listings)):
            try:
                info = listings[k].find('div', {'class': 'vehicle-card-details-container'})
                info = info.text
                if info not in all_listings_set:
                    all_listings_set.add(info)
                    car = CreateListing(info, condition)
                    all_data.append(car) 
            except:
                print("Missed a listing")

        try:
            driver.get(f'{link}?start={i*18 + 18}')
        except:
            print("Trying to go to the next page again")
            time.sleep(5)
            try:
                driver.get(f'{link}?start={i*18 + 18}')
            except:
                print("Trying one last time")
                time.sleep(10)
                driver.get(f'{link}?start={i*18 + 18}')

        print(len(all_listings_set))

    fields = ['date', 'condition', 'name', 'year', 'make', 'price', 'mileage',
        'stockNumber', 'dealer']
    with open(f'lithia-{condition}-cars.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

    driver.quit()

# run the scripts to generate and import Lithia data
def RunAll():
    GetData('New', NEW_LINK)
    GetData('Certified', CERTIFIED_LINK)
    GetData('Pre-Owned', PREOWONED_LINK)

    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: Car-Dealers, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file lithia-New-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file lithia-Certified-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file lithia-Pre-Owned-cars.csv --headerline')
    else:
        print("Importing data into database: Car-Dealers, collection: Lithia")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Lithia --type csv --file lithia-New-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Lithia --type csv --file lithia-Certified-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Lithia --type csv --file lithia-Pre-Owned-cars.csv --headerline')
    
    os.system(f'rm lithia-New-cars.csv')
    os.system(f'rm lithia-Certified-cars.csv')
    os.system(f'rm lithia-Pre-Owned-cars.csv')

