'''Imports the on sale Lowes and Academy data'''

import os

# request users MongoDB database credentials
def GetCredentials():
    username = input("Enter your MongoDB Database username:").strip()
    password = input("Enter your MongoDB Database username:").strip()
    print("Does this look right?")
    print(f"username: {username}, password: {password}")
    confirm = input("y/n:")
    if confirm.lower() == "y":
        return username, password
    else:
        return GetCredentials()

# request which collection the user would like to import the data into
def GetTargetCollection():
    print("Would you like to import the data into the Test collection (TEST)")
    print("Or import the data into the intended collection? (REAL)")
    target = input("TEST/REAL:").strip()
    if target.lower() == "test":
        return True
    elif target.lower() == "real":
        return False
    else:
        return GetTargetCollection()

# imports Lowes and Academy on sale listings data into MongoDB
def ImportData():
    test = GetTargetCollection()
    username, password = GetCredentials()
    if test:
        print("Importing data into database: Home-Improvement, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Home-Improvement --collection Test --type csv --file Lowes.csv --headerline')
        print("Importing data into database: Sports-Retail, collection: Test")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Sports-Retail --collection Test --type csv --file Academy.csv --headerline')
    else:
        print("Importing data into database: Home-Improvement, collection: Lowes")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Home-Improvement --collection Lowes --type csv --file Lowes.csv --headerline')
        print("Importing data into database: Sports-Retail, collection: Academy")
        os.system(f'mongoimport --uri mongodb+srv://{username}:{password}@projects.bcwtn.mongodb.net/Sports-Retail --collection Academy --type csv --file Academy.csv --headerline')

