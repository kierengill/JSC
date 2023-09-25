'''Generate moving average statistics of combined app revenue and downloads'''

import csv
import pandas as pd

# merge the aggregated revenue and downloads csv files into a single file
def Merge():
    a = pd.read_csv("aggregatedRevenue.csv")
    b = pd.read_csv("aggregatedDownloads.csv")

    b = b.dropna(axis=1)
    merge = a.merge(b)
    merge.to_csv("mergedRevenueDownloads.csv", index=False)

# write calculated revenue and downloads data to a CSV file
def WriteAll(category):
    df = pd.read_csv("mergedRevenueDownloads.csv")
    lendf = len(df)

    all_data = []
    saved_app = ''
    app_index = 0

    i = 0
    while i < lendf:
        if saved_app != df.iloc[i][0]:
            yoy_rev = []
            yoy_down = []

            saved_app = df.iloc[i][0]
            app_index = 0

        yoy_rev.append(df.iloc[i][2])
        yoy_down.append(df.iloc[i][3])

        if len(yoy_rev) >= 53:
            if yoy_rev[app_index - 52] == 0 or yoy_rev[app_index - 52] == None:
                yoy_weekly_revenue = None
            else:
                diff = yoy_rev[app_index] - yoy_rev[app_index - 52]
                yoy_weekly_revenue = (diff)/(yoy_rev[app_index - 52])
        else: 
            yoy_weekly_revenue = None

        if len(yoy_down) >= 53:
            if (yoy_down[app_index - 52] == 0
                    or yoy_down[app_index - 52] == None):
                yoy_weekly_downloads = None
            else:
                diff = yoy_down[app_index] - yoy_down[app_index - 52]
                yoy_weekly_downloads = (diff)/(yoy_down[app_index - 52])
        else: 
            yoy_weekly_downloads = None

        day = {
            'category': category,
            'app': df.iloc[i][0],
            'date': df.iloc[i][1],
            'weeklyRevenue': df.iloc[i][2],
            'weeklyDownloads': df.iloc[i][3],
            'yoyWeeklyRevenue': yoy_weekly_revenue,
            'yoyWeeklyDownloads': yoy_weekly_downloads,
        }

        all_data.append(day)
        app_index += 1
        i += 1

    fields = ['category', 'app', 'date', 'weeklyRevenue', 'weeklyDownloads',
        'yoyWeeklyRevenue', 'yoyWeeklyDownloads']

    with open('outputRevenueDownloads.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# filter out data points that are not equal to the inputed date
def UpdateAll(date):
    df = pd.read_csv("outputRevenueDownloads.csv")
    lendf = len(df)

    all_data = []
    i = 0
    while i < lendf:
        if df.iloc[i][2] == date:
            day = {
                'category': df.iloc[i][0],
                'app': df.iloc[i][1],
                'date': df.iloc[i][2],
                'weeklyRevenue': df.iloc[i][3],
                'weeklyDownloads': df.iloc[i][4],
                'yoyWeeklyRevenue': df.iloc[i][5],
                'yoyWeeklyDownloads': df.iloc[i][6],
            }

            all_data.append(day)
        i += 1
    
    fields = ['category', 'app', 'date', 'weeklyRevenue', 'weeklyDownloads',
        'yoyWeeklyRevenue', 'yoyWeeklyDownloads']

    with open('outputRevenueDownloads.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

