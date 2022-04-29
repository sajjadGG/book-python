.. testsetup::

    # doctest: +SKIP_FILE

    >>> class Dragon:
    ...     def __init__(*args, **kwargs):
    ...         pass


Dragon ADR Init Position
========================
* ADR - Architecture Design Records


Problem
-------
* Create dragon at x=50, y=120 position


Option 1
--------
>>> dragon = Dragon('Wawelski', 50, 120)

* Good: easy to use
* Bad: not explicit
* Bad: requires knowledge of API to answer what are those numbers
* Bad: It does suggest, that x and y are some parameters to texture (for example width and height of a texture image)

Problems:

>>> dragon = Dragon('Wawelski', 'img/dragon/alive.png', 50, 120)
>>> knn = KNearestNeighbors(k=3)


Option 2
--------
>>> dragon = Dragon('Wawelski', x=50, y=120)

* Good: easy to use
* Good: short argument names
* Good: verbose in this example
* Bad: It does suggest, that x and y are some parameters to texture (for example width and height of a texture image)

Problems:

>>> dragon = Dragon('Wawelski', 'img/dragon/alive.png', x=50, y=120)
>>> knn = KNearestNeighbors(k=3, w=[1,2,3])


Option 3
--------
>>> dragon = Dragon('Wawelski', posx=50, posy=120)
>>> dragon = Dragon('Wawelski', pos_x=50, pos_y=120)

* Good: simple, easy to use
* Good: you can assign ``None`` by default to set default point
* Good: extensible, easy to add ``pos_z`` with default value ``0``

Problem:

>>> knn = KNearestNeighbors(k=3, wgt=[1,2,3])


Option 4
--------
>>> dragon = Dragon('Wawelski', positionx=50, positiony=120)
>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

* Good: simple, easy to use
* Good: you can assign ``None`` by default to set default point
* Good: extensible, easy to add ``position_z`` with default value ``0``

Problem:

>>> knn = KNearestNeighbors(k=3, weights=[1,2,3])


Option 5
--------
>>> dragon = Dragon('Wawelski', pos=(50, 120))
>>> dragon = Dragon('Wawelski', position=(50, 120))

* Good: data is stored together (coordinate)
* Good: simple, easy to use
* Good: you can assign ``None`` by default to set default ``position``
* Good: always has to pass both ``x`` and ``y``
* Bad: always has to pass both ``x`` and ``y``
* Bad: you have to know that first is ``x`` and second is ``y``
* Bad: order is important
* Bad: unpacking
* Bad: not extensible, ``position`` will always be 2D


Option 6
--------
>>> dragon = Dragon('Wawelski', posxy=(50, 120))
>>> dragon = Dragon('Wawelski', pos_xy=(50, 120))
>>> dragon = Dragon('Wawelski', position_xy=(50, 120))

* Good: data is stored together (coordinate)
* Good: simple, easy to use
* Good: you can assign ``None`` by default to set default ``position``
* Good: always has to pass both ``x`` and ``y``
* Bad: always has to pass both ``x`` and ``y``
* Bad: you have to know that first is ``x`` and second is ``y``
* Bad: order is important
* Bad: unpacking
* Bad: not extensible, ``position_xy`` will always be 2D


Option 7
--------
>>> dragon = Dragon('Wawelski', pos={'x':50, 'y':120})
>>> dragon = Dragon('Wawelski', position={'x':50, 'y':120})

* Good: data is stored together (coordinate)
* Good: you can assign ``None`` by default to set default point
* Good: order is not important
* Good: always has to pass both ``x`` and ``y``
* Good: possible to extend to 3D with refactoring
* Good: easier to refactor than tuple - ``pattern = r'{'x':\d+, 'y':\d+}'``
* Bad: always has to pass both ``x`` and ``y``
* Bad: unpacking
* Bad: not extensible, ``position`` will always be 2D


Option 8
--------
>>> from collections import namedtuple
>>>
>>>
>>> Position = namedtuple('Position', ['x', 'y'])
>>>
>>> dragon = Dragon('Wawelski', Position(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=120))

* Good: data is stored together (coordinate)
* Good: simple, easy to use
* Good: always has to pass both ``x`` and ``y``
* Good: relatively easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Bad: always has to pass both ``x`` and ``y``
* Bad: not extensible, ``position`` will always be 2D


Option 9
--------
>>> from typing import NamedTuple
>>>
>>>
>>> class Position(NamedTuple):
...     x: int = 0
...     y: int = 0
>>>
>>>
>>> dragon = Dragon('Wawelski', Position(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=120))

* Good: data is stored together (coordinate)
* Good: simple, easy to use
* Good: verbose
* Good: you can assign ``None`` by default to set default ``position``
* Good: very easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough


Option 10
---------
>>> from typing import TypedDict
>>>
>>>
>>> class Position(TypedDict):
...     x: int
...     y: int
>>>
>>>
>>> pt1 = Position(x=50, y=120)
>>> pt2: Position = {'x': 50, 'y': 120}
>>>
>>> dragon = Dragon('Wawelski', position=pt1)
>>> dragon = Dragon('Wawelski', position=pt2)

* Good: data is stored together (coordinate)
* Good: simple
* Good: you can assign ``position=None`` by default to set default ``position``
* Good: relatively easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Bad: ``TypeDict`` does not support default values


Option 11
---------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Point:
...     x: int = 0
...     y: int = 0
>>>
>>>
>>> dragon = Dragon('Wawelski', Point(50, 120))
>>> dragon = Dragon('Wawelski', pos=Point(50, 120))
>>> dragon = Dragon('Wawelski', posxy=Point(50, 120))
>>> dragon = Dragon('Wawelski', pos_xy=Point(50, 120))
>>> dragon = Dragon('Wawelski', position=Point(50, 120))

* Good: data is stored together (coordinate)
* Good: simple, easy to use
* Good: verbose
* Good: you can assign ``None`` by default to set default ``position``
* Good: very easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough


Option 12
---------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(frozen=True, slots=True)
... class Point:
...     x: int = 0
...     y: int = 0
>>>
>>>
>>> dragon = Dragon('Wawelski', Point(50, 120))
>>> dragon = Dragon('Wawelski', pos=Point(50, 120))
>>> dragon = Dragon('Wawelski', posxy=Point(50, 120))
>>> dragon = Dragon('Wawelski', pos_xy=Point(50, 120))
>>> dragon = Dragon('Wawelski', position=Point(50, 120))

* Good: data is stored together (coordinate)
* Good: simple, easy to use
* Good: verbose
* Good: you can assign ``None`` by default to set default ``position``
* Good: very easy to extend to 3D
* Good: keyword argument is not required, class name is verbose enough
* Good: is faster and leaner than simple dataclass


Option 13
---------
>>> class Point:
...     x: int
...     y: int
...
...     def __init__(self, x: int = 0, y: int = 0) -> None:
...         self.x = x
...         self.y = y
>>>
>>>
>>> dragon = Dragon('Wawelski', Point(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Point(posx=50, posy=120))
>>> dragon = Dragon('Wawelski', position=Point(position_x=50, position_y=120))

* Good: very common
* Good: easy to use
* Good: more explicit than ``dataclass``
* Good: easy to extend to 3D
* Good: can sat default values
* Good: keyword argument is not required, class name is verbose enough


Decision
--------
>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

* Good: simple
* Good: explicit
* Good: verbose
* Good: extensible

Alternative:

>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))

* Choices: ``NameTuple``, ``dataclass(frozen=True, slots=True)``
* Good: explicit
* Good: verbose
* Good: extensible
* Bad: to complex for now
