"""
* Assignment: OOP InheritancePatterns NoInheritance
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Create classes `MarsMission`, `Habitat`, `Rocket`, `Astronaut`
    2. Do not use inheritance
    3. Assignment demonstrates syntax, so do not add any attributes and methods
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasy `MarsMission`, `Habitat`, `Rocket`, `Astronaut`
    2. Nie używaj dziedziczenia
    3. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Habitat)
    >>> assert isclass(Astronaut)
    >>> assert isclass(Rocket)
    >>> assert isclass(MarsMission)
"""


# Solution
class Habitat:
    pass


class Astronaut:
    pass


class Rocket:
    pass


class MarsMission:
    pass
