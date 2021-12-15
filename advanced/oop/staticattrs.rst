OOP Static and Dynamic Attrs
============================


Recap
-----
Type annotations are not variable definition:

>>> x: int
>>>
>>> print(x)
Traceback (most recent call last):
NameError: name 'x' is not defined

Type annotations will only tell, that if there will be a identifier with
name ``x``, it should be an ``int``:

>>> x: int
>>> x = 0
>>>
>>> print(x)
0

Typically it is written in shorter form:

>>> x: int = 0
>>>
>>> print(x)
0


Static Fields
-------------
* Fields defined on a class
* Must have default values
* Share state

Static fields defined in class:

>>> class Astronaut:
...     firstname = 'Mark'
...     lastname = 'Watney'

Static fields defined in code:

>>> class Astronaut:
...     pass
>>>
>>>
>>> Astronaut.firstname = 'Mark'
>>> Astronaut.lastname = 'Watney'


Dynamic Fields
--------------
* Fields defined on an instance
* Do not share state (unless mutable argument)
* By convention initialized in ``__init__()``

Dynamic fields with variable values:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname


Dynamic fields with constant values:

>>> class Astronaut:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'

Dynamic fields initialized outside init:

>>> class Astronaut:
...     pass
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'


Static and Dynamic Fields
-------------------------
Static and dynamic fields defined in class:

>>> class Astronaut:
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'

Static and dynamic fields defined in code:

>>> class Astronaut:
...     pass
>>>
>>>
>>> Astronaut.firstname = 'Mark'
>>> Astronaut.lastname = 'Watney'
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Melissa'
>>> astro.lastname = 'Lewis'


Type Annotations
----------------
No fields at all, type annotations only:

>>> class Astronaut:
...     firstname: str
...     lastname: str

Static fields with type annotations:

>>> class Astronaut:
...     firstname: str = 'Mark'
...     lastname: str = 'Watney'

Dynamic fields with type annotations:

>>> class Astronaut:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname

Both static and dynamic fields with type annotations:

>>> class Astronaut:
...     firstname: str = 'Mark'
...     lastname: str = 'Watney'
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname


Dataclasses
-----------
* Dataclass uses static field notation to create dynamic fields
* Dataclass do not validate type annotations, unless ``ClassVar`` or ``InitVar``

>>> from dataclasses import dataclass, InitVar
>>> from typing import ClassVar

Dynamic fields:

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str

Dynamic fields with default values

>>> @dataclass
... class Astronaut:
...     firstname: str = 'Mark'
...     lastname: str = 'Watney'

Static fields created by ``ClassVar``

>>> @dataclass
... class Astronaut:
...     firstname: ClassVar[str] = 'Mark'
...     lastname: ClassVar[str] = 'Watney'

Using ``InitVar`` will not produce any fields at all. ``InitVar``
specifies parameters to ``__post_init__()`` method. They will be
forgotten as soon after ``__post_init__()`` returns, unless you
assign them to whatever fields.

>>> @dataclass
... class Astronaut:
...     firstname: InitVar[str] = 'Mark'
...     lastname: InitVar[str] = 'Watney'


Static vs. Dynamic Fields
-------------------------
Static vs. Dynamic fields:

Lets define a class with static field:

>>> class Astronaut:
...     agency = 'NASA'

Lets create three instances of ``Astronaut`` class:

>>> watney = Astronaut()
>>> twardowski = Astronaut()
>>> ivanovic = Astronaut()

We will print ``agency`` field:

>>> print(watney.agency)
NASA
>>>
>>> print(twardowski.agency)
NASA
>>>
>>> print(ivanovic.agency)
NASA
>>>
>>> print(Astronaut.agency)
NASA

Lets change field on a class and print ``agency`` field:

>>> Astronaut.agency = 'ESA'
>>>
>>>
>>> print(watney.agency)
ESA
>>>
>>> print(twardowski.agency)
ESA
>>>
>>> print(ivanovic.agency)
ESA
>>>
>>> print(Astronaut.agency)
ESA

Lets change field on an instance and print ``agency`` field:

>>> ivanovic.agency = 'Roscosmos'
>>>
>>>
>>> print(watney.agency)
ESA
>>>
>>> print(twardowski.agency)
ESA
>>>
>>> print(ivanovic.agency)
Roscosmos
>>>
>>> print(Astronaut.agency)
ESA

Note, that the class which defined field shadowed the static field from
class.

Lets change field on a class and print ``agency`` field:

>>> Astronaut.agency = 'POLSA'
>>>
>>>
>>> print(watney.agency)
POLSA
>>>
>>> print(twardowski.agency)
POLSA
>>>
>>> print(ivanovic.agency)
Roscosmos
>>>
>>> print(Astronaut.agency)
POLSA

Lets delete field from an instance and print ``agency`` field:

>>> del ivanovic.agency
>>>
>>>
>>> print(watney.agency)
POLSA
>>>
>>> print(twardowski.agency)
POLSA
>>>
>>> print(ivanovic.agency)
POLSA
>>>
>>> print(Astronaut.agency)
POLSA


Mechanism
---------
* ``vars(obj)`` is will return ``obj.__dict__``

>>> class Astronaut:
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Melissa', 'Lewis')
>>>
>>> vars(astro)
{'firstname': 'Melissa', 'lastname': 'Lewis'}
>>>
>>> vars(Astronaut)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
mappingproxy({
    '__module__': 'builtins',
    'firstname': 'Mark',
    'lastname': 'Watney',
    '__init__': <function Astronaut.__init__ at 0x...>,
    '__dict__': <attribute '__dict__' of 'Astronaut' objects>,
    '__weakref__': <attribute '__weakref__' of 'Astronaut' objects>,
    '__doc__': None})


Assignments
-----------
.. todo:: Create assignments
