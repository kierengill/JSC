'''Retrieve revenue and downloads for both iOS and Andriod apps'''

import csv
import requests

# 
def IosScript(ios_list, token, date):
    all_data = []
    for ios_app in ios_list:
        url = f'https://api.sensortower.com/v1/ios/sales_report_estimates?app_ids={ios_app}&countries=WW&date_granularity=weekly&start_date=2021-01-01&end_date={date}&auth_token={token}'
        response = requests.request("GET", url)

        result = eval(response.text)

        for stat in result:
            app_id = stat['aid']
            app_name = ios_list[app_id]

            revenue = 0
            if 'ar' in stat and 'ir' in stat:
                revenue = stat['ar'] + stat['ir']
            elif 'ar' in stat:
                revenue = stat['ar']
            elif 'ir' in stat:
                revenue = stat['ir']

            downloads = 0
            if 'au' in stat and 'iu' in stat:
                downloads = stat['au'] + stat['iu']
            elif 'ai' in stat:
                downloads = stat['au']
            elif 'iu' in stat:
                downloads = stat['iu']
            
            data = {
                'appID': app_id,
                'appName': app_name,
                'date': stat['d'],
                'downloads': downloads,
                'revenue': revenue
            }
            all_data.append(data)

    fields = ['appID', 'appName', 'date', 'downloads', 'revenue']

    with open('iosDownloads.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# 
def AndroidScript(android_list, token, date):
    all_data = []
    for android_app in android_list:
        url = f'https://api.sensortower.com/v1/android/sales_report_estimates?app_ids={android_app}&countries=WW&date_granularity=weekly&start_date=2021-01-01&end_date={date}&auth_token={token}'
        response = requests.request("GET", url)

        result = eval(response.text)

        for stat in result:
            app_id = stat['aid']
            app_name = android_list[app_id]

            revenue = 0
            if 'r' in stat:
                revenue = stat['r']

            downloads = 0
            if 'u' in stat:
                downloads = stat['u']
            
            data = {
                'appID': app_id,
                'appName': app_name,
                'date': stat['d'],
                'downloads': downloads,
                'revenue': revenue
            }
            all_data.append(data)

    fields = ['appID', 'appName', 'date', 'downloads', 'revenue']

    with open('androidDownloads.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

