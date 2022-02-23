"""
* Assignment: Model Data AstronautAgency
* Complexity: easy
* Lines of code: 11 lines
* Time: 8 min

English:
    1. Create propper classes to model the data:
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    2. Create instances (watney, nasa) filling it with data
    3. Non-functional requirements:
        a. Do not convert data, just model it
        b. You can use any Python standard library module
        c. You can use SQLAlchemy and Alembic
        d. Do not install or use 3rd party modules
    4. Run doctests - all must succeed

Polish:
    1. Stwórz odpowiednie klasy aby zamodelować dane:
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    2. Stwórz instancje (watney, nasa) wypełniając je danymi
    3. Wymagania niefunkcjonalne:
        a. Nie konwertuj danych, tylko je zamodeluj
        b. Możesz użyć dowolnego modułu z biblioteki standardowej
        c. Możesz użyć SQLAlchemy i Alembic
        d. Nie instaluj ani nie używaj dodatkowych pakietów
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert 'Watney' in vars(watney).values()
    >>> assert 'USA' in vars(watney).values()
    >>> assert '1969-07-21' in vars(watney).values()
    >>> assert 'NASA' in vars(nasa).values()
    >>> assert 'USA' in vars(nasa).values()
    >>> assert '1958-07-29' in vars(nasa).values()
"""


# object: Model from data: 'Watney', 'USA', '1969-07-21'
watney = ...

# object: Model from data: 'NASA', 'USA', '1958-07-29'
nasa = ...


# Solution
from dataclasses import dataclass


@dataclass
class Astronaut:
    name: str
    country: str
    date: str


@dataclass
class SpaceAgency:
    name: str
    country: str
    date: str
