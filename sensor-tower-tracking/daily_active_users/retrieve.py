'''Retrieve daily active users for both iOS and Andriod apps'''

import csv
import requests

# retrieve iOS daily active users for each app in the list
def IosScript(ios_list, token):
    ios_app_ids = ''
    for ios_app in ios_list:
        ios_app_ids = ios_app_ids + str(ios_app) + ','
    ios_app_ids = ios_app_ids[0:-1]

    url = f'https://api.sensortower.com/v1/ios/usage/active_users?app_ids={ios_app_ids}&time_period=day&start_date=2021-01-01&end_date=2030-01-01&countries=WW&auth_token={token}'
    response = requests.request("GET", url)

    result = eval(response.text)

    all_data = []
    for stat in result:
        app_id = stat['app_id']
        app_name = ios_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'users': stat['ipad_users'] + stat['iphone_users']
        }
        all_data.append(data)

    fields = ['appID', 'appName', 'date', 'users']

    with open('iosDAUs.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# retrieve Android daily active users for each app in the list
def AndroidScript(android_list, token):
    android_app_ids = ''
    for androidApp in android_list:
        android_app_ids = android_app_ids + str(androidApp) + ','
    android_app_ids = android_app_ids[0:-1]

    url = f'https://api.sensortower.com/v1/android/usage/active_users?app_ids={android_app_ids}&time_period=day&start_date=2021-01-01&end_date=2030-01-01&countries=WW&auth_token={token}'
    response = requests.request("GET", url)

    result = eval(response.text)

    all_data = []
    for stat in result:
        app_id = stat['app_id']
        app_name = android_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'users': stat['users']
        }
        all_data.append(data)

    fields = ['appID', 'appName', 'date', 'users']

    with open('androidDAUs.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

