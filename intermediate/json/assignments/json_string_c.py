"""
* Assignment: JSON String LoadObject
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Load `DATA` from JSON format
    2. Convert data to `result: list[dict]`
    3. Do not add header as a first line
    4. Run doctests - all must succeed

Polish:
    1. Wczytaj `DATA` z formatu JSON
    2. Przekonwertuj dane do `result: list[dict]`
    3. Nie dodawaj nagłówka jako pierwsza linia
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'
    >>> assert len(result) > 0, \
    'Variable `result` should not be empty'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Sepal length': 5.1,
     'Sepal width': 3.5,
     'Petal length': 1.4,
     'Petal width': 0.2,
     'Species': 'setosa'}
"""

import json


DATA = """
{
    "Sepal length": 5.1,
    "Sepal width": 3.5,
    "Petal length": 1.4,
    "Petal width": 0.2,
    "Species": "setosa"
}
"""


# Load `DATA` from JSON format
# type: list[dict]
result = ...

# Solution
result = json.loads(DATA)
