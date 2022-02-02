"""
* Assignment: Mapping Keys List
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: list[str]` with list of `DATA` keys
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[str]` z listą kluczy z `DATA`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `list()`
    * `dict.keys()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is str for x in result), \
    'All elements in `result` should be str'

    >>> result
    ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']
"""

DATA = {'Sepal length': 5.8,
        'Sepal width': 2.7,
        'Petal length': 5.1,
        'Petal width': 1.9}

# list[str]: with keys from DATA
result = ...

# Solution
result = list(DATA.keys())
