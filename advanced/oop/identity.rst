OOP Object Identity
===================


Rationale
---------
* ``=`` assignment
* ``==`` checks for object equality
* ``is`` checks for object identity

>>> from typing import Optional
>>>
>>>
>>> firstname: str = 'Melissa'
>>> lastname: str = 'Lewis'
>>> age: Optional[int] = None
>>>
>>> age is None
True
>>> age is not None
False


Identity
--------
* ``id(obj) -> int``
* ``id()`` will change every time you execute script
* ``id()`` returns an integer which is guaranteed to be unique and constant for object during its lifetime
* Two objects with non-overlapping lifetimes may have the same ``id()`` value
* In CPython it's also the memory address of the corresponding C object

>>> id('Watney')  # doctest: +SKIP
4499664048
>>>
>>> hex(id('Watney'))  # doctest: +SKIP
'0x10c336cb0'


Identity Check
--------------
* ``is`` checks for object identity
* ``is`` compares ``id()`` output for both objects
* CPython: compares the memory address a object resides in
* Testing strings with ``is`` only works when the strings are interned
* Since Python 3.8 - Compiler produces a ``SyntaxWarning`` when identity checks (``is`` and ``is not``) are used with certain types of literals (e.g. ``str``, ``int``). These can often work by accident in *CPython*, but are not guaranteed by the language spec. The warning advises users to use equality tests (``==`` and ``!=``) instead.

>>> name = None
>>>
>>> name is None
True
>>> name is not None
False


Bool Identity
-------------
>>> name = None
>>>
>>> name is None
True
>>> name is False
False

>>> found = True
>>>
>>> found == True
True
>>> found is True
True


String Identity
---------------
>>> a = 'Mark Watney'
>>> b = 'Mark Watney'
>>>
>>> a == b
True
>>> a is b
False

>>> 'Mark Watney' is 'Mark Watney'  # doctest: +ELLIPSIS
<...>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True


Type Identity
-------------
>>> name = ...
>>>
>>> type(name) is int
False
>>> type(name) is float
False
>>> type(name) is complex
False
>>> type(name) is bool
False
>>> type(name) is None
False
>>> type(name) is str
False
>>> type(name) is bytes
False
>>> type(name) is list
False
>>> type(name) is tuple
False
>>> type(name) is set
False
>>> type(name) is frozenset
False
>>> type(name) is dict
False


Object Identity
---------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro1 = Astronaut('Jan', 'Twardowski')
>>> astro2 = Astronaut('Jan', 'Twardowski')
>>>
>>> astro1 is astro2
False

>>> id(astro1)  # doctest: +SKIP
4421890496
>>> id(astro2)  # doctest: +SKIP
4421893328

>>> hex(id(astro1))  # doctest: +SKIP
'0x10790b1c0'
>>> hex(id(astro2))  # doctest: +SKIP
'0x10790bcd0'

>>> print(astro1)  # doctest: +SKIP
<Astronaut object at 0x107905820>
>>> print(astro2)  # doctest: +SKIP
<Astronaut object at 0x10790bcd0>


Value Comparison
----------------
* ``==`` checks for object equality

>>> 'Mark Watney' == 'Mark Watney'
True

>>> a = 'Mark Watney'
>>> b = 'Mark Watney'
>>>
>>> a == b
True

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro1 = Astronaut('Jan', 'Twardowski')
>>> astro2 = Astronaut('Jan', 'Twardowski')
>>>
>>> astro1 == astro2
False


Compare Value vs. Identity
--------------------------
>>> name = 'Mark Watney'
>>> expected = 'Mark Watney'
>>>
>>> name == expected
True
>>> name is expected
False

>>> name = 'Mark Watney'
>>>
>>> name == 'Mark Watney'
True
>>>
>>> name is 'Mark Watney'  # doctest: +ELLIPSIS
<...>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False


String Value vs Identity Problem
--------------------------------
* CPython optimization
* Can be misleading

>>> a = 'Mark Watney'
>>> b = 'Mark Watney'
>>>
>>> a == b
True
>>> a is b
False
>>> a is 'Mark Watney'  # doctest: +ELLIPSIS
<...>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False

>>> a = 'Mark'
>>> b = 'Mark'
>>>
>>> a == b
True
>>> a is b
True
>>> a is 'Mark'  # doctest: +ELLIPSIS
<...>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True


Use Case - Make Equal
---------------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return self.firstname == other.firstname \
...            and self.lastname == other.lastname
>>>
>>>
>>> a1 = Astronaut('Jan', 'Twardowski')
>>> a2 = Astronaut('Jan', 'Twardowski')
>>>
>>> a1 == a2
True
>>> a1 is a2
False


Use Case - Equal Problem
------------------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return self.firstname == other.firstname \
...            and self.lastname == other.lastname
>>>
>>>
>>> class Cosmonaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = Astronaut('Jan', 'Twardowski')
>>> c = Cosmonaut('Jan', 'Twardowski')
>>>
>>> a == c
True
>>> a is c
False


Use Case - Make Unequal
-----------------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other):
...         return self.__class__ is other.__class__ \
...            and self.firstname == other.firstname \
...            and self.lastname == other.lastname
>>>
>>>
>>> class Cosmonaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = Astronaut('Jan', 'Twardowski')
>>> c = Cosmonaut('Jan', 'Twardowski')
>>>
>>> a == c
False
>>> a is c
False


Use Case - Overload
-------------------
* Could be implemented through `from functools import singledispatchmethod`
* More information: https://python.astrotech.io/advanced/funcprog/functools.html#singledispatchmethod

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def __eq__(self, other: Astronaut):
...         return self.firstname == other.firstname \
...            and self.lastname == other.lastname
...
...     def __eq__(self, other: Cosmonaut):
...         return False
>>>
>>>
>>> class Cosmonaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> a = Astronaut('Jan', 'Twardowski')
>>> c = Cosmonaut('Jan', 'Twardowski')
>>>
>>> a == c
False
>>> a is c
False


Assignments
-----------
.. todo:: Create assignments
