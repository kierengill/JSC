# Github Developer Activity Tracker

Track developer activity on GitHub of organizations core repositories

Total stars, watchers, forks, and commits as well as authors monthly and commits monthly are recorded

## allRepos.py

List of all repositories to track with the user, repo, organization type, and category

## scrape.py

Generates a csv file with all of the statistics on each repository

## automate.py

Runs the scraper and imports the data into MongoDB Atlas

# Running the program (automate.py)

1. Run importData with test = False and the appropriate username and password
2. Make sure everything ran smoothly and check MongoDB Atlas for quality and correctness