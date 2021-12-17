Dataclass Parameters
====================


Rationale
---------
.. csv-table:: Dataclass options
    :header: "Option", "Default", "Description (if True)"
    :widths: 10, 10, 80

    ``init``,         ``True``,   "Generate ``__init__()`` method"
    ``repr``,         ``True``,   "Generate ``__repr__()`` method"
    ``eq``,           ``True``,   "Generate ``__eq__()`` and ``__ne__()`` methods"
    ``order``,        ``False``,  "Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods"
    ``unsafe_hash``,  ``False``,  "If False: the ``__hash__()`` method is generated according to how eq and frozen are set"
    ``frozen``,       ``False``,  "If ``True``: assigning to fields will generate an exception"
    ``match_args``,   ``True``,   "Generate ``__match_args__()`` method"
    ``kw_only``,      ``False``,  "Mark all fields as keyword-only"
    ``slots``,        ``False``,  "Create class with ``__slots__``"


Example
-------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False,
...            frozen=False, match_args=True, kw_only=False, slots=False)
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>> astro1 = Astronaut('Mark', 'Watney')
>>> astro2 = Astronaut('Mark', 'Watney')
>>> astro3 = Astronaut('Jan', 'Twardowski')


Init
----
* ``init=True`` by default
* Generate ``__init__()`` method

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(init=True)
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
* Assigning to fields will generate an exception

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(frozen=False)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>> p.x = 30
>>>
>>> print(p)
Point(x=30, y=20)

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

Hash
----
* ``hash=False`` by default
* the ``__hash__()`` method is generated according to how eq and frozen are set


Order
-----
* ``order=False`` by default
* Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods


Match_args
----------
* ``match_args=True`` by default
* Since Python 3.10

If true, the __match_args__ tuple will be created from the list of parameters
to the generated __init__() method (even if __init__() is not generated, see
above). If false, or if __match_args__ is already defined in the class, then
__match_args__ will not be generated.
New in version 3.10.


Kw_only
----------
* ``kw_only=False`` by default
* Mark all fields as keyword-only
* Since Python 3.10

If true, then all fields will be marked as keyword-only. If a field is marked
as keyword-only, then the only affect is that the __init__() parameter
generated from a keyword-only field must be specified with a keyword when
__init__() is called. There is no effect on any other aspect of dataclasses.


Slots
-----
* ``slots=False`` by default
* Create class with ``__slots__``
* Since Python 3.10

If true, __slots__ attribute will be generated and new class will be returned
instead of the original one. If __slots__ is already defined in the class,
then TypeError is raised.
