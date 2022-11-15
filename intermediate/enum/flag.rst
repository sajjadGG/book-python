Enum StrEnum
============
* Flag
* ``Flag``
* ``IntFlag``

Flags have an expanded view of aliasing: to be canonical, the value of
a flag needs to be a power-of-two value, and not a duplicate name. So,
in addition to the Enum definition of alias, a flag with no value
(a.k.a. 0) or with more than one power-of-two value (e.g. 3)
is considered an alias.

>>> from enum import IntFlag

>>> class Perm(IntFlag):
...     R = 4
...     W = 2
...     X = 1

>>> Perm.R | Perm.W
<Perm.R|W: 6>
>>>
>>> Perm.R + Perm.W
6
>>>
>>> RW = Perm.R | Perm.W
>>> Perm.R in RW
True


SetUp
-----
>>> from enum import Enum, Flag, IntFlag, FlagBoundary, auto


Example
-------
>>> class Color(Flag):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...     WHITE = RED | BLUE | GREEN
...     MAGENTA = RED | BLUE
...     YELLOW = RED | GREEN
...     CYAN = GREEN | BLUE

>>> Color.WHITE
<Color.WHITE: 7>
>>>
>>> Color.GREEN in Color.WHITE
True

>>> purple = Color.RED | Color.BLUE
>>>
>>> Color.GREEN in purple
False
>>>
>>> purple in Color.WHITE
True
>>>
>>> Color.WHITE in purple
False


FlagBoundary
------------
*FlagBoundary* controls how out-of-range values are handled in *Flag* and its
subclasses.


STRICT
------
Out-of-range values cause a :exc:`ValueError` to be raised.  This is the
default for :class:`Flag`:

>>> from enum import Flag, STRICT

>>> class StrictFlag(Flag, boundary=STRICT):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()

>>> StrictFlag(2**2 + 2**4)
Traceback (most recent call last):
ValueError: <flag 'StrictFlag'> invalid value 20
    given 0b0 10100
  allowed 0b0 00111


CONFORM
-------
Out-of-range values have invalid values removed, leaving a valid *Flag*
value:

>>> from enum import Flag, CONFORM

>>> class ConformFlag(Flag, boundary=CONFORM):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()

>>> ConformFlag(2**2 + 2**4)
<ConformFlag.BLUE: 4>


EJECT
-----
Out-of-range values lose their *Flag* membership and revert to :class:`int`.
This is the default for :class:`IntFlag`:

>>> from enum import Flag, EJECT

>>> class EjectFlag(Flag, boundary=EJECT):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()

>>> EjectFlag(2**2 + 2**4)
20


KEEP
----
Out-of-range values are kept, and the *Flag* membership is kept.  This is
used for some stdlib flags:

>>> from enum import Flag, KEEP

>>> class KeepFlag(Flag, boundary=KEEP):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()

>>> KeepFlag(2**2 + 2**4)
<KeepFlag.BLUE|16: 20>


.. todo:: Assignments
