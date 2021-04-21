"""
* Assignment: Exception Custom Exception
* Status: optional
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define custom exception `NegativeKelvinError`
    2. Check value passed to a `check` function
    3. If value is lower than 0, raise `NegativeKelvinError`
    4. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj własny wyjątek `NegativeKelvinError`
    2. Sprawdź wartośc przekazaną do funckji jako `float`
    3. Jeżeli wartość jest mniejsza niż 0, podnieś `NegativeKelvinError`
    4. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> from inspect import isclass
    >>> isclass(NegativeKelvinError)
    True
    >>> issubclass(NegativeKelvinError, Exception)
    True
    >>> check(1)
    >>> check(0)
    >>> check(-1)
    Traceback (most recent call last):
    exception_custom_a.NegativeKelvinError
"""

def check(value):
    ...


# Solution
class NegativeKelvinError(Exception):
    pass


def check(value):
    if value < 0:
        raise NegativeKelvinError
