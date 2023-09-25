'''Runs the scripts to retrieve and import Sonic car listings data'''

from bs4 import BeautifulSoup
import csv
import datetime
import os
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

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

# get Sonic car listings data
def GetData(condition):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    link = f'https://www.sonicautomotive.com/{condition}-inventory/index.htm?start=0'
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

    allData = []
    all_listings_set = set()
    for i in range(num_pages):
        link = f'https://www.sonicautomotive.com/{condition}-inventory/index.htm?start={i*35}'
        driver.get(link)

        time.sleep(.5)
        for j in range(1, 32):
            time.sleep(.05)
            driver.execute_script(f"window.scrollTo(0, {600*j});")

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        listings = soup.find_all('li', {'class': 'box box-border vehicle-card vehicle-card-detailed vehicle-card-horizontal'})

        for k in range(len(listings)):
            try:
                vehicle_id = listings[k].find('li', {'class': 'vin'}).text
                vehicle_id = vehicle_id.split(": ")[1].strip()

                if vehicle_id not in all_listings_set:
                    all_listings_set.add(vehicle_id)
                    try:
                        if condition == 'certified':
                            name = listings[k].find('h2', {'class': f'vehicle-card-title mt-0 d-flex justify-content-between align-items-end inv-type-certified-pre-owned'})
                            name = name.text.strip()
                        else:
                            name = listings[k].find('h2', {'class': f'vehicle-card-title mt-0 d-flex justify-content-between align-items-end inv-type-{condition}'})
                            name = name.text.strip()
                        year = name.split(" ")[0]
                        make = name.split(" ")[1]
                    except:
                        name = -1
                        year = -1
                        make = -1
                    try:
                        mileage = listings[k].find('li', {'class': 'odometer'})
                        mileage = mileage.text.split(": ")[1].split(" ")[0]
                        mileage = int(mileage.replace(",", ""))
                    except:
                        mileage = -1
                    try:
                        stock_number = listings[k].find('li', {'class': 'stockNumber'})
                        stock_number = stock_number.text.split(": ")[1].strip()
                    except:
                        stock_number = -1
                    try:
                        price = listings[k].find('span', {'class': 'price-value'})
                        price = price.text.replace("$", "")
                        price = float(price.replace(",", ""))
                    except:
                        price = -1

                    car = {
                        'date': datetime.date.today(),
                        'condition': str(condition),
                        'name': str(name),
                        'year': int(year),
                        'make': str(make),
                        'price': float(price),
                        'mileage': int(mileage),
                        'stockNumber': str(stock_number),
                        'vehicleId': str(vehicle_id),
                        'dealer': 'Sonic'
                    }
                    allData.append(car)
            except:
                print("Missed a listing")
        print(len(all_listings_set))

    fields = ['date', 'condition', 'name', 'year', 'make', 'price', 'mileage',
        'stockNumber', 'vehicleId', 'dealer']
    with open(f'sonic-{condition}-cars.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(allData)

    driver.quit()

# run the scripts to generate and import Sonic data
def RunAll():
    GetData('used')
    GetData('new')
    GetData('certified')

    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: Car-Dealers, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file sonic-new-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file sonic-certified-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file sonic-used-cars.csv --headerline')
    else:
        print("Importing data into database: Car-Dealers, collection: Sonic")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Sonic --type csv --file sonic-new-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Sonic --type csv --file sonic-certified-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Sonic --type csv --file sonic-used-cars.csv --headerline')
    
    os.system(f'rm sonic-new-cars.csv')
    os.system(f'rm sonic-certified-cars.csv')
    os.system(f'rm sonic-used-cars.csv')

