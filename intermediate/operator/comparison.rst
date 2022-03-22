Operator Comparison
===================
* ``==`` - eq
* ``!=`` - ne
* ``<`` - lt
* ``<=`` - le
* ``>`` - gt
* ``>=`` - ge


About
-----
.. csv-table:: Comparison Operator Overload
    :header: "Operator", "Method"

    "``obj == other``",   "``obj.__eq__(other)``"
    "``obj != other``",   "``obj.__ne__(other)``"
    "``obj < other``",    "``obj.__lt__(other)``"
    "``obj <= other``",   "``obj.__le__(other)``"
    "``obj > other``",    "``obj.__gt__(other)``"
    "``obj >= other``",   "``obj.__ge__(other)``"


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
>>>
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
>>>
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
...         return (self.__class__ is other.__class__) \
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


Use Case - 0x01
---------------
* Game

>>> hero < Damage(20)  # doctest: +SKIP
>>> hero > Damage(20)  # doctest: +SKIP


Assignments
-----------
.. literalinclude:: assignments/operator_comparison_a.py
    :caption: :download:`Solution <assignments/operator_comparison_a.py>`
    :end-before: # Solution
