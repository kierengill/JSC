'''Scrapes data from GitHub related to repository developer activity'''

from bs4 import BeautifulSoup
import csv
import datetime
import requests
import time

import repos

REPOS = repos.repos_core

# return html data ready to be parsed
def GetData(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

# return project statistics from the given user and repository
def ParseWebData(user, repositories, category, description, name):
    for i in range(3, len(repositories)):
        soup = GetData(f'https://github.com/{user}/{repositories[i]}')

        commits_total = soup.find('a', {'class': 'pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 Link--primary no-underline no-wrap'})
        commits_total = commits_total.text.replace(",", "").replace("\n", "")
        commits_total = commits_total.replace("commits", "")
        commits_total = int(commits_total.replace("commit", ""))
        
        sidebar_container = soup.find('div', {'class': 'Layout-sidebar'})
        sidebar = sidebar_container.find_all('div', {'class': 'mt-2'})
        for j in range(len(sidebar)):
            text = sidebar[j].text
            if "star" in text:
                stars = text.replace(" ", "").replace("\n", "")
                stars = stars.replace("stars", "").replace("star", "")
                if "k" in stars:
                    stars_total = int(float(stars[:-1]) * 1000)
                else:
                    stars_total = int(stars)
            elif "watching" in text:
                watchers = text.replace(" ", "").replace("\n", "")
                watchers = watchers.replace("watching", "")
                if "k" in watchers:
                    watchers_total = int(float(watchers[:-1]) * 1000)
                else:
                    watchers_total = int(watchers)
            elif "fork" in text:
                forks = text.replace(" ", "").replace("\n", "")
                forks = forks.replace("forks", "").replace("fork", "")
                if "k" in forks:
                    forks_total = int(float(forks[:-1]) * 1000)
                else:
                    forks_total = int(forks)

        soup = GetData(f'https://github.com/{user}/{repositories[i]}/pulse_diffstat_summary?period=monthly')

        blurb = soup.find('div', {'class': 'color-fg-muted'})
        parsed_blurb = blurb.text.strip().replace(" ", ",").split(",")
        authors_monthly = int(parsed_blurb[3])
        commits_all_branches_monthly = int(parsed_blurb[15])

        project = {
            'category': str(category),
            'description': str(description),
            'name': str(name),
            'user': str(user),
            'repo': str(repositories[i]),
            'commitsTotal': int(commits_total),
            'watchersTotal': int(watchers_total),
            'forksTotal': int(forks_total),
            'authorsMonthly': int(authors_monthly),
            'commitsAllBranchesMonthly': int(commits_all_branches_monthly),
            'starsTotal': int(stars_total),
            'date': datetime.date.today()
        }
    return project

# create and aggregate all statistics into one csv file
def RunScript():
    organization_projects = []
    for org in REPOS:
        success = False
        while not success:
            try:
                organization_projects.append(ParseWebData(org, REPOS[org], REPOS[org][0], REPOS[org][1], REPOS[org][2]))
                success = True
            except:
                print("Waiting a couple of seconds to try again")
                time.sleep(2.5)
        print(f"{org} finished")

    fields = ['category', 'description', 'name', 'user', 'repo', 'commitsTotal',
        'watchersTotal', 'forksTotal', 'authorsMonthly',
        'commitsAllBranchesMonthly', 'starsTotal', 'date']
    with open(f'github-dev-activity.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            writer.writerows(organization_projects)
            
    print("Everything is Finished!")

