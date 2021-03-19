"""
* Assignment: Protocol Reflection Setattr
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Create class `Point` with `x`, `y`, `z` attributes
    3. Prevent creation of new attributes
    4. Allow modifying values of `x`, `y`, `z`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `Point` z atrybutami `x`, `y`, `z`
    3. Zablokuj tworzenie nowych atrybutów
    4. Zezwól na modyfikowanie wartości `x`, `y`, `z`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> pt = Point(1, 2, 3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)
    >>> pt.notexisting = 10
    Traceback (most recent call last):
    PermissionError: Cannot set other attributes than x,y,z
    >>> pt.x = 10
    >>> pt.y = 20
    >>> pt.z = 30
    >>> pt.x, pt.y, pt.z
    (10, 20, 30)
"""


# Given
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    z: int


# Solution
@dataclass
class Point:
    x: int
    y: int
    z: int

    def __setattr__(self, name, value):
        if name not in ('x', 'y', 'z'):
            raise PermissionError('Cannot set other attributes than x,y,z')
        return super().__setattr__(name, value)
