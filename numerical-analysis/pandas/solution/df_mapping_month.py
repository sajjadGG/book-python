import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/phones.csv'

MONTHS_EN = ['January', 'February', 'March', 'April',
             'May', 'June', 'July', 'August', 'September',
             'October', 'November', 'December']

MONTHS = {f'{k:02}':v for k,v in enumerate(MONTHS_EN, start=1)}


## Solution 1
phones = pd.read_csv(DATA)
phones[['year', 'month_name']] = phones['month'].str.split('-', expand=True)
phones['month_name'] = phones['month_name'].map(MONTHS)
phones


## Solution 2
phones = pd.read_csv(DATA)
phones[['year', 'month_name']] = phones['month'].str.split('-', expand=True)
phones['month_name'].replace(MONTHS, inplace=True)
phones


## Solution 3
phones = pd.read_csv(DATA)
phones['year'] = phones['month'].str[:4]
phones['month_name'] = phones['month'].str[-2:]
phones['month_name'].replace(MONTHS, inplace=True)
phones
