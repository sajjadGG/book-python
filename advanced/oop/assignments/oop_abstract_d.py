"""
* Assignment: OOP Abstract Implement
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define class `Setosa` implementing `IrisAbstract`
    2. All method signatures must be identical to `IrisAbstract`
    2. Don't implement methods, leave `...` as content
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Setosa` implementującą `IrisAbstract`
    2. Sygnatury wszystkich metod muszą być identyczne do `IrisAbstract`
    2. Nie implementuj metod, pozostaw `...` jako zawartość
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isabstract, isclass, ismethod, signature

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

    >>> assert isclass(Setosa)
    >>> result = Setosa(5.1, 3.5, 1.4, 0.2)

    >>> result.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>, 'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>, 'petal_width': <class 'float'>}

    >>> assert hasattr(result, '__init__')
    >>> assert hasattr(result, 'len')
    >>> assert hasattr(result, 'sum')
    >>> assert hasattr(result, 'mean')

    >>> assert ismethod(result.__init__)
    >>> assert ismethod(result.len)
    >>> assert ismethod(result.sum)
    >>> assert ismethod(result.mean)

    >>> signature(result.__init__)  # doctest: +NORMALIZE_WHITESPACE
    <Signature (sepal_length: float, sepal_width: float, petal_length:
    float, petal_width: float) -> None>
    >>> signature(result.len)
    <Signature () -> int>
    >>> signature(result.sum)
    <Signature () -> float>
    >>> signature(result.mean)
    <Signature () -> float>

    >>> assert vars(result) == {}
    >>> assert result.len() is None
    >>> assert result.mean() is None
    >>> assert result.sum() is None
"""

from abc import ABCMeta, abstractmethod


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


# Solution
class Setosa(IrisAbstract):
    def __init__(self, sepal_length: float, sepal_width: float,
                 petal_length: float, petal_width: float) -> None:
        ...

    def mean(self) -> float:
        ...

    def sum(self) -> float:
        ...

    def len(self) -> int:
        ...
