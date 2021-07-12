Operators About
===============


Rationale
---------
* Operator Overload
* Readable syntax
* Simpler operations
* Following examples uses ``dataclasses`` to focus on action code, not boilerplate

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Vector:
...     x: int = 0
...     y: int = 0
>>>
>>>
>>> Vector(x=1, y=2) + Vector(x=3, y=4)
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Vector:
...     x: int = 0
...     y: int = 0
...
...     def __add__(self, other):
...         return Vector(
...             self.x + other.x,
...             self.y + other.y)
>>>
>>>
>>> Vector(x=1, y=2) + Vector(x=3, y=4)
Vector(x=4, y=6)
>>>
>>> Vector(x=1, y=2) + Vector(x=3, y=4) + Vector(x=5, y=6)
Vector(x=9, y=12)


Use Case - Game
---------------
>>> hero @ Position(x=50, y=120)  # doctest: +SKIP
>>> hero >> Direction(left=10, up=20)  # doctest: +SKIP
>>>
>>> hero < Damage(20)  # doctest: +SKIP
>>> hero > Damage(20)  # doctest: +SKIP
>>>
>>> hero['gold'] += dragon['gold']  # doctest: +SKIP


Further Reading
---------------
* https://docs.python.org/reference/datamodel.html#emulating-numeric-types
* https://docs.python.org/library/operator.html
