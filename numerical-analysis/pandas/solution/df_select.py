import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/iris.csv'

df = pd.read_csv(DATA, encoding='utf-8')

df.columns = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species',
]

df.where(df['Petal length'] > 2.0, inplace=True)

df.head(5)


# Alternative
df = df[ df['Petal length'] > 2.0 ]
