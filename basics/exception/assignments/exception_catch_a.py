"""
* Assignment: Exception Catch Except
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Convert value passed to the `check` function as a `float`
    3. If conversion fails then print 'Invalid value'
    4. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj wartośc przekazaną do funckji `check` jako `float`
    3. Jeżeli konwersja się nie powiedzie to wypisz 'Invalid value'
    4. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> check('1')
    >>> check('1.0')
    >>> check('1,0')
    Invalid value
"""


# Given
def check(value):
    ...


# Solution
def check(value):
    try:
        float(value)
    except ValueError:
        print('Invalid value')
