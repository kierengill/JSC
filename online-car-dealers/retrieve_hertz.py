'''Runs the scripts to retrieve and import Hertz car listings data'''

from bs4 import BeautifulSoup
import csv
import datetime
import os
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

LINK_CERTIFIED = f'https://www.hertzcarsales.com/used-cars-for-sale.htm?geoZip=11375&geoRadius=0&compositeType=certified&start='
LINK_USED = f'https://www.hertzcarsales.com/used-cars-for-sale.htm?geoZip=11375&geoRadius=0&compositeType=Rent2Buy&start='

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

# get Hertz car listings data
def GetData(link, condition):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get(link)

    try:
        num_results = int(input("How many results are there?").strip())
    except:
        print("Please input an integer value")
        num_results = int(input("How many pages are there?").strip())
    confirm = input(f"Type 'y' to confirm and anything else to try again:")
    confirm = confirm.strip()

    while confirm.lower() != 'y':
        try:
            num_results = int(input("How many pages are there?").strip())
        except:
            print("Please input an integer value")
            num_results = int(input("How many pages are there?").strip())
        confirm = input(f"Type 'y' to confirm and anything else to try again:")
        confirm = confirm.strip()

    num_pages = int(num_results//18 + 1)
    all_data = []

    for i in range(num_pages):
        page_link = f'{link}{i*18}'
        driver.get(page_link)

        time.sleep(.5)
        for j in range(1, 12):
            time.sleep(.1)
            driver.execute_script(f"window.scrollTo(0, {600*j});")

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        listings = soup.find_all('div', {'class': 'vehicle-card-details-container'})

        for k in range(len(listings)):
            try:
                header = listings[k].text
                name = header.split("$")[0].strip()

                try:
                    year = int(name.split(" ")[0].strip())
                except:
                    year = -1
                try:
                    make = name.split(" ")[1].strip()
                except:
                    make = -1
                try:
                    price = header.split("$")[1].split("InfoLocation")[0]
                    price = float(price.replace(",", "").strip())
                except:
                    price = -1
                try:
                    mileage = listings[k].find('li', {'class': 'odometer'})
                    mileage = mileage.text.strip().split(" ")[0]
                    mileage = int(mileage.replace(",", ""))
                except:
                    mileage = -1

                car = {
                    'date': datetime.date.today(),
                    'condition': str(condition),
                    'name': str(name),
                    'year': int(year),
                    'make': str(make),
                    'price': float(price),
                    'mileage': int(mileage),
                    'dealer': 'Hertz'
                }
                all_data.append(car)
            except:
                print("Missed a listing")

    fields = ['date', 'condition', 'name', 'year', 'make', 'price', 'mileage',
        'dealer']
    with open(f'hertz-{condition}-cars.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

    driver.quit()

# run the scripts to generate and import Hertz data
def RunAll():
    GetData(LINK_CERTIFIED, 'Certified')
    GetData(LINK_USED, 'Used')

    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: Car-Dealers, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file hertz-Certified-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file hertz-Used-cars.csv --headerline')
    else:
        print("Importing data into database: Car-Dealers, collection: Hertz")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Hertz --type csv --file hertz-Certified-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Hertz --type csv --file hertz-Used-cars.csv --headerline')

    os.system('rm hertz-Certified-cars.csv')
    os.system('rm hertz-Used-cars.csv')

