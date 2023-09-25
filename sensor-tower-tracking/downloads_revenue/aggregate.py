'''Aggregates and parse iOS and Andriod revenue and downloads data into CSVs'''

import csv
import json
import pandas as pd

# aggregate iOS and Android downloads data into a single JSON file
def AggregateDownloads():
    json_data = {}

    df = pd.read_csv('iosDownloads.csv')
    row = 0

    while row < len(df):
        one = str(df.iloc[row][1])
        two = str(df.iloc[row][2])
        three = int(df.iloc[row][3])
        try:
            json_data[one]['Downloads'][two] = three
        except:
            json_data[one] = {'Downloads': {two: three}}

        row += 1

    df = pd.read_csv('androidDownloads.csv')
    row2 = 0

    while row2 < len(df):
        one = str(df.iloc[row2][1])
        two = str(df.iloc[row2][2])
        three = int(df.iloc[row2][3])
        try:
            try:
                json_data[one]['Downloads'][two] += three
            except:
                json_data[one]['Downloads'][two] = three
        except:
            json_data[one] = {'Downloads': {two: three}}

        row2 += 1

    json_object = json.dumps(json_data, indent = 4)
    with open("aggregatedDownloads.json", "w") as outfile:
        outfile.write(json_object)

# aggregate iOS and Android revenue data into a single JSON file
def AggregateRevenue():
    json_data = {}

    df = pd.read_csv('iosDownloads.csv')
    row = 0

    while row < len(df):
        one = str(df.iloc[row][1])
        two = str(df.iloc[row][2])
        four = int(df.iloc[row][4])
        try:
            json_data[one]['Revenue'][two] = four
        except:
            json_data[one] = {'Revenue': {two: four}}

        row += 1

    df = pd.read_csv('androidDownloads.csv')
    row2 = 0

    while row2 < len(df):
        one = str(df.iloc[row2][1])
        two = str(df.iloc[row2][2])
        four = int(df.iloc[row2][4])
        try:
            try:
                json_data[one]['Revenue'][two] += four
            except:
                json_data[one]['Revenue'][two] = four
        except:
            json_data[one] = {'Revenue': {two: four}}

        row2 += 1

    json_object = json.dumps(json_data, indent = 4)
    with open("aggregatedRevenue.json", "w") as outfile:
        outfile.write(json_object)

# generate CSV file of aggregated JSON downloads data
def RunScriptDownloads():
    combined = open('aggregatedDownloads.json')
    data = json.load(combined)

    all_data = []
    for comp in data:
        for date in sorted(data[comp]['Downloads'].keys()):
            stat = {
                'app': comp,
                'date': date[:-10],
                'downloads': data[comp]['Downloads'][date],
            }
            all_data.append(stat)

    fields = ['app', 'date', 'downloads']
    with open('aggregatedDownloads.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_data)

# generate CSV file of aggregated JSON revenue data
def RunScriptRevenue():
    combined = open('aggregatedRevenue.json')
    data = json.load(combined)

    all_data = []
    for comp in data:
        for date in sorted(data[comp]['Revenue'].keys()):
            stat = {
                'app': comp,
                'date': date[:-10],
                'revenue': data[comp]['Revenue'][date],
            }
            all_data.append(stat)

    fields = ['app', 'date', 'revenue']
    with open('aggregatedRevenue.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_data)

