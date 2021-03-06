"""
* Assignment: ControlFlow Exception Finally
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Check age passed to a function
    2. If value is below AGE,
       raise `PermissionError` with message "Adults only"
    3. Write solution inside `check` function
    4. Mind the indentation level

Polish:
    1. Sprawdź wiek przekazany do funkcji
    2. Jeżeli wartość jest poniżej AGE,
       podnieś wyjątek `PermissionError` z komunikatem "Adults only"
    3. Rozwiązanie zapisz wewnątrz funkcji `check`
    4. Zwróć uwagę na poziom wcięć

Tests:
    >>> check(1)
    >>> check(-1)
    Traceback (most recent call last):
    ValueError
"""

# Given
ADULT = 18


def check(age):
    ...


# Solution
def check(age):
    if float(age) < ADULT:
        raise PermissionError('Adults only')
