'''Scrapes on sale listings from Dicks Sporting Goods website'''

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

    driver.get(url_list[index])
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    num_listings = soup.find_all('span', {'class': 'rs-page-count-label'})[1]
    num_listings = num_listings.text.split(" ")[0]

    split_name = url_names[index].split("_")
    listings = soup.find_all('div', {'class': 'dsg-flex flex-column dsg-react-product-card rs_product_card dsg-react-product-card-col-4'})
    items = []
    for listing in listings:
        unlisted = listing.find('p', {'class': 'unlisted-price'})
        was_price = listing.find('p', {'class': 'was-price'})
        if unlisted == None and was_price != None:
            original = was_price.text.replace(" ", "").replace("$", "")
            original = original.replace("WAS:", "").replace("*", "").split("-")
            if len(original) == 2:
                full_price = (float(original[0]) + float(original[1]))/2
            else:
                full_price = float(original[0])

            new = listing.find('p', {'class': 'offer-price'}).text
            new = new.replace(" ", "").replace("$", "").split("-")
            if len(new) == 2:
                sale_price = (float(new[0]) + float(new[1]))/2
            else:
                sale_price = float(new[0])

            product = {
                'brand': "Dick's Sporting Goods",
                'category': str(split_name[0]),
                'product': str(split_name[1]),
                'fullPrice': float(full_price),
                'salePrice': float(sale_price),
                'salePercentOff': float((full_price - sale_price)/full_price),
                'numListings': int(num_listings)
            }
            items.append(product)

    fields = ['brand', 'category', 'product', 'fullPrice', 'salePrice',
        'salePercentOff', 'numListings']
    with open(f'{url_names[index]}.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(items)

    driver.quit()

# generate csv file for all products from every category
def RunScript():
    for i in range(len(urls.catalog_list_urls)):
        threads = []
        for j in range(len(urls.catalog_list_urls[i])):
            browser_thread = threading.Thread(target=RunScraper, args=(urls.catalog_list_urls[i], urls.catalog_list_url_names[i], j))
            browser_thread.start()
            threads.append(browser_thread)

        for thread in threads:
            thread.join()

        print("Category Finished!")
    print("Everything is Finished!")

