"""
* Assignment: OOP Abstract Annotate
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Modify abstract class `IrisAbstract`
    2. Add type annotation to all methods and attributes
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę abstrakcyjną `IrisAbstract`
    2. Dodaj anotację typów do wszystkich metod i atrybutów
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isabstract, isclass

    >>> assert isclass(IrisAbstract)
    >>> assert isabstract(IrisAbstract)
    >>> assert hasattr(IrisAbstract, '__init__')
    >>> assert hasattr(IrisAbstract, 'mean')
    >>> assert hasattr(IrisAbstract, 'sum')
    >>> assert hasattr(IrisAbstract, 'len')
    >>> assert hasattr(IrisAbstract.__init__, '__isabstractmethod__')
    >>> assert hasattr(IrisAbstract.mean, '__isabstractmethod__')
    >>> assert hasattr(IrisAbstract.sum, '__isabstractmethod__')
    >>> assert hasattr(IrisAbstract.len, '__isabstractmethod__')
    >>> assert IrisAbstract.__init__.__isabstractmethod__ == True
    >>> assert IrisAbstract.mean.__isabstractmethod__ == True
    >>> assert IrisAbstract.sum.__isabstractmethod__ == True
    >>> assert IrisAbstract.len.__isabstractmethod__ == True

    >>> IrisAbstract.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>,
     'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>,
     'petal_width': <class 'float'>}

    >>> IrisAbstract.__init__.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>,
     'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>,
     'petal_width': <class 'float'>,
     'return': None}

     >>> IrisAbstract.mean.__annotations__
     {'return': <class 'float'>}

     >>> IrisAbstract.sum.__annotations__
     {'return': <class 'float'>}

     >>> IrisAbstract.len.__annotations__
     {'return': <class 'int'>}
"""

from abc import ABC, abstractmethod


class IrisAbstract(ABC):

    @abstractmethod
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        ...

    @abstractmethod
    def mean(self):
        ...

    @abstractmethod
    def sum(self):
        ...

    @abstractmethod
    def len(self):
        ...

# Modify abstract class `IrisAbstract`
# Add type annotation to all methods and attributes

# Solution
class IrisAbstract(ABC):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    @abstractmethod
    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:
        ...

    @abstractmethod
    def mean(self) -> float:
        ...

    @abstractmethod
    def sum(self) -> float:
        ...

    @abstractmethod
    def len(self) -> int:
        ...
