'''Splits 3070 and 3090 GPU files into Ti and non-Ti files'''

import csv
import pandas as pd

FIELDS = ['marketplace', 'model', 'memory', 'condition', 'title', 'price', 'date', 'link']

# write the listing data of the given dataframe's row into a dictionary
def WriteListingData(df, i):
    listing = {
        'marketplace': str(df.iloc[i][0]),
        'model': str(df.iloc[i][1]),
        'memory': int(df.iloc[i][2]),
        'condition': str(df.iloc[i][3]),
        'title': str(df.iloc[i][4]),
        'price': float(df.iloc[i][5]),
        'date': df.iloc[i][6],
        'link': df.iloc[i][7]
    }
    return listing

# split 3090 new data into Ti and non-Ti files
def SplitEbay3090New():
    df = pd.read_csv("ebay_3090_24_new_past.csv")
    lendf = len(df)

    listings = []
    i = 0

    # loop through the entire length of the dataframe
    while i < lendf:
        # check to see if the listing is a Ti model
        if "ti " in str(df.iat[i,4]).lower():
            listings.append(WriteListingData(df, i))

            # drop the row from the dataframe and manipulate the indices so that
            # the original dataframe does not contain Ti listings
            df.drop(df.index[i], inplace=True)
            lendf -= 1
            i -= 1

        i += 1

    # write the split Ti data to a new file
    with open ('ebay_3090Ti_24_new_past.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = FIELDS)
        writer.writeheader()
        writer.writerows(listings)

    # commit the edited csv that contains non-Ti listings to the original file
    df.to_csv("ebay_3090_24_new_past.csv", index=False)

# split 3090 used data into Ti and non-Ti files
def SplitEbay3090Used():
    df = pd.read_csv("ebay_3090_24_used_past.csv")
    lendf = len(df)

    listings = []
    i = 0

    # loop through the entire length of the dataframe
    while i < lendf:
        # check to see if the listing is a Ti model
        if "ti " in str(df.iat[i,4]).lower():
            listings.append(WriteListingData(df, i))

            # drop the row from the dataframe and manipulate the indices so that
            # the original dataframe does not contain Ti listings
            df.drop(df.index[i], inplace=True)
            lendf -= 1
            i -= 1
        i += 1

    # write the split Ti data to a new file
    with open ('ebay_3090Ti_24_used_past.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = FIELDS)
        writer.writeheader()
        writer.writerows(listings)
    
    # commit the edited csv that contains non-Ti listings to the original file
    df.to_csv("ebay_3090_24_used_past.csv", index=False)

# split 3070 new data into Ti and non-Ti files
def SplitEbay3070New():
    df = pd.read_csv("ebay_3070_8_new_past.csv")
    lendf = len(df)

    listings = []
    i = 0

    # loop through the entire length of the dataframe
    while i < lendf:
        # check to see if the listing is a Ti model
        if "ti " in str(df.iat[i,4]).lower():
            listings.append(WriteListingData(df, i))

            # drop the row from the dataframe and manipulate the indices so that
            # the original dataframe does not contain Ti listings
            df.drop(df.index[i], inplace=True)
            lendf -= 1
            i -= 1
        i += 1
        
    # write the split Ti data to a new file
    with open ('ebay_3070Ti_8_new_past.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = FIELDS)
        writer.writeheader()
        writer.writerows(listings)

    # commit the edited csv that contains non-Ti listings to the original file
    df.to_csv("ebay_3070_8_new_past.csv", index=False)

# split 3070 used data into Ti and non-Ti files
def SplitEbay3070Used():
    df = pd.read_csv("ebay_3070_8_used_past.csv")
    lendf = len(df)

    listings = []
    i = 0

    # loop through the entire length of the dataframe
    while i < lendf:
        # check to see if the listing is a Ti model
        if "ti " in str(df.iat[i,4]).lower():
            listings.append(WriteListingData(df, i))

            # drop the row from the dataframe and manipulate the indices so that
            # the original dataframe does not contain Ti listings
            df.drop(df.index[i], inplace=True)
            lendf -= 1
            i -= 1
        i += 1
    
    # write the split Ti data to a new file
    with open ('ebay_3070Ti_8_used_past.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = FIELDS)
        writer.writeheader()
        writer.writerows(listings)

    # commit the edited csv that contains non-Ti listings to the original file
    df.to_csv("ebay_3070_8_used_past.csv", index=False)

# run scripts to split 3070 and 3090 new and used data into Ti and non-Ti files
def SplitAll():
    SplitEbay3090New()
    SplitEbay3090Used()
    SplitEbay3070New()
    SplitEbay3070Used()

