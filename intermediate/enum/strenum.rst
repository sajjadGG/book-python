Enum StrEnum
============
* List of finite choices
* Enumerations
* ``Enum``
* ``IntEnum``
* ``StrEnum``
* ``Flag``
* ``IntFlag``
* ``auto()``

SetUp
-----
>>> from enum import Enum, IntEnum, StrEnum, auto


Syntax
------
>>> class Select(Enum):
...     OPTION1 = 1
...     OPTION2 = 2


Example
-------
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'


Use Case - 0x01
---------------
* Dead or Alive

>>> class Status(StrEnum):
...     ALIVE = 'alive'
...     DEAD = 'dead'


Use Case - 0x03
---------------
* Issue Status

>>> class IssueStatus(StrEnum):
...     TODO = 'todo'
...     IN_PROGRESS = 'in-progress'
...     IN_REVIEW = 'in-review'
...     IN_TEST = 'in-test'
...     DONE = 'done'
...     REJECTED = 'rejected'


Use Case - 0x04
---------------
* HTML Colors

>>> class Color(StrEnum):
...     AQUA = '#00FFFF'
...     BLACK = '#000000'
...     BLUE = '#0000ff'
...     FUCHSIA = '#FF00FF'
...     GRAY = '#808080'
...     GREEN = '#008000'
...     LIME = '#00ff00'
...     MAROON = '#800000'
...     NAVY = '#000080'
...     OLIVE = '#808000'
...     PINK = '#ff1a8c'
...     PURPLE = '#800080'
...     RED = '#ff0000'
...     SILVER = '#C0C0C0'
...     TEAL = '#008080'
...     WHITE = '#ffffff'
...     YELLOW = '#FFFF00'


Use Case - 0x05
---------------
>>> Point = tuple[int,int]
>>>
>>> class Color(Enum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'

>>> def draw_line(A: Point, B: Point, color: Color):
...     if type(color) is not Color:
...         possible = [str(c) for c in Color]
...         raise TypeError(f'Invalid color, possible choices: {possible}')
...     print(f'Drawing line from {A} to {B} with color {color.value}')

>>> draw_line(A=(0,0), B=(3,5), color=Color.RED)
Drawing line from (0, 0) to (3, 5) with color #FF0000

>>> draw_line(A=(0,0), B=(3,5), color='red')
Traceback (most recent call last):
TypeError: Invalid color, possible choices: ['Color.RED', 'Color.GREEN', 'Color.BLUE']


Use Case - 0x08
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> class Agency(StrEnum):
...     NASA = auto()
...     ESA = auto()
...     JAXA = auto()
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: Agency
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', agency='not-existing')
>>> mark = Astronaut('Mark', 'Watney', agency=Agency.NASA)


Use Case - 0x09
---------------
>>> # doctest: +SKIP
... from django.db import models
...
... class HttpMethod(models.TextChoices):
...     GET = 'GET', _('GET')
...     POST = 'POST', _('POST')
...     PATCH = 'PATCH', _('PATCH')
...     PUT = 'PUT', _('PUT')
...     HEAD = 'HEAD', _('HEAD')
...     DELETE = 'DELETE', _('DELETE')
...     OPTIONS = 'OPTIONS', _('OPTIONS')
...     TRACE = 'TRACE', _('TRACE')
...     CONNECT = 'CONNECT', _('CONNECT')
...
...
... class Stage(models.TextChoices):
...     PRODUCTION = 'production', _('Production')
...     TEST = 'test', _('Test')



References
----------
.. [mskeycodes] https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
.. [jskeycodes] https://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes


.. todo:: Assignments
