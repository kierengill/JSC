''''''

import csv
import pandas as pd

# 
def Merge():
    a = pd.read_csv("aggregatedSessionCount.csv")
    b = pd.read_csv("aggregatedSessionDuration.csv")

    b = b.dropna(axis=1)
    first_merge = a.merge(b)
    first_merge.to_csv("firstMergeSessionStats.csv", index=False)

    c = pd.read_csv("aggregatedTimeSpent.csv")
    c = c.dropna(axis=1)
    merge = first_merge.merge(c)
    merge.to_csv("mergedSessionStats.csv", index=False)

# 
def WriteAll(category):
    df = pd.read_csv("mergedSessionStats.csv")
    lendf = len(df)

    all_data = []
    saved_app = ''
    app_index = 0

    i = 0
    while i < lendf:
        if saved_app != df.iloc[i][0]:
            yoy_day = []
            yoy_week = []
            yoy_month = []
            yoy_duration = []
            yoy_day_dime = []
            yoy_week_time = []
            yoy_month_time = []

            saved_app = df.iloc[i][0]
            app_index = 0

        yoy_day.append(df.iloc[i][2])
        yoy_week.append(df.iloc[i][3])
        yoy_month.append(df.iloc[i][4])
        yoy_duration.append(df.iloc[i][5])
        yoy_day_dime.append(df.iloc[i][6])
        yoy_week_time.append(df.iloc[i][7])
        yoy_month_time.append(df.iloc[i][8])

        if len(yoy_day) >= 13:
            if yoy_day[app_index - 12] == 0 or yoy_day[app_index - 12] == None:
                yoy_day_session_count = None
            else:
                diff = yoy_day[app_index] - yoy_day[app_index - 12]
                yoy_day_session_count = (diff)/(yoy_day[app_index - 12])
        else: 
            yoy_day_session_count = None

        if len(yoy_week) >= 13:
            if (yoy_week[app_index - 12] == 0
                    or yoy_week[app_index - 12] == None):
                yoy_week_session_count = None
            else:
                diff = yoy_week[app_index] - yoy_week[app_index - 12]
                yoy_week_session_count = (diff)/(yoy_week[app_index - 12])
        else: 
            yoy_week_session_count = None

        if len(yoy_month) >= 13:
            if (yoy_month[app_index - 12] == 0
                    or yoy_month[app_index - 12] == None):
                yoy_month_session_count = None
            else:
                diff = yoy_month[app_index] - yoy_month[app_index - 12]
                yoy_month_session_count = (diff)/(yoy_month[app_index - 12])
        else: 
            yoy_month_session_count = None

        if len(yoy_duration) >= 13:
            if (yoy_duration[app_index - 12] == 0
                    or yoy_duration[app_index - 12] == None):
                yoy_day_session_duration = None
            else:
                diff = yoy_duration[app_index] - yoy_duration[app_index - 12]
                yoy_day_session_duration = (diff)/(yoy_duration[app_index - 12])
        else: 
            yoy_day_session_duration = None

        if len(yoy_day_dime) >= 13:
            if (yoy_day_dime[app_index - 12] == 0
                    or yoy_day_dime[app_index - 12] == None):
                yoy_day_time_spent = None
            else:
                diff = yoy_day_dime[app_index] - yoy_day_dime[app_index - 12]
                yoy_day_time_spent = (diff)/(yoy_day_dime[app_index - 12])
        else: 
            yoy_day_time_spent = None

        if len(yoy_week_time) >= 13:
            if (yoy_week_time[app_index - 12] == 0
                    or yoy_week_time[app_index - 12] == None):
                yoy_week_time_spent = None
            else:
                diff = yoy_week_time[app_index] - yoy_week_time[app_index - 12]
                yoy_week_time_spent = (diff)/(yoy_week_time[app_index - 12])
        else: 
            yoy_week_time_spent = None

        if len(yoy_month_time) >= 13:
            if (yoy_month_time[app_index - 12] == 0
                    or yoy_month_time[app_index - 12] == None):
                yoy_month_time_spent = None
            else:
                diff = yoy_month_time[app_index] - yoy_month_time[app_index-12]
                yoy_month_time_spent = (diff)/(yoy_month_time[app_index - 12])
        else: 
            yoy_month_time_spent = None

        day = {
            'category': category,
            'app': df.iloc[i][0],
            'date': df.iloc[i][1],
            'daySessionCount': df.iloc[i][2],
            'weekSessionCount': df.iloc[i][3],
            'monthSessionCount': df.iloc[i][4],
            'daySessionDuration': df.iloc[i][5],
            'yoyDaySessionCount': yoy_day_session_count,
            'yoyWeekSessionCount': yoy_week_session_count,
            'yoyMonthSessionCount': yoy_month_session_count,
            'yoyDaySessionDuration': yoy_day_session_duration,
            'dayTimeSpent': df.iloc[i][6],
            'weekTimeSpent': df.iloc[i][7],
            'monthTimeSpent': df.iloc[i][8],
            'yoyDayTimeSpent': yoy_day_time_spent,
            'yoyWeekTimeSpent': yoy_week_time_spent,
            'yoyMonthTimeSpent': yoy_month_time_spent,
        }

        all_data.append(day)
        app_index += 1
        i += 1

    fields = ['category', 'app', 'date', 'daySessionCount', 'weekSessionCount',
        'monthSessionCount', 'daySessionDuration', 'yoyDaySessionCount',
        'yoyWeekSessionCount', 'yoyMonthSessionCount', 'yoyDaySessionDuration',
        'dayTimeSpent', 'weekTimeSpent', 'monthTimeSpent', 'yoyDayTimeSpent',
        'yoyWeekTimeSpent', 'yoyMonthTimeSpent']

    with open('outputSessionStats.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

# 
def UpdateAll(date):
    df = pd.read_csv("outputSessionStats.csv")
    lendf = len(df)

    all_data = []
    i = 0
    while i < lendf:
        if df.iloc[i][2] == date:
            day = {
                'category': df.iloc[i][0],
                'app': df.iloc[i][1],
                'date': df.iloc[i][2],
                'daySessionCount': df.iloc[i][3],
                'weekSessionCount': df.iloc[i][4],
                'monthSessionCount': df.iloc[i][5],
                'daySessionDuration': df.iloc[i][6],
                'yoyDaySessionCount': df.iloc[i][7],
                'yoyWeekSessionCount': df.iloc[i][8],
                'yoyMonthSessionCount': df.iloc[i][9],
                'yoyDaySessionDuration': df.iloc[i][10],
                'dayTimeSpent': df.iloc[i][11],
                'weekTimeSpent': df.iloc[i][12],
                'monthTimeSpent': df.iloc[i][13],
                'yoyDayTimeSpent': df.iloc[i][14],
                'yoyWeekTimeSpent': df.iloc[i][15],
                'yoyMonthTimeSpent': df.iloc[i][16],
            }

            all_data.append(day)
        i += 1
    
    fields = ['category', 'app', 'date', 'daySessionCount', 'weekSessionCount',
        'monthSessionCount', 'daySessionDuration', 'yoyDaySessionCount',
        'yoyWeekSessionCount', 'yoyMonthSessionCount', 'yoyDaySessionDuration',
        'dayTimeSpent', 'weekTimeSpent', 'monthTimeSpent', 'yoyDayTimeSpent',
        'yoyWeekTimeSpent', 'yoyMonthTimeSpent']

    with open('outputSessionStats.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

