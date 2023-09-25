'''Automates running each script to track daily Newegg Nvidia GPU listings'''

import os

import newegg_daily.aggregate
import newegg_daily.retrieve
import newegg_daily.urls_daily

URL_NAMES = newegg_daily.urls_daily.url_names

# run all scripts to generate and import daily Newegg Nvidia GPU listings
def RunAll(username, password, test):
    newegg_daily.retrieve.WriteFiles()
    newegg_daily.aggregate.AggregateData()

    if test:
        print("Importing data into database: Nvidia-GPUs, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Nvidia-GPUs --collection Test --type csv --file newegg_daily_aggregated.csv --headerline')
    else:
        print("Importing data into database: Nvidia-GPUs, collection: Daily")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Nvidia-GPUs --collection Daily --type csv --file newegg_daily_aggregated.csv --headerline')

    for i in range(len(URL_NAMES)):
        try:
            os.system(f'rm {URL_NAMES[i]}.csv')
        except:
            print(f'Failed to rm {URL_NAMES[i]}.csv')
            
    try:
        os.system('rm newegg_daily_aggregated.csv')
    except:
        print('Failed to rm newegg_daily_aggregated.csv')

