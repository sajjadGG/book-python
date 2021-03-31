"""
* Assignment: Sequence Frozenset Create
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create frozenset `result` with elements:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz frozenset `result` z elementami:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assignment solution must be in `result` instead of ... (Ellipsis)'

    >>> type(result)
    <class 'frozenset'>
    >>> len(result)
    3

    >>> 'a' in result
    True
    >>> 1 in result
    True
    >>> 2.2 in result
    True
"""

# Given
result = ...  # frozenset with 'a' and 1 and 2.2

# Solution
result = frozenset({'a', 1, 2.2})
