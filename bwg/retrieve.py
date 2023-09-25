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

def RunAll():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    link = 'https://portal.bwgstrategy.com/libraryforums#Library'
    driver = TryGetLink(driver, link)
    time.sleep(3)

    username = driver.find_element(By.XPATH , "//input[@name='username']")
    username.send_keys('twestcott@jsoros.com')
    time.sleep(1)

    password = driver.find_element(By.XPATH , "//input[@name='password']")
    password.send_keys('JSCapital1*')
    time.sleep(1)

    submit = driver.find_element(By.XPATH , "//button[@type='submit']").click()
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    dates = soup.find_all('div', {'class': 'tile-publication-date pull-right'})
    articles = soup.find_all('div', {'class': 'tile wide'})

    today = datetime.date.today()
    formatted_date = today.strftime('%m/%d/%Y')
    body = "Hello! <br> <br> Below are the BWG Strategy Insights from today. <br> <br>"
    titles = "Here are the titles of the forum summaries: <br> <ul>"
    body2 = ""
    count = 0

    for article in articles:
        date = article.find('div', {'class': 'tile-publication-date pull-right'}).text
        title = article.find('span', {'class': 'tile-title-inner'}).text
        check = article.find('span', {'class': 'tile-publication-type'}).text
        if (date == formatted_date) and ('Weekly Summary' not in title) and (check == 'Forum Synopsis'):
            titles += "<li>" + str(title) + "</li>"
            link = article.find('a', class_='tile-link-wrapper')['href']
            myUrl = 'https://portal.bwgstrategy.com/' + link

            driver = TryGetLink(driver, myUrl)
            css_selector = '.summary-info'  # Replace with the CSS selector for the dynamic content
            title_selector = '.document-name'
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
                )
            except TimeoutError:
                print("Timeout: Unable to find the dynamic content")

            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            body2 += "<h2>" + str(soup.select(title_selector)[0]) + "</h2>"
            body2 += str(soup.select(css_selector)[0])
            body2 += "<br>"
            count += 1
            # print(soup.select(css_selector)[0].get_text(strip=True))

    titles += "</ul>"
    driver.quit()

    email_sender = "ksg7699@nyu.edu"
    email_receiver = ["sseshadri@jsoros.com", "twestcott@jsoros.com", "jlobel@jsoros.com", "ksehgal@jsoros.com", "kgill@jsoros.com"]
    # email_receiver = ["kgill@jsoros.com"]
    email_password = "zovrtywzgxvxpkqb"
    subject = "BWG Strategy Insights " + formatted_date

    em = MIMEMultipart('alternative')
    em['From'] = email_sender
    em['To'] = ", ".join(email_receiver)
    em['Subject'] = subject

    body3 = "Hello! <br> <br> There are no forum summaries for today."

    if count != 0:
        em.attach(MIMEText(body + titles + body2, 'html'))
    else:
        em.attach(MIMEText(body3, 'html'))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        for receiver in email_receiver:
            smtp.sendmail(email_sender, receiver, em.as_string())

try:
    RunAll()
except:
    email_sender = "ksg7699@nyu.edu"
    email_receiver = ["ksg7699@nyu.edu", "kgill@jsoros.com"]
    email_password = "zovrtywzgxvxpkqb"
    subject = "Error with BWG Script"
    em = MIMEMultipart('alternative')
    em['From'] = email_sender
    em['To'] = ", ".join(email_receiver)
    em['Subject'] = subject
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        for receiver in email_receiver:
            smtp.sendmail(email_sender, receiver, em.as_string())