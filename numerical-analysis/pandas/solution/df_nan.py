import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/iris-dirty.csv'

COLUMNS = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species']

SPECIES = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
}


iris = pd.read_csv(DATA, skiprows=1, names=COLUMNS)
iris['Species'].replace(SPECIES, inplace=True)
iris = iris.sample(frac=1.0).reset_index(drop=True)

iris.head(2)
#    Sepal length  Sepal width  Petal length  Petal width    Species
# 0           6.4          2.8           5.6          2.1  virginica
# 1           5.1          3.5           1.4          0.2     setosa

len(iris)
# 151
