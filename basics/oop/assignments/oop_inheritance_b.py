"""
* Assignment: OOP Inheritance Multiple
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Use data from "Given" section (see below)
    2. Create class `Astronaut` which inherits from all of those classes
    3. Run doctests - all must succeed

Polish:
    1. Use data from "Given" section (see below)
    2. Stwórz klasę `Astronaut`, która dziedziczy po tych wszystkich klasach
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> from inspect import isclass
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert isclass(Scientist)
    >>> assert isclass(Engineer)
    >>> assert isclass(Pilot)
    >>> assert isclass(MedicalDoctor)
    >>> assert isclass(Astronaut)
    >>> assert issubclass(Astronaut, Scientist)
    >>> assert issubclass(Astronaut, Engineer)
    >>> assert issubclass(Astronaut, Pilot)
    >>> assert issubclass(Astronaut, MedicalDoctor)
"""


# Given
class Scientist:
    pass


class Engineer:
    pass


class Pilot:
    pass


class MedicalDoctor:
    pass


# Solution
class Astronaut(Scientist, Engineer, Pilot, MedicalDoctor):
    pass
