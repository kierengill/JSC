# Restoration Hardware Tracker

Track listings of products on sale at Restoration Hardware

Number of listings, average percent off, and number of items in each percent off bucket are recorded

## scrape.py

Scrapes data of every product from all categories of Restoration Hardware and writes the data into csv files

## aggregate.py

Reads csv files from every product of each category and generates the relevant statistics for each respective product

# Running the program (scrape.py and aggregate.py)

1. Run runScript() in scrape.py, the program will open up numerous Chrome browsers
2. Wait for each browser to finish loading and scroll to the bottom until every page displays all the listings possible
3. Press the return/enter key, the same number of times as there are browsers open *** important ***
4. Repeat steps 2 and 3 until every product category has been scraped
5. Run importData in aggregate.py with test = False and appropriate username and password
6. Make sure everything ran smoothly and check MongoDB Atlas for quality and correctness