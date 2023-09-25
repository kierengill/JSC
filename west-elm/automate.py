'''Automates the running of each script to track on sale West Elm listings'''

import csv
import datetime
import numpy as np
import os

import retrieve
import urls

CATALOG_NAMES_FROM_SCRAPE = urls.catalog_list_url_names

# generate summary statistics for a given product
def GetStats(url_names, num_listings):
    stats = []
    for i in range(len(url_names)):
        with open(f"{url_names[i]}.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            regular_prices = []
            sale_prices = []
            sale_percent_offs = []
            zero_range_percent_off = 0
            ten_range_percent_off = 0
            twenty_range_percent_off = 0
            thirty_range_percent_off = 0
            forty_range_percent_off = 0
            fifty_plus_range_percent_off = 0

            count = 0
            for row in reader:
                if row[2][0].isdigit():
                    count += 1
                    regular_prices.append(float(row[2]))
                    sale_prices.append(float(row[3]))
                    percent_off = float(row[4])
                    sale_percent_offs.append(percent_off)
                    if percent_off < .1:
                        zero_range_percent_off += 1
                    elif percent_off < .2:
                        ten_range_percent_off += 1
                    elif percent_off < .3:
                        twenty_range_percent_off += 1
                    elif percent_off < .4:
                        thirty_range_percent_off += 1
                    elif percent_off < .5:
                        forty_range_percent_off += 1
                    else:
                        fifty_plus_range_percent_off += 1

            stat = {
                'brand': 'West Elm',
                'category': str(url_names[i]),
                'numberOfListingsOnSale': int(num_listings[i]),
                'numberOfListingsCollected': int(count),
                'averagePercentOff': float(np.mean(percent_off)),
                'zeroRangePercentOff': int(zero_range_percent_off),
                'tenRangePercentOff': int(ten_range_percent_off),
                'twentyRangePercentOff': int(twenty_range_percent_off),
                'thirtyRangePercentOff': int(thirty_range_percent_off),
                'fortyRangePercentOff': int(forty_range_percent_off),
                'fiftyPlusRangePercentOff': int(fifty_plus_range_percent_off),
                'date': datetime.date.today()
            }
            stats.append(stat)
        os.system(f'rm "{url_names[i]}.csv"')

    fields = ['brand', 'category', 'numberOfListingsOnSale',
        'numberOfListingsCollected', 'averagePercentOff', 'zeroRangePercentOff',
        'tenRangePercentOff', 'twentyRangePercentOff', 'thirtyRangePercentOff',
        'fortyRangePercentOff', 'fiftyPlusRangePercentOff', 'date']
    # write condensed data to csv
    with open(f'aggregated.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(stats)

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

# run all scripts to generate and import West Elm on sale listings data
def ImportData():
    num_listings = retrieve.RunScript()
    GetStats(CATALOG_NAMES_FROM_SCRAPE, num_listings)

    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: Home-Furnishing, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Home-Furnishing --collection Test --type csv --file aggregated.csv --headerline')
        os.system('rm aggregated.csv')
        print(f'Finished importing aggregated.csv')
    else:
        print("Importing data into database: Home-Furnishing, collection: West-Elm")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Home-Furnishing --collection West-Elm --type csv --file aggregated.csv --headerline')
        os.system('rm aggregated.csv')
        print(f'Finished importing aggregated.csv')

