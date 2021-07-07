Dataclass Define
================


Example 1
---------
``class``:

>>> class Point:
...     def __init__(self, x, y, z=0):
...         self.x = x
...         self.y = y
...         self.z = z
>>>
>>>
>>> p0 = Point()
Traceback (most recent call last):
TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
>>>
>>> p1 = Point(10)
Traceback (most recent call last):
TypeError: __init__() missing 1 required positional argument: 'y'
>>>
>>> p2 = Point(10, 20)
>>> p3 = Point(10, 20, 30)
>>> p4 = Point(10, 20, z=30)
>>> p5 = Point(10, 20, z=30)
>>> p6 = Point(x=10, y=20, z=30)

``dataclass``:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Point:
...     x: int
...     y: int
...     z: int = 0
>>>
>>>
>>> p0 = Point()
Traceback (most recent call last):
TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
>>>
>>> p1 = Point(10)
Traceback (most recent call last):
TypeError: __init__() missing 1 required positional argument: 'y'
>>>
>>> p2 = Point(10, 20)
>>> p3 = Point(10, 20, 30)
>>> p4 = Point(10, 20, z=30)
>>> p5 = Point(10, 20, z=30)
>>> p6 = Point(x=10, y=20, z=30)


Example 2
---------
``class``:

>>> class Astronaut:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname: str, lastname: str, agency: str = 'POLSA'):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.agency = agency
>>>
>>>
>>> twardowski = Astronaut('Jan', 'Twardowski')
>>>
>>> print(twardowski.firstname)
Jan
>>> print(twardowski.lastname)
Twardowski
>>> print(twardowski.agency)
POLSA

``dataclass``:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: str = 'POLSA'
>>>
>>>
>>> twardowski = Astronaut('Jan', 'Twardowski')
>>>
>>> print(twardowski.firstname)
Jan
>>> print(twardowski.lastname)
Twardowski
>>> print(twardowski.agency)
POLSA


Example 3
---------
>>> from dataclasses import dataclass
>>> from datetime import date
>>> from typing import Final, Optional
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     born: date = date.today()
...     height: Optional[int] = None
...     friends: Optional[list['Astronaut']] = None
...     AGE_MIN: Final[int] = 27
...     AGE_MAX: Final[int] = 42
>>>
>>>
>>> Astronaut('Mark', 'Watney', date(1994, 10, 12))
Astronaut(firstname='Mark', lastname='Watney', born=datetime.date(1994, 10, 12), height=None, friends=None, AGE_MIN=27, AGE_MAX=42)
>>>
>>> astro = Astronaut('Mark', 'Watney', date(1994, 10, 12), friends=[
...         Astronaut('Melissa', 'Lewis', date(1995, 7, 15)),
...         Astronaut('Rick', 'Martinez', date(1996, 1, 21)),
...         Astronaut('Beth', 'Johansen', date(2006, 5, 9)),
...         Astronaut('Chris', 'Beck', date(1999, 8, 2)),
...         Astronaut('Alex', 'Vogel', date(1994, 11, 15))])
>>>
>>> astro  # doctest: +NORMALIZE_WHITESPACE
Astronaut(firstname='Mark', lastname='Watney', born=datetime.date(1994, 10, 12), height=None, friends=[Astronaut(firstname='Melissa', lastname='Lewis', born=datetime.date(1995, 7, 15), height=None, friends=None, AGE_MIN=27, AGE_MAX=42), Astronaut(firstname='Rick', lastname='Martinez', born=datetime.date(1996, 1, 21), height=None, friends=None, AGE_MIN=27, AGE_MAX=42), Astronaut(firstname='Beth', lastname='Johansen', born=datetime.date(2006, 5, 9), height=None, friends=None, AGE_MIN=27, AGE_MAX=42), Astronaut(firstname='Chris', lastname='Beck', born=datetime.date(1999, 8, 2), height=None, friends=None, AGE_MIN=27, AGE_MAX=42), Astronaut(firstname='Alex', lastname='Vogel', born=datetime.date(1994, 11, 15), height=None, friends=None, AGE_MIN=27, AGE_MAX=42)], AGE_MIN=27, AGE_MAX=42)


Example 4
---------
``class``:

>>> from datetime import datetime
>>>
>>>
>>> class StarWarsMovie:
...     title: str
...     episode_id: int
...     opening_crawl: str
...     director: str
...     producer: str
...     release_date: datetime
...     characters: tuple[str]
...     planets: tuple[str]
...     starships: tuple[str]
...     vehicles: tuple[str]
...     species: tuple[str]
...     created: datetime
...     edited: datetime
...     url: str
...
...     def __init__(self, title: str, episode_id: int, opening_crawl: str,
...                  director: str, producer: str, release_date: datetime,
...                  characters: tuple[str], planets: tuple[str], starships: tuple[str],
...                  vehicles: tuple[str], species: tuple[str], created: datetime,
...                  edited: datetime, url: str):
...
...         self.title = title
...         self.episode_id = episode_id
...         self.opening_crawl= opening_crawl
...         self.director = director
...         self.producer = producer
...         self.release_date = release_date
...         self.characters = characters
...         self.planets = planets
...         self.starships = starships
...         self.vehicles = vehicles
...         self.species = species
...         self.created = created
...         self.edited = edited
...         self.url = url

``dataclass``:

>>> from dataclasses import dataclass
>>> from datetime import datetime
>>>
>>>
>>> @dataclass
... class StarWarsMovie:
...     title: str
...     episode_id: int
...     opening_crawl: str
...     director: str
...     producer: str
...     release_date: datetime
...     characters: tuple[str]
...     planets: tuple[str]
...     starships: tuple[str]
...     vehicles: tuple[str]
...     species: tuple[str]
...     created: datetime
...     edited: datetime
...     url: str


Assignments
-----------
.. literalinclude:: assignments/dataclass_define_a.py
    :caption: :download:`Solution <assignments/dataclass_define_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/dataclass_define_b.py
    :caption: :download:`Solution <assignments/dataclass_define_b.py>`
    :end-before: # Solution
