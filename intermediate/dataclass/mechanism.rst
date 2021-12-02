Dataclass Mechanism
===================


Input
-----
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class ShoppingCartItem:
...     name: str
...     unit_price: float
...     quantity: int = 0
...
...     def total_cost(self) -> float:
...         return self.unit_price * self.quantity


Output
------
>>> class ShoppingCartItem:
...     name: str
...     unit_price: float
...     quantity: int
...
...     def total_cost(self) -> float:
...         return self.unit_price * self.quantity
...
...     ## All code below is added by dataclass
...
...     def __init__(self, name: str, unit_price: float,
...                  quantity: int = 0) -> None:
...         self.name = name
...         self.unit_price = unit_price
...         self.quantity = quantity
...
...     def __repr__(self):
...         return f'ShoppingCartItem(name={self.name!r}, ' \
...                f'unit_price={self.unit_price!r}, ' \
...                f'quantity={self.quantity!r})'
...
...     def __eq__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 == (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __ne__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 != (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __lt__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                  < (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __le__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 <= (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __gt__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                  > (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __ge__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 >= (other.name, other.unit_price, other.quantity)
...         return NotImplemented


Use Case - 0x01
---------------
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

