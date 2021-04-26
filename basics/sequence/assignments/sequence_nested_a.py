"""
* Assignment: Sequence Nested Create
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Create nested list `result` with elements:
        a. tuple: `1`, `2`, `3`
        b. list: `1.1`, `2.2`, `3.3`
        c. set: `'Mark Watney'`, `'Melissa Lewis'`, `'Jan Twardowski'`
    2. Run doctests - all must succeed

Polish:
    1. Stwórz zagnieżdżoną listę `result` z elementami:
        a. tuple: `1`, `2`, `3`
        b. list: `1.1`, `2.2`, `3.3`
        c. set: `'Mark Watney'`, `'Melissa Lewis'`, `'Jan Twardowski'`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is list, 'Variable `result` has invalid type, should be list'
    >>> assert len(result) == 3, 'Variable `result` length should be 3'

    >>> (1, 2, 3) in result
    True
    >>> [1.1, 2.2, 3.3] in result
    True
    >>> {'Mark Watney', 'Melissa Lewis', 'Jan Twardowski'} in result
    True
"""

result = ...  # list[tuple|list|set]: with tuple 1, 2, 3 and list 1.1, 2.2, 3.3 and set 'Mark Watney', 'Melissa Lewis', 'Jan Twardowski'

# Solution
result = [
        (1, 2, 3),
        [1.1, 2.2, 3.3],
        {'Mark Watney', 'Melissa Lewis', 'Jan Twardowski'},
]
