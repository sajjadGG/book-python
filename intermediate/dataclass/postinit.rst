Dataclass Postinit
==================


Rationale
---------
* Dataclasses generate ``__init__()``
* Overloading ``__init__()`` manually will destroy it
* For init time validation there is ``__post_init__()``
* It is run after all parameters are set in the class
* Hence you have to take care about negative cases (errors)


Initial Validation in Classes
-----------------------------
>>> class Astronaut:
...
...     def __init__(self, firstname, lastname, age):
...         self.firstname = firstname
...         self.lastname = lastname
...         if 30 <= age < 50:
...             self.age = age
...         else:
...             raise ValueError('Age is out of range')
...
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', age=44)
>>> vars(astro)
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 44}
>>>
>>> astro = Astronaut('Mark', 'Watney', age=60)
Traceback (most recent call last):
ValueError: Age is out of range

>>> from typing import Final
>>>
>>>
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: Final[int] = 30
...     AGE_MAX: Final[int] = 50
...
...     def __init__(self, firstname, lastname, age):
...         self.firstname = firstname
...         self.lastname = lastname
...
...         if not self.AGE_MIN <= age < self.AGE_MAX:
...             raise ValueError('Age is out of range')
...         else:
...             self.age = age
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', age=44)
>>> vars(astro)
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 44}
>>>
>>> Astronaut('Mark', 'Watney', age=60)
Traceback (most recent call last):
ValueError: Age is out of range


Initial Validation in Dataclasses
---------------------------------
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
...
...     def __post_init__(self):
...         if not self.AGE_MIN <= self.age < self.AGE_MAX:
...             raise ValueError('Age is out of range')
>>>
>>>
>>> Astronaut('Mark', 'Watney', age=44)
Astronaut(firstname='Mark', lastname='Watney', age=44, AGE_MIN=30, AGE_MAX=50)
>>>
>>> Astronaut('Mark', 'Watney', age=60)
Traceback (most recent call last):
ValueError: Age is out of range


Date and Time Conversion
------------------------
>>> from dataclasses import dataclass
>>> from datetime import date
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     born: date
...
...     def __post_init__(self):
...         self.born = date.fromisoformat(self.born)
>>>
>>>
>>> Astronaut('Mark', 'Watney', '1961-04-12')  # doctest: +NORMALIZE_WHITESPACE
Astronaut(firstname='Mark', lastname='Watney',
          born=datetime.date(1961, 4, 12))

>>> from dataclasses import dataclass
>>> from datetime import datetime
>>> from typing import Optional
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     launch: Optional[datetime] = None
...
...     def __post_init__(self):
...         if self.launch is not None:
...             self.launch = datetime.fromisoformat(self.launch)
>>>
>>>
>>> Astronaut('Mark', 'Watney')
Astronaut(firstname='Mark', lastname='Watney', launch=None)
>>>
>>> Astronaut('Mark', 'Watney', '1969-07-21T02:56:15+00:00')  # doctest: +NORMALIZE_WHITESPACE
Astronaut(firstname='Mark', lastname='Watney',
          launch=datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc))


InitVar
-------
* Init-only fields are added as parameters to the generated ``__init__`` method, and are passed to the optional ``__post_init__`` method
* They are not otherwise used by Data Classes

>>> from dataclasses import dataclass, InitVar, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     fullname: InitVar[str] = None
...     firstname: str = field(init=False, default=None)
...     lastname: str = field(init=False, default=None)
...
...     def __post_init__(self, fullname: str):
...         self.firstname, self.lastname = fullname.split()
>>>
>>>
>>> astro = Astronaut('Mark Watney')
>>>
>>> astro
Astronaut(firstname='Mark', lastname='Watney')
>>>
>>> vars(astro)
{'firstname': 'Mark', 'lastname': 'Watney'}


ClassVar
--------
One of two places where dataclass() actually inspects the type of a field
is to determine if a field is a class variable as defined in PEP 526. It
does this by checking if the type of the field is typing.ClassVar. If a
field is a ClassVar, it is excluded from consideration as a field and is
ignored by the dataclass mechanisms. Such ClassVar pseudo-fields are not
returned by the module-level fields() function.

>>> from typing import ClassVar
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     fullname: str
...     firstname: str
...     age: int
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50


Use Case - 0x01
---------------
* Boundary check

