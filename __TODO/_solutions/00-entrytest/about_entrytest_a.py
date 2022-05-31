"""
* Assignment: About EntryTest Warmup
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define variable `result` with value 1
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną `result` z wartością 1
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result` instead of Ellipsis `...`'
    >>> assert type(result) is int, \
    'Variable `result` has invalid type, should be int'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    1
"""

# int: with value 1
result = 1
