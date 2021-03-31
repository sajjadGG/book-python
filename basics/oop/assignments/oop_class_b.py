"""
* Assignment: OOP Class Instance
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. Define class `Astronaut`
    2. Define class `SpaceAgency`
    3. Create instance `watney` of a class `Astronaut`
    4. Create instance `nasa` of a class `SpaceAgency`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj klasę `Astronaut`
    2. Zdefiniuj klasę `SpaceAgency`
    3. Stwórz instancję `watney` klasy `Astronaut`
    4. Stwórz instancję `nasa` klasy `SpaceAgency`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert isclass(Astronaut)
    >>> assert isclass(SpaceAgency)
    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
"""


# Solution
class Astronaut:
    pass


class SpaceAgency:
    pass


watney = Astronaut()
nasa = SpaceAgency()
