'''Aggregates all current Newegg Nvidia GPU listings into a CSV file w/ stats'''

import csv
import datetime
import numpy as np
from os.path import exists

# names of urls
URL_NAMES = ['newegg_4090_24_new', 'newegg_4080_16_new', 'newegg_4070Ti_12_new', 
             'newegg_3090Ti_24_new', 'newegg_3090_24_new', 'newegg_3080Ti_12_new',
             'newegg_3080_1012_new', 'newegg_3070Ti_8_new', 'newegg_3070_8_new',
             'newegg_3060Ti_8_new', 'newegg_3060_12_new']

MSRPS = {'4090': 1599.00, '4080': 1199.00, '4070Ti': 799.00, '3090Ti': 1999.99, 
         '3090': 1499.99, '3080Ti': 1199.99, '3080': 699.99, '3070Ti': 599.99, 
         '3070': 499.99, '3060Ti': 399.99, '3060': 329.99}

# generate stats for each type of GPU and aggregate them into one CSV file
def AggregateData():
    stats = []

    # loop through each file
    for i in range(len(URL_NAMES)):
        # make sure the file exists
        file_exists = exists(f"{URL_NAMES[i]}.csv")
        if file_exists:
            with open(f"{URL_NAMES[i]}.csv", 'r') as csvfile:
                reader = csv.reader(csvfile)
                prices = []
                num_listings = 0
                for row in reader:
                    if row[5] != 'price':
                        prices.append(float(row[5]))
                    if row[8] != 'numListings':
                        num_listings += int(row[8])
                
                model = URL_NAMES[i].split("_")[1]
                memory = URL_NAMES[i].split("_")[2]
                if memory == "1012":
                    memory = "10/12"
                condition = URL_NAMES[i].split("_")[3]
                msrp = MSRPS[model.split("_")[0]]

                stat = {
                    'marketplace': 'Newegg',
                    'date': datetime.date.today(),
                    'model': str(model.split("_")[0]),
                    'memory': str(memory),
                    'condition': str(condition),
                    'numberOfListings': int(num_listings),
                    'median': float(np.median(prices)),
                    'lowerQuartile': float(np.percentile(prices, 25)),
                    'upperQuartile': float(np.percentile(prices, 75)),
                    'msrp': float(msrp)
                }
                stats.append(stat)

    fields = ['marketplace', 'date', 'model', 'memory', 'condition',
        'numberOfListings', 'median', 'lowerQuartile', 'upperQuartile', 'msrp']
    # write condensed data to csv
    with open('newegg_daily_aggregated.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(stats)

