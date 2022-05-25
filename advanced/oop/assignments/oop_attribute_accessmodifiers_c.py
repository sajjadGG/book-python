"""
* Assignment: OOP Access Members
* Complexity: easy
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Extract from class `Iris` attribute names and their values:
        a. Define `protected: dict` with protected attributes
        b. Define `private: dict` with private attributes
        c. Define `public: dict` with public attributes
    2. Run doctests - all must succeed

Polish:
    1. Wydobądź z klasy `Iris` nazwy atrybutów i ich wartości:
        a. Zdefiniuj `protected: dict` z atrybutami chronionymi (protected)
        b. Zdefiniuj `private: dict` z atrybutami prywatnymi (private)
        c. Zdefiniuj `public: dict` z atrybutami publicznymi (public)
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(public) is dict
    >>> assert all(type(k) is str for k,v in public.items())
    >>> assert all(type(v) is str for k,v in public.items())

    >>> assert type(protected) is dict
    >>> assert all(type(k) is str for k,v in protected.items())
    >>> assert all(type(v) is float for k,v in protected.items())

    >>> assert type(private) is dict
    >>> assert all(type(k) is str for k,v in private.items())
    >>> assert all(type(v) is float for k,v in private.items())

    >>> assert len(public) > 0, \
    'public: list[dict] must not be empty'

    >>> assert len(protected) > 0, \
    'protected: list[dict] must not be empty'

    >>> assert len(private) > 0, \
    'private: list[dict] must not be empty'

    >>> public
    {'species': 'virginica'}

    >>> protected
    {'_sepal_width': 5.8, '_sepal_length': 2.7}

    >>> private
    {'_Iris__petal_width': 5.1, '_Iris__petal_length': 1.9}

"""
from dataclasses import dataclass


@dataclass
class Iris:
    _sepal_width: float
    _sepal_length: float
    __petal_width: float
    __petal_length: float
    species: str


DATA = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')


# All public attributes and their values
# type: dict[str,float|str]
public = ...

# All protected attributes and their values
# type: dict[str,float|str]
protected = ...

# All private attributes and their values
# type: dict[str,float|str]
private = ...

# Solution
public = {attrname: attrvalue
          for attrname, attrvalue in vars(DATA).items()
          if not attrname.startswith('_')}

protected = {attrname: attrvalue
             for attrname, attrvalue in vars(DATA).items()
             if attrname.startswith('_')
             and not attrname.startswith(f'_Iris')}

private = {attrname: attrvalue
           for attrname, attrvalue in vars(DATA).items()
           if attrname.startswith(f'_Iris')}
