"""
* Assignment: Math Trigonometry
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Read input (angle in degrees) from user
    2. User will type `int` or `float`
    3. Print all trigonometric functions (sin, cos, tg, ctg)
    4. If there is no value for this angle, raise an exception
    5. Run doctests - all must succeed

Polish:
    1. Program wczytuje od użytkownika wielkość kąta w stopniach
    2. Użytkownik zawsze podaje `int` albo `float`
    3. Wyświetl wartość funkcji trygonometrycznych (sin, cos, tg, ctg)
    4. Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta podnieś
       stosowny wyjątek
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `input('Type angle [deg]: ')`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result
    {'sin': 0.02, 'cos': 1.0, 'tg': 0.02, 'ctg': 0.02, 'PI': 3.14}
"""

import math
from unittest.mock import MagicMock


# Simulate user input (for test automation)
input = MagicMock(side_effect=['1'])


PRECISION = 2

degrees = input('What is the angle [deg]?: ')

# Solution
radians = math.radians(float(degrees))

result = {
    'sin': round(math.sin(radians), PRECISION),
    'cos': round(math.cos(radians), PRECISION),
    'tg': round(math.tan(radians), PRECISION),
    'ctg': round(math.atan(radians), PRECISION),
    'PI': round(math.pi, PRECISION),
}
