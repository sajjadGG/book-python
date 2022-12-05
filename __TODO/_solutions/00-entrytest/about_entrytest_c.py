"""
* Assignment: About EntryTest Endswith
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Define `result: set[str]`
    2. Iterate over `DATA`
    3. Append to `result` species with endings in `SUFFIXES`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: set[str]`
    2. Iterując po `DATA`
    3. Dodaj do `result` nazwy gatunków z końcówkami w `SUFFIXES`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result` instead of Ellipsis `...`'
    >>> assert type(result) is set, \
    'Result must be a set'
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert all(type(element) is str for element in result), \
    'All elements in result must be a str'

    >>> sorted(result)
    ['setosa', 'virginica']
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, {'virginica'}),
    (5.1, 3.5, 1.4, 0.2, {'setosa'}),
    (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
    (6.3, 2.9, 5.6, 1.8, {'virginica'}),
    (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
    (4.7, 3.2, 1.3, 0.2, {'setosa'}),
    (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
    (7.6, 3.0, 6.6, 2.1, {'virginica'}),
    (4.6, 3.1, 1.5, 0.2, {'setosa'})]

SUFFIXES = ('ca', 'osa')

# set[str]: species names with word endings in `SUFFIXES`

# Solution 1
result = set()
for row in DATA[1:]:
    species: str = row[-1].pop()
    if species.endswith(SUFFIXES):
        result.add(species)

# Solution 2
result = set(species
             for row in DATA[1:]
             if (species := row[-1].pop())
             and species.endswith(SUFFIXES))
