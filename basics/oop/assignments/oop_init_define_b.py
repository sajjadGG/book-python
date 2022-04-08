"""
* Assignment: OOP Init Model
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Modify code below
    2. Define `__init__()` method in both classes
    3. Signature should reflect class attributes
    4. Do not execute any code inside `__init__()`, leave `...`
    5. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej
    2. Zdefiniuj metodę `__init__()` w obu klasach
    3. Sygnaturą powinna odpowiadać atrybutom klasy
    4. Nie uruchamiaj żadnego kodu wewnątrz `__init__()`, pozostaw `...`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import ismethod, signature

    >>> watney = Astronaut('Watney', 'USA', '1969-07-21')
    >>> nasa = Astronaut('NASA', 'USA', '1958-07-29')

    >>> assert ismethod(watney.__init__)
    >>> assert ismethod(nasa.__init__)

    >>> signature(watney.__init__)
    <Signature (name, country, date)>
    >>> signature(Astronaut.__init__)
    <Signature (self, name, country, date)>
    >>> signature(SpaceAgency.__init__)
    <Signature (self, name, country, date)>
    >>> signature(nasa.__init__)
    <Signature (self, name, country, date)>
"""


# Watney, USA, 1969-07-21
# NASA, USA, 1958-07-29

class Astronaut:
    name: str
    country: str
    date: str


class SpaceAgency:
    name: str
    country: str
    date: str


# Solution
class Astronaut:
    name: str
    country: str
    date: str

    def __init__(self, name, country, date):
        ...


class SpaceAgency:
    name: str
    country: str
    date: str

    def __init__(self, name, country, date):
        ...