"""
* Assignment: Sequence Tuple Create
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create tuple `result` with elements:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Run doctests - all must succeed

Polish:
    1. Stwórz tuple `result` z elementami:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is tuple, 'Variable `result` has invalid type, should be tuple'
    >>> assert len(result) == 3, 'Variable `result` length should be 3'

    >>> 'a' in result
    True
    >>> 1 in result
    True
    >>> 2.2 in result
    True
"""

result = ...  # tuple[str|int|float]: with 'a' and 1 and 2.2

# Solution
result = ('a', 1, 2.2)
