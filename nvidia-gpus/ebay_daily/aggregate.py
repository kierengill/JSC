'''Aggregates all current eBay Nvidia GPU listings into one CSV file w/ stats'''

import csv
import datetime
import numpy as np
from os.path import exists

# names of eBay daily urls
URL_NAMES = ['ebay_3090_24_new', 'ebay_3090_24_used', 'ebay_3080Ti_12_new',
    'ebay_3080Ti_12_used', 'ebay_3080_1012_new', 'ebay_3080_1012_used',
    'ebay_3070_8_new', 'ebay_3070_8_used', 'ebay_3060Ti_8_new',
    'ebay_3060Ti_8_used', 'ebay_3060_12_new', 'ebay_3060_12_used',
    'ebay_3070Ti_8_new', 'ebay_3070Ti_8_used', 'ebay_3090Ti_24_new',
    'ebay_3090Ti_24_used']
# msrp prices of Nvidia 30 Series GPUs
MSRPS = {'3090Ti': 1999.99, '3090': 1499.99, '3080Ti': 1199.99, '3080': 699.99,
    '3070Ti': 599.99, '3070': 499.99, '3060Ti': 399.99, '3060': 329.99}

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

                for row in reader:
                    if row[5] != 'price':
                        prices.append(float(row[5]))

                model = URL_NAMES[i].split("_")[1]
                memory = URL_NAMES[i].split("_")[2]
                if memory == "1012":
                    memory = "10/12"
                condition = URL_NAMES[i].split("_")[3]



                msrp = MSRPS[model.split("_")[0]]
                number_of_listings = len(prices)

                if number_of_listings != 0:
                    median = np.median(prices)
                    lower_quartile = np.percentile(prices, 25)
                    upper_quartile = np.percentile(prices, 75)

                    stat = {
                        'marketplace': 'eBay',
                        'date': datetime.date.today(),
                        'model': str(model),
                        'memory': str(memory),
                        'condition': str(condition),
                        'numberOfListings': int(number_of_listings),
                        'median': float(median),
                        'lowerQuartile': float(lower_quartile),
                        'upperQuartile': float(upper_quartile),
                        'msrp': float(msrp)
                    }
                    stats.append(stat)

    fields = ['marketplace', 'date', 'model', 'memory', 'condition',
        'numberOfListings', 'median', 'lowerQuartile', 'upperQuartile', 'msrp']
    # write condensed data to csv
    with open('ebay_daily_aggregated.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(stats)

