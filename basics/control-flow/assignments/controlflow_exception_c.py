"""
* Assignment: ControlFlow Exception Except
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. Check value passed to a function
    2. Try converting it to `float`
    3. If unsuccessful, then print 'Invalid value' and exit with status code 1
    4. Write solution inside `check` function
    5. Mind the indentation level

Polish:
    1. Sprawdź wartość przekazaną do funkcji
    2. Spróbuj skonwertować ją do `float`
    3. Jeżeli się nie uda to wypisz 'Invalid value' i wyjdź z kodem błędu 1
    4. Rozwiązanie zapisz wewnątrz funkcji `check`
    5. Zwróć uwagę na poziom wcięć

Tests:
    >>> check('1')
    >>> check('1.0')
    >>> check('1,0')
    Traceback (most recent call last):
    SystemExit: 1
"""


# Given
def check(value):
    ...


# Solution
def check(value):
    try:
        float(value)
    except ValueError:
        exit(1)
