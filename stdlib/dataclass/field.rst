Dataclass Field
===============


Rationale
---------
* ``name`` - The name of the field.
* ``type`` - The type of the field.
* ``default`` - Default value
* ``default_factory`` - Field factory
* ``init``
* ``repr``
* ``hash``
* ``compare``
* ``metadata`` - This can be a mapping or ``None``. ``None`` is treated as an empty ``dict``. It is not used at all by Data Classes, and is provided as a third-party extension mechanism.



Default
-------
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     mission: str = 'Ares3'

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     mission: str = field(default='Ares3')


Default Factory
---------------
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str] = ['Ares3', 'Apollo18']

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str] = field(default_factory=lambda: ['Ares3', 'Apollo18'])






>>> from __future__ import annotations  # od Python 3.7
>>> from dataclasses import dataclass, field
>>> from typing import Optional, Union
>>>
>>>
>>>
>>> @dataclass
>>> class Person:
>>>     firstname: str
>>>     lastname: str
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: Optional[str] = 'Polsa'
...     missions: Optional[list[str]] = field(default_factory=list)
...     age: Optional[int|float] = field(repr=False, default=None)
...     height: Optional[float] = field(repr=False, default=None)
...     weight: Optional[float] = field(repr=False, default=None)
...     friends: list[Person] = field(default_factory=list)
...     crew_mates: list[Astronaut] = field(default_factory=list)
...
...     def __post_init__(self):
...         if self.age and self.age < 0:
...             raise ValueError('Age must above 0')
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', age=44)

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass(frozen=True)
... class Astronaut:
...     firstname: str
...     lastname: str
...     weight: float = field(metadata={'unit': 'kg'})
...     missions: list[str] = field(metadata={'choices': ['Apollo11', 'Apollo12']})
...     groups: list[str] = field(default_factory=lambda: ['astronauts', 'managers'])
...     job: str = 'astronaut'
>>>
>>> mark = Astronaut('Mark', 'Watney', weight=..., missions=['Apollo18', 'Ares3'])

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


>>> @dataclass
... class Astronaut:
...     email: str
...     username: str
...     firstname: str
...     lastname: str
...     friends: List[Astronaut] = field(default_factory=list)
...     agency: str = field(default='NASA')
...     weight: float = None
...     height: float = field(default=None, metadata={'unit': 'cm', 'min': 140, 'max': 210})
...     age: float = None
...     account_last_login: datetime = datetime.now(tz=timezone.utc)
...     account_updated: datetime = datetime.now(tz=timezone.utc)
...     account_created: datetime = datetime.now(tz=timezone.utc)
...
...     def __setattr__(self, attrname, attrvalue):
...         min = Astronaut.__dataclass_fields__[attrname].metadata['min']
...         max = Astronaut.__dataclass_fields__[attrname].metadata['max']
...
...         if attrvalue < min:
...             raise ValueError
...         if attrvalue > max:
...             raise ValueError


Assignments
-----------
.. literalinclude:: assignments/dataclass_field_a.py
    :caption: :download:`Solution <assignments/dataclass_field_a.py>`
    :end-before: # Solution
