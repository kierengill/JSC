'''Retrieves revenue and downloads data for all the apps tracked'''

import os

import aggregate
import analyze
import apps
import retrieve
from datetime import date, timedelta


TOKEN = 'ST0_zhV7EBR6_JQUyiKRiteWqDC'

IOS_LISTS = apps.iosLists
ANDROID_LISTS = apps.androidLists
CATEGORIES = apps.categories

# automates the running of each script to import data into MongoDB
def Automate(ios_list, android_list, category, date, token, username, password, test):
    retrieve.IosScript(ios_list, token, date)
    retrieve.AndroidScript(android_list, token, date)

    aggregate.AggregateDownloads()
    aggregate.AggregateRevenue()
    aggregate.RunScriptDownloads()
    aggregate.RunScriptRevenue()

    analyze.Merge()
    analyze.WriteAll(category)
    analyze.UpdateAll(date)

    if test:
        print(f"Importing data into database: Sensor-Tower-Apps, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Sensor-Tower-Apps --collection Test --type csv --file outputRevenueDownloads.csv --headerline')
    else:
        print(f"Importing data into database: Sensor-Tower-Apps, collection: Revenue-Downloads")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Sensor-Tower-Apps --collection Revenue-Downloads --type csv --file outputRevenueDownloads.csv --headerline')

# request users MongoDB database credentials
def GetCredentials():
    username = input("Enter your MongoDB Database username:").strip()
    password = input("Enter your MongoDB Database password:").strip()
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

# runs the automated script on every app in every category
def RunAll(date):
    test = GetTargetCollection()
    username, password = GetCredentials()
    for i in range(len(CATEGORIES)):
        Automate(IOS_LISTS[i], ANDROID_LISTS[i], CATEGORIES[i], date, TOKEN, username, password, test)
        print(f'Finished {CATEGORIES[i]}!')
    print('Finished all Revenue and Downloads!')
    os.system('rm aggregatedDownloads.csv')
    os.system('rm aggregatedDownloads.json')
    os.system('rm aggregatedRevenue.csv')
    os.system('rm aggregatedRevenue.json')
    os.system('rm androidDownloads.csv')
    os.system('rm iosDownloads.csv')
    os.system('rm mergedRevenueDownloads.csv')
    os.system('rm outputRevenueDownloads.csv')

today = date.today()
last_monday = today - timedelta(days = 9)

# Run this on Wednesdays to get last Monday's date
RunAll(last_monday)