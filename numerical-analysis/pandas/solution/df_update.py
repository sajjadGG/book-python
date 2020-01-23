import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/iris-dirty.csv'

df = pd.read_csv(DATA, skiprows=1)

df.columns = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species'
]

df['Species'].replace({
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
}, inplace=True)

df = df.sample(frac=1.0).reset_index(drop=True)

df.head(5)
df.tail(3)

df.describe()
