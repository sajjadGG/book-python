"""
* Assignment: Operator String Format
* Required: yes
* Complexity: easy
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Overload `format()`
    2. Has to convert length units: km, cm, m
    3. Round result to one decimal place
    4. Run doctests - all must succeed

Polish:
    1. Przeciąż `format()`
    2. Ma konwertować jednostki długości: km, cm, m
    3. Wynik zaokrąglij do jednego miejsca po przecinku
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 1 km = 1000 m
    * 1 m = 100 cm

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = Distance(meters=1337)

    >>> format(result, 'km')
    '1.3'

    >>> format(result, 'cm')
    '133700.0'

    >>> format(result, 'm')
    '1337.0'
"""


METER = 1
CENTIMETER = METER * 0.01
KILOMETER = METER * 1000

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
        result = self.meters
        if unit in ('cm', 'centimeters'):
            result /= CENTIMETER
        elif unit in ('m', 'meters'):
            result /= METER
        elif unit in ('km', 'kilometers'):
            result /= KILOMETER
        return f'{result:.1f}'

    # Alternative Solution
    def __format__(self, unit):
        result = self.meters
        match unit:
            case 'cm' | 'centimeters':  result /= CENTIMETER
            case 'm'  | 'meters':       result /= METER
            case 'km' | 'kilometers':   result /= KILOMETER
        return f'{result:.1f}'
