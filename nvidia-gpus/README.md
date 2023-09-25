# Nvidia GPU Tracker
Track Nvidia GeForce RTX 30 Series GPUs starting from late February for sold GPUs and beginning in late May for current listing prices

Marketplaces: eBay for historic sales prices and eBay, Newegg, and StockX for daily listing prices

GPUs tracked: 3060, 3060 Ti, 3070, 3070 Ti, 3080, 3080 Ti, 3090, 3090 Ti

GPU conditions: new and used for eBay data, new for Newegg and StockX

MSRPs are recorded for each model

Note: Daily number of listings is primarily based on Newegg data

## eBay Historic
### ebay_historic.py
Scrapes data from approximately the last three months on eBay of GPUs sold and writes the data to csv files for each model and condition pair

### clean_ebay_historic.py
Splits the 3070 and 3090 new and used datasets into files that contain GPU data on Ti models and non-Ti models

## eBay Historic Cleaned
### ebay_historic_clean.tfl
Cleans eBay historic datasets in Data Tableau Prep by excluding bad data
Not to be used directly again; however, if historic data is collected in a similar fashion, the data should be cleaned

### ebay_historic_aggregation.py
Takes in all historic eBay datasets and aggregates the data into a single csv file

## eBay Historic Updates
### ebay_historic_update.py
Scrapes data from the previous day on eBay of GPUs sold and writes the data to csv files for each model and condition pair

### clean_ebay_historic_update.py
Splits the 3070 and 3090 new and used datasets into files that contain GPU data on Ti models and non-Ti models

### ebay_historic_updates_aggregation.py
Takes in all daily historic eBay datasets and aggregates the data into a single csv file

## eBay Daily
### ebay_daily.py
Scrapes data from the current day on eBay of GPUs listed for sale and writes the data to csv files for each model and condition pair

### clean_ebay_daily.py
Splits the 3070 and 3090 new and used datasets into files that contain GPU data on Ti models and non-Ti models

### ebay_daily_normalized.py
Takes in all daily eBay listing datasets and aggregates the data into meaningful fields and statistics written to a single csv file

## Newegg Daily
### newegg_daily.py
Scrapes data from the current day on Newegg of GPUs listed for sale and writes the data to csv files for each model and condition pair

### newegg_daily_normalized.py
Takes in all daily Newegg listing datasets and aggregates the data into meaningful fields and statistics written to a single csv file

## StockX Daily
### stockx_daily.py
Scrapes data from the current day on StockX of GPUs listed for sale and writes the data to csv files for each model and condition pair

### stockx_daily_normalized.py
Takes in all daily StockX listing datasets and aggregates the data into meaningful fields and statistics written to a single csv file

## Automated Script
### automated_script.py
Runs all of the programs sequentially generating appropriate csv files and importing them into MongoDB Atlas

# Running the automated script

1) Run the script by running runAll with test = False and appropriate username and password
2) Make sure everything ran smoothly and check MongoDB Atlas for quality and correctness