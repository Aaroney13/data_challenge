# Meta Data Challenge
import pandas as pd
from pandasql import sqldf
import os
os.chdir(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge")

df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge\NetflixData\netflix_titles.csv")
webscrape = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\Meta Challenge\my_movies.csv")
webscrape = webscrape.drop(columns='check')

pysqldf = lambda q: sqldf(q, globals())

Canada = pysqldf("SELECT * FROM df WHERE country LIKE '%Canada%' ")

new = Canada.merge(webscrape, how='inner', left_on='title', right_on='title')


