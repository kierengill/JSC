'''Automates running each script to track daily eBay Nvidia GPU listings'''

import os

import ebay_daily.aggregate
import ebay_daily.retrieve
import ebay_daily.split
import ebay_daily.urls_daily

URL_NAMES = ebay_daily.urls_daily.url_names
SPLIT_URL_NAMES = ['ebay_3070Ti_8_new', 'ebay_3070Ti_8_used',
    'ebay_3090Ti_24_new', 'ebay_3090Ti_24_used']

# run all scripts to generate and import daily eBay Nvidia GPU listings
def RunAll(username, password, test):
    ebay_daily.retrieve.WriteFiles()
    ebay_daily.split.SplitAll()
    ebay_daily.aggregate.AggregateData()

    if test:
        print("Importing data into database: Nvidia-GPUs, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Nvidia-GPUs --collection Test --type csv --file ebay_daily_aggregated.csv --headerline')
    else:
        print("Importing data into database: Nvidia-GPUs, collection: Daily")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Nvidia-GPUs --collection Daily --type csv --file ebay_daily_aggregated.csv --headerline')

    for i in range(len(URL_NAMES)):
        try:
            os.system(f'rm {URL_NAMES[i]}.csv')
        except:
            print(f'Failed to rm {URL_NAMES[i]}.csv')

    for i in range(len(SPLIT_URL_NAMES)):
        try:
            os.system(f'rm {SPLIT_URL_NAMES[i]}.csv')
        except:
            print(f'Failed to rm {SPLIT_URL_NAMES[i]}.csv')

    try:
        os.system('rm ebay_daily_aggregated.csv')
    except:
        print('Failed to rm ebay_daily_aggregated.csv')

