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
genres  = ['Action', 'Horror', 'Documentaries', 'Independent', 'Comedies', 'Children', 'Thrillers', 'Drama', 'Sci-Fi']
count = 0
colors = ['r', 'g', 'b', 'p']
for genre in genres:

    gen = pysqldf("SELECT rating_y, reviews FROM full_set WHERE listed_in LIKE '% "+ genre +"%' ")
    plt.plot(gen['rating_y'], gen['reviews'], 'o', color='g')
    count += 1

#print(action)



plt.show()