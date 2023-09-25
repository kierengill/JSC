'''Scrapes on sale listings from Williams Sonoma website'''

from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import urls

# generate csv file of all listings given a category and product
def RunScraper(url_list, url_names, index):
    # initiate driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(url_list[index])
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    confirm = input(f"Finished scrolling to load {url_names[index]}? Input 'y' if completed:")
    while confirm.lower() != 'y':
        confirm = input(f"Finished scrolling to load {url_names[index]}? Input 'y' if completed:")

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.find_all('div', {'data-component': 'Shop-GridItem'})

    listings = []
    count = 0
    for item in products:
        if item != None:
            count += 1
            sale = item.find('div', {'class': 'sale-price'})
            suggested = item.find('div', {'class': 'suggested-price'})
            if sale != None and suggested != None:
                sale_amounts = sale.find_all('span', {'class': 'amount'})
                suggested_amounts = suggested.find_all('span', {'class': 'amount'})

                if sale_amounts != None and suggested_amounts != None:
                    if len(sale_amounts) == 2:
                        first = sale_amounts[0].text.replace(",", "")
                        second = sale_amounts[1].text.replace(",", "")
                        sale_price = (float(first) + float(second))/2
                    else:
                        sale_price = sale_amounts[0].text
                        sale_price = float(sale_price.replace(",", ""))

                    if len(suggested_amounts) == 2:
                        first = suggested_amounts[0].text.replace(",", "")
                        second = suggested_amounts[1].text.replace(",", "")
                        regular_price = (float(first) + float(second))/2
                    else:
                        regular_price = suggested_amounts[0].text
                        regular_price = float(regular_price.replace(",", ""))
                    sale_percent_off = (regular_price-sale_price)/regular_price

                    listing = {
                        'brand': 'Williams Sonoma',
                        'category': str(urls.catalog_list_url_names[index]),
                        'regularPrice': float(regular_price),
                        'salePrice': float(sale_price),
                        'salePercentOff': float(sale_percent_off)
                    }
                    listings.append(listing)

    fields = ['brand', 'category', 'regularPrice', 'salePrice', 'salePercentOff']
    with open(f'{url_names[index]}.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(listings)
        
    driver.quit()
    return count

# generate csv file for all products from every category
def RunScript():
    number_of_listings = []
    for i in range(len(urls.catalog_list_urls)):
        number_of_listings.append(RunScraper(urls.catalog_list_urls, urls.catalog_list_url_names, i))
    return(number_of_listings)

