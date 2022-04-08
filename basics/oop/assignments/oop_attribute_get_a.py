"""
* Assignment: OOP Attribute Set
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `result_watney: dict[str,str]`
       with all attributes and values of `watney` object
    2. Define `result_watney: dict[str,str]`
       with all attributes and values of `nasa` object
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result_watney: dict[str,str]`
       z wszystkimi atrybutami i wartościami obiektu `watney`
    2. Zdefiniuj `result_nasa: dict[str,str]`
       z wszystkimi atrybutami i wartościami obiektu `nasa`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result_watney) is dict
    >>> assert type(result_nasa) is dict

    >>> result_watney
    {'name': 'Watney', 'country': 'USA', 'date': '1969-07-21'}

    >>> result_nasa
    {'name': 'NASA', 'country': 'USA', 'date': '1958-07-29'}
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

watney.name = 'Watney'
watney.country = 'USA'
watney.date = '1969-07-21'

nasa.name = 'NASA'
nasa.country = 'USA'
nasa.date = '1958-07-29'


# Dict with all attributes and values of `watney` object
# type: dict[str,str]
result_watney = ...

# Dict with all attributes and values of `nasa` object
# type: dict[str,str]
result_nasa = ...


# Solution
result_watney = vars(watney)
result_nasa = vars(nasa)
