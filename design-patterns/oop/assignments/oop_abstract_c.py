"""
* Assignment: OOP Abstract Annotate
* Complexity: easy
* Lines of code: 13 lines
* Time: 8 min

English:
    1. Define abstract class `IrisAbstract`
    2. Attributes: `sepal_length, sepal_width, petal_length, petal_width`
    3. Abstract methods: `__init__`, `sum()`, `len()`, `mean()`
    4. Add type annotation to all methods and attibutes
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę abstrakcyjną `IrisAbstract`
    2. Atrybuty: `sepal_length, sepal_width, petal_length, petal_width`
    3. Metody abstrakcyjne: `__init__`, `sum()`, `len()`, `mean()`
    4. Dodaj anotację typów do wszystkich metod i atrybutów
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isabstract

    >>> assert isabstract(IrisAbstract), \
    'IrisAbstract should be an abstract class, inherit from ABC or use ABCMeta'

    >>> assert hasattr(IrisAbstract, '__init__'), \
    'IrisAbstract, should have .__init__() abstract method'

    >>> assert hasattr(IrisAbstract, 'mean'), \
    'IrisAbstract, should have .mean() abstract method'

    >>> assert hasattr(IrisAbstract, 'sum'), \
    'IrisAbstract should have .sum() abstract method'

    >>> assert hasattr(IrisAbstract, 'len'), \
    'IrisAbstract should have .len() abstract method'

    >>> assert hasattr(IrisAbstract.__init__, '__isabstractmethod__'), \
    'IrisAbstract.__init__() should be an abstract method, use @abstractmethod'

    >>> assert hasattr(IrisAbstract.mean, '__isabstractmethod__'), \
    'IrisAbstract.mean() should be an abstract method, use @abstractmethod'

    >>> assert hasattr(IrisAbstract.sum, '__isabstractmethod__'), \
    'IrisAbstract.sum() should be an abstract method, use @abstractmethod'

    >>> assert hasattr(IrisAbstract.len, '__isabstractmethod__'), \
    'IrisAbstract.len() should be an abstract method, use @abstractmethod'

    >>> assert hasattr(IrisAbstract, '__annotations__'), \
    'IrisAbstract class should have fields type annotations'

    >>> assert hasattr(IrisAbstract.__init__, '__annotations__'), \
    'IrisAbstract.__init__() method should have parameter type annotations'

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

from abc import ABCMeta, abstractmethod


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
