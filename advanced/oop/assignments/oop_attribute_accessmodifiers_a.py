"""
* Assignment: OOP AttributeAccessModifiers Dataclass
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Modify dataclass `Iris` to add attributes:
        a. Protected attributes: `sepal_length, sepal_width`
        b. Private attributes: `petal_length, petal_width`
        c. Public attribute: `species`
    2. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj dataclass `Iris` aby dodać atrybuty:
        a. Chronione atrybuty: `sepal_length, sepal_width`
        b. Private attributes: `petal_length, petal_width`
        c. Publiczne atrybuty: `species`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Iris)
    >>> assert hasattr(Iris, '__annotations__')

    >>> assert '_sepal_width' in Iris.__dataclass_fields__
    >>> assert '_sepal_length' in Iris.__dataclass_fields__
    >>> assert '_Iris__petal_width' in Iris.__dataclass_fields__
    >>> assert '_Iris__petal_length' in Iris.__dataclass_fields__
    >>> assert 'species' in Iris.__dataclass_fields__
"""
from dataclasses import dataclass


@dataclass
class Iris:
    pass


# Solution
@dataclass
class Iris:
    _sepal_width: float
    _sepal_length: float
    __petal_width: float
    __petal_length: float
    species: str
