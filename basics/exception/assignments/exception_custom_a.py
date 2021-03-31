"""
* Assignment: Exception Custom Exception
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define custom exception `NegativeKelvin`
    3. Check value passed to a `check` function
    4. If input value is lower than 0, raise `NegativeKelvin`
    5. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj własny wyjątek `NegativeKelvin`
    3. Sprawdź wartośc przekazaną do funckji jako `float`
    4. Jeżeli wprowadzona wartość jest mniejsza niż 0, podnieś `NegativeKelvin`
    5. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass
    >>> isclass(NegativeKelvin)
    True
    >>> issubclass(NegativeKelvin, Exception)
    True
    >>> check(1)
    >>> check(0)
    >>> check(-1)
    Traceback (most recent call last):
    exception_custom_a.NegativeKelvin
"""


# Given
def check(value):
    ...


# Solution
class NegativeKelvin(Exception):
    pass


def check(value):
    if value < 0:
        raise NegativeKelvin
