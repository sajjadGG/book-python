"""
* Assignment: OOP Composition Composition
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create class `MarsMission` from classes `Habitat`, `Rocket`, `Astronaut`
    3. Use composition
    4. Assignment demonstrates syntax, so do not add any attributes and methods (only type annotations)
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `MarsMission` z klas `Habitat`, `Rocket`, `Astronaut`
    3. Użyj kompozycji
    4. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod (tylko anotacje typów)
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass
    >>> assert isclass(Habitat)
    >>> assert isclass(Astronaut)
    >>> assert isclass(Rocket)
    >>> assert isclass(MarsMission)
    >>> assert MarsMission.__annotations__['habitat'] is Habitat
    >>> assert MarsMission.__annotations__['astronaut'] is Astronaut
    >>> assert MarsMission.__annotations__['rocket'] is Rocket
"""


# Solution
class Habitat:
    pass


class Astronaut:
    pass


class Rocket:
    pass


class MarsMission:
    habitat: Habitat
    astronaut: Astronaut
    rocket: Rocket
