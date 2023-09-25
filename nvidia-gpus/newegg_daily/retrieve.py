'''Scrapes Newegg for current Nvidia GPU listings'''

from bs4 import BeautifulSoup
import csv
from datetime import date
import requests

import newegg_daily.urls_daily

URLS = newegg_daily.urls_daily.urls
URL_NAMES = newegg_daily.urls_daily.url_names

# return html data ready to be parsed
def GetData(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

# return  model, memory size, and condition of GPU based on URL name
def ParseURLName(url_name):
    split_url = url_name.split('_')
    model = split_url[1]
    memory = split_url[2]
    condition = split_url[3]
    return model, memory, condition

# return list of products listed from html data based on given characteristics
def ParseWebData(soup, model, memory, condition):
    results = soup.find_all('div', {'class': 'item-cell'})
    listings = []

    # loop through every listing found 
    for item in results:
        # make sure the item is in fact a listing and not out of stock
        out_of_stock = item.find('span', {'class': 'btn btn-message btn-mini'})
        if out_of_stock != None:
            out_of_stock_text = out_of_stock.text.lower().replace(" ", "")

        if out_of_stock == None or out_of_stock_text != "outofstock":
            if item.find('li', {'class': 'price-current'}) != None:

                num_listings = 1
                if item.find('a', {'class': 'price-current-num'}) != None:
                    num_listings = item.find('a', {'class': 'price-current-num'})
                    num_listings = num_listings.text.split(" ")[0][1:]

                price_current = item.find('li', {'class': 'price-current'}).text
                price_current = price_current.split('\xa0')[0]
                price_current = price_current.replace(",","")[1:]
                if price_current == "":
                    price_was = item.find('li', {'class': 'price-was'}).text
                    price_was = price_was.split('\xa0')[0].replace(",","")[1:]
                    try:
                        price = float(price_was)
                    except:
                        print("Exception in converting price_was to float")
                else:
                    price = float(price_current)
                
                title = item.find('a', {'class': 'item-title'}).text
                link = item.find('a', {'class': 'item-title'})['href']

                product = {
                    'marketplace': 'Newegg',
                    'model': str(model),
                    'memory': str(memory),
                    'condition': str(condition),
                    'title': str(title),
                    'price': float(price),
                    'date': date.today(),
                    'link': link,
                    'numListings': int(num_listings)
                }
                listings.append(product)
    return listings

# write csv files of all Newegg Nvidia GPU listings
def WriteFiles():
    fields = ['marketplace', 'model', 'memory', 'condition', 'title', 'price',
        'date', 'link', 'numListings']

    # loop through every url
    for i in range(len(URLS)):
        soup = GetData(URLS[i])
        model, memory, condition = ParseURLName(URL_NAMES[i])
        listings = ParseWebData(soup, model, memory, condition)

        # write a csv file with the generated listings
        with open(f"{URL_NAMES[i]}.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(listings)

