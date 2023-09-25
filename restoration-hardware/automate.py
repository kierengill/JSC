'''Automates running each script to track on sale RH listings'''

import csv
import datetime
import numpy as np
import os

import retrieve
import urls

CATALOG_NAMES_FROM_SCRAPE = urls.caltalog_list_url_names
CSV_NAMES = ['Aggregated_RH_Living.csv', 'Aggregated_RH_Dining.csv',
    'Aggregated_RH_Bed.csv', 'Aggregated_RH_Bath.csv',
    'Aggregated_RH_Lighting.csv', 'Aggregated_RH_Textiles.csv',
    'Aggregated_RH_Rugs.csv', 'Aggregated_RH_Windows.csv',
    'Aggregated_RH_Decor.csv', 'Aggregated_RH_Outdoor.csv']

# generate summary statistics for a given product
def GetStats(url_names, catalog_names):
    stats = []
    for i in range(len(url_names)):
        with open(f"{url_names[i]}.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            
            regular_prices = []
            final_sale_prices = []
            member_prices = []
            final_sale_percent_offs = []

            zero_range_percent_off = 0
            ten_range_percent_off = 0
            twenty_range_percent_off = 0
            thirty_range_percent_off = 0
            forty_range_percent_off = 0
            fifty_plus_range_percent_off = 0

            for row in reader:
                if row[0] != "brand":
                    regular_prices.append(float(row[4]))
                    final_sale_prices.append(float(row[5]))
                    member_prices.append(float(row[6]))
                    percent_off = float(row[7])
                    final_sale_percent_offs.append(percent_off)

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

            split_name = url_names[i].split("_")
            
            stat = {
                'brand': str(split_name[0]),
                'catalog': str(split_name[1]),
                'category': str(split_name[2]),
                'product':  str(split_name[3]),
                'numberOfListingsOnSale': int(len(regular_prices)),
                'averagePercentOff': float(np.mean(final_sale_percent_offs)),
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
    
    fields = ['brand', 'catalog', 'category', 'product',
        'numberOfListingsOnSale', 'averagePercentOff', 'zeroRangePercentOff',
        'tenRangePercentOff', 'twentyRangePercentOff', 'thirtyRangePercentOff',
        'fortyRangePercentOff', 'fiftyPlusRangePercentOff', 'date']
    # write condensed data to csv
    with open(f'{catalog_names}', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(stats)

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

# run all scripts to generate and import RH on sale listings data
def ImportData():
    RunScript()

    test = GetTargetCollection()
    username, password = GetCredentials()

    if test:
        for i in range(len(CSV_NAMES)):
            print("Importing data into database: Home-Furnishing, collection: Test")
            os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Home-Furnishing --collection Test --type csv --file {CSV_NAMES[i]} --headerline')
            os.system(f"rm {CSV_NAMES[i]}")
            print(f'{CSV_NAMES[i]} finished importing')
    else:
        for i in range(len(CSV_NAMES)):
            print("Importing data into database: Home-Furnishing, collection: Restoration-Hardware")
            os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Home-Furnishing --collection Restoration-Hardware --type csv --file {CSV_NAMES[i]} --headerline')
            os.system(f"rm {CSV_NAMES[i]}")
            print(f'{CSV_NAMES[i]} finished importing')

ImportData()