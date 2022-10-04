"""
* Assignment: OOP AttributeSlots Define
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

    >>> assert not hasattr(iris, '__dict__')
    >>> assert not hasattr(iris, '__weakref__')
    >>> assert hasattr(iris, '__slots__')

    >>> assert 'sepal_length' in iris.__slots__
    >>> assert 'sepal_width' in iris.__slots__
    >>> assert 'petal_length' in iris.__slots__
    >>> assert 'petal_width' in iris.__slots__
    >>> assert 'species' in iris.__slots__
"""

class Iris:
    ...


# Solution
class Iris:
    __slots__ = ('sepal_length', 'sepal_width',
                 'petal_length', 'petal_width', 'species')
