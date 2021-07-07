Operators Builtin
=================


Rationale
---------
.. csv-table:: Builtin Functions Overload
    :header: "Function", "Method"

    "``abs(obj)``",                      "``obj.__abs__()``"
    "``bool(obj)``",                     "``obj.__bool__()``"
    "``complex(obj)``",                  "``obj.__complex__()``"
    "``del obj``",                       "``obj.__del__()``"
    "``delattr(obj, name)``",            "``obj.__delattr__(name)``"
    "``dir(obj)``",                      "``obj.__dir__()``"
    "``divmod(obj, other)``",            "``obj.__divmod__(other)``"
    "``float(obj)``",                    "``obj.__float__()``"
    "``getattr(obj, name, default)``",   "``obj.__getattr__(name, default)``"
    "``hash(obj)``",                     "``obj.__hash__()``"
    "``hex(obj)``",                      "``obj.__hex__()``"
    "``int(obj)``",                      "``obj.__int__()``"
    "``iter(obj)``",                     "``obj.__iter__()``"
    "``len(obj)``",                      "``obj.__len__()``"
    "``next(obj)``",                     "``obj.__next__()``"
    "``oct(obj)``",                      "``obj.__oct__()``"
    "``pow(obj)``",                      "``obj.__pow__()``"
    "``reversed(obj)``",                 "``obj.__reversed__()``"
    "``round(obj, ndigits)``",           "``obj.__round__(ndigits)``"
    "``setattr(obj, name)``",            "``obj.__setattr__(name)``"


Example
-------
>>> from math import sqrt
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Vector:
...     x: int = 0
...     y: int = 0
...
...     def __abs__(self):
...         return sqrt(self.x**2 + self.y**2)
>>>
>>>
>>> abs(Vector(x=3, y=4))
5.0


Use Case
--------
>>> class Astronaut:
...     def __float__(self) -> float:
...         return 1961.0
...
...     def __int__(self) -> int:
...         return 1969
...
...     def __len__(self) -> int:
...         return 170
...
...     def __str__(self) -> str:
...         return 'My name... José Jiménez'
...
...     def __repr__(self) -> str:
...         return f'Astronaut()'
>>>
>>> astro = Astronaut()
>>>
>>> float(astro)
1961.0
>>>
>>> int(astro)
1969
>>>
>>> len(astro)
170
>>>
>>> repr(astro)
'Astronaut()'
>>>
>>> str(astro)
'My name... José Jiménez'
>>>
>>> print(astro)
My name... José Jiménez
