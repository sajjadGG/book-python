"""
* Assignment: Exception Custom Exception
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Ask user to input angle in degrees
    2. Define custom exception `NegativeKelvin`
    3. If input temperature is lower than 0, raise `NegativeKelvin`
    4. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    5. Compare result with "Tests" section (see below)

Polish:
    1. Poproś użytkownika o wprowadzenie kąta
    2. Zdefiniuj własny wyjątek `NegativeKelvin`
    3. Jeżeli wprowadzona temperature jest mniejsza niż 0, podnieś `NegativeKelvin`
    4. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(temperature)
    <class 'float'>
    >>> from inspect import isclass
    >>> isclass(NegativeKelvin)
    True
    >>> issubclass(NegativeKelvin, Exception)
    True

TODO: Input Stub
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
