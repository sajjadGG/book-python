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

    "``-obj``",           "``obj.__neg__()``"
    "``+obj``",           "``obj.__pos__()``"
    "``~obj``",           "``obj.__invert__()``"


Object Equality
---------------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = Astronaut('Mark', 'Watney')
>>> b = Astronaut('Mark', 'Watney')
>>> c = Astronaut('Melissa', 'Lewis')
>>>
>>> a == c
False
>>> b == c
False
>>> a == b
False
>>>
>>> hex(id(a))  # doctest: +SKIP
'0x11b9706a0'
>>> hex(id(b))  # doctest: +SKIP
'0x11b970700'
>>> id(a) == id(b)
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
>>>
>>> a = Astronaut('Mark', 'Watney')
>>> b = Astronaut('Mark', 'Watney')
>>> c = Astronaut('Melissa', 'Lewis')
>>>
>>> print(a == c)
False
>>> print(b == c)
False
>>> print(a == b)
True
>>>
>>> hex(id(a))  # doctest: +SKIP
'0x11b970c70'
>>> hex(id(b))  # doctest: +SKIP
'0x11b9704c0'
>>> id(a) == id(b)
False


Problem
--------
* When you compare objects with the same fields from two different classes

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


Solution
--------
* Always remember to compare classes
* This way you avoid bug, when both has the same fields and values

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return (self.__class__ is other.__class) \
...            and (self.firstname == other.firstname) \
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
False


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



Use Case - Game
---------------
>>> hero @ Position(x=50, y=120)  # doctest: +SKIP
>>> hero >> Direction(left=10, up=20)  # doctest: +SKIP
>>>
>>> hero < Damage(20)  # doctest: +SKIP
>>> hero > Damage(20)  # doctest: +SKIP
>>>
>>> hero['gold'] += dragon['gold']  # doctest: +SKIP


Assignments
-----------
.. literalinclude:: assignments/operators_comparison_a.py
    :caption: :download:`Solution <assignments/operators_comparison_a.py>`
    :end-before: # Solution
