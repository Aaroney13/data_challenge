# Meta Data Challenge
import pandas as pd
from pandasql import sqldf
import os
os.chdir(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge")

df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge\NetflixData\netflix_titles.csv")
rt = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge\rotten_tomatoes_movies.csv")

pysqldf = lambda q: sqldf(q, globals())

Canada = pysqldf("SELECT * FROM df WHERE country LIKE '%Canada%' ")

#Experimenting with Google Ads
#Canada_Movies = Canada['title']
# Canada_Movies.to_csv(os.getcwd() + '/out.csv', index=False)

new = Canada.merge(rt, how='inner', left_on='title', right_on='movie_title')
print(Canada)
print(new)
