"""
* Assignment: JSON File Load
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Read JSON data from `FILE`
    2. Run doctests - all must succeed

Polish:
    1. Odczytaj dane JSON z pliku `FILE`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert len(result) > 0, \
    'Variable `result` should not be empty'
    >>> assert all(type(row) is dict for row in result), \
    'Variable `result` should be a list[dict]'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
     {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
     {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
     {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'},
     {'Sepal length': 6.4, 'Sepal width': 3.2, 'Petal length': 4.5, 'Petal width': 1.5, 'Species': 'versicolor'},
     {'Sepal length': 4.7, 'Sepal width': 3.2, 'Petal length': 1.3, 'Petal width': 0.2, 'Species': 'setosa'},
     {'Sepal length': 7.0, 'Sepal width': 3.2, 'Petal length': 4.7, 'Petal width': 1.4, 'Species': 'versicolor'},
     {'Sepal length': 7.6, 'Sepal width': 3.0, 'Petal length': 6.6, 'Petal width': 2.1, 'Species': 'virginica'},
     {'Sepal length': 4.9, 'Sepal width': 3.0, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'}]

     >>> remove(FILE)
"""

import json


FILE = r'_temporary.json'

DATA = """[{"Sepal length": 5.8, "Sepal width": 2.7, "Petal length": 5.1, "Petal width": 1.9, "Species": "virginica"},
{"Sepal length": 5.1, "Sepal width": 3.5, "Petal length": 1.4, "Petal width": 0.2, "Species": "setosa"},
{"Sepal length": 5.7, "Sepal width": 2.8, "Petal length": 4.1, "Petal width": 1.3, "Species": "versicolor"},
{"Sepal length": 6.3, "Sepal width": 2.9, "Petal length": 5.6, "Petal width": 1.8, "Species": "virginica"},
{"Sepal length": 6.4, "Sepal width": 3.2, "Petal length": 4.5, "Petal width": 1.5, "Species": "versicolor"},
{"Sepal length": 4.7, "Sepal width": 3.2, "Petal length": 1.3, "Petal width": 0.2, "Species": "setosa"},
{"Sepal length": 7.0, "Sepal width": 3.2, "Petal length": 4.7, "Petal width": 1.4, "Species": "versicolor"},
{"Sepal length": 7.6, "Sepal width": 3.0, "Petal length": 6.6, "Petal width": 2.1, "Species": "virginica"},
{"Sepal length": 4.9, "Sepal width": 3.0, "Petal length": 1.4, "Petal width": 0.2, "Species": "setosa"}]"""

with open(FILE, mode='w') as file:
    file.write(DATA)

# Read JSON data from `FILE`
# type: list[tuple]
result = ...

# Solution
with open(FILE, mode='r') as file:
    result = json.load(file)
