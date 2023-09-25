'''Automates the running of each script to track historic Nvidia GPU listings'''

import os

import ebay_historic.aggregate
import ebay_historic.retrieve
import ebay_historic.split
import ebay_historic.urls_historic

URL_NAMES = ebay_historic.urls_historic.url_names
SPLIT_URL_NAMES = ['ebay_3070Ti_8_new_past', 'ebay_3070Ti_8_used_past',
    'ebay_3090Ti_24_new_past', 'ebay_3090Ti_24_used_past']

# run historic scripts
def RunAll(username, password, test, update):
    ebay_historic.retrieve.WriteFiles(update)
    ebay_historic.split.SplitAll()
    ebay_historic.aggregate.AggregateData()

    if test:
        print("Importing data into database: Nvidia-GPUs, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Nvidia-GPUs --collection Test --type csv --file ebay_historic_aggregated.csv --headerline')
    else:
        print("Importing data into database: Nvidia-GPUs, collection: Historic")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Nvidia-GPUs --collection Historic --type csv --file ebay_historic_aggregated.csv --headerline')

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
        os.system('rm ebay_historic_aggregated.csv')
    except:
        print('Failed to rm ebay_historic_aggregated.csv')

