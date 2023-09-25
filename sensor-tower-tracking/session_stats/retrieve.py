''''''

import csv
import json
import requests

# 
def IosScriptSessionCount(ios_list, token, date):
    ios_app_ids = ''
    for ios_app in ios_list:
        ios_app_ids = ios_app_ids + str(ios_app) + ','
    ios_app_ids = ios_app_ids[0:-1]

    url = f'https://api.sensortower.com/v1/ios/usage/session_count?app_ids={ios_app_ids}&date_granularity=monthly&start_date=2021-01-01&end_date={date}&auth_token={token}'
    response = requests.request("GET", url)
    result = json.loads(response.text)

    all_data = []
    for stat in result['app_data']['day']:
        app_id = stat['app_id']
        app_name = ios_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'sessionCount': stat['average_sessions_per_user']
        }
        all_data.append(data)

    for stat in result['app_data']['week']:
        app_id = stat['app_id']
        app_name = ios_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'sessionCount': stat['average_sessions_per_user']
        }
        all_data.append(data)

    for stat in result['app_data']['month']:
        app_id = stat['app_id']
        app_name = ios_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'sessionCount': stat['average_sessions_per_user']
        }
        all_data.append(data)

    fields = ['appID', 'appName', 'date', 'timePeriod', 'sessionCount']

    with open('iosSessionCount.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# 
def AndroidScriptSessionCount(android_list, token, date):
    android_app_ids = ''
    for android_app in android_list:
        android_app_ids = android_app_ids + str(android_app) + ','
    android_app_ids = android_app_ids[0:-1]

    url = f'https://api.sensortower.com/v1/android/usage/session_count?app_ids={android_app_ids}&date_granularity=monthly&start_date=2021-01-01&end_date={date}&auth_token={token}'
    response = requests.request("GET", url)
    result = json.loads(response.text)

    all_data = []
    for stat in result['app_data']['day']:
        app_id = stat['app_id']
        app_name = android_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'sessionCount': stat['average_sessions_per_user']
        }
        all_data.append(data)

    for stat in result['app_data']['week']:
        app_id = stat['app_id']
        app_name = android_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'sessionCount': stat['average_sessions_per_user']
        }
        all_data.append(data)

    for stat in result['app_data']['month']:
        app_id = stat['app_id']
        app_name = android_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'sessionCount': stat['average_sessions_per_user']
        }
        all_data.append(data)

    fields = ['appID', 'appName', 'date', 'timePeriod', 'sessionCount']

    with open('androidSessionCount.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# 
def IosScriptSessionDuration(ios_list, token, date):
    ios_app_ids = ''
    for ios_app in ios_list:
        ios_app_ids = ios_app_ids + str(ios_app) + ','
    ios_app_ids = ios_app_ids[0:-1]

    url = f'https://api.sensortower.com/v1/ios/usage/session_duration?app_ids={ios_app_ids}&date_granularity=monthly&start_date=2021-01-01&end_date={date}&auth_token={token}'
    response = requests.request("GET", url)
    result = json.loads(response.text)['app_data']

    all_data = []
    for stat in result:
        app_id = stat['app_id']
        app_name = ios_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'sessionDuration': stat['average_session_duration']
        }
        all_data.append(data)

    fields = ['appID', 'appName', 'date', 'timePeriod', 'sessionDuration']

    with open('iosSessionDuration.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# 
def AndroidScriptSessionDuration(android_list, token, date):
    android_app_ids = ''
    for android_app in android_list:
        android_app_ids = android_app_ids + str(android_app) + ','
    android_app_ids = android_app_ids[0:-1]

    url = f'https://api.sensortower.com/v1/android/usage/session_duration?app_ids={android_app_ids}&date_granularity=monthly&start_date=2021-01-01&end_date={date}&auth_token={token}'
    response = requests.request("GET", url)
    result = json.loads(response.text)

    all_data = []
    for stat in result['app_data']:
        app_id = stat['app_id']
        app_name = android_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'sessionDuration': stat['average_session_duration']
        }
        all_data.append(data)

    fields = ['appID', 'appName', 'date', 'timePeriod', 'sessionDuration']

    with open('androidSessionDuration.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# 
def IosScriptTimeSpent(ios_list, token, date):
    ios_app_ids = ''
    for ios_app in ios_list:
        ios_app_ids = ios_app_ids + str(ios_app) + ','
    ios_app_ids = ios_app_ids[0:-1]

    url = f'https://api.sensortower.com/v1/ios/usage/time_spent?app_ids={ios_app_ids}&date_granularity=monthly&start_date=2021-01-01&end_date={date}&auth_token={token}'
    response = requests.request("GET", url)
    result = json.loads(response.text)

    all_data = []
    for stat in result['app_data']['day']:
        app_id = stat['app_id']
        app_name = ios_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'timeSpent': stat['average_time_spent_per_user']
        }
        all_data.append(data)

    for stat in result['app_data']['week']:
        app_id = stat['app_id']
        app_name = ios_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'timeSpent': stat['average_time_spent_per_user']
        }
        all_data.append(data)

    for stat in result['app_data']['month']:
        app_id = stat['app_id']
        app_name = ios_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'timeSpent': stat['average_time_spent_per_user']
        }
        all_data.append(data)

    fields = ['appID', 'appName', 'date', 'timePeriod', 'timeSpent']

    with open('iosTimeSpent.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# 
def AndroidScriptTimeSpent(android_list, token, date):
    android_app_ids = ''
    for android_app in android_list:
        android_app_ids = android_app_ids + str(android_app) + ','
    android_app_ids = android_app_ids[0:-1]

    url = f'https://api.sensortower.com/v1/android/usage/time_spent?app_ids={android_app_ids}&date_granularity=monthly&start_date=2021-01-01&end_date={date}&auth_token={token}'
    response = requests.request("GET", url)
    result = json.loads(response.text)

    all_data = []
    for stat in result['app_data']['day']:
        app_id = stat['app_id']
        app_name = android_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'timeSpent': stat['average_time_spent_per_user']
        }
        all_data.append(data)

    for stat in result['app_data']['week']:
        app_id = stat['app_id']
        app_name = android_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'timeSpent': stat['average_time_spent_per_user']
        }
        all_data.append(data)

    for stat in result['app_data']['month']:
        app_id = stat['app_id']
        app_name = android_list[app_id]
        data = {
            'appID': app_id,
            'appName': app_name,
            'date': stat['date'],
            'timePeriod': stat['time_period'],
            'timeSpent': stat['average_time_spent_per_user']
        }
        all_data.append(data)

    fields = ['appID', 'appName', 'date', 'timePeriod', 'timeSpent']

    with open('androidTimeSpent.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

