Dataclass Helpers
=================


Helper functions
----------------
* ``fields(class_or_instance)`` - Returns a tuple of Field objects that define the fields for this Data Class. Accepts either a Data Class, or an instance of a Data Class. Raises ValueError if not passed a Data Class or instance of one. Does not return pseudo-fields which are ClassVar or InitVar.
* ``asdict(instance, *, dict_factory=dict)`` - Converts the Data Class instance to a dict (by using the factory function dict_factory)
* ``astuple(*, tuple_factory=tuple)`` - Converts the Data Class instance to a tuple (by using the factory function tuple_factory). Each Data Class is converted to a tuple of its field values. Data Classes, dicts, lists, and tuples are recursed into.
* ``make_dataclass(cls_name, fields, *, bases=(), namespace=None)`` - Creates a new Data Class with name cls_name, fields as defined in fields, base classes as given in bases, and initialized with a namespace as given in namespace.
* ``replace(instance, **changes)`` - Creates a new object of the same type of instance, replacing fields with values from changes. If instance is not a Data Class, raises TypeError. If values in changes do not specify fields, raises TypeError.
* ``is_dataclass(class_or_instance)`` - Returns True if its parameter is a dataclass or an instance of one, otherwise returns False.

>>> from dataclasses import dataclass, asdict, astuple
>>>
>>>
>>> @dataclass
... class Point:
...     x: int
...     y: int
>>>
>>> @dataclass
... class Coordinates:
...     points: list[Point]
>>>
>>>
>>> p = Point(10, 20)
>>> c = Coordinates([Point(0, 0), Point(10, 4)])
>>>
>>> asdict(p)
{'x': 10, 'y': 20}
>>> asdict(c)
{'points': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}
>>>
>>> astuple(p)
(10, 20)
>>> astuple(c)
([(0, 0), (10, 4)],)

