'''Automates the running of the scripts to retrieve and import GitHub data'''

import sys
import os
import retrieve
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib

# request users MongoDB database credentials
def GetCredentials():
    #username = input("Enter your MongoDB Database username:").strip()
    #password = input("Enter your MongoDB Database username:").strip()
    username = sys.argv[2]
    password = sys.argv[3]
    print("Does this look right?")
    print(f"username: {username}, password: {password}")
    #confirm = input("y/n:")
    confirm = sys.argv[4]
    if confirm.lower() == "y":
        return username, password
    else:
        return GetCredentials()

# request which collection the user would like to import the data into
def GetTargetCollection():
    print("Would you like to import the data into the Test collection (TEST)")
    print("Or import the data into the intended collection? (REAL)")
    #target = input("TEST/REAL:").strip()
    target = sys.argv[1]
    if target.lower() == "test":
        return True
    elif target.lower() == "real":
        return False
    else:
        return GetTargetCollection()

# run the script to retrieve dev activity data and import the it into MongoDB
def ImportData():
    retrieve.RunScript()

    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: GitHub-Developer-Activity, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/GitHub-Developer-Activity --collection Test --type csv --file github-dev-activity.csv --headerline')
    else:
        print("Importing data into database: GitHub-Developer-Activity, collection: Core")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/GitHub-Developer-Activity --collection Core --type csv --file github-dev-activity.csv --headerline')
    os.system('rm github-dev-activity.csv')

try:
    ImportData()
except:
    email_sender = "ksg7699@nyu.edu"
    email_receiver = ["ksg7699@nyu.edu", "kgill@jsoros.com"]
    email_password = "zovrtywzgxvxpkqb"
    subject = "Error with GitHub Developer Activity Script"
    em = MIMEMultipart('alternative')
    em['From'] = email_sender
    em['To'] = ", ".join(email_receiver)
    em['Subject'] = subject
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        for receiver in email_receiver:
            smtp.sendmail(email_sender, receiver, em.as_string())
