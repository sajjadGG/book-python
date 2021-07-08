"""
* Assignment: OOP Abstract Interface
* Complexity: easy
* Lines of code: 11 lines
* Time: 8 min

English:
    1. Define abstract class `IrisAbstract`
    3. Abstract methods: `__init__`, `sum()`, `len()`, `mean()`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę abstrakcyjną `IrisAbstract`
    3. Metody abstrakcyjne: `__init__`, `sum()`, `len()`, `mean()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isabstract, isclass

    >>> assert isclass(IrisAbstract)
    >>> assert isabstract(IrisAbstract)
    >>> assert hasattr(IrisAbstract, '__init__')
    >>> assert hasattr(IrisAbstract, 'mean')
    >>> assert hasattr(IrisAbstract, 'sum')
    >>> assert hasattr(IrisAbstract, 'len')
    >>> assert IrisAbstract.__init__.__isabstractmethod__ == True
    >>> assert IrisAbstract.mean.__isabstractmethod__ == True
    >>> assert IrisAbstract.sum.__isabstractmethod__ == True
    >>> assert IrisAbstract.len.__isabstractmethod__ == True

    >>> IrisAbstract.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>,
     'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>,
     'petal_width': <class 'float'>}
"""

from abc import ABCMeta, abstractmethod


class IrisAbstract:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:
        ...


# Solution
class IrisAbstract(metaclass=ABCMeta):
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
