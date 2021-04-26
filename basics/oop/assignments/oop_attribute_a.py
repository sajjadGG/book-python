"""
* Assignment: OOP Attribute Model
* Required: yes
* Complexity: easy
* Lines of code: 15 lines
* Time: 8 min

English:
    1. Model the data using classes
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    2. How many classes are there?
    3. How many instances are there?
    4. Create instances filling it with data
    5. Run doctests - all must succeed

Polish:
    1. Zamodeluj dane za pomocą klas
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    2. Ile jest klas?
    3. Ile jest instancji?
    4. Stwórz instancje wypełniając je danymi
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
    >>> assert 'Watney' in watney.__dict__.values()
    >>> assert 'USA' in watney.__dict__.values()
    >>> assert '1969-07-21' in watney.__dict__.values()
    >>> assert 'NASA' in nasa.__dict__.values()
    >>> assert 'USA' in nasa.__dict__.values()
    >>> assert '1958-07-29' in nasa.__dict__.values()
"""

# Watney, USA, 1969-07-21
# NASA, USA, 1958-07-29


# Solution
class Astronaut:
    pass


class SpaceAgency:
    pass


watney = Astronaut()
watney.name = 'Watney'
watney.country = 'USA'
watney.date = '1969-07-21'

nasa = SpaceAgency()
nasa.name = 'NASA'
nasa.country = 'USA'
nasa.date = '1958-07-29'
