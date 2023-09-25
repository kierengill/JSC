'''Scrapes eBay for sold Nvidia 30 Series GPUs going back 3 months'''

from bs4 import BeautifulSoup
import csv
import datetime
from datetime import timedelta
import requests

import ebay_historic.urls_historic

# dictionary of month abbreviations and corresponding month numbers
MONTHS = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

# import the urls list and the urls names list
URLS = ebay_historic.urls_historic.urls
URL_NAMES = ebay_historic.urls_historic.url_names

# return html data ready to be parsed
def GetData(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

# return  model, memory size, and condition of GPU based on the URL name
def ParseURLName(url_name):
    split_url = url_name.split('_')
    model = split_url[1]
    memory = split_url[2]
    condition = split_url[3]
    return model, memory, condition

# return all listings from the html data based on the given characteristics
def ParseWebData(soup, model, memory, condition, update):
    # find every listing container from the html data
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    listings = []

    # counter is used to ignore the first item container in results since it is
    # not an actual product listing and would otherwise through an error
    counter = 0

    # loop through every listing found 
    for item in results:
        # make sure the item is in fact a listing
        if counter != 0:
            # get the date from the item container
            date = item.find('div', {'class': 's-item__title--tag'})
            date = date.find('span', {'class': 'POSITIVE'}).text[6:]
            day = int(date[4:6].replace(",", ""))
            month = int(MONTHS[date[0:3]])
            year = int(date.split(',')[1].strip())

            # get the title, price, and like from the item container
            #title = item.find('h3', {'class': 's-item__title s-item__title--has-tags'}).text
            title = item.find('span',{'aria-level': '3', 'role' : 'heading'}).text
            price = item.find('span', {'class': 's-item__price'}).text[1:]
            price = price.replace(",", "")
            link = item.find('a', {'class': 's-item__link'})['href']
            
            yesterday = datetime.date.today() - timedelta(days=1)
            
            # create the listing entry
            if update and (datetime.date(year, month, day) == yesterday):
                product = {
                    'marketplace': 'eBay',
                    'model': str(model),
                    'memory': int(memory),
                    'condition': str(condition),
                    'title': str(title),
                    'price': float(price),
                    'date': datetime.date(year, month, day),
                    'link': link
                }
                listings.append(product)

            elif not update:
                # create the listing entry
                product = {
                    'marketplace': 'eBay',
                    'model': str(model),
                    'memory': int(memory),
                    'condition': str(condition),
                    'title': str(title),
                    'price': float(price),
                    'date': datetime.date(year, month, day),
                    'link': link
                }
                listings.append(product)
        else:
            counter += 1
    
    return listings

# write csv files of all the retrieved eBay Nvidia GPU listings
def WriteFiles(update):
    fields = ['marketplace', 'model', 'memory', 'condition', 'title', 'price',
        'date', 'link']

    # loop through every url
    for i in range(len(URLS)):
        soup = GetData(URLS[i])
        model, memory, condition = ParseURLName(URL_NAMES[i])
        productList = ParseWebData(soup, model, memory, condition, update)

        # write a csv file with the generated listings
        with open(f"{URL_NAMES[i]}.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(productList)

