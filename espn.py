# http://www.espn.com/mlb/recap?gameId=401074993
# http://www.espn.com/mlb/recap?gameId=401074978
# http://www.espn.com/mlb/story/_/id/26542288/fan-sues-dodgers-says-security-roughed-up

import requests
from bs4 import BeautifulSoup
from inflection import titleize

def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)


    for link in links:
        post_formatter(link['href'])


    return titles


r = requests.get('http://www.espn.com/mlb/team/_/name/lad/los-angeles-dodgers')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')

titles = title_generator(links)

for title in titles:
    print(title)