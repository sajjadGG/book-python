Enum StrEnum
============
* List of finite choices
* Enumerations with str values
* ``StrEnum``


SetUp
-----
>>> from enum import StrEnum


Example
-------
>>> class Color(StrEnum):
...     RED = '#FF0000'
...     GREEN = '#00FF00'
...     BLUE = '#0000FF'


Use Case - 0x01
---------------
* Dead or Alive

>>> class Status(StrEnum):
...     ALIVE = 'alive'
...     DEAD = 'dead'


Use Case - 0x02
---------------
>>> class Ordinal(StrEnum):
...     NORTH = 'N'
...     SOUTH = 'S'
...     EAST = 'E'
...     WEST = 'W'


Use Case - 0x03
---------------
>>> class Mood(StrEnum):
...     SAD = 'sad'
...     HAPPY = 'happy'


Use Case - 0x04
---------------
* Issue Status

>>> class IssueStatus(StrEnum):
...     TODO = 'todo'
...     IN_PROGRESS = 'in-progress'
...     IN_REVIEW = 'in-review'
...     IN_TEST = 'in-test'
...     DONE = 'done'
...     REJECTED = 'rejected'


Use Case - 0x05
---------------
* HTML Colors

>>> class Color(StrEnum):
...     AQUA = '#00FFFF'
...     BLACK = '#000000'
...     BLUE = '#0000FF'
...     FUCHSIA = '#FF00FF'
...     GRAY = '#808080'
...     GREEN = '#008000'
...     LIME = '#00FF00'
...     MAROON = '#800000'
...     NAVY = '#000080'
...     OLIVE = '#808000'
...     PINK = '#FF1A8C'
...     PURPLE = '#800080'
...     RED = '#ff0000'
...     SILVER = '#C0C0C0'
...     TEAL = '#008080'
...     WHITE = '#FFFFFF'
...     YELLOW = '#FFFF00'


Use Case - 0x06
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> class Agency(StrEnum):
...     NASA = 'NASA'
...     ESA = 'ESA'
...     JAXA = 'JAXA'
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


Use Case - 0x07
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


.. todo:: Assignments
