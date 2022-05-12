Dataclass Metadata
==================
* ``metadata`` - For storing extra information about field
* ``dict | None``
* ``None`` is treated as an empty ``dict``
* Metadata is not used at all by Data Classes
* Metadata is provided as a third-party extension mechanism
* Use Case: SQLAlchemy https://python.astrotech.io/database/sqlalchemy/model-dataclass.html

.. code-block:: text

    def field(*,
              default: Any,
              default_factory: Callable,
              init: bool = True,
              repr: bool = True,
              hash: bool|None = None,
              compare: bool = True,
              metadata: dict = None) -> None


Syntax
------
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int = field(metadata={'min': 27, 'max': 50})
...     agency: str = field(metadata={'choices': ['NASA', 'ESA']})
...     height: float = field(metadata={'unit': 'cm'})
...     weight: float = field(metadata={'unit': 'kg'})


Validation
----------
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int = field(default=None, metadata={'min': 27, 'max': 50})
...
...     def __post_init__(self):
...         AGE_MIN = self.__dataclass_fields__['age'].metadata['min']
...         AGE_MAX = self.__dataclass_fields__['age'].metadata['max']
...
...         if self.age not in range(AGE_MIN, AGE_MAX):
...             raise ValueError('Invalid age')
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney', age=99)
Traceback (most recent call last):
ValueError: Invalid age


Use Case - 0x01
---------------
* Validation

>>> from dataclasses import dataclass, field, KW_ONLY
>>> from datetime import date, time, datetime, timezone, timedelta
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>>
>>> @dataclass(frozen=True)
... class Astronaut:
...     firstname: str
...     lastname: str
...     _: KW_ONLY
...     born: date
...     job: str = 'astronaut'
...     agency: str = field(default='NASA', metadata={'choices': ['NASA', 'ESA']})
...     age: int | None = None
...     height: int | float | None = field(default=None, metadata={'unit': 'cm', 'min': 156, 'max': 210})
...     weight: int | float | None = field(default=None, metadata={'unit': 'kg', 'min': 50, 'max': 90})
...     groups: list[str] = field(default_factory=lambda: ['astronauts', 'managers'])
...     friends: dict[str,str] = field(default_factory=dict)
...     assignments: list[str] | None = field(default=None, metadata={'choices': ['Apollo18', 'Ares3', 'STS-136']})
...     missions: list[Mission] = field(default_factory=list)
...     experience: timedelta = timedelta(hours=0)
...     account_last_login: datetime | None = None
...     account_created: datetime = datetime.now(tz=timezone.utc)
...     AGE_MIN: int = field(default=30, init=False, repr=False)
...     AGE_MAX: int = field(default=50, init=False, repr=False)
...
...     def __post_init__(self):
...         HEIGHT_MIN = self.__dataclass_fields__['height'].metadata['min']
...         HEIGHT_MAX = self.__dataclass_fields__['height'].metadata['max']
...         WEIGHT_MIN = self.__dataclass_fields__['weight'].metadata['min']
...         WEIGHT_MAX = self.__dataclass_fields__['weight'].metadata['max']
...         if not HEIGHT_MIN <= self.height < HEIGHT_MAX:
...             raise ValueError(f'Height {self.height} is not in between {HEIGHT_MIN} and {HEIGHT_MAX}')
...         if not WEIGHT_MIN <= self.weight < WEIGHT_MAX:
...             raise ValueError(f'Height {self.weight} is not in between {WEIGHT_MIN} and {WEIGHT_MAX}')
...         if self.age not in range(self.AGE_MIN, self.AGE_MAX):
...             raise ValueError('Age is not valid for an astronaut')
>>>
>>>
>>> mark = Astronaut(firstname='Mark',
...                   lastname='Watney',
...                   born=date(1961, 4, 12),
...                   age=44,
...                   height=175.5,
...                   weight=75.5,
...                   assignments=['STS-136'],
...                   missions=[Mission(2035, 'Ares 3'), Mission(1973, 'Apollo 18')])
>>>
>>> print(mark)  # doctest: +NORMALIZE_WHITESPACE +SKIP
Astronaut(firstname='Mark', lastname='Watney', born=datetime.date(1961, 4, 12),
          job='astronaut', agency='NASA', age=44, height=175.5, weight=75.5,
          groups=['astronauts', 'managers'], friends={}, assignments=['STS-136'],
          missions=[Mission(year=2035, name='Ares 3'), Mission(year=1973, name='Apollo 18')],
          experience=datetime.timedelta(0), account_last_login=None,
          account_created=datetime.datetime(1969, 7, 21, 2, 56, 15, 123456, tzinfo=datetime.timezone.utc))


