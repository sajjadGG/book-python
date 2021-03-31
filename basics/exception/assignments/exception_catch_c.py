"""
* Assignment: Exception Catch Finally
* Complexity: easy
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Convert value passed to the function as a `int`
    3. If conversion fails, raise exception `TypeError` with message:
        'Invalid type, expected int or float'
    4. Use `finally` to print `degree` value
    5. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj wartośc przekazaną do funckji jako `int`
    3. Jeżeli konwersja się nie powiedzie to podnieś wyjątek `TypeError`
        z komunikatem 'Invalid type, expected int or float'
    4. Użyj `finally` do wypisania wartości `degree`
    5. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> check(1)
    1
    >>> check(180)
    180
    >>> check(1.0)
    1
    >>> check('one')
    Traceback (most recent call last):
    TypeError: Invalid type, expected int or float
"""


# Given
def check(value):
    ...


# Solution
def check(degrees):
    try:
        degrees = int(degrees)
    except ValueError:
        raise TypeError('Invalid type, expected int or float')
    finally:
        print(degrees)
