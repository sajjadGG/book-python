"""
* Assignment: Exception Custom Exception
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Ask user to input angle in degrees
    2. Validate value passed to a `check` function
    2. Define custom exception `NegativeKelvin`
    3. If input temperature is lower than 0, raise `NegativeKelvin`

Polish:
    1. Poproś użytkownika o wprowadzenie kąta
    2. Zdefiniuj własny wyjątek `NegativeKelvin`
    3. Jeżeli wprowadzona temperature jest mniejsza niż 0, podnieś `NegativeKelvin`

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
