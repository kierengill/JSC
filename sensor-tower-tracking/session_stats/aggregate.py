''''''

import csv
import json
import pandas as pd

# 
def AggregateSessionCount():
    json_data = {}

    df = pd.read_csv('iosSessionCount.csv')
    row = 0

    while row < len(df):
        one = str(df.iloc[row][1])
        two = str(df.iloc[row][2])
        three = str(df.iloc[row][3])
        four = float(df.iloc[row][4])
        try:
            json_data[one][two][three] = four
        except:
            try:
                json_data[one][two] = {three: four}
            except:
                json_data[one] = {two: {three: four}}

        row += 1

    df = pd.read_csv('androidSessionCount.csv')
    row2 = 0

    while row2 < len(df):
        one = str(df.iloc[row2][1])
        two = str(df.iloc[row2][2])
        three = str(df.iloc[row2][3])
        four = float(df.iloc[row2][4])
        try:
            try:
                json_data[one][two][three] += four
                json_data[one][two][three] /= 2
            except:
                json_data[one][two][three] = four
        except:
            try:
                json_data[one][two] = {three: four}
            except:
                json_data[one] = {two: {three: four}}

        row2 += 1

    json_object = json.dumps(json_data, indent = 4)
    with open("aggregatedSessionCount.json", "w") as outfile:
        outfile.write(json_object)

# 
def AggregateSessionDuration():
    json_data = {}

    df = pd.read_csv('iosSessionDuration.csv')
    row = 0

    while row < len(df):
        one = str(df.iloc[row][1])
        two = str(df.iloc[row][2])
        four = float(df.iloc[row][4])
        try:
            json_data[one]['Session Duration'][two] = four
        except:
            json_data[one] = {'Session Duration': {two: four}}

        row += 1

    df = pd.read_csv('androidSessionDuration.csv')
    row2 = 0

    while row2 < len(df):
        one = str(df.iloc[row2][1])
        two = str(df.iloc[row2][2])
        four = float(df.iloc[row2][4])
        try:
            try:
                json_data[one]['Session Duration'][two] += four
                json_data[one]['Session Duration'][two] /= 2

            except:
                json_data[one]['Session Duration'][two] = four
        except:
            try:
                json_data[one]['Session Duration'][two] = four
            except:
                json_data[one] = {'Session Duration': {two: four}}

        row2 += 1

    json_object = json.dumps(json_data, indent = 4)
    with open("aggregatedSessionDuration.json", "w") as outfile:
        outfile.write(json_object)

# 
def AggregateTimeSpent():
    json_data = {}

    df = pd.read_csv('iosTimeSpent.csv')
    row = 0

    while row < len(df):
        one = str(df.iloc[row][1])
        two = str(df.iloc[row][2])
        three = str(df.iloc[row][3])
        four = float(df.iloc[row][4])
        try:
            json_data[one][two][three] = four
        except:
            try:
                json_data[one][two] = {three: four}
            except:
                json_data[one] = {two: {three: four}}

        row += 1

    df = pd.read_csv('androidTimeSpent.csv')
    row2 = 0

    while row2 < len(df):
        one = str(df.iloc[row2][1])
        two = str(df.iloc[row2][2])
        three = str(df.iloc[row2][3])
        four = float(df.iloc[row2][4])
        try:
            try:
                json_data[one][two][three] += four
                json_data[one][two][three] /= 2
            except:
                json_data[one][two][three] = four
        except:
            try:
                json_data[one][two] = {three: four}
            except:
                json_data[one] = {two: {three: four}}

        row2 += 1

    json_object = json.dumps(json_data, indent = 4)
    with open("aggregatedTimeSpent.json", "w") as outfile:
        outfile.write(json_object)

# 
def RunScriptSessionCount():
    combined = open('aggregatedSessionCount.json')
    data = json.load(combined)

    all_data = []
    for comp in data:
        for date in sorted(data[comp].keys()):
            period_stats = []
            for period in data[comp][date]:
                period_stats.append(data[comp][date][period])
                
            stat = {
                'app': comp,
                'date': date[:-10],
                'day': period_stats[0],
                'week': period_stats[1],
                'month': period_stats[2],
            }
            all_data.append(stat)

    fields = ['app', 'date', 'day', 'week', 'month']
    with open('aggregatedSessionCount.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_data)

# 
def RunScriptSessionDuration():
    combined = open('aggregatedSessionDuration.json')
    data = json.load(combined)

    all_data = []
    for comp in data:
        for date in sorted(data[comp]['Session Duration'].keys()):
            stat = {
                'app': comp,
                'date': date[:-10],
                'sessionDuration': data[comp]['Session Duration'][date],
            }
            all_data.append(stat)

    fields = ['app', 'date', 'sessionDuration']
    with open('aggregatedSessionDuration.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_data)

# 
def RunScriptTimeSpent():
    combined = open('aggregatedTimeSpent.json')
    data = json.load(combined)

    all_data = []
    for comp in data:
        for date in sorted(data[comp].keys()):
            period_stats = []
            for period in data[comp][date]:
                period_stats.append(data[comp][date][period])
                
            stat = {
                'app': comp,
                'date': date[:-10],
                'dayTime': period_stats[0],
                'weekTime': period_stats[1],
                'monthTime': period_stats[2],
            }
            all_data.append(stat)

    fields = ['app', 'date', 'dayTime', 'weekTime', 'monthTime']
    with open('aggregatedTimeSpent.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_data)

