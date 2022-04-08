"""
* Assignment: OOP Attribute Set
* Required: yes
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Modify code below
    2. Set attibutes of watney and nasa instances to model the data:
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej
    2. Ustaw atrybuty instancji watney i nasa by zamodelować dane:
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
    >>> assert 'Watney' in vars(watney).values()
    >>> assert 'USA' in vars(watney).values()
    >>> assert '1969-07-21' in vars(watney).values()
    >>> assert 'NASA' in vars(nasa).values()
    >>> assert 'USA' in vars(nasa).values()
    >>> assert '1958-07-29' in vars(nasa).values()
"""


class Astronaut:
    name: str
    country: str
    date: str


class SpaceAgency:
    name: str
    country: str
    date: str


watney = Astronaut()
nasa = SpaceAgency()

# Watney, USA, 1969-07-21
# NASA, USA, 1958-07-29


# Solution
watney.name = 'Watney'
watney.country = 'USA'
watney.date = '1969-07-21'

nasa.name = 'NASA'
nasa.country = 'USA'
nasa.date = '1958-07-29'
