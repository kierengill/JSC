''''''

import os

import apps
import retrieve
import aggregate
import analyze

TOKEN = 'ST0_zhV7EBR6_JQUyiKRiteWqDC'

IOS_LISTS = apps.iosLists
ANDROID_LISTS = apps.androidLists
CATEGORIES = apps.categories

# automates the running of each script to import data into MongoDB
def Automate(ios_list, android_list, category, date, token, username, password, test):
    retrieve.IosScriptSessionCount(ios_list, token, date)
    retrieve.AndroidScriptSessionCount(android_list, token, date)
    retrieve.IosScriptSessionDuration(ios_list, token, date)
    retrieve.AndroidScriptSessionDuration(android_list, token, date)
    retrieve.IosScriptTimeSpent(ios_list, token, date)
    retrieve.AndroidScriptTimeSpent(android_list, token, date)

    aggregate.AggregateSessionCount()
    aggregate.AggregateSessionDuration()
    aggregate.AggregateTimeSpent()

    aggregate.RunScriptSessionCount()
    aggregate.RunScriptSessionDuration()
    aggregate.RunScriptTimeSpent()

    analyze.Merge()
    analyze.WriteAll(category)
    analyze.UpdateAll(date)

    if test:
        print(f"Importing data into database: Sensor-Tower-Apps, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Sensor-Tower-Apps --collection Test --type csv --file outputSessionStats.csv --headerline')
    else:
        print(f"Importing data into database: Sensor-Tower-Apps, collection: Session-Stats")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Sensor-Tower-Apps --collection Session-Stats --type csv --file outputSessionStats.csv --headerline')

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
    print('Finished all Session Stats!')
    os.system('rm androidSessionCount.csv')
    os.system('rm iosSessionCount.csv')
    os.system('rm androidSessionDuration.csv')
    os.system('rm iosSessionDuration.csv')
    os.system('rm androidTimeSpent.csv')
    os.system('rm iosTimeSpent.csv')
    os.system('rm aggregatedSessionCount.csv')
    os.system('rm aggregatedSessionCount.json')
    os.system('rm aggregatedSessionDuration.csv')
    os.system('rm aggregatedSessionDuration.json')
    os.system('rm aggregatedTimeSpent.csv')
    os.system('rm aggregatedTimeSpent.json')
    os.system('rm firstMergeSessionStats.csv')
    os.system('rm mergedSessionStats.csv')
    os.system('rm outputSessionStats.csv')

