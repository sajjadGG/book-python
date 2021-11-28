"""
* Assignment: CSV Format Enumerate
* Complexity: easy
* Lines of code: 9 lines
* Time: 8 min

English:
    1. Convert `DATA` to `result: list[tuple[str]]`
    2. Generate `LABEL_ENCODER: dict[int,str]` from `header: list[str]`
    3. Substitute last element (class label) with value from `LABEL_ENCODER`
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` to `result: list[tuple[str]]`
    2. Wygeneruj `LABEL_ENCODER: dict[int,str]` z `header: list[str]`
    3. Podmień ostatni element (etykietę klasową) z wartością z `LABEL_ENCODER`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('5.8', '2.7', '5.1', '1.9', 'virginica'),
     ('5.1', '3.5', '1.4', '0.2', 'setosa'),
     ('5.7', '2.8', '4.1', '1.3', 'versicolor')]
"""

DATA = """3,4,setosa,virginica,versicolor
5.8,2.7,5.1,1.9,1
5.1,3.5,1.4,0.2,0
5.7,2.8,4.1,1.3,2"""

header, *data = DATA.splitlines()

# list[tuple]: data from file (note the list[tuple] format!)
result = ...

# Solution
result = []

header = header.strip().split(',')
nrows, ncols, *class_labels = header
LABEL_ENCODER = dict(enumerate(class_labels))

for line in data:
    *values, species = line.strip().split(',')
    species = LABEL_ENCODER[int(species)]
    row = values + [species]
    result.append(tuple(row))
