Enum Auto
=========
* Automatically generated value
* ``auto()``

SetUp
-----
>>> from enum import StrEnum, IntEnum, auto


StrEnum
-------
>>> class Color(StrEnum):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()

>>> Color.RED
<Color.RED: 'red'>


IntEnum
-------
>>> class Color(IntEnum):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()

>>> Color.RED
<Color.RED: 1>
