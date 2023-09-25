'''Runs the scripts to retrieve and import used Ferrari data'''

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

# get used Ferrari data
def GetData():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    link = f'https://preowned.ferrari.com/en-US/r/north-america/used-ferrari/usa/rfc?pl=0'

    driver.get(link)
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    num_pages_sentence = soup.find('div', {'class': 'SearchResultListing__loadMore__J4c-7T-3'})
    
    num_pages_arr = num_pages_sentence.text.split(' ')
    num_pages = int(num_pages_arr[4]) // int(num_pages_arr[2]) + 1

    # try:
    #     num_pages = int(input("How many pages are there?").strip())
    # except:
    #     print("Please input an integer value")
    #     num_pages = int(input("How many pages are there?").strip())
    # confirm = input(f"Type 'y' to confirm and anything else to try again:")
    # confirm = confirm.strip()

    # while confirm.lower() != 'y':
    #     try:
    #         num_pages = int(input("How many pages are there?").strip())
    #     except:
    #         print("Please input an integer value")
    #         num_pages = int(input("How many pages are there?").strip())
    #     confirm = input(f"Type 'y' to confirm and anything else to try again:")
    #     confirm = confirm.strip()

    all_data = []
    for i in range(num_pages):
        link = f'https://preowned.ferrari.com/en-US/r/north-america/used-ferrari/usa/rfc?pl={i}'
        driver.get(link)

        time.sleep(.5)
        for j in range(1, 10):
            time.sleep(.1)
            driver.execute_script(f"window.scrollTo(0, {600*j});")

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        listings = soup.find_all('article', {'class': 'VehicleCard__wrapper__2VCV2pTX'})

        for k in range(len(listings)):
            try:
                name = listings[k].find('div', {'class': 'VehicleCard__specsHeadCarName__3Y9jfj2A'})
                name = str(name.text)
            except:
                name = -1
            try:
                year = listings[k].find('div', {'class': 'VehicleCard__year__31akchrt'})
                year = int(year.text)
            except:
                year = -1
            try:
                mileage = listings[k].find('div', {'class': 'VehicleCard__odometer__2Aa-D18j'})
                mileage = int(mileage.text.split(" ")[0].replace(",", ""))
            except:
                mileage = -1
            try:
                price = listings[k].find('div', {'class': 'VehicleCard__specsHeadPriceWithCurrency__P4OZb2Up'})
                price = float(price.text.replace("$", "").replace(",", ""))
            except:
                price = -1

            car = {
                'date': datetime.date.today(),
                'condition': 'Used',
                'name': str(name),
                'year': int(year),
                'make': 'Ferrari',
                'price': float(price),
                'mileage': int(mileage),
                'dealer': 'Ferrari'
            }
            all_data.append(car)

    fields = ['date', 'condition', 'name', 'year', 'make', 'price', 'mileage',
        'dealer']
    with open(f'ferrari-used-cars.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

    driver.quit()

# run the scripts to generate and import used Ferrari data
def RunAll():
    GetData()

    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: Car-Dealers, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Test --type csv --file ferrari-used-cars.csv --headerline')
    else:
        print("Importing data into database: Car-Dealers, collection: Ferrari")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Car-Dealers --collection Ferrari --type csv --file ferrari-used-cars.csv --headerline')
    os.system(f'rm ferrari-used-cars.csv')

RunAll()