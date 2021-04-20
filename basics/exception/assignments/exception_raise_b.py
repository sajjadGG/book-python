"""
* Assignment: Exception Raise Many
* Status: required
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Validate value passed to a `check` function
    2. If `value` is:
        a. other type than `int` or `float` raise `TypeError`
        a. less than zero, raise `ValueError`
        a. below `ADULT`, raise `PermissionError`
    3. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    4. Run doctests - all must succeed

Polish:
    1. Sprawdź poprawność wartości przekazanej do funckji `check`
    2. Jeżeli `age` jest:
        b. innego typu niż `int` lub `float`, podnieś wyjątek `TypeError`
        b. mniejsze niż zero, podnieś wyjątek `ValueError`
        c. mniejsze niż `ADULT`, podnieś wyjątek `PermissionError`
    3. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> check(18)
    >>> check(17.9999)
    Traceback (most recent call last):
    PermissionError
    >>> check(-1)
    Traceback (most recent call last):
    ValueError
    >>> check('one')
    Traceback (most recent call last):
    TypeError
    >>> check(True)
    Traceback (most recent call last):
    TypeError
"""

ADULT = 18


def check(age):
    ...


# Solution
def check(age):
    if type(age) not in (int, float):
        raise TypeError
    if age < 0:
        raise ValueError
    if age < ADULT:
        raise PermissionError
