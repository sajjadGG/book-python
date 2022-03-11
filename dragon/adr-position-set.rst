Dragon ADR Position Change
==========================


Rationale
---------
* ADR - Architecture Design Records
* Set new position to x=10, y=20


Possibilities
-------------
>>> dragon.set_position(10, 20)

>>> dragon.teleport(10, 20)

>>> dragon.fly(10, 20)

>>> dragon.set_position(x=10, y=20)  # good

>>> dragon.teleport(x=10, y=20)

>>> dragon.fly(x=10, y=20)

>>> dragon.set(position_x=10, position_y=20)

>>> dragon.position_x = 10

>>> dragon.position_y = 20

>>> dragon.position_x, dragon.position_y = 10, 20

>>> dragon.position = (10, 20)

>>> dragon.position @ (10, 20)

>>> dragon.position @ Point(10, 20)

>>> dragon.x, y.position_y = 10, 20

>>> dragon.x = 10

>>> dragon.y = 20
