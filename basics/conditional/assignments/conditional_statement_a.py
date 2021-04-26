"""
* Assignment: Conditional Statement Adult
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Ask user to input age
    2. User will pass only valid `int`
    3. Print whether user is adult (age above 18)
    4. Run doctests - all must succeed

Polish:
    1. Poproś użytkownika o wprowadzenie swojego wieku
    2. Użytkownika poda tylko poprawne `int`
    3. Wypisz czy użytkownik jest pełnoletni (wiek powyżej 18)
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is str, 'Variable `result` has invalid type, should be str'

    >>> result in ('Adult', 'Young')
    True
"""

# Simulate user input (for test automation)
from unittest.mock import MagicMock
input = MagicMock(side_effect=['21'])
age = input('What is your age?: ')


result = ...  # str: Whether 'Adult' or 'Young'


# Solution
ADULT = 18

if int(age) >= ADULT:
    result = 'Adult'
else:
    result = 'Young'
