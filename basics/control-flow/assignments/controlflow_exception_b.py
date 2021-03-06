"""
* Assignment: ControlFlow Exception Raise
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Check value passed to a function
    2. If value is below zero, raise `ValueError`
    3. Write solution inside `check` function
    4. Mind the indentation level

Polish:
    1. Sprawdź wartość przekazaną do funkcji
    2. Jeżeli wartość jest poniżej zera, podnieś wyjątek `ValueError`
    3. Rozwiązanie zapisz wewnątrz funkcji `check`
    4. Zwróć uwagę na poziom wcięć

Tests:
    >>> check(1)
    >>> check(-1)
    Traceback (most recent call last):
    ValueError
"""


# Given
def check(value):
    ...


# Solution
def check(value):
    if value < 0:
        raise ValueError
