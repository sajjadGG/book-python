Dataclass Field
===============


Field Object
------------
* ``name`` - The name of the field.
* ``type`` - The type of the field.
* ``default`` - Default value
* ``default_factory`` - Field factory
* ``init``
* ``repr``
* ``hash``
* ``compare``
* ``metadata`` - This can be a mapping or ``None``. ``None`` is treated as an empty ``dict``. It is not used at all by Data Classes, and is provided as a third-party extension mechanism.

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     publicname: int = field(repr=False)
...     agency: int = field(repr=False, default='NASA')

>>> from __future__ import annotations
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass(frozen=True)
... class Mission:
...     year: int
...     name: str
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: float
...     height: float = field(metadata={'unit': 'cm'})
...     weight: float = field(metadata={'unit': 'km'})
...     mission: list[Mission]
...     agency: str = field(default='NASA', metadata={'choices': ['NASA', 'ESA']})
...     friends: list[Astronaut] = field(default_factory=list)
...     country: str = 'USA'
...
...     def __post_init__(self):
...         if self.age > 65:
...             raise ValueError('Too old for an astronaut')
...
...     def say_hello(self):
...         print(f'Howdy, I am {self.firstname} {self.lastname}')
...
...
>>> astro = Astronaut('Mark', 'Watney',
...                   age=44,
...                   height=170,
...                   weight=75,
...                   mission=[Mission(2035, 'Ares 3')],
...                   friends=[],
...                   agency='NASA')
>>>
>>> astro
Astronaut(firstname='Mark', lastname='Watney', age=44, height=170, weight=75, mission=[Mission(year=2035, name='Ares 3')], agency='NASA', friends=[], country='USA')
>>>
>>> astro.__dataclass_fields__['agency'].metadata['choices']
['NASA', 'ESA']
>>> astro.__dataclass_fields__['height'].metadata['unit']
'cm'
>>> Astronaut.__dataclass_fields__['agency'].metadata['choices']
['NASA', 'ESA']


Metadata
--------
>>> from dataclasses import dataclass, field
>>> from typing import Literal
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: Literal['NASA', 'ESA', 'Roscosmos']
...     height: float = field(default=None, metadata={'unit': 'cm'})
...     weight: float = field(default=None, metadata={'unit': 'kg'})
...     age: float = field(default=None, metadata={'min': 27, 'max': 50})
...
...     def __post_init__(self):
...         AGE_MIN = self.__dataclass_fields__['age'].metadata['min']
...         AGE_MAX = self.__dataclass_fields__['age'].metadata['max']
...
...         if self.age < AGE_MIN:
...             raise ValueError('Age is below minimum')
...         if self.age > AGE_MAX:
...             raise ValueError('Age is above maximum')
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', agency='NASA', age=51)



Mutable attributes
------------------
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


Assignments
-----------
.. literalinclude:: assignments/dataclass_field_a.py
    :caption: :download:`Solution <assignments/dataclass_field_a.py>`
    :end-before: # Solution
