'''Runs the scripts to retrieve and import Group 1 car listings data'''

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

# get Group 1 car listings data
def GetData(condition):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    link = f'https://www.group1auto.com/search/{condition}+t?page=1'
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

    num_pages = int(num_results//12 + 1)
    all_data = []

    for i in range(num_pages):
        link = f'https://www.group1auto.com/search/{condition}+t?page={i + 1}'
        driver.get(link)

        time.sleep(.5)
        for j in range(1, 8):
            time.sleep(.1)
            driver.execute_script(f"window.scrollTo(0, {600*j});")

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        listings = soup.find_all('div', {'class': 'af-vehicle-s-wrapper'})

        for k in range(len(listings)):
            name = listings[k].find('h2', {'class': 'af-vehicle-name'})
            name = name.text.strip()
            try:
                year = listings[k].find('span', {'class': 'af-vehicle-year-make-model'})
                year = int(year.text.strip().split(" ")[0])
            except:
                year = -1
            make = listings[k].find('span', {'class': 'af-vehicle-year-make-model'})
            make = make.text.strip().split(" ")[1]
            try:
                mileage = listings[k].find('span', {'class': 'af-vehicle-mileage'})
                mileage = int(mileage.text.split(" ")[0].replace(",", ""))
            except:
                mileage = -1
            try:
                price = listings[k].find('td', {'class': 'af-price-value af-final-price-value'})
                price = price.text.replace("$", "").replace(",", "")
                price = float(price.replace("*", ""))
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
                'dealer': 'Group1'
            }
            all_data.append(car)

    fields = ['date', 'condition', 'name', 'year', 'make', 'price', 'mileage',
        'dealer']
    with open(f'group1-{condition}-cars.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

    driver.quit()

# run the scripts to generate and import Group 1 data
def RunAll():
    GetData('New')
    GetData('Used')
    GetData('Certified Pre-Owned')

    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: Car-Dealers, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file group1-New-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file group1-Used-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file "group1-Certified Pre-Owned-cars.csv" --headerline')
    else:
        print("Importing data into database: Car-Dealers, collection: Group1")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Group1 --type csv --file group1-New-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Group1 --type csv --file group1-Used-cars.csv --headerline')
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Group1 --type csv --file "group1-Certified Pre-Owned-cars.csv" --headerline')
    
    os.system(f'rm group1-Used-cars.csv')
    os.system(f'rm group1-New-cars.csv')
    os.system(f'rm "group1-Certified Pre-Owned-cars.csv"')

