"""
* Assignment: CSV Format Syntax
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Convert `DATA` to `result: list[tuple[str]]`
    2. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` to `result: list[tuple[str]]`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.splitlines()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
     ('5.8', '2.7', '5.1', '1.9', 'virginica'),
     ('5.1', '3.5', '1.4', '0.2', 'setosa'),
     ('5.7', '2.8', '4.1', '1.3', 'versicolor')]
"""

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""


# list[tuple]: data from file (note the list[tuple] format!)
result = ...

# Solution
result = []

for line in DATA.splitlines():
    line = line.strip().split(',')
    result.append(tuple(line))
