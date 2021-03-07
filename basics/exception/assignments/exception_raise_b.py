"""
* Assignment: Exception Raise Many
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Use data from "Given" section (see below)
    2. Validate value passed to a `check` function
    3. If `value` is:
        a. other type than `int` or `float` raise `TypeError`
        a. less than zero, raise `ValueError`
        a. below ADULT, raise `PermissionError`
    3. Non functional Requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Sprawdź poprawność wartości przekazanej do funckji `check`
    3. Jeżeli `age` jest:
        b. innego typu niż `float` lub int, podnieś wyjątek `TypeError`
        b. mniejsze niż zero, podnieś wyjątek `ValueError`
        c. mniejsze niż ADULT, podnieś wyjątek `PermissionError`
    3. Non functional Requirements
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

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

# Given
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
