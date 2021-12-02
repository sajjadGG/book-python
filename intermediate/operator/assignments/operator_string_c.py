"""
* Assignment: Operator String Format
* Required: yes
* Complexity: easy
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Overload `format()`
    2. Has to convert length units: km, cm, m
    3. Run doctests - all must succeed

Polish:
    1. Przeciąż `format()`
    2. Ma konwertować jednostki długości: km, cm, m
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 1 km = 1000 m
    * 1 m = 100 cm

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = Distance(meters=1337)
    >>> format(result, 'km')
    '1.337'
    >>> format(result, 'cm')
    '133700'
    >>> format(result, 'm')
    '1337'
"""


class Distance:
    meters: int

    def __init__(self, meters):
        self.meters = meters


# Solution
class Distance:
    meters: int

    def __init__(self, meters):
        self.meters = meters

    def __format__(self, unit):
        if unit in ('cm', 'centimeter', 'centimeters'):
            result = self.meters * 100
        elif unit in ('m', 'meter', 'meters'):
            result = self.meters
        elif unit in ('km', 'kilometer', 'kilometers'):
            result = self.meters / 1000
        return str(result)
