"""
* Assignment: Exception Catch Except
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Convert value passed to the `check` function as a `float`
        a. If conversion fails, exit program with status code 1
    3. Non functional Requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj wartośc przekazaną do funckji `check` jako `float`
        a. Jeżeli konwersja się nie powiedzie, zakończ program ze statusem 1
    3. Non functional Requirements
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

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
