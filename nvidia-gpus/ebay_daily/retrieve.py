'''Scrapes eBay for current Nvidia GPU listings'''

from bs4 import BeautifulSoup
import csv
from datetime import date
import requests

import ebay_daily.urls_daily

URLS = ebay_daily.urls_daily.urls
URL_NAMES = ebay_daily.urls_daily.url_names

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
def ParseWebData(soup, model, memory, condition):
    # find every listing container from the html data
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    listings = []

    # loop through every listing found
    for item in results:
        # make sure the item is in fact a listing
        #if item.find('h3', {'class': 's-item__title'}) != None:
        if item.find('span',{'aria-level': '3', 'role' : 'heading'}) != None:
            #title = item.find('h3', {'class': 's-item__title'}).text
            title = item.find('span',{'aria-level': '3', 'role' : 'heading'}).text
            price = item.find('span', {'class': 's-item__price'}).text[1:]
            price = price.replace(",", "").replace("U $", "")
            link = item.find('a', {'class': 's-item__link'})['href']
            try:
                float(price)
            except ValueError:
                continue
            product = {
                'marketplace': 'eBay',
                'model': str(model),
                'memory': str(memory),
                'condition': str(condition),
                'title': str(title),
                'price': float(price),
                'date': date.today(),
                'link': link
            }
            listings.append(product)
    return listings

# write csv files of all the retrieved eBay Nvidia GPU listings
def WriteFiles():
    fields = ['marketplace', 'model', 'memory', 'condition', 'title', 'price',
        'date', 'link']

    # loop through every url
    for i in range(len(URLS)):
        soup = GetData(URLS[i])
        model, memory, condition = ParseURLName(URL_NAMES[i])
        productList = ParseWebData(soup, model, memory, condition)

        # write a csv file with the generated listings
        with open(f"{URL_NAMES[i]}.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(productList)

