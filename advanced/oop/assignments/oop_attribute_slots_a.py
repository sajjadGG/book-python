"""
* Assignment: OOP Slots Define
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define class `Iris` with attributes: `sepal_length, sepal_width,
       petal_length, petal_width, species`
    2. All attributes must be in `__slots__`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Iris` z atrybutami: `sepal_length, sepal_width,
       petal_length, petal_width, species`
    2. Wszystkie atrybuty muszą być w `__slots__`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> iris = Iris()

    >>> iris.__slots__
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')

    >>> iris.__dict__
    Traceback (most recent call last):
    AttributeError: 'Iris' object has no attribute '__dict__'
"""

class Iris:
    ...


# Solution
class Iris:
    __slots__ = ('sepal_length', 'sepal_width',
                 'petal_length', 'petal_width', 'species')
