"""
* Assignment: CSV Format Substitute
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Convert `DATA` to `result: list[tuple[str]]`
    2. Substitute last element (class label) with value from `LABEL_ENCODER`
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` to `result: list[tuple[str]]`
    2. Podmień ostatni element (etykietę klasową) z wartością z `LABEL_ENCODER`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('5.8', '2.7', '5.1', '1.9', 'virginica'),
     ('5.1', '3.5', '1.4', '0.2', 'setosa'),
     ('5.7', '2.8', '4.1', '1.3', 'versicolor')]
"""

DATA = """5.8,2.7,5.1,1.9,1
5.1,3.5,1.4,0.2,0
5.7,2.8,4.1,1.3,2"""

LABEL_ENCODER = {
    '0': 'setosa',
    '1': 'virginica',
    '2': 'versicolor'}

# list[tuple]: data from file (note the list[tuple] format!)
result = ...

# Solution
result = []

for line in DATA.splitlines():
    *values, species = line.strip().split(',')
    species = LABEL_ENCODER.get(species)
    row = values + [species]
    result.append(tuple(row))
