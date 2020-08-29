import pandas as pd


URL = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/astro-dates.csv'

df = pd.read_csv(URL, parse_dates=['Mission Date'])

print(df)
