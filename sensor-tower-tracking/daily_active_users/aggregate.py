'''Aggregates and parses iOS and Andriod data into JSON and CSV files'''

import csv
import json
import pandas as pd

# aggregate iOS and Android daily active user data into a single JSON file
def Aggregate():
    json_data = {}

    df = pd.read_csv('iosDAUs.csv')
    row = 0

    while row < len(df):
        one = str(df.iloc[row][1])
        two = str(df.iloc[row][2])
        three = int(df.iloc[row][3])
        try:
            json_data[one]['DAUs'][two] = three
        except:
            json_data[one] = {'DAUs': {two: three}}

        row += 1

    df = pd.read_csv('androidDAUs.csv')
    row2 = 0

    while row2 < len(df):
        one = str(df.iloc[row2][1])
        two = str(df.iloc[row2][2])
        three = int(df.iloc[row2][3])
        try:
            try:
                json_data[one]['DAUs'][two] += three
            except:
                json_data[one]['DAUs'][two] = three
        except:
            json_data[one] = {'DAUs': {two: three}}

        row2 += 1

    json_object = json.dumps(json_data, indent = 4)
    with open("aggregatedDAUs.json", "w") as outfile:
        outfile.write(json_object)

# generate CSV file of aggregated JSON data
def Parse():
    combined = open('aggregatedDAUs.json')
    data = json.load(combined)

    all_data = []
    for comp in data:
        for date in sorted(data[comp]['DAUs'].keys()):
            stat = {
                'app': comp,
                'date': date[:-10],
                'DAUs': data[comp]['DAUs'][date]
            }
            all_data.append(stat)

    fields = ['app', 'date', 'DAUs']
    with open('aggregatedDAUs.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_data)

