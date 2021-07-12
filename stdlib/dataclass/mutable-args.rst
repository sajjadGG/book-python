Mutable attributes
==================

* problem with ``dict``, ``list``, ``set``
* You should not set mutable objects as a default function argument
* ``field()`` creates new empty ``list`` for each object
* It does not reuse pointer
* Discussion: https://github.com/ericvsmith/dataclasses/issues/3

.. warning:: Note, You should not set mutable objects as a default function argument. More information in `Argument Mutability`

    >>> class Astronaut:
    ...     def __init__(self, name, missions=[]):
    ...         self.name = name
    ...         self.missions = missions
    >>>
    >>>
    >>> watney = Astronaut('Mark Watney')
    >>> twardowski = Astronaut('Jan Twardowski')
    >>>
    >>> watney.missions.append('Ares 1')
    >>> watney.missions.append('Ares 2')
    >>> watney.missions.append('Ares 3')
    >>> watney.missions.append('Ares 4')
    >>> watney.missions.append('Ares 5')
    >>>
    >>> print('Watney:', watney.missions)
    Watney: ['Ares 1', 'Ares 2', 'Ares 3', 'Ares 4', 'Ares 5']
    >>>
    >>> print('Twardowski:', twardowski.missions)
    Twardowski: ['Ares 1', 'Ares 2', 'Ares 3', 'Ares 4', 'Ares 5']

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str] = field(default_factory=list)
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: dict[int,str] = field(default_factory=dict)
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[Mission] = field(default_factory=list)
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     jobs: list[str] = field(default_factory=lambda: ['Astronaut'])
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>> astro
Astronaut(firstname='Mark', lastname='Watney', jobs=['Astronaut'])

Init
----
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: Final[int] = field(init=False, default=27)
...     AGE_MAX: Final[int] = field(init=False, default=50)
