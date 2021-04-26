"""
* Assignment: Sequence Set Create
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create set `result` with elements:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Run doctests - all must succeed

Polish:
    1. Stwórz zbiór `result` z elementami:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is set, 'Variable `result` has invalid type, should be set'
    >>> assert len(result) == 3, 'Variable `result` length should be 3'

    >>> 'a' in result
    True
    >>> 1 in result
    True
    >>> 2.2 in result
    True
"""

result = ...  # set[str|int|float]: with 'a' and 1 and 2.2

# Solution
result = {'a', 1, 2.2}
