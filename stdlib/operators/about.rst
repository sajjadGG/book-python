Operators About
===============


Rationale
---------
* Operator Overload
* Readable syntax
* Simpler operations
* All examples in this chapter uses ``dataclasses`` for you to focus
  on the important code, not boilerplate code just to make it works


Example
-------
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
...         new_x = self.x + other.x
...         new_y = self.y + other.y
...         return Vector(new_x, new_y)
>>>
>>>
>>> Vector(x=1, y=2) + Vector(x=3, y=4)
Vector(x=4, y=6)
>>>
>>> Vector(x=1, y=2) + Vector(x=3, y=4) + Vector(x=5, y=6)
Vector(x=9, y=12)


Further Reading
---------------
* https://docs.python.org/reference/datamodel.html#emulating-numeric-types
* https://docs.python.org/library/operator.html
