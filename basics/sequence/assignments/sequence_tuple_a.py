"""
* Assignment: Sequence Tuple Create
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create tuple `result` with elements:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz tuple `result` z elementami:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert result is not Ellipsis, \
    'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> type(result)
    <class 'tuple'>
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
result = ...  # tuple with 'a' and 1 and 2.2

# Solution
result = ('a', 1, 2.2)
