'''Retrieves Similarweb daily visits data and imports it into MongoDB'''

import csv
import os
import pandas as pd
import requests

import urls

CATEGORIES = urls.categories

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

# filter out data points older than the inputed date in the CSV file
def UpdateAll(last_date, csvfile):
    df = pd.read_csv(csvfile)
    lendf = len(df)

    all_data = []
    row = 0
    while row < lendf:
        if str(df.iloc[row][3]) >= last_date:
            data = {
                'company': df.iloc[row][0],
                'site': df.iloc[row][1],
                'category': df.iloc[row][2],
                'date': df.iloc[row][3],
                'visits': df.iloc[row][4],
                '30DMA': df.iloc[row][5],
                '90DMA': df.iloc[row][6],
                '365DMA': df.iloc[row][7],
                'wow30DMA': df.iloc[row][8],
                'yoy30DMA': df.iloc[row][9],
                'wow90DMA': df.iloc[row][10],
                'yoy90DMA': df.iloc[row][11]
            }
            all_data.append(data)
        row += 1
    fields = ['company', 'site', 'category', 'date', 'visits', '30DMA',
        '90DMA', '365DMA', 'wow30DMA', 'yoy30DMA', 'wow90DMA', 'yoy90DMA']

    with open(csvfile, 'w') as filecsv:
        writer = csv.DictWriter(filecsv, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# retrieves web research data from similarweb and imports the data into MongoDB 
def RunScript(dictionary, category, last_date, username, password, test):
    for company in dictionary:
        try:
            url = f"https://api.similarweb.com/v1/website/{dictionary[company]}/total-traffic-and-engagement/visits?api_key=e5e015783b674c6b951e01c3242132ef&start_date=2021-07&country=world&granularity=daily&main_domain_only=false&format=json&mtd=true"
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            string = str(response.text).replace('false', 'False')
            string = string.replace('true', 'True').replace('null', 'None')

            json_data = eval(string)
            list_data = json_data['visits']

            monthly_size = 30
            monthly_averages = []
            monthly_moving = []

            quarterly_size = 90
            quarterly_averages = []
            quarterly_moving = []

            yearly_size = 365
            yearly_averages = []
            yearly_moving = []

            all_data = []

            i = 0
            while i < len(list_data):
                monthly_averages.append(list_data[i]['visits'])
                quarterly_averages.append(list_data[i]['visits'])
                yearly_averages.append(list_data[i]['visits'])
                
                # 30 day moving average
                if len(monthly_averages) == monthly_size:
                    thirty_dma = sum(monthly_averages) / monthly_size
                    monthly_moving.append(thirty_dma)
                    monthly_averages = monthly_averages[1:]
                else:
                    thirty_dma = None
                    monthly_moving.append(thirty_dma)

                # 90 day moving average
                if len(quarterly_averages) == quarterly_size:
                    ninety_dma = sum(quarterly_averages) / quarterly_size
                    quarterly_moving.append(ninety_dma)
                    quarterly_averages = quarterly_averages[1:]
                else:
                    ninety_dma = None
                    quarterly_moving.append(ninety_dma)

                # 365 day moving average
                if len(yearly_averages) == yearly_size:
                    yearly_dma = sum(yearly_averages) / yearly_size
                    yearly_moving.append(yearly_dma)
                    yearly_averages = yearly_averages[1:]
                else:
                    yearly_dma = None
                    yearly_moving.append(yearly_dma)

                    
                if len(monthly_moving) >= 8:
                    if (monthly_moving[i - 7] == 0
                            or monthly_moving[i - 7] == None):
                        wow_thirty_dma = None
                    else:
                        diff = monthly_moving[i] - monthly_moving[i - 7]
                        wow_thirty_dma = (diff)/(monthly_moving[i - 7])
                else:
                    wow_thirty_dma = None

                if len(monthly_moving) >= 366:
                    if (monthly_moving[i - 365] == 0
                            or monthly_moving[i - 365] == None):
                        yoy_thirty_dma = None
                    else:
                        diff = monthly_moving[i] - monthly_moving[i - 365]
                        yoy_thirty_dma = (diff)/(monthly_moving[i - 365])
                else:
                    yoy_thirty_dma = None

                if len(quarterly_moving) >= 8:
                    if (quarterly_moving[i - 7] == 0
                            or quarterly_moving[i - 7] == None):
                        wow_ninety_dma = None
                    else:
                        diff = quarterly_moving[i] - quarterly_moving[i - 7]
                        wow_ninety_dma = (diff)/(quarterly_moving[i - 7])
                else:
                    wow_ninety_dma = None

                if len(quarterly_moving) >= 366:
                    if (quarterly_moving[i - 365] == 0
                            or quarterly_moving[i - 365] == None):
                        yoy_ninety_dma = None
                    else:
                        diff = quarterly_moving[i] - quarterly_moving[i - 365]
                        yoy_ninety_dma = (diff)/(quarterly_moving[i - 365])
                else:
                    yoy_ninety_dma = None

                day = {
                    'company': company,
                    'site': dictionary[company],
                    'category': category,
                    'date': list_data[i]['date'],
                    'visits': list_data[i]['visits'],
                    '30DMA': thirty_dma,
                    '90DMA': ninety_dma,
                    '365DMA': yearly_dma,
                    'wow30DMA': wow_thirty_dma,
                    'yoy30DMA': yoy_thirty_dma,
                    'wow90DMA': wow_ninety_dma,
                    'yoy90DMA': yoy_ninety_dma
                }
                all_data.append(day)

                i += 1

            fields = ['company', 'site', 'category', 'date', 'visits', '30DMA',
                '90DMA', '365DMA', 'wow30DMA', 'yoy30DMA', 'wow90DMA',
                'yoy90DMA']

            with open(f'{dictionary[company]}.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = fields)
                writer.writeheader()
                writer.writerows(all_data)

            UpdateAll(last_date, f'{dictionary[company]}.csv')

            if test:
                os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Similarweb-Web-Traffic --collection Test --type csv --file {dictionary[company]}.csv --headerline')
            else:
                os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Similarweb-Web-Traffic --collection Visits --type csv --file {dictionary[company]}.csv --headerline')
            os.system(f'rm {dictionary[company]}.csv')
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            print(f'Failed to retrieve data from {dictionary[company]}')

# runs the scripts to retrieve and import all of Similarweb data tracked
def RunAll(last_date):
    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: Similarweb-Web-Traffic, collection: Test")
    else:
        print("Importing data into database: Similarweb-Web-Traffic, collection: Visits")

    for category in CATEGORIES:
        RunScript(CATEGORIES[category], category, last_date, username, password, test)
        print(category, 'finished!')
    print('everything is finished!')


LAST_DATE = '2023-08-01' 
RunAll(LAST_DATE)