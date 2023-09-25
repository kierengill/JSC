'''Automates running each script to track on sale Dicks Sporting Goods listings'''

import csv
import datetime
import numpy as np
import os

import retrieve
import urls

CATALOG_NAMES_FROM_SCRAPE = urls.catalog_list_url_names
CSV_NAMES = ['Aggregated_Women.csv', 'Aggregated_Men.csv',
    'Aggregated_Kids.csv', 'Aggregated_Sports1.csv', 'Aggregated_Sports2.csv',
    'Aggregated_Fitness.csv', 'Aggregated_Outdoor.csv', 'Aggregated_Fans.csv',
    'Aggregated_Accessories.csv']

# generate summary statistics for a given product
def GetStats(url_names, catalog_names):
    stats = []
    for i in range(len(url_names)):
        with open(f"{url_names[i]}.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            regular_prices = []
            sale_prices = []
            sale_percent_offs = []
            
            for row in reader:
                if row[6].isdigit():
                    regular_prices.append(float(row[3]))
                    sale_prices.append(float(row[4]))
                    sale_percent_offs.append(float(row[5]))
                    num_listings = int(row[6])

            split_name = url_names[i].split("_")

            stat = {
                'brand': "Dick's Sporting Goods",
                'category': str(split_name[0]),
                'product':  str(split_name[1]),
                'numberOfListingsOnSale': int(num_listings),
                'averagePercentOff': float(np.mean(sale_percent_offs)),
                'date': datetime.date.today()
            }
            stats.append(stat)

            fields = ['brand', 'category', 'product', 'numberOfListingsOnSale',
                'averagePercentOff', 'date']
            # write condensed data to csv
            with open(f'{catalog_names}', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = fields)
                writer.writeheader()
                writer.writerows(stats)
        os.system(f'rm "{url_names[i]}.csv"')

# generate all summary statistics for all products from every category
def RunScript():
    retrieve.RunScript()
    for i in range(len(CATALOG_NAMES_FROM_SCRAPE)):
        GetStats(CATALOG_NAMES_FROM_SCRAPE[i], CSV_NAMES[i])

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

# run all scripts to generate and import on sale Dicks Sporting Goods listings
def ImportData():
    RunScript()

    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        for i in range(len(CSV_NAMES)):
            print("Importing data into database: Sports-Retail, collection: Test")
            os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Sports-Retail --collection Test --type csv --file {CSV_NAMES[i]} --headerline')
            os.system(f'rm "{CSV_NAMES[i]}"')
            print(f'Finished importing {CSV_NAMES[i]}')
    else:
        for i in range(len(CSV_NAMES)):
            print("Importing data into database: Sports-Retail, collection: Dicks-Sporting-Goods")
            os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Sports-Retail --collection Dicks-Sporting-Goods --type csv --file {CSV_NAMES[i]} --headerline')
            os.system(f'rm "{CSV_NAMES[i]}"')
            print(f'Finished importing {CSV_NAMES[i]}')

ImportData()