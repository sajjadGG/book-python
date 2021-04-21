"""
* Assignment: Exception Raise One
* Status: required
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Validate value passed to a `check` function
        a. If `value` is less than zero, raise `ValueError`
    2. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    3. Run doctests - all must succeed

Polish:
    1. Sprawdź poprawność wartości przekazanej do funckji `check`
        a. Jeżeli `value` jest mniejsze niż zero, podnieś wyjątek `ValueError`
    2. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> check(1)
    >>> check(0)
    >>> check(-1)
    Traceback (most recent call last):
    ValueError
"""

def check(value):
    ...


# Solution
def check(value):
    if value < 0:
        raise ValueError
