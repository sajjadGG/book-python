"""
* Assignment: OOP Abstract Interface
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

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
    >>> from inspect import isabstract

    >>> assert isabstract(IrisAbstract), \
    'IrisAbstract should be an abstract class, inherit from ABC or use ABCMeta'

    >>> assert hasattr(IrisAbstract, 'mean'), \
    'IrisAbstract, should have .mean() abstract method'

    >>> assert hasattr(IrisAbstract, 'sum'), \
    'IrisAbstract should have .sum() abstract method'

    >>> assert hasattr(IrisAbstract, 'len'), \
    'IrisAbstract should have .len() abstract method'

    >>> assert hasattr(IrisAbstract.mean, '__isabstractmethod__'), \
    'IrisAbstract.mean() should be an abstract method, use @abstractmethod'

    >>> assert hasattr(IrisAbstract.sum, '__isabstractmethod__'), \
    'IrisAbstract.sum() should be an abstract method, use @abstractmethod'

    >>> assert hasattr(IrisAbstract.len, '__isabstractmethod__'), \
    'IrisAbstract.len() should be an abstract method, use @abstractmethod'
"""

from abc import ABCMeta, abstractmethod


# Solution
class IrisAbstract(metaclass=ABCMeta):
    @abstractmethod
    def mean(self) -> float:
        ...

    @abstractmethod
    def sum(self) -> float:
        ...

    @abstractmethod
    def len(self) -> int:
        ...
