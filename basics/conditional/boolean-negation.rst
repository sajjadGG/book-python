Boolean Negation
================


Rationale
---------
* ``not`` logically inverts


Example
-------
>>> not True
False

>>> not False
True


Control Flow
------------
* ``not`` negates (logically inverts) condition

>>> name = None
>>>
>>> if not name:
...     print('Name is empty')
Name is empty

>>> crew = {'Lewis', 'Watney', 'Twardowski'}
>>>
>>> if 'Ivanovich' not in crew:
...     print('You are not assigned to the crew')
You are not assigned to the crew

>>> name = None
>>>
>>> if name is not None:
...     print(name)



Assignments
-----------
.. todo:: Create assignments
