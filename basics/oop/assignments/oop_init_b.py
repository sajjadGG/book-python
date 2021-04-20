"""
* Assignment: OOP Init Model
* Complexity: easy
* Lines of code: 12 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Model the data using classes
    3. Create instances for each record
    4. Values must be passed at the initialization
    5. Create instances of a first class using positional arguments
    6. Create instances of a second class using keyword arguments
    7. Do not use `@dataclass`
    8. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zamodeluj dane za pomocą klas
    3. Stwórz instancje dla każdego wpisu
    4. Wartości mają być podawane przy inicjalizacji
    5. Twórz instancje pierwszej klasy używając argumentów pozycyjnych
    6. Twórz instancje drugiej klasy używając argumentów nazwanych
    7. Nie używaj `@dataclass`
    8. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
    >>> assert 'Watney' in vars(watney).values()
    >>> assert 'USA' in vars(watney).values()
    >>> assert '1969-07-21' in vars(watney).values()
    >>> assert 'NASA' in vars(nasa).values()
    >>> assert 'USA' in vars(nasa).values()
    >>> assert '1958-07-29' in vars(nasa).values()
"""


# Given
"""
Watney, USA, 1969-07-21
NASA, USA, 1958-07-29
"""


# Solution
class Astronaut:
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


class SpaceAgency:
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


watney = Astronaut('Watney', 'USA', '1969-07-21')

nasa = SpaceAgency(name='NASA', country='USA', date='1958-07-29')