>>> class Point:
...     def __init__(self, x, y):
...         if x < 0:
...             raise ValueError('Coordinate cannot be negative')
...         else:
...             self.x = x
...
...         if y < 0:
...             raise ValueError('Coordinate cannot be negative')
...         else:
...             self.y = y

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Point:
...     x: int = 0
...     y: int = 0
...
...     def __post_init__(self):
...         if self.x < 0 or self.y < 0:
...             raise ValueError('Coordinate cannot be negative')


Use Case - 0x02
---------------
* Var Range

>>> from dataclasses import dataclass, field
>>> from typing import Final
>>>
>>>
>>> @dataclass
... class Point:
...     x: int = 0
...     y: int = 0
...     X_MIN: Final[int] = 0
...     X_MAX: Final[int] = 1024
...     Y_MIN: Final[int] = 0
...     Y_MAX: Final[int] = 768
...
...     def __post_init__(self):
...         if not self.X_MIN <= self.x < self.X_MAX:
...             raise ValueError(f'x value ({self.x}) is not between {self.X_MIN} and {self.X_MAX}')
...         if not self.Y_MIN <= self.y < self.Y_MAX:
...             raise ValueError(f'y value ({self.y}) is not between {self.Y_MIN} and {self.Y_MAX}')
>>>
>>>
>>> Point(0, 0)
Point(x=0, y=0, X_MIN=0, X_MAX=1024, Y_MIN=0, Y_MAX=768)
>>>
>>> Point(-1, 0)
Traceback (most recent call last):
ValueError: x value (-1) is not between 0 and 1024
>>>
>>> Point(0, 2000)
Traceback (most recent call last):
ValueError: y value (2000) is not between 0 and 768
>>>
>>> Point(0, 0, X_MIN=10, X_MAX=100)
Traceback (most recent call last):
ValueError: x value (0) is not between 10 and 100


Use Case - 0x03
---------------
* Const Range

>>> from dataclasses import dataclass, field
>>> from typing import Final
>>>
>>>
>>> @dataclass
... class Point:
...     x: int = 0
...     y: int = 0
...     X_MIN: Final[int] = field(init=False, default=0)
...     X_MAX: Final[int] = field(init=False, default=1024)
...     Y_MIN: Final[int] = field(init=False, default=0)
...     Y_MAX: Final[int] = field(init=False, default=768)
...
...     def __post_init__(self):
...         if not self.X_MIN <= self.x < self.X_MAX:
...             raise ValueError(f'x value ({self.x}) is not between {self.X_MIN} and {self.X_MAX}')
...         if not self.Y_MIN <= self.y < self.Y_MAX:
...             raise ValueError(f'y value ({self.y}) is not between {self.Y_MIN} and {self.Y_MAX}')
>>>
>>>
>>> Point(0, 0)
Point(x=0, y=0, X_MIN=0, X_MAX=1024, Y_MIN=0, Y_MAX=768)
>>>
>>> Point(0, 0, X_MIN=10, X_MAX=100)
Traceback (most recent call last):
TypeError: __init__() got an unexpected keyword argument 'X_MIN'


Use Case - 0x04
---------------
* Init, Repr

>>> from dataclasses import dataclass, field
>>> from typing import Final
>>>
>>>
>>> @dataclass
... class Point:
...     x: int = 0
...     y: int = 0
...     X_MIN: Final[int] = field(init=False, repr=False, default=0)
...     X_MAX: Final[int] = field(init=False, repr=False, default=1024)
...     Y_MIN: Final[int] = field(init=False, repr=False, default=0)
...     Y_MAX: Final[int] = field(init=False, repr=False, default=768)
...
...     def __post_init__(self):
...         if not self.X_MIN <= self.x < self.X_MAX:
...             raise ValueError(f'x value ({self.x}) is not between {self.X_MIN} and {self.X_MAX}')
...         if not self.Y_MIN <= self.y < self.Y_MAX:
...             raise ValueError(f'y value ({self.y}) is not between {self.Y_MIN} and {self.Y_MAX}')
>>>
>>>
>>> Point(0, 0)
Point(x=0, y=0)
>>>
>>> Point(-1, 0)
Traceback (most recent call last):
ValueError: x value (-1) is not between 0 and 1024
>>>
>>> Point(0, -1)
Traceback (most recent call last):
ValueError: y value (-1) is not between 0 and 768


Assignments
-----------
.. literalinclude:: assignments/dataclass_postinit_a.py
    :caption: :download:`Solution <assignments/dataclass_postinit_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/dataclass_postinit_b.py
    :caption: :download:`Solution <assignments/dataclass_postinit_b.py>`
    :end-before: # Solution
