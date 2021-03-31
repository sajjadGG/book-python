"""
* Assignment: Exception Catch Else
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Convert value passed to the `check` function as a `float`
    3. If conversion fails, raise `TypeError`
    4. If value is below AGE, raise `PermissionError`
    5. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj wartośc przekazaną do funckji `check` jako `float`
    3. Jeżeli konwersja się nie powiedzie, podnieś `TypeError`
    4. Jeżeli wartość jest poniżej AGE, podnieś `PermissionError`
    5. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> check(21)
    >>> check('one')
    Traceback (most recent call last):
    TypeError
    >>> check(1)
    Traceback (most recent call last):
    PermissionError
"""

# Given
ADULT = 18


def check(age):
    ...


# Solution
def check(age):
    try:
        age = float(age)
    except Exception:
        raise TypeError
    else:
        if age < ADULT:
            raise PermissionError
