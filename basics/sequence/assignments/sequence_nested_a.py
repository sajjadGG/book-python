"""
* Assignment: Sequence Nested Create
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Create nested sequence `result` with elements:
        a. tuple: `1`, `2`, `3`
        b. list: `1.1`, `2.2`, `3.3`
        c. set: `'Mark Watney'`, `'Melissa Lewis'`, `'Jan Twardowski'`
    2. Print `result`
    3. Print number of elements in `result`

Polish:
    1. Stwórz zagnieżdżoną sekwencję `result` z elementami:
        a. tuple: `1`, `2`, `3`
        b. list: `1.1`, `2.2`, `3.3`
        c. set: `'Mark Watney'`, `'Melissa Lewis'`, `'Jan Twardowski'`
    2. Wypisz `result`
    3. Wypisz liczbę elementów `result`

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assignment solution must be in `result` instead of ... (Ellipsis)'

    >>> type(result)
    <class 'list'>
    >>> len(result)
    3

    >>> (1, 2, 3) in result
    True
    >>> [1.1, 2.2, 3.3] in result
    True
    >>> {'Mark Watney', 'Melissa Lewis', 'Jan Twardowski'} in result
    True
"""

# Given
result = ...  # list with tuple 1, 2, 3 and list 1.1, 2.2, 3.3 and set 'Mark Watney', 'Melissa Lewis', 'Jan Twardowski'

# Solution
result = [
        (1, 2, 3),
        [1.1, 2.2, 3.3],
        {'Mark Watney', 'Melissa Lewis', 'Jan Twardowski'},
]
