Dataclass Flags
===============


Flags
-----
.. todo:: Table is more readable

        * ``init`` - Generate ``__init__()`` method (default ``True``)
        * ``repr`` - Generate ``__repr__()`` method (default ``True``)
        * ``eq`` - Generate ``__eq__()`` and ``__ne__()`` methods (default ``True``)
        * ``order`` - Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods (default ``False``)
        * ``unsafe_hash`` - if ``False``: the ``__hash__()`` method is generated according to how eq and frozen are set (default ``False``)
        * ``frozen`` - if ``True``: assigning to fields will generate an exception (default ``False``)

.. csv-table:: Dataclass options
    :header: "Option", "Default", "Description (if True)"
    :widths: 10, 10, 80

    "``init``", "``True``", "Generate ``__init__()`` method"
    "``repr``", "``True``", "Generate ``__repr__()`` method"
    "``eq``", "``True``", "Generate ``__eq__()`` and ``__ne__()`` methods"
    "``order``", "``False``", "Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods"
    "``unsafe_hash``", "``False``", "if False: the ``__hash__()`` method is generated according to how eq and frozen are set"
    "``frozen``", "``False``", "if ``True``: assigning to fields will generate an exception"


Init
----
* Generate ``__init__()`` method

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(init=False)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
Traceback (most recent call last):
TypeError: Point() takes no arguments


Repr
----
* ``repr=True`` by default
* Generate ``__repr__()`` for pretty printing

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(repr=True)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>>
>>> print(p)
Point(x=10, y=20)

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(repr=False)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>>
>>> print(p)  # doctest: +ELLIPSIS
<Point object at 0x...>


Frozen
------
* ``frozen=False`` by default
* Prevents object from modifications

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(frozen=True)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>>
>>> p.x = 30
Traceback (most recent call last):
dataclasses.FrozenInstanceError: cannot assign to field 'x'


Eq
--
* ``eq=True`` by default
* when ``eq=False`` compare objects by ``id()`` not values
* when ``eq=True`` compare objects by value not ``id()``

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(eq=True)
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> astro1 = Astronaut('Mark', 'Watney')
>>> astro2 = Astronaut('Mark', 'Watney')
>>> astro3 = Astronaut('Jan', 'Twardowski')
>>>
>>> astro1 == astro1
True
>>> astro1 == astro2
True
>>> astro1 == astro3
False
>>>
>>> astro1 != astro1
False
>>> astro1 != astro2
False
>>> astro1 != astro3
True

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(eq=False)
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> astro1 = Astronaut('Mark', 'Watney')
>>> astro2 = Astronaut('Mark', 'Watney')
>>> astro3 = Astronaut('Jan', 'Twardowski')
>>>
>>> astro1 == astro1
True
>>> astro1 == astro2
False
>>> astro1 == astro3
False
>>>
>>> astro1 != astro1
False
>>> astro1 != astro2
True
>>> astro1 != astro3
True


Other flags
-----------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>> astro1 = Astronaut('Mark', 'Watney')
>>> astro2 = Astronaut('Mark', 'Watney')
>>> astro3 = Astronaut('Jan', 'Twardowski')


InitVar
-------
* Init-only fields are added as parameters to the generated ``__init__`` method, and are passed to the optional ``__post_init__`` method
* They are not otherwise used by Data Classes

>>> # doctest: +SKIP
... from dataclasses import dataclass, InitVar
...
...
... @dataclass
... class Astronaut:
...     fullname: InitVar[str] = None
...     _firstname: str = None
...     _lastname: str = None
...
...     def __post_init__(self, fullname: str):
...         fullname = fullname.split()
...         self._firstname = fullname[0]
...         self._lastname = fullname[1]
...
...
... astro = Astronaut('Mark Watney')
...
... print(astro._firstname)
Mark
... print(astro._lastname)
Watney
