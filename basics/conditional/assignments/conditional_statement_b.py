"""
* Assignment: Conditional Statement Oneliner
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. User typed his/her age
    2. Check whether user is adult (age above 18)
    3. Use one line `if`
    4. Run doctests - all must succeed

Polish:
    1. Użytkownik wprowadził swój wiek
    2. Sprawdź czy użytkownik jest pełnoletni (wiek powyżej 18)
    3. Wykorzystaj jednolinikowego `if`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result in 'Young'
    True
"""

ADULT = 18
AGE = 12

# str: Whether 'Adult' or 'Young'
result = ...

# Solution
result = 'Adult' if AGE >= ADULT else 'Young'
