# Meta Data Challenge
import pandas as pd
from pandasql import sqldf
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge")

df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge\NetflixData\netflix_titles.csv")
webscrape = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge\my_movies.csv")
webscrape = webscrape.drop(columns='check')

pysqldf = lambda q: sqldf(q, globals())

Canada = pysqldf("SELECT * FROM df WHERE country LIKE '%Canada%' ")

full_set = Canada.merge(webscrape, how='inner', left_on='title', right_on='title')
full_set['reviews'] = pd.to_numeric(full_set['reviews'].str.replace('K', '000').str.replace('.', ''), errors='coerce')
full_set['rating_y'] = pd.to_numeric(full_set['rating_y'], errors='coerce')
#genres  = ['Sci-Fi', 'Thrillers', 'Drama', 'Independent', 'Internat', 'Comed']
genres  = ['Sci-Fi', 'Drama',  'Comed']
count = 0
#colors = ['#26547C', '#ef476f', '#ffd166', '#06d6a0', '#a6cfd5', '#c8b8db']
colors = ['#26547C', '#ffd166', '#c8b8db']

#Plot properties
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.set_facecolor('#002845')
fig.set_facecolor('#002845')
ax.spines['bottom'].set_color('#1a5e8f')
ax.spines['left'].set_color('#1a5e8f')
ax.spines['right'].set_color('#002845')
ax.spines['top'].set_color('#002845')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

for genre in genres:
    color = colors[count]
    #color = '#%02X%02X%02X' % (r(),r(),r())
    gen = pysqldf("SELECT rating_y, reviews FROM full_set WHERE listed_in LIKE '% "+ genre +"%'")
    print(len(gen))
    plt.subplot(1, 1, 1)
    plt.plot(gen['rating_y'], gen['reviews'], 'o', color=color, label=genre, alpha=.6)
   # plt.subplot(1, 1, 1)
   # plt.bar(genre, gen['reviews'].median(), color=color)
    count += 1
# count = 0
# ratings = ['PG-13', 'R', 'PG', 'TV-MA', 'TV-14', 'TV-G', 'TV-Y', 'TV-PG']
# sizes = []
# colors2= ['#227c9d', '#17c3b2', '#ffcb77', '#fef9ef', '#fe6d73', "#562c2c","#f2542d","#f5dfbb","#0e9594","#127475"]
# for rating in ratings:
#     gen = pysqldf("SELECT reviews, rating_x FROM full_set WHERE rating_x LIKE '%"+ rating +"%'")
#     if (rating == 'PG'):
#         gen = pysqldf("SELECT reviews, rating_x FROM gen WHERE rating_x NOT LIKE '%PG-13%'")
#         gen = pysqldf("SELECT reviews, rating_x FROM gen WHERE rating_x NOT LIKE '%TV-PG%'")
#     sizes.append(gen['reviews'].count())
#     #ax.bar(rating, gen['reviews'].median(), color=colors2[count])
# #     # ax.bar(rating, len(gen), color=color)
#     count+= 1
# ax.pie(sizes, labels=ratings, autopct='%1.1f%%',
#        shadow=True, startangle=90, colors=colors2)
    
#ax.axis('equal')
#fig.savefig('dotsaved.png', dpi=300, transparent=True)
plt.show()
