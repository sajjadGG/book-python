from datetime import datetime, timezone
import pandas as pd
import numpy as np


URL = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/iris.csv'

df = pd.read_csv(URL, encoding='utf-8')
df.columns = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species',
]

df.where(df['Petal length'] > 2.0, inplace=True)
df.dropna(how='all', inplace=True)

df['datetime'] = datetime.now(tz=timezone.utc)
df['big_enough'] = np.where(df['Petal width'] > 1.0, True, False)

columns = ['Sepal length', 'Sepal width', 'Species']
df = df[columns]
df.describe()
