OOP Stringify Nested
====================


Important
---------
* Printing ``list`` will call ``__repr__()`` method on each element


Example
-------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname: str, lastname: str):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __str__(self):
...         return f'{self.firstname} {self.lastname}'
...
...     def __repr__(self):
...         clsname = self.__class__.__name__
...         firstname = self.firstname
...         lastname = self.lastname
...         return f'{clsname}({firstname=}, {lastname=})'
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> melissa = Astronaut('Melissa', 'Lewis')
>>> rick = Astronaut('Rick', 'Martinez')
>>>
>>> crew = [mark, melissa, rick]
>>>
>>> print(crew)
[Astronaut(firstname='Mark', lastname='Watney'), Astronaut(firstname='Melissa', lastname='Lewis'), Astronaut(firstname='Rick', lastname='Martinez')]


Assignments
-----------
.. literalinclude:: assignments/oop_stringify_c.py
    :caption: :download:`Solution <assignments/oop_stringify_c.py>`
    :end-before: # Solution
