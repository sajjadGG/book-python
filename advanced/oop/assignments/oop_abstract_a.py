"""
* Assignment: OOP Abstract Syntax
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Create abstract class `IrisAbstract`
    2. Create abstract method `get_name()` in `IrisAbstract`
    3. Create class `Setosa` inheriting from `IrisAbstract`
    4. Try to create instance of a class `Setosa`
    5. Try to create instance of a class `IrisAbstract`
    6. Run doctests - all must succeed

Polish:
    1. Stwórz klasę abstrakcyjną `IrisAbstract`
    2. Stwórz metodę abstrakcyjną `get_name()` w `IrisAbstract`
    3. Stwórz klasę `Setosa` dziedziczące po `IrisAbstract`
    4. Spróbuj stworzyć instancje klasy `Setosa`
    5. Spróbuj stworzyć instancję klasy `IrisAbstract`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, isabstract, ismethod

    >>> assert isclass(IrisAbstract)
    >>> assert isclass(Setosa)
    >>> assert isabstract(IrisAbstract)
    >>> assert not isabstract(Setosa)
    >>> assert hasattr(IrisAbstract, 'get_name')
    >>> assert hasattr(Setosa, 'get_name')
    >>> assert not hasattr(Setosa.get_name, '__isabstractmethod__')
    >>> assert hasattr(IrisAbstract.get_name, '__isabstractmethod__')
    >>> assert IrisAbstract.get_name.__isabstractmethod__ == True
    >>> assert not hasattr(IrisAbstract, '__annotations__')
    >>> assert not hasattr(Setosa, '__annotations__')

    >>> iris = IrisAbstract()
    Traceback (most recent call last):
    TypeError: Can't instantiate abstract class IrisAbstract with abstract method get_name
    >>> setosa = Setosa()
    >>> assert ismethod(setosa.get_name)

Warning:
    * Last line of doctest, second to last word of `TypeError` message
    * In Python 3.7, 3.8 there is "methods" word in doctest
    * In Python 3.9 there is "method" word in doctest
    * So it differs by "s" at the end of "method" word
"""

# Solution
from abc import ABC, abstractmethod


class IrisAbstract(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Setosa(IrisAbstract):
    def get_name(self):
        pass
