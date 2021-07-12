Dataclass Mutable Attrs
=======================


Rationale
---------
* problem with ``dict``, ``list``, ``set``
* You should not set mutable objects as a default function argument
* ``field()`` creates new empty ``list`` for each object
* It does not reuse pointer
* Discussion: https://github.com/ericvsmith/dataclasses/issues/3


Problem
-------
.. warning:: Note, You should not set mutable objects as a default function argument. More information in `Argument Mutability`

>>> class Astronaut:
...     def __init__(self, name, missions=[]):
...         self.name = name
...         self.missions = missions
>>>
>>>
>>> watney = Astronaut('Mark Watney')
>>> lewis = Astronaut('Melissa Lewis')
>>>
>>> watney.missions.append('Ares 1')
>>> watney.missions.append('Ares 2')
>>> watney.missions.append('Ares 3')
>>>
>>> print(f'Name: {watney.name}, Missions: {watney.missions}')
Name: Mark Watney, Missions: ['Ares 1', 'Ares 2', 'Ares 3']
>>>
>>> print(f'Name: {lewis.name}, Missions: {lewis.missions}')
Name: Melissa Lewis, Missions: ['Ares 1', 'Ares 2', 'Ares 3']


List of Strings
---------------
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
>>> Astronaut('Mark', 'Watney')
Astronaut(firstname='Mark', lastname='Watney', missions=[])


List of Objects
---------------
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
Astronaut(firstname='Mark', lastname='Watney', missions=[])


Dict
----
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
Astronaut(firstname='Mark', lastname='Watney', missions={})


Default Values
--------------
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
