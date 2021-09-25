OOP Stringify Objects
=====================


Rationale
---------
* ``str(obj)`` -> ``obj.__str__()``
* ``repr(obj)`` -> ``obj.__repr__()``
* ``print(obj)`` -> ``str(obj)`` -> ``obj.__str__()``

>>> import datetime
>>> date = datetime.date(1961, 4, 12)
>>>
>>>
>>> str(date)
'1961-04-12'
>>>
>>> print(date)
1961-04-12
>>>
>>>
>>> repr(date)
'datetime.date(1961, 4, 12)'
>>>
>>> date
datetime.date(1961, 4, 12)


String
------
* Calling function ``print(obj)`` calls ``str(obj)``
* Calling function ``str(obj)`` calls ``obj.__str__()``
* Method ``obj.__str__()`` must return ``str``
* This is dedicated for end-user of your class

>>> class Astronaut:
...     pass
>>>
>>>
>>> astro = Astronaut()
>>> str(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'

Object without ``__str__()`` method overloaded prints their memory address:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> print(astro)  # doctest: +ELLIPSIS
<Astronaut object at 0x...>
>>>
>>> str(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'
>>>
>>> astro.__str__()  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'

Objects can verbose print if ``__str__()`` method is present:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __str__(self):
...         return f'Hello {self.firstname} {self.lastname}'
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> print(astro)
Hello Mark Watney
>>>
>>> str(astro)
'Hello Mark Watney'
>>>
>>> astro.__str__()
'Hello Mark Watney'


Representation
--------------
* Calling function ``repr(obj)`` calls ``obj.__repr__()``
* Method ``obj.__repr__()`` must return ``str``
* Dedicated for developers
* Shows object representation
* Copy-paste for creating object with the same values
* Useful for debugging
* Printing ``list`` will call ``__repr__()`` method on each element

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> repr(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'

Using ``__repr__()`` on a class:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __repr__(self):
...         firstname = self.firstname
...         lastname = self.lastname
...         return f'Astronaut({firstname=}, {lastname=})'
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> repr(astro)
"Astronaut(firstname='Mark', lastname='Watney')"
>>>
>>> astro
Astronaut(firstname='Mark', lastname='Watney')


Printing Sequence Elements
--------------------------
Printing ``list`` will call ``__repr__()`` method on each element:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> crew = [Astronaut('Jan', 'Twardowski'),
...         Astronaut('Mark', 'Watney'),
...         Astronaut('Melissa', 'Lewis')]
>>>
>>> print(crew)  # doctest: +ELLIPSIS
[<Astronaut object at 0x...>, <Astronaut object at 0x...>, <Astronaut object at 0x...>]

Printing ``list`` will call ``__repr__()`` method on each element:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __repr__(self):
...         return f'{self.firstname} {self.lastname}'
>>>
>>>
>>> crew = [Astronaut('Jan', 'Twardowski'),
...         Astronaut('Mark', 'Watney'),
...         Astronaut('Melissa', 'Lewis')]
>>>
>>> print(crew)
[Jan Twardowski, Mark Watney, Melissa Lewis]


Assignments
-----------
.. literalinclude:: assignments/oop_stringify_a.py
    :caption: :download:`Solution <assignments/oop_stringify_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_stringify_b.py
    :caption: :download:`Solution <assignments/oop_stringify_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_stringify_c.py
    :caption: :download:`Solution <assignments/oop_stringify_c.py>`
    :end-before: # Solution
