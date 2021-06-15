"""
* Assignment: Str Define Emoticon
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `name` with value `Mark Watney`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `name` z wartością `Mark Watney`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> name in result
    True
    >>> result
    'Hello Mark Watney'
"""

# str: Mark Watney
name = ...

# str: Hello Mark Watney
result = ...

# Solution
name = 'Mark Watney'
result = f'Hello {name}'
