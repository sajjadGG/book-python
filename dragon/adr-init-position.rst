Dragon ADR Init Position
========================


.. testsetup::

    class Dragon:
        def __init__(*args, **kwargs):
            pass


Rationale
---------
* ADR - Architecture Design Records
* Create dragon at x=50, y=120 position and name it "Wawelski"


Option 1
--------
>>> dragon = Dragon('Wawelski', 50, 120)

* Good: easy to use
* Bad: not explicit
* Bad: requires knowledge of API to answer what are those numbers


Option 2
--------
>>> dragon = Dragon('Wawelski', x=50, y=120)

* Good: short argument names
* Good: easy to use
* Good: verbose in this example

Problems:

>>> dragon = Dragon('Wawelski', 'img/dragon/alive.png', 50, 120)
>>> dragon = Dragon('Wawelski', 'img/dragon/alive.png', x=50, y=120)

* Bad: It does suggest, that x and y are some parameters to texture (for example width and height of a texture image)


Option 3
--------
>>> dragon = Dragon('Wawelski', posx=50, posy=120)
>>> dragon = Dragon('Wawelski', positionx=50, positiony=120)
>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)


Option 4
--------
>>> dragon = Dragon('Wawelski', pos=(50, 120))
>>> dragon = Dragon('Wawelski', posxy=(50, 120))
>>> dragon = Dragon('Wawelski', pos_xy=(50, 120))
>>> dragon = Dragon('Wawelski', position=(50, 120))
>>> dragon = Dragon('Wawelski', position_xy=(50, 120))


Option 5
--------
>>> dragon = Dragon('Wawelski', pos={'x':50, 'y':120})
>>> dragon = Dragon('Wawelski', position={'x':50, 'y':120})


Option 6
--------
>>> from collections import namedtuple
>>>
>>>
>>> Position = namedtuple('Position', ['x', 'y'])
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=120))


Option 7
--------
>>> from typing import NamedTuple
>>>
>>>
>>> class Position(NamedTuple):
...     x: int
...     y: int
>>>
>>> dragon = Dragon('Wawelski', position=Position(x=50, y=120))


Option 8
--------
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


Option 9
--------
>>> dragon = Dragon('Wawelski', pos=Point(50, 120))
>>> dragon = Dragon('Wawelski', posxy=Point(50, 120))
>>> dragon = Dragon('Wawelski', pos_xy=Point(50, 120))
>>> dragon = Dragon('Wawelski', position=Point(50, 120))


Option 10
--------
>>> dragon = Dragon('Wawelski', pos=Point(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))
>>> dragon = Dragon('Wawelski', position=Point(posx=50, posy=120))
>>> dragon = Dragon('Wawelski', position=Point(position_x=50, position_y=120))


Decision
--------
>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

* Good: explicit
* Good: verbose
* Good: extensible


Alternative
-----------
>>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))

* Good: explicit
* Good: verbose
* Good: extensible
* Bad: to complex for now
