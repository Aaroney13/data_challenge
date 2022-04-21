import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from pandasql import sqldf
from urllib.request import Request, urlopen
import re

os.chdir(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge")

test_title = ['Squid Game']
all_data = pd.DataFrame(data={'title':[], 'rating':[], 'reviews':[], 'check':[]})
pysqldf = lambda q: sqldf(q, globals())

for x in test_title:
    open = requests.get('https://www.rottentomatoes.com/' + x)

for x in test_title:
    url = "https://www4.bing.com/search?q=imdb+" + x
    url = url.replace(" ", "%20")
    custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    req = Request(url, headers={"User-Agent": custom_user_agent})
    
    html_page = urlopen(req)
    links = []
    soup = BeautifulSoup(html_page, "lxml")
    for link in soup.findAll('a'):
        # links.append(link.get('href'))
        if (link.get('href').find('www.imdb.com/title') != -1):
            links = link.get('href')
            break
    try:
        links = links[(links.find('e/') + 1):links.rfind('/')]
        open = requests.get('https://www.imdb.com/title' + links + '/', headers={"User-Agent": custom_user_agent})
        soup = BeautifulSoup(open.content, 'html.parser')
        rating = soup.find('span', class_='sc-7ab21ed2-1 jGRxWM')
        reviews = soup.find('div', class_='sc-7ab21ed2-3 dPVcnq')
        #redundancy to ensure im grabbing the right page
        check = soup.find('h1', class_='sc-b73cd867-0 eKrKux')
        all_data.loc[-1] = [x, rating.text, reviews.text, check.text]
        all_data.index = all_data.index + 1
    except:
        print("unable to get " + x)
    
    #print(links)

print(all_data)
#all_data.to_csv(os.getcwd() + '/my_movies.csv', index=False)