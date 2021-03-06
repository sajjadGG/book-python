"""
* Assignment: ControlFlow Exception RaiseOne
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Use data from "Given" section (see below)
    2. Validate value passed to a `check` function
        a. If `value` is less than zero, raise `ValueError`
    3. Non functional Requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Sprawdź poprawność wartości przekazanej do funckji `check`
        a. Jeżeli `value` jest mniejsze niż zero, podnieś wyjątek `ValueError`
    3. Non functional Requirements
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> check(1)
    >>> check(0)
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
