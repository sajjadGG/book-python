"""
* Assignment: Pandas Read CSV Replace
* Filename: pandas_read_csv_replace.py
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from ``DATA`` to ``result: pd.DataFrame``
    3. Use provided column names in ``COLUMNS``
    4. Read labels from the first row
    5. Replace data in ``label`` column with values extracted above
    6. Store in `result` only 20 first rows

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z ``DATA`` do ``result: pd.DataFrame``
    3. Użyj podanych w ``COLUMNS`` nazw kolumn
    4. Wczytaj nazwy labeli z pierwszego wiersza
    5. Podmień dane w kolumnie ``label`` na wartości wyciągnięte powyżej
    6. Zachowaj w `result` tylko 20 pierwszych wierszy

Hints:
    * ``pd.read_csv(url, nrows=0).columns``
    * ``df['label'].replace({'from': 'to'}, inplace=True)``

Tests:
    >>> type(result) is pd.DataFrame
    True
    >>> len(result) == 20
    True
    >>> result.loc[[0,9,19], ['mean radius', 'mean texture', 'label']]
        mean radius  mean texture      label
    0         17.99         10.38  malignant
    9         12.46         24.04  malignant
    19        13.54         14.36     benign
"""


# Given
import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/breast-cancer.csv'

COLUMNS = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
           'mean smoothness', 'mean compactness', 'mean concavity',
           'mean concave points', 'mean symmetry', 'mean fractal dimension',
           'radius error', 'texture error', 'perimeter error', 'area error',
           'smoothness error', 'compactness error', 'concavity error',
           'concave points error', 'symmetry error',
           'fractal dimension error', 'worst radius', 'worst texture',
           'worst perimeter', 'worst area', 'worst smoothness',
           'worst compactness', 'worst concavity', 'worst concave points',
           'worst symmetry', 'worst fractal dimension', 'label']


# Solution
header = pd.read_csv(DATA, nrows=0)
labels = dict(enumerate(header.columns[2:]))

df = pd.read_csv(DATA, skiprows=1, names=COLUMNS)
df['label'].replace(to_replace=labels, inplace=True)
result = df.head(20)
