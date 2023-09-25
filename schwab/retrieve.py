from bs4 import BeautifulSoup
import csv
import datetime
from datetime import timedelta
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
from selenium.webdriver.chrome.options import Options
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date


def TryGetLink(driver, link):
    try:
        driver.get(link)
    except:
        try:
            driver.get(link)
        except:
            time.sleep(1)
            try:
                driver.get(link)
            except:
                time.sleep(3)
                try:
                    driver.get(link)
                except:
                    time.sleep(5)
                    try:
                        driver.get(link)
                    except:
                        print("Failed to get link 5 times, moving on...")
    return driver

driver = webdriver.Chrome(ChromeDriverManager().install())
link = 'https://www.schwabassetmanagement.com/product-finder?combine=&field_asset_class_target_id%5B%5D=286'
driver = TryGetLink(driver, link)

tickers = [
    "SWWXX",
    "SCAXX",
    "SWGXX",
    "SWPXX",
    "SWOXX",
    "SNYXX",
    "SNRXX",
    "SCOXX",
    "SNSXX",
    "SWVXX",
    "SVUXX"
]

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
ticker_links = soup.find_all('a', {'class': 'csim-cta--chevron'})


for i in ticker_links:
    ticker = ((i["href"]).split('/')[-1].upper())
    if ticker in tickers:
        tickers.remove(ticker)
        driver = TryGetLink(driver, i["href"])
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        even = soup.find_all('tr', {'class': 'even'})[:2]
        net_assets = float(even[0].find_all('td')[-1].text.replace('$', '').replace(',', ''))
        shareholder_flows = float(even[1].find_all('td')[-1].text.replace('$', '').replace(',', ''))
        print(net_assets, shareholder_flows)