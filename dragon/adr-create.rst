Create Dragon ADR
=================

* ADR - Architecture Design Records

.. testsetup::

    class Dragon:
        def __init__(*args, **kwargs):
            pass


Rationale
---------
* Create dragon at x=50, y=120 position and name it "Wawelski"


Name
----
Option 1:

    >>> dragon = Dragon('Wawelski')

    * Good: easy to use
    * Bad: does not allow to set initial position

Option 2:

    >>> dragon = Dragon(name='Wawelski')

    * Good: easy to use
    * Good: more verbose than positional arguments
    * Bad: too verbose for such simple example
    * Bad: does not allow to set initial position

Decision:

    >>> dragon = Dragon('Wawelski')


Position
--------
Option 1:

    >>> dragon = Dragon('Wawelski', 50, 120)

    * Good: easy to use
    * Bad: not explicit (requires knowlege to answer what are those numbers)

Option 2:

    >>> dragon = Dragon('Wawelski', x=50, y=120)

    * Good: short argument names
    * Good: easy to use
    * Good: verbose in this example

Problems:

    >>> dragon = Dragon('Wawelski', 'img/dragon/alive.png', 50, 120)
    >>> dragon = Dragon('Wawelski', 'img/dragon/alive.png', x=50, y=120)

    * Bad: It does suggest, that x and y are some parameters to texture

Option 3:

    >>> dragon = Dragon('Wawelski', posx=50, posy=120)
    >>> dragon = Dragon('Wawelski', positionx=50, positiony=120)
    >>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

Option 4:

    >>> dragon = Dragon('Wawelski', pos=(50, 120))
    >>> dragon = Dragon('Wawelski', posxy=(50, 120))
    >>> dragon = Dragon('Wawelski', pos_xy=(50, 120))
    >>> dragon = Dragon('Wawelski', position=(50, 120))

Option 5:

    >>> dragon = Dragon('Wawelski', pos={'x':50, 'y':120})
    >>> dragon = Dragon('Wawelski', pos={'x':50, 'r':120})
    >>> dragon = Dragon('Wawelski', posxy={'x':50, 'y':120})
    >>> dragon = Dragon('Wawelski', position={'x':50, 'y':120})

Option 6:

    >>> from collections import namedtuple
    >>>
    >>>
    >>> Position = namedtuple('Position', ['x', 'y'])
    >>> dragon = Dragon('Wawelski', position=Position(x=50, y=120))

Option 7:

    >>> from typing import NamedTuple
    >>>
    >>>
    >>> class Position(NamedTuple):
    ...     x: int
    ...     y: int
    >>>
    >>> dragon = Dragon('Wawelski', position=Position(x=50, y=120))

Option 8:

    >>> from typing import TypedDict
    >>>
    >>>
    >>> class Position(TypedDict):
    ...     x: int
    ...     y: int
    >>>
    >>> pt1 = Position(x=50, y=120)
    >>> pt2: Position = {'x': 50, 'y': 120}

Option 9:

    >>> dragon = Dragon('Wawelski', pos=Point(50, 120))
    >>> dragon = Dragon('Wawelski', posxy=Point(50, 120))
    >>> dragon = Dragon('Wawelski', position=Point(50, 120))
    >>> dragon = Dragon('Wawelski', pos=Point(x=50, y=120))
    >>> dragon = Dragon('Wawelski', posxy=Point(x=50, y=120))
    >>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))
    >>> dragon = Dragon('Wawelski', position=Point(posx=50, posy=120))
    >>> dragon = Dragon('Wawelski', position=Point(position_x=50, position_y=120))

Decision:

    >>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

Alternative:

    >>> dragon = Dragon('Wawelski', position=Point(x=50, y=120))