Use Case - 0x02
---------------
* Setattr

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: float = field(default=None, metadata={'unit': 'years', 'min': 30, 'max': 50})
...     height: float = field(default=None, metadata={'unit': 'cm', 'min': 156, 'max': 210})
...     weight: float = field(default=None, metadata={'unit': 'kg', 'min': 50, 'max': 90})
...
...     def __setattr__(self, attrname, attrvalue):
...         if attrvalue is None:
...             return super().__setattr__(attrname, attrvalue)
...         try:
...             min = Astronaut.__dataclass_fields__[attrname].metadata['min']
...             max = Astronaut.__dataclass_fields__[attrname].metadata['max']
...         except KeyError:
...             # field does not have min and max metadata
...             pass
...         else:
...             assert min <= attrvalue < max, f'{attrname} value {attrvalue} is not between {min} and {max}'
...         finally:
...             super().__setattr__(attrname, attrvalue)
>>>
>>>
>>>
>>> Astronaut('Mark', 'Watney')
Astronaut(firstname='Mark', lastname='Watney', age=None, height=None, weight=None)
>>>
>>> Astronaut('Mark', 'Watney', age=44)
Astronaut(firstname='Mark', lastname='Watney', age=44, height=None, weight=None)
>>>
>>> Astronaut('Mark', 'Watney', age=44, height=175, weight=75)
Astronaut(firstname='Mark', lastname='Watney', age=44, height=175, weight=75)
>>>
>>> Astronaut('Mark', 'Watney', age=99)
Traceback (most recent call last):
AssertionError: age value 99 is not between 30 and 50
>>>
>>> Astronaut('Mark', 'Watney', age=44, weight=200)
Traceback (most recent call last):
AssertionError: weight value 200 is not between 50 and 90
>>>
>>> Astronaut('Mark', 'Watney', age=44, height=120)
Traceback (most recent call last):
AssertionError: height value 120 is not between 156 and 210


Use Case - 0x03
---------------
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int = field(default=None, metadata={'type': 'range', 'unit': 'years', 'min': 30, 'max': 50})
...     height: float | None = field(default=None, metadata={'type': 'range', 'unit': 'cm',  'min': 156, 'max': 210})
...     agency: str | None = field(default='NASA', metadata={'type': 'choices', 'options': ['NASA', 'ESA']})
...
...     def _validate_range(self, attrname, value):
...         min = self.__dataclass_fields__[attrname].metadata['min']
...         max = self.__dataclass_fields__[attrname].metadata['max']
...         if value and not min <= value <= max:
...             raise ValueError(f'Attribute {attrname} is not between {min} and {max}')
...
...     def _validate_choices(self, attrname, value):
...         options = self.__dataclass_fields__[attrname].metadata['options']
...         if options and value not in options:
...             raise ValueError(f'Attribute {attrname} is not an option, choices are: {options}')
...
...     def __setattr__(self, attrname, value):
...         try:
...             attrtype = self.__dataclass_fields__[attrname].metadata['type']
...         except KeyError:
...             return super().__setattr__(attrname, value)
...         match attrtype:
...             case 'range':   self._validate_range(attrname, value)
...             case 'choices': self._validate_choices(attrname, value)
...             case _: raise NotImplementedError
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>>
>>> mark
Astronaut(firstname='Mark', lastname='Watney', age=35, height=None, agency='NASA')
>>>
>>> mark.agency = 'ESA'
>>> mark.agency = 'Roscosmos'
ValueError: Attribute agency is not an option, choices are: ['NASA', 'ESA']
>>>
>>> mark.age = 40
>>> mark.age = 10
ValueError: Attribute age is not between 30 and 50


Use Case - 0x04
---------------
>>> # doctest: +SKIP
... from __future__ import annotations
... from dataclasses import dataclass, field
... from sqlalchemy import Column, ForeignKey, Integer, String
... from sqlalchemy.orm import registry, relationship
...
... mapper_registry = registry()
...
...
... @mapper_registry.mapped
... @dataclass
... class User:
...     __tablename__ = "user"
...     __sa_dataclass_metadata_key__ = "db"
...
...     id: int = field(init=False, metadata={"db": Column(Integer, primary_key=True)})
...     name: str = field(default=None, metadata={"db": Column(String(50))})
...     fullname: str = field(default=None, metadata={"db": Column(String(50))})
...     nickname: str = field(default=None, metadata={"db": Column(String(12))})
...     addresses: list[Address] = field(default_factory=list, metadata={"db": relationship("Address")})
...
...
... @mapper_registry.mapped
... @dataclass
... class Address:
...     __tablename__ = "address"
...     __sa_dataclass_metadata_key__ = "db"
...
...     id: int = field(init=False, metadata={"db": Column(Integer, primary_key=True)})
...     user_id: int = field(init=False, metadata={"db": Column(ForeignKey("user.id"))})
...     email_address: str = field(default=None, metadata={"db": Column(String(50))})


Assignments
-----------
.. literalinclude:: assignments/dataclass_field_a.py
    :caption: :download:`Solution <assignments/dataclass_field_a.py>`
    :end-before: # Solution
