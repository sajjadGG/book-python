Operators
=========


Rationale
---------
* Operator Overload
* Readable syntax
* Simpler operations
* Following examples uses ``dataclasses`` to focus on action code, not boilerplate

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Vector:
...     x: int = 0
...     y: int = 0
>>>
>>>
>>> Vector(x=1, y=2) + Vector(x=3, y=4)
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Vector:
...     x: int = 0
...     y: int = 0
...
...     def __add__(self, other):
...         return Vector(
...             self.x + other.x,
...             self.y + other.y)
>>>
>>>
>>> Vector(x=1, y=2) + Vector(x=3, y=4)
Vector(x=4, y=6)
>>>
>>> Vector(x=1, y=2) + Vector(x=3, y=4) + Vector(x=5, y=6)
Vector(x=9, y=12)


Use Case - Game
---------------
>>> # doctest: +SKIP
...
... hero @ Position(x=50, y=120)
... hero >> Direction(left=10, up=20)
...
... hero < Damage(20)
... hero > Damage(20)
...
... hero['gold'] += dragon['gold']


Use Case - Cache
----------------
>>> class Cache(dict):
...     def __init__(self, func):
...         self.func = func
...
...     def __call__(self, *args):
...         if args not in self:
...             self[args] = self.func(*args)
...         return self[args]
>>>
>>>
>>> @Cache
... def add(a, b):
...     return a + b
>>>
>>>
>>> _ = add(1,2)  # computed
>>> _ = add(1,2)  # fetched from cache
>>> _ = add(1,2)  # fetched from cache
>>> _ = add(1,2)  # fetched from cache
>>> _ = add(2,1)  # computed
>>> _ = add(2,1)  # fetched from cache
>>>
>>> add  # doctest: +NORMALIZE_WHITESPACE
{(1, 2): 3,
 (2, 1): 3}

>>> class Cache(dict):
...     def __init__(self, func):
...         self.func = func
...
...     def __call__(self, *args):
...         return self[args]
...
...     def __missing__(self, key):
...         self[key] = self.func(*key)
...         return self[key]
>>>
>>>
>>> @Cache
... def add(a, b):
...     return a + b
>>>
>>>
>>> _ = add(1,2)  # computed
>>> _ = add(1,2)  # fetched from cache
>>> _ = add(1,2)  # fetched from cache
>>> _ = add(1,2)  # fetched from cache
>>> _ = add(2,1)  # computed
>>> _ = add(2,1)  # fetched from cache
>>>
>>> add  # doctest: +NORMALIZE_WHITESPACE
{(1, 2): 3,
 (2, 1): 3}


Further Reading
---------------
* https://docs.python.org/reference/datamodel.html#emulating-numeric-types
* https://docs.python.org/library/operator.html
