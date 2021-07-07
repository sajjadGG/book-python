Operators Comparison
====================


Rationale
---------
.. csv-table:: Comparison Operators Overload
    :header: "Operator", "Method"

    "``obj == other``",   "``obj.__eq__(other)``"
    "``obj != other``",   "``obj.__ne__(other)``"
    "``obj < other``",    "``obj.__lt__(other)``"
    "``obj <= other``",   "``obj.__le__(other)``"
    "``obj > other``",    "``obj.__gt__(other)``"
    "``obj >= other``",   "``obj.__ge__(other)``"


Example
-------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Vector:
...     x: int = 0
...     y: int = 0
...
...     def __eq__(self, other):
...         if (self.x == other.x) and (self.y == other.y):
...             return True
...         else:
...             return False
>>>
>>>
>>> Vector(x=1, y=2) == Vector(x=3, y=4)
False
>>>
>>> Vector(x=1, y=2) == Vector(x=1, y=2)
True


Eq Works at Both Sides
----------------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> class Cosmonaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = Astronaut('Mark', 'Watney')
>>> c = Cosmonaut('Mark', 'Watney')
>>>
>>> print(a == c)
False

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return (self.firstname == other.firstname) \
...            and (self.lastname == other.lastname)
>>>
>>>
>>> class Cosmonaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = Astronaut('Mark', 'Watney')
>>> c = Cosmonaut('Mark', 'Watney')
>>>
>>> print(a == c)
True

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> class Cosmonaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return (self.firstname == other.firstname) \
...            and (self.lastname == other.lastname)
>>>
>>>
>>> a = Astronaut('Mark', 'Watney')
>>> c = Cosmonaut('Mark', 'Watney')
>>>
>>> print(a == c)
True


Assignments
-----------
.. literalinclude:: assignments/operators_comparison_a.py
    :caption: :download:`Solution <assignments/operators_comparison_a.py>`
    :end-before: # Solution
