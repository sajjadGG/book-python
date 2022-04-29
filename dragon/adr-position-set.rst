.. testsetup::

    # doctest: +SKIP_FILE

    >>> from dataclasses import dataclass
    >>>
    >>> @dataclass
    ... class Point:
    ...     x: int
    ...     y: int


Dragon ADR Position Set
=======================
* ADR - Architecture Design Records


Problem
-------
* Set new position to x=10, y=20


Option 1
--------
>>> dragon.fly(10, 20)
>>> dragon.teleport(10, 20)
>>> dragon.set_position(10, 20)
>>> dragon.set_position_xy(10, 20)

* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: ``teleport()`` and ``fly()`` are bad names
* Bad: arguments are implicit, require knowledge of an API


Option 2
--------
>>> dragon.fly(x=10, y=20)
>>> dragon.teleport(x=10, y=20)
>>> dragon.set_position(x=10, y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: ``teleport()`` and ``fly()`` are bad names


Option 3
--------
>>> dragon.set(position_x=10, position_y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: encapsulation
* Good: easy to add validation if needed
* Bad: ``set()`` is to generic
* Bad: gateway to abuse


Option 4
--------
>>> dragon.x = 10
>>> dragon.y = 20

>>> dragon.x, dragon.y = 10, 20

* Good: easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Bad: encapsulation
* Bad: names ``x`` and ``y`` are weakly related to ``dragon``

Example:

>>> knn.w = [1,2,3]


Option 5
--------
>>> dragon.position_x = 10
>>> dragon.position_y = 20

>>> dragon.position_x, dragon.position_y = 10, 20

* Good: easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Bad: encapsulation

Example:

>>> knn.weights = [1,2,3]


Option 6
--------
>>> dragon.position = (10, 20)
>>> dragon.position @ (10, 20)

* Good: easy to use
* Good: can use ``@property`` for validation if needed
* Good: using ``@`` (matmul) it is easy to validation
* Bad: arguments are implicit
* Bad: require knowledge of an API
* Bad: always 2D
* Bad: not extensible, hard to refactor to 3D


Option 7
--------
>>> dragon.position = Point(x=10, y=20)
>>> dragon.position @ Point(x=10, y=20)

* Good: easy to use
* Good: can use ``@property`` for validation if needed
* Good: arguments are explicit
* Good: readability
* Bad: require knowledge of an API
* Bad: extensible, easy to refactor to 3D


Option 8
--------
>>> dragon.position.x = 10
>>> dragon.position.y = 20

>>> dragon.position.x, dragon.position.y = 10, 20

* Good: more or less easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Good: encapsulation
* Good: more or less readable
* Bad: extensible, easy to refactor to 3D
* Bad: nested
* Bad: require knowledge of an API


Decision
--------
>>> dragon.set_position(x=10, y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: encapsulation
* Good: easy to add validation if needed
* Good: extensible, easy to refactor to 3D
