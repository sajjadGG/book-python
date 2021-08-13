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
>>> repr(date)
'datetime.date(1961, 4, 12)'
>>>
>>> print(date)
1961-04-12


String
------
* Calling function ``str(obj)`` calls ``obj.__str__()``
* Calling function ``print(obj)`` calls ``str(obj)``, which calls ``obj.__str__()``
* Method ``obj.__str__()`` must return ``str``
* for end-user

>>> class Astronaut:
...     pass
>>>
>>> astro = Astronaut()
>>> str(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'

Object without ``__str__()`` method overloaded prints their memory address:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> astro = Astronaut('José Jiménez')
>>>
>>> print(astro)  # doctest: +ELLIPSIS
<Astronaut object at 0x...>
>>> str(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'
>>> astro.__str__()  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'

Objects can verbose print if ``__str__()`` method is present:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def __str__(self):
...         return f'My name... {self.name}'
>>>
>>>
>>> astro = Astronaut('José Jiménez')
>>>
>>> print(astro)
My name... José Jiménez
>>> str(astro)
'My name... José Jiménez'
>>> astro.__str__()
'My name... José Jiménez'


Representation
--------------
* Calling function ``repr(obj)`` calls ``obj.__repr__()``
* Method ``obj.__repr__()`` must return ``str``
* for developers
* object representation
* copy-paste for creating object with the same values
* useful for debugging
* printing ``list`` will call ``__repr__()`` method on each element

>>> class Astronaut:
...     pass
>>>
>>> astro = Astronaut()
>>> repr(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'

Using ``__repr__()`` on a class:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def __repr__(self):
...         return f'Astronaut(name="{self.name}")'
>>>
>>>
>>> astro = Astronaut('José Jiménez')
>>>
>>> repr(astro)
'Astronaut(name="José Jiménez")'
>>> astro
Astronaut(name="José Jiménez")

Printing ``list`` will call ``__repr__()`` method on each element:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
>>>
>>> crew = [Astronaut('Jan Twardowski'),
...         Astronaut('Mark Watney'),
...         Astronaut('Melissa Lewis')]
>>>
>>> print(crew)  # doctest: +ELLIPSIS
[<Astronaut object at 0x...>, <Astronaut object at 0x...>, <Astronaut object at 0x...>]

Printing ``list`` will call ``__repr__()`` method on each element:

>>> class Astronaut:
...     def __init__(self, name):
...         self.name = name
...
...     def __repr__(self):
...         return f'{self.name}'
>>>
>>> crew = [Astronaut('Jan Twardowski'),
...         Astronaut('Mark Watney'),
...         Astronaut('Melissa Lewis')]
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
