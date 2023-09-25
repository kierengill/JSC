'''Aggregates all historic Nvidia GPU listings into one CSV file'''

import csv
import pandas as pd

# names of urls
URLS = ['ebay_3060_12_new_past.csv', 'ebay_3060_12_used_past.csv',
    'ebay_3060Ti_8_new_past.csv', 'ebay_3060Ti_8_used_past.csv',
    'ebay_3070_8_new_past.csv', 'ebay_3070_8_used_past.csv',
    'ebay_3070Ti_8_new_past.csv', 'ebay_3070Ti_8_used_past.csv',
    'ebay_3080_1012_new_past.csv', 'ebay_3080_1012_used_past.csv',
    'ebay_3080Ti_12_new_past.csv', 'ebay_3080Ti_12_used_past.csv',
    'ebay_3090_24_new_past.csv', 'ebay_3090_24_used_past.csv',
    'ebay_3090Ti_24_new_past.csv', 'ebay_3090Ti_24_used_past.csv']

# dictionary of every GPU model and its corresponding MSRP price
MSRPS = {'3090Ti': 1999.99, '3090': 1499.99, '3080Ti': 1199.99, '3080': 699.99,
    '3070Ti': 599.99, '3070': 499.99, '3060Ti': 399.99, '3060': 329.99}

# aggregate all eBay historic GPU data into one CSV files
def AggregateData():
    listings = []

    # loop through each url
    for i in range(len(URLS)):
        try:
            df = pd.read_csv(URLS[i])
            # loop through the length of the dataframe 
            for j in range(len(df)):
                date = df.iloc[j][6].split(" ")[0]
                model = URLS[i].split("_")[1]

                msrp = MSRPS[model.split("_")[0]]

                memory = URLS[i].split("_")[2]
                if memory == "1012":
                    memory = "10/12"

                condition = URLS[i].split("_")[3]
                price = float(df.iloc[j][5])
                
                product = {
                    'marketplace': 'eBay',
                    'date': date,
                    'model': str(model),
                    'memory': str(memory),
                    'condition': str(condition),
                    'price': float(price),
                    'msrp': float(msrp),
                }
                listings.append(product)
        except:
            print(URLS[i], "does not exist")

    fields = ['marketplace', 'date', 'model', 'memory', 'condition', 'price',
        'msrp']

    # write aggregated normalized data to csv
    with open ('ebay_historic_aggregated.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(listings)

