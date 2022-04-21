import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import numpy as np
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from pandasql import sqldf
from urllib.request import Request, urlopen
import re

os.chdir(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge")
df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge\out.csv")
test_title = df.to_numpy()
#test_title = ['Squid Game']
all_data = pd.DataFrame(data={'title':[], 'rating':[], 'reviews':[], 'check':[]})
pysqldf = lambda q: sqldf(q, globals())
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

for x in test_title:
    try:
        title = str(x).strip("['']")
        url = "https://www4.bing.com/search?q=imdb+" + title
        url = url.replace(" ", "%20")
        custom_user_agent = user_agent_rotator.get_random_user_agent()
        #custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
        req = Request(url, headers={"User-Agent": custom_user_agent})
        
        html_page = urlopen(req)
        links = None
        soup = BeautifulSoup(html_page, "lxml")
        for link in soup.findAll('a'):
            # links.append(link.get('href'))
            if (link != None and link.get('href').find('www.imdb.com/title') != -1):
                links = link.get('href')
                print("link got for" + title)
                break
    #   try:
    #       if (links == None):
    #          print("link not found for" + title)
        links = links[(links.find('e/') + 1):links.rfind('/')]
        open = requests.get('https://www.imdb.com/title' + links + '/', headers={"User-Agent": custom_user_agent})
        soup = BeautifulSoup(open.content, 'html.parser')
        try:
            rating = soup.find('span', class_='sc-7ab21ed2-1 jGRxWM').text
        except:
            rating = 'Na'
            print('unable to get rating for ' + title)
        try:
            reviews = soup.find('div', class_='sc-7ab21ed2-3 dPVcnq').text
        except:
            reviews = 'Na'
            print('unable to get reviews for ' + title)
        try:
            #redundancy to ensure im grabbing the right page
            check = soup.find('h1', class_='sc-b73cd867-0 eKrKux').text
        except:
            print('unable to get check for' + title)
            check = 'Na'
        all_data.loc[-1] = [title, rating, reviews, check]
        all_data.index = all_data.index + 1
    except:
        print("unable to get " + str(x))
    
    #print(links)

print(all_data)
all_data.to_csv(os.getcwd() + '/my_movies.csv', index=False)