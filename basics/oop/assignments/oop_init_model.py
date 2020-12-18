"""
* Assignment: OOP Init Model
* Filename: oop_init_model.py
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
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zamodeluj dane za pomocą klas
    3. Stwórz instancje dla każdego wpisu
    4. Wartości mają być podawane przy inicjalizacji
    5. Twórz instancje pierwszej klasy używając argumentów pozycyjnych
    6. Twórz instancje drugiej klasy używając argumentów nazwanych
    7. Nie używaj `@dataclass`
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
    >>> assert 'Watney' in watney.__dict__.values()
    >>> assert 'USA' in watney.__dict__.values()
    >>> assert '1969-07-21' in watney.__dict__.values()
    >>> assert 'NASA' in nasa.__dict__.values()
    >>> assert 'USA' in nasa.__dict__.values()
    >>> assert '1958-07-29' in nasa.__dict__.values()
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

nasa = SpaceAgency(
    name='NASA',
    country='USA',
    date='1958-07-29')
