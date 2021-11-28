"""
* Assignment: CSV Format ListDict
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Convert data in `FILE` to `result: list[dict]`
    2. Replace column names with `FIELDNAMES`
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj dane w `FILE` do `result: list[dict]`
    2. Podmień nazwy kolumn na `FIELDNAMES`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Variable `result` must be a list'

    >>> assert all(type(row) is dict for row in result), \
    'All rows in `result` must be a dict'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'Sepal Length': '5.8', 'Sepal Width': '2.7', 'Petal Length': '5.1',
      'Petal Width': '1.9', 'Species': 'virginica'},
     {'Sepal Length': '5.1', 'Sepal Width': '3.5', 'Petal Length': '1.4',
      'Petal Width': '0.2', 'Species': 'setosa'},
     {'Sepal Length': '5.7', 'Sepal Width': '2.8', 'Petal Length': '4.1',
      'Petal Width': '1.3', 'Species': 'versicolor'}]
"""

import csv


DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

FIELDNAMES = ['Sepal Length', 'Sepal Width',
              'Petal Length', 'Petal Width', 'Species']

FILE = r'_temporary.csv'

with open(FILE, mode='w') as file:
    file.write(DATA)

result: list = []

# Solution
with open(FILE) as file:
    header = file.readline()
    for line in file:
        line = line.strip().split(',')
        line = zip(FIELDNAMES, line)
        result.append(dict(line))
