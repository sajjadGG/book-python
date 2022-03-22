OOP Stringify Str
=================
* Calling function ``print(obj)`` calls ``str(obj)``
* Calling function ``str(obj)`` calls ``obj.__str__()``
* Method ``obj.__str__()`` must return ``str``
* This is dedicated for end-user of your class


Inherited
---------
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


Overloaded
----------
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


Assignments
-----------
.. literalinclude:: assignments/oop_stringify_a.py
    :caption: :download:`Solution <assignments/oop_stringify_a.py>`
    :end-before: # Solution
