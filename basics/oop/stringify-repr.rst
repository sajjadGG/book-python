OOP Stringify Repr
==================
* Calling function ``repr(obj)`` calls ``obj.__repr__()``
* Method ``obj.__repr__()`` must return ``str``
* Dedicated for developers
* Shows object representation
* Copy-paste for creating object with the same values
* Useful for debugging
* Printing ``list`` will call ``__repr__()`` method on each element


Inherited
---------
Object without ``__repr__()`` method overloaded prints their memory address:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> astro  # doctest: +ELLIPSIS
<Astronaut object at 0x...>
>>>
>>> repr(astro)  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'
>>>
>>> astro.__repr__()  # doctest: +ELLIPSIS
'<Astronaut object at 0x...>'


Overloaded
----------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __repr__(self):
...         clsname = self.__class__.__name__
...         firstname = self.firstname
...         lastname = self.lastname
...         return f'{clsname}({firstname=}, {lastname=})'
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> astro
Astronaut(firstname='Mark', lastname='Watney')
>>>
>>> repr(astro)
"Astronaut(firstname='Mark', lastname='Watney')"
>>>
>>> astro.__repr__()
"Astronaut(firstname='Mark', lastname='Watney')"


Assignments
-----------
.. literalinclude:: assignments/oop_stringify_b.py
    :caption: :download:`Solution <assignments/oop_stringify_b.py>`
    :end-before: # Solution
