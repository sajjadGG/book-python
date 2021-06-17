"""
* Assignment: Conditional Statement Adult
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Ask user to input age
    2. Check whether user is adult (age above 18)
    3. Run doctests - all must succeed

Polish:
    1. Poproś użytkownika o wprowadzenie wieku
    2. Sprawdź czy użytkownik jest pełnoletni (wiek powyżej 18)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result in ('Adult', 'Young')
    True
"""

from unittest.mock import MagicMock


# Simulate user input (for test automation)
input = MagicMock(side_effect=['21'])
age = input('What is your age?: ')

# str: Whether 'Adult' or 'Young'
result = ...

# Solution
ADULT = 18

if int(age) >= ADULT:
    result = 'Adult'
else:
    result = 'Young'
