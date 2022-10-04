OOP Attribute Access Modifiers
==============================
* Attributes and methods are always public
* No protected and private keywords
* Protecting is only by convention [#pydocprivatevar]_
* ``name`` - public attribute
* ``_name`` - protected attribute (non-public by convention)
* ``__name`` - private attribute (name mangling)
* ``__name__`` - system attribute
* ``name_`` - avoid name collision with built-ins

>>> class Astronaut:
...     firstname: str          # public
...     lastname: str           # public
...     _salary: int            # protected
...     _address: int           # protected
...     __username: str         # private
...     __password: str         # private
...     id_: int                # avoid name collision
...     type_: str              # avoid name collision
...     __doc__: str            # system
...     __module__: str         # system


SetUp
-----
>>> from dataclasses import dataclass


Example
-------
>>> @dataclass
... class Public:
...     firstname: str
...     lastname: str
>>>
>>>
>>> @dataclass
... class Protected:
...     _firstname: str
...     _lastname: str
>>>
>>>
>>> @dataclass
... class Private:
...     __firstname: str
...     __lastname: str


Public Attribute
----------------
* ``name`` - public attribute

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')

To print attributes directly:

>>> print(astro.firstname)
Mark
>>>
>>> print(astro.lastname)
Watney

To list all the attributes once again we can use `vars()`:

>>> vars(astro)
{'firstname': 'Mark', 'lastname': 'Watney'}


Protected Attribute
-------------------
* ``_name`` - protected attribute (non-public by convention)

>>> @dataclass
... class Astronaut:
...     _firstname: str
...     _lastname: str
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')

Python will allow the following statement, however your IDE should
warn you "Access to a protected member _firstname of a class":

>>> print(astro._firstname)
Mark
>>>
>>> print(astro._lastname)
Watney

To list all the attributes once again we can use `vars()`:

>>> vars(astro)
{'_firstname': 'Mark', '_lastname': 'Watney'}


Private Attribute
-----------------
* ``__name`` - private attribute (name mangling)

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     __firstname: str
...     __lastname: str
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')

There are no attributes with names ``__firstname`` and ``__lastname``:

>>> print(astro.__firstname)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__firstname'
>>>
>>> print(astro.__lastname)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__lastname'

To print attributes directly:

>>> print(astro._Astronaut__firstname)
Mark
>>>
>>> print(astro._Astronaut__lastname)
Watney

To list all the attributes once again we can use `vars()`:

>>> vars(astro)  # doctest: +NORMALIZE_WHITESPACE
{'_Astronaut__firstname': 'Mark',
 '_Astronaut__lastname': 'Watney'}


Name Mangling
-------------
>>> @dataclass
... class English:
...     greeting: str = 'Hello'
>>>
>>>
>>> @dataclass
... class Texan(English):
...     greeting: str = 'Howdy'
>>>
>>>
>>> mark = Texan()
>>>
>>> print(mark.greeting)
Howdy

>>> @dataclass
... class English:
...     __greeting: str = 'Hello'
>>>
>>>
>>> @dataclass
... class Texan(English):
...     __greeting: str = 'Howdy'
>>>
>>>
>>> mark = Texan()
>>>
>>> print(mark._English__greeting)
Hello
>>>
>>> print(mark._Texan__greeting)
Howdy

To list all the attributes once again we can use `vars()`:

>>> vars(mark)  # doctest: +NORMALIZE_WHITESPACE
{'_English__greeting': 'Hello',
 '_Texan__greeting': 'Howdy'}


Name Collision
--------------
* Example colliding names: ``type_``, ``id_``, ``hash_``

>>> type_ = type('myobject')
>>> id_ = id('myobject')
>>> hash_ = hash('myobject')

Example:

>>> class User:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.type_ = type(self)
...         self.id_ = id(self)
...         self.hash_ = hash(self)


System Attributes
-----------------
* ``__name__`` - Current module
* ``obj.__class__`` - Class from which object was instantiated
* ``obj.__dict__`` - Stores instance variables
* ``obj.__doc__`` - Object docstring
* ``obj.__annotations__`` - Object attributes type annotations
* ``obj.__module__`` - Name of a module in which object was defined

>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')

>>> astro.__class__
<class '__main__.Astronaut'>
>>>
>>> astro.__dict__
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> astro.__doc__
'Astronaut(firstname: str, lastname: str)'
>>>
>>> astro.__annotations__
{'firstname': <class 'str'>, 'lastname': <class 'str'>}
>>>
>>> astro.__module__
'__main__'


Show Attributes
---------------
* ``vars()`` display ``obj.__dict__``

>>> class Astronaut:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self._salary = 10_000
...         self._address = '2101 E NASA Pkwy, Houston 77058, Texas, USA'
...         self.__username = 'mwatney'
...         self.__password = 'ares3'
...         self.id_ = 1337
...         self.type_ = 'astronaut'
...         self.__doc__ = 'Astronaut Class'
...         self.__module__ = '__main__'
>>>
>>>
>>> astro = Astronaut()

All attributes:

>>> vars(astro)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 '_salary': 10000,
 '_address': '2101 E NASA Pkwy, Houston 77058, Texas, USA',
 '_Astronaut__username': 'mwatney',
 '_Astronaut__password': 'ares3',
 'id_': 1337,
 'type_': 'astronaut',
 '__doc__': 'Astronaut Class',
 '__module__': '__main__'}

Public attributes:

>>> result = {attribute: value
...           for attribute, value in vars(astro).items()
...           if not attribute.startswith('_')}
>>>
>>> print(result)
{'firstname': 'Mark', 'lastname': 'Watney', 'id_': 1337, 'type_': 'astronaut'}

Protected attributes:

>>> result = {attribute: value
...           for attribute, value in vars(astro).items()
...           if attribute.startswith('_')
...           and not attribute.startswith('__')
...           and not attribute.startswith(f'_{astro.__class__.__name__}__')}
>>>
>>> print(result)
{'_salary': 10000, '_address': '2101 E NASA Pkwy, Houston 77058, Texas, USA'}

Private attributes:

>>> result = {attribute: value
...           for attribute, value in vars(astro).items()
...           if attribute.startswith(f'_{astro.__class__.__name__}__')}
>>>
>>> print(result)
{'_Astronaut__username': 'mwatney', '_Astronaut__password': 'ares3'}

System attributes:

>>> result = {attribute: value
...           for attribute, value in vars(astro).items()
...           if attribute.startswith('__')
...           and attribute.endswith('__')}
>>>
>>> print(result)
{'__doc__': 'Astronaut Class', '__module__': '__main__'}


References
----------
.. [#pydocprivatevar] https://docs.python.org/3/tutorial/classes.html#private-variables


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_accessmodifiers_a.py
    :caption: :download:`Solution <assignments/oop_attribute_accessmodifiers_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_attribute_accessmodifiers_b.py
    :caption: :download:`Solution <assignments/oop_attribute_accessmodifiers_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_attribute_accessmodifiers_c.py
    :caption: :download:`Solution <assignments/oop_attribute_accessmodifiers_c.py>`
    :end-before: # Solution
