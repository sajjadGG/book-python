"""
* Assignment: Function Generator Chain
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `result: float` with arithmetic mean of `DATA`
    2. Note, that all the time you are working on a data stream
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: float` ze średnią arytmetyczną z `DATA`
    2. Zwróć uwagę, że cały czas pracujesz na strumieniu danych
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * type cast to `list()` to expand generator before calculating mean
    * `mean = sum(...) / len(...)`
    * TypeError: object of type 'map' has no len()
    * ZeroDivisionError: division by zero

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(odd)
    >>> assert isfunction(cube)
    >>> assert type(result) is float

    >>> result
    245.0
"""

def odd(x):
    return x % 2


def cube(x):
    return x ** 3


DATA = range(0, 10)
DATA = filter(odd, DATA)
DATA = map(cube, DATA)

# Calculate mean of DATA
# type: float
result = ...


# Solution
data = list(DATA)
result = sum(result) / len(result)
