"""
* Assignment: Function Scope Roman to Int
* Complexity: hard
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Define function converting roman numerals to integer
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję przeliczającą liczbę rzymską na całkowitą
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(roman_to_int)
    True
    >>> result(1)
    'I'
    >>> result(9)
    'IX'
    >>> result(1550)
    'MDL'
    >>> result(1540)
    'MXDL'
    >>> result(14)
    'XIV'
"""

CONVERSION = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    500: 'D',
    1000: 'M',
}


# type: Callable[[int], str]
def result(number):
    ...


# Solution
def result(number):
    ...
