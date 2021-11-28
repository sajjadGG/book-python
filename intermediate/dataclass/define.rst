Dataclass Define
================


Required Fields
---------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str


Default Fields
--------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: str = 'NASA'


Optional Fields
---------------
>>> from dataclasses import dataclass
>>> from typing import Optional
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: Optional[str] = None


Literal Field
-------------
>>> from dataclasses import dataclass, field
>>> from typing import Literal
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: Literal['NASA', 'ESA', 'Roscosmos']


Union Fields
------------
>>> from dataclasses import dataclass
>>> from typing import Union
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: Union[int,float]

Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass  # doctest: +SKIP
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int|float


Final Fields
------------
* In Python there is no constants

>>> from dataclasses import dataclass
>>> from typing import Final
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: Final[int] = 30
...     AGE_MAX: Final[int] = 50


Relation to Objects
-------------------
>>> from dataclasses import dataclass
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
...     missions: list[Mission]
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', missions=[
...     Mission(1973, 'Apollo 18'),
...     Mission(2012, 'STS-136'),
...     Mission(2035, 'Ares 3')])
>>>
>>> astro  # doctest: +NORMALIZE_WHITESPACE
Astronaut(firstname='Mark', lastname='Watney',
          missions=[Mission(year=1973, name='Apollo 18'),
                    Mission(year=2012, name='STS-136'),
                    Mission(year=2035, name='Ares 3')])


Relation to Self
----------------
* Note, that there are ``None`` default friends
* Using an empty list ``[]`` as a default value will not work
* We will cover this topic later

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     friends: list['Astronaut'] = None
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', friends=[
...     Astronaut('Melissa', 'Lewis'),
...     Astronaut('Rick', 'Martinez'),
...     Astronaut('Beth', 'Johansen'),
...     Astronaut('Chris', 'Beck'),
...     Astronaut('Alex', 'Vogel')])
>>>
>>> astro  # doctest: +NORMALIZE_WHITESPACE
Astronaut(firstname='Mark', lastname='Watney',
          friends=[Astronaut(firstname='Melissa', lastname='Lewis', friends=None),
                   Astronaut(firstname='Rick', lastname='Martinez', friends=None),
                   Astronaut(firstname='Beth', lastname='Johansen', friends=None),
                   Astronaut(firstname='Chris', lastname='Beck', friends=None),
                   Astronaut(firstname='Alex', lastname='Vogel', friends=None)])


Usecase
-------
``class``:

>>> from datetime import date
>>> from typing import Final, Optional
>>>
>>>
>>> class Mission:
...    year: int
...    name: str
...
...    def __init__(self, year: int, name: str):
...        self.name = name
...        self.year = year
>>>
>>>
>>> class Astronaut:
...    firstname: str
...    lastname: str
...    born: date
...    agency: str = 'NASA'
...    age: Optional[int] = None
...    height: Optional[float] = None
...    weight: Optional[float] = None
...    friends: Optional[list['Astronaut']] = None
...    missions: Optional[list[Mission]] = None
...    rank: Optional[str] = None
...    previous_job: Optional[str] = None
...    experience: Optional[list[str]] = None
...    AGE_MIN: Final[int] = 27
...    AGE_MAX: Final[int] = 50
...    WEIGHT_MIN: Final[int] = 50
...    WEIGHT_MAX: Final[int] = 90
...    HEIGHT_MIN: Final[int] = 156
...    HEIGHT_MAX: Final[int] = 210
...
...
...    def __init__(self,
...                 firstname: str,
...                 lastname: str,
...                 born: date,
...                 agency: str = 'NASA',
...                 age: Optional[int] = None,
...                 height: Optional[float] = None,
...                 weight: Optional[float] = None,
...                 friends: Optional[list['Astronaut']] = None,
...                 missions: Optional[list[Mission]] = None,
...                 rank: Optional[str] = None,
...                 previous_job: Optional[str] = None,
...                 experience: Optional[list[str]] = None):
...
...        self.born = born
...        self.rank = rank
...        self.previous_job = previous_job
...        self.experience = experience
...        self.missions = missions
...        self.friends = friends
...        self.weight = weight
...        self.height = height
...        self.age = age
...        self.agency = agency
...        self.firstname = firstname
...        self.lastname = lastname

``dataclass``:

>>> from dataclasses import dataclass
>>> from datetime import date
>>> from typing import Final, Optional
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
...
...
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     born: date
...     agency: str = 'NASA'
...     age: Optional[int] = None
...     height: Optional[float] = None
...     weight: Optional[float] = None
...     friends: Optional[list['Astronaut']] = None
...     missions: Optional[list[Mission]] = None
...     rank: Optional[str] = None
...     previous_job: Optional[str] = None
...     experience: Optional[list[str]] = None
...     AGE_MIN: Final[int] = 27
...     AGE_MAX: Final[int] = 50
...     WEIGHT_MIN: Final[int] = 50
...     WEIGHT_MAX: Final[int] = 90
...     HEIGHT_MIN: Final[int] = 156
...     HEIGHT_MAX: Final[int] = 210


Assignments
-----------
