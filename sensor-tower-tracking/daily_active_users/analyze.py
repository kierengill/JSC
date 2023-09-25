'''Generate moving average statistics of combined app DAUs'''

import csv
import pandas as pd

# calculate thirty, ninety, and three sixty five day moving averages and more
def RunScript(category):
    df = pd.read_csv('aggregatedDAUs.csv')
    lendf = len(df)

    row = 0
    all_data = []

    monthly_size = 30
    quarterly_size = 90
    yearly_size = 365

    monthly_averages = []
    monthly_moving = []

    quarterly_averages = []
    quarterly_moving = []

    yearly_averages = []
    yearly_moving = []

    saved_app = ''
    app_row = 0

    while row < lendf:
        if df.iloc[row][0] != saved_app:
            app_row = 0

            monthly_averages = []
            monthly_moving = []

            quarterly_averages = []
            quarterly_moving = []

            yearly_averages = []
            yearly_moving = []

            saved_app = df.iloc[row][0]
            app_row = 0

        monthly_averages.append(df.iloc[row][2])
        quarterly_averages.append(df.iloc[row][2])
        yearly_averages.append(df.iloc[row][2])

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
            if (monthly_moving[app_row - 7] == 0
                    or monthly_moving[app_row - 7] == None):
                wow_thirty_dma = None
            else:
                diff = monthly_moving[app_row] - monthly_moving[app_row - 7]
                wow_thirty_dma = (diff)/(monthly_moving[app_row - 7])
        else:
            wow_thirty_dma = None

        if len(monthly_moving) >= 366:
            if (monthly_moving[app_row - 365] == 0
                    or monthly_moving[app_row - 365] == None):
                yoy_thirty_dma = None
            else:
                diff = monthly_moving[app_row] - monthly_moving[app_row - 365]
                yoy_thirty_dma = (diff)/(monthly_moving[app_row - 365])
        else:
            yoy_thirty_dma = None

        if len(quarterly_moving) >= 8:
            if (quarterly_moving[app_row - 7] == 0
                    or quarterly_moving[app_row - 7] == None):
                wow_ninety_dma = None
            else:
                diff = quarterly_moving[app_row] - quarterly_moving[app_row - 7]
                wow_ninety_dma = (diff)/(quarterly_moving[app_row - 7])
        else:
            wow_ninety_dma = None

        if len(quarterly_moving) >= 366:
            if (quarterly_moving[app_row - 365] == 0
                    or quarterly_moving[app_row - 365] == None):
                yoy_ninety_dma = None
            else:
                diff = quarterly_moving[app_row] - quarterly_moving[app_row - 365]
                yoy_ninety_dma = (diff)/(quarterly_moving[app_row - 365])
        else:
            yoy_ninety_dma = None

        data = {
            'category': category,
            'app': df.iloc[row][0],
            'date': df.iloc[row][1],
            'DAUs': df.iloc[row][2],
            '30DMA': thirty_dma,
            '90DMA': ninety_dma,
            '365DMA': yearly_dma,
            'wow30DMA': wow_thirty_dma,
            'yoy30DMA': yoy_thirty_dma,
            'wow90DMA': wow_ninety_dma,
            'yoy90DMA': yoy_ninety_dma
        }
        all_data.append(data)

        app_row += 1
        row += 1

    return all_data

# write calculated daily active users data to a CSV file
def WriteAll(category):
    data_list = RunScript(category)

    fields = ['category', 'app', 'date', 'DAUs', '30DMA', '90DMA', '365DMA',
        'wow30DMA', 'yoy30DMA', 'wow90DMA', 'yoy90DMA']

    with open('outputDAUs.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(data_list)

# filter out data points older than the inputed date in the calculated data CSV
def UpdateAll(last_date):
    df = pd.read_csv('outputDAUs.csv')
    lendf = len(df)

    all_data = []
    row = 0
    while row < lendf:
        if str(df.iloc[row][2]) >= last_date:
            data = {
                'category': df.iloc[row][0],
                'app': df.iloc[row][1],
                'date': df.iloc[row][2],
                'DAUs': df.iloc[row][3],
                '30DMA': df.iloc[row][4],
                '90DMA': df.iloc[row][5],
                '365DMA': df.iloc[row][6],
                'wow30DMA': df.iloc[row][7],
                'yoy30DMA': df.iloc[row][8],
                'wow90DMA': df.iloc[row][9],
                'yoy90DMA': df.iloc[row][10]
            }
            all_data.append(data)
        row += 1

    fields = ['category', 'app', 'date', 'DAUs', '30DMA', '90DMA', '365DMA',
        'wow30DMA', 'yoy30DMA', 'wow90DMA', 'yoy90DMA']

    with open('outputDAUs.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(all_data)

