"""
* Assignment: RE Standards IsValidPesel
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Napisz implementację `is_pesel_valid`
       a. Temat walidacji Pesel jest zbyt trudny dla Regex
       b. W tej funkcji użujemy prostego sprawdzenia r'^\d{11}$'
       c. Już tylko taki kawałek kodu pozwoli na uniknięcie 80% błędów
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> is_pesel_valid('69072101234')
    True
    >>> is_pesel_valid('18220812345')
    True
"""

import re

PATTERN = r'^\d{11}$'


def is_pesel_valid(pesel: str) -> bool:
    ...


# Solution
def is_pesel_valid(pesel):
    if re.match(PATTERN, pesel):
        return True
    else:
        return False
