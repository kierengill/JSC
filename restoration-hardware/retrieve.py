'''Scrapes on sale listings from RH website'''

from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import threading
from webdriver_manager.chrome import ChromeDriverManager

import urls

# generate csv file of all listings given a category and product
def RunScraper(url_list, url_names, index):
    # initiate driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    url = url_list[index]
    driver.get(url)
    print("Page loaded")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    confirm = input(f"Finished scrolling to load {url_names[index]}? Input 'y' if completed:")
    while confirm.lower() != 'y':
        confirm = input(f"Finished scrolling to load {url_names[index]}? Input 'y' if completed:")
    print(f"Finished scrolling {url_names[index]}")

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.find_all('div', {'style': 'background-color: rgb(249, 247, 244);'})

    listings = []
    length = int(len(products))
    split_name = url_names[index].split("_")

    for i in range(length):
        prices = products[i].find_all('p', {'id': 'price'})
        if len(prices) != 3:
            continue
        regular_price = int(prices[0].text[1:])
        final_sale_price = int(prices[1].text[1:])
        member_price = int(prices[2].text[1:])
        final_sale_percent_off = (regular_price-final_sale_price)/regular_price

        item = {
            'brand': str(split_name[0]),
            'catalog': str(split_name[1]),
            'category': str(split_name[2]),
            'product':  str(split_name[3]),
            'regularPrice': float(regular_price),
            'finalSalePrice': float(final_sale_price),
            'memberPrice': float(member_price),
            'finalSalePercentOff': float(final_sale_percent_off)
        }
        listings.append(item)

    fields = ['brand', 'catalog', 'category', 'product', 'regularPrice',
        'finalSalePrice', 'memberPrice', 'finalSalePercentOff']
    with open(f'{url_names[index]}.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(listings)
        
    driver.quit()

# generate csv file for all products from every category
def RunScript():
    for i in range(len(urls.catalog_list_urls)):
        threads = []
        confirm = input("Type 'continue' to proceed:")
        while confirm.lower() != 'continue':
            confirm = input("Type 'continue' to proceed:")
        for j in range(len(urls.catalog_list_urls[i])):
            browser_thread = threading.Thread(target=RunScraper, args=(urls.catalog_list_urls[i], urls.caltalog_list_url_names[i], j))
            browser_thread.start()
            threads.append(browser_thread)

        for thread in threads:
            thread.join()

        print("Category Finished!")
    print("Everything is Finished!")

