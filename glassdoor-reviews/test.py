import pandas as pd
from bs4 import BeautifulSoup
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
from datetime import timedelta

df = pd.read_csv("full.csv")
df = df[["company", "rating", "conReview"]]
df = df[df["rating"]<=2]
html = df.to_html(justify = "left", index=False, border = 1)
soup = BeautifulSoup(html, 'html.parser')

table = soup.table
table["style"] = "border: 1px solid black; border-collapse: collapse;"

tags = ["th","td"]
for tag in soup.find_all(tags):
    tag["style"] = "padding: 5px 5px 5px 5px;"

final = str(soup.prettify())

email_sender = "ksg7699@nyu.edu"
email_receiver = ["kgill@jsoros.com", "kierengill2000@gmail.com"]
email_password = "zovrtywzgxvxpkqb"

yesterday = date.today() - timedelta(days = 1)
formatted_date = date.strftime(yesterday, "%m/%d/%Y")
subject = "Glassdoor Reviews " + formatted_date
text = "Hello! <br> Below are the negative Glassdoor reviews from yesterday: <br><br>"
body = text + final

em = MIMEMultipart('alternative')
em['From'] = email_sender
em['To'] = ", ".join(email_receiver)
em['Subject'] = subject

em.attach(MIMEText(body, 'html'))

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    for receiver in email_receiver:
        print(receiver)
        smtp.sendmail(email_sender, receiver, em.as_string())