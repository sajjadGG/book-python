"""
* Assignment: Mapping Generate Zip
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: dict`
    2. Assign to `result` converted `DATA` to `dict`
    3. Use `zip()`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict`
    2. Przypisz do `result` przekonwertowane `DATA` do `dict`
    3. Użyj `zip()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert all(type(x) is str for x in result.keys()), \
    'All dict keys should be str'

    >>> assert ('Sepal length' in result.keys()
    ...     and 'Sepal width' in result.keys()
    ...     and 'Petal length' in result.keys()
    ...     and 'Petal width' in result.keys()
    ...     and 'Species' in result.keys())

    >>> assert (5.8 in result.values()
    ...     and 2.7 in result.values()
    ...     and 5.1 in result.values()
    ...     and 1.9 in result.values()
    ...     and 'virginica' in result.values())

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Sepal length': 5.8,
     'Sepal width': 2.7,
     'Petal length': 5.1,
     'Petal width': 1.9,
     'Species': 'virginica'}
"""

KEYS = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
VALUES = [5.8, 2.7, 5.1, 1.9, 'virginica']

# dict[str,float|str]: converted zipped KEYS and VALUES
result = ...

# Solution
result = dict(zip(KEYS, VALUES))
