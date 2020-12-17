"""
* Assignment: Function Parameters Sequence
* Filename: function_parameters_sequence.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define function `total`
    2. Function parameter is `data` sequence of integers
    3. Function returns sum of all values in sequence
    4. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj funkcję `total`
    2. Parametrem do funkcji jest `data` sekwencja liczb
    3. Funkcja zwraca sumę wszystkich wartości z sekwencji
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isfunction
    >>> isfunction(total)
    True
    >>> type(total([0, 1])) is int
    True
    >>> type(total([0.0, 1.1])) is float
    True
    >>> total([1,2,3])
    6
    >>> total([1,2,3,4,5,6])
    21
    >>> total(range(0,101))
    5050
"""


# Solution
def total(data):
    return sum(data)
