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
              default_factory: Any,
              init: Any = True,
              repr: Any = True,
              hash: Any = None,
              compare: Any = True,
              metadata: Any = None) -> None


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
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: int = field(metadata={'min': 30, 'max': 50})
...
...     def _validate_range(self, field):
...         value = getattr(self, field)
...         MIN = self.__dataclass_fields__[field].metadata['min']
...         MAX = self.__dataclass_fields__[field].metadata['max']
...         if value not in range(MIN, MAX):
...             raise ValueError(f'Field {field} with value={value} is not in range from {MIN} to {MAX}')
...
...     def __post_init__(self):
...         self._validate_range('age')
>>>
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney', age=60)
Traceback (most recent call last):
ValueError: Field age with value=60 is not in range from 30 to 50
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney', age=40)
Astronaut(firstname='Mark', lastname='Watney', age=40)


Use Case - 0x02
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
>>> astro = Astronaut(firstname='Mark',
...                   lastname='Watney',
...                   born=date(1961, 4, 12),
...                   age=44,
...                   height=175.5,
...                   weight=75.5,
...                   assignments=['STS-136'],
...                   missions=[Mission(2035, 'Ares 3'), Mission(1973, 'Apollo 18')])
>>>
>>> print(astro)  # doctest: +NORMALIZE_WHITESPACE +SKIP
Astronaut(firstname='Mark', lastname='Watney', born=datetime.date(1961, 4, 12),
          job='astronaut', agency='NASA', age=44, height=175.5, weight=75.5,
          groups=['astronauts', 'managers'], friends={}, assignments=['STS-136'],
          missions=[Mission(year=2035, name='Ares 3'), Mission(year=1973, name='Apollo 18')],
          experience=datetime.timedelta(0), account_last_login=None,
          account_created=datetime.datetime(1969, 7, 21, 2, 56, 15, 123456, tzinfo=datetime.timezone.utc))


Use Case - 0x03
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


Use Case - 0x04
---------------
>>> from dataclasses import dataclass, field
>>> from datetime import date
>>> from typing import Literal
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>>
>>> # doctest: +SKIP
... @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: Literal['NASA', 'ESA', 'POLSA'] = field(metadata={'choices': ['NASA', 'ESA', 'POLSA']})
...     age: int = field(metadata={'min': 30, 'max': 50})
...     height: int | float = field(metadata={'unit': 'cm'})
...     weight: int | float = field(metadata={'unit': 'kg'})
...     born: date | None
...     friends: list['Astronaut'] | None = None
...     missions: list[Mission] | None = None
...     medals: list[str] | None = None
...
...     def _validate_age(self, age):
...         AGE_MIN = self.__dataclass_fields__['age'].metadata['min']
...         AGE_MAX = self.__dataclass_fields__['age'].metadata['max']
...         if not AGE_MIN <= age < AGE_MAX:
...             raise ValueError(f'Invalid age, must be between {AGE_MIN} and {AGE_MAX}')
...
...     def _validate_agency(self, agency):
...         AGENCY_CHOICES = self.__dataclass_fields__['agency'].metadata['choices']
...         if agency not in AGENCY_CHOICES:
...             raise ValueError(f'Invalid agency, must be one of {AGENCY_CHOICES}')
...
...     def __setattr__(self, attrname, attrvalue):
...         match attrname:
...             case 'age':    self._validate_age(attrvalue)
...             case 'agency': self._validate_agency(attrvalue)
...         return super().__setattr__(attrname, attrvalue)
>>>
>>>
>>> # doctest: +SKIP
... mark = Astronaut(
...         firstname='Mark',
...         lastname='Watney',
...         agency='NASA',
...         age=35,
...         height=185.5,
...         weight=75.5,
...         born=date(1969, 7, 21),
...         missions=[Mission(1973, 'Apollo 18'),
...                   Mission(2012, 'STS-136'),
...                   Mission(2035, 'Ares 3')],
... )
>>>
>>> mark.age = 10  # doctest: +SKIP
Traceback (most recent call last):
ValueError: Invalid age, must be between 30 and 50
>>>
>>> mark.agency = 'CNSA'  # doctest: +SKIP
Traceback (most recent call last):
ValueError: Invalid agency, must be one of ['NASA', 'ESA', 'POLSA']


Use Case - 0x05
---------------
>>> from dataclasses import KW_ONLY, dataclass, field
>>> from typing import Literal
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     _: KW_ONLY
...     age: int | float | None = field(default=None, metadata={'unit': 'years', 'min': 30, 'max': 50})
...     weight: int | float | None = field(default=None, metadata={'unit': 'kg'})
...     height: int | float | None = field(default=None, metadata={'unit': 'cm'})
...     agency: Literal['NASA','ESA','POLSA'] | None = field(default=None, metadata={'choices': ['NASA','ESA','POLSA']})
...
...     def _validate_age(self):
...         metadata = self.__dataclass_fields__['age'].metadata
...         if not metadata['min'] <= self.age < metadata['max']:
...             raise ValueError(f'Age "{self.age}" is invalid, '
...                              f'should be between {metadata["min"]} and {metadata["max"]}')
...
...     def _validate_agency(self):
...         metadata = self.__dataclass_fields__['agency'].metadata
...         if self.agency not in metadata['choices']:
...             raise ValueError(f'Agency "{self.agency}" is invalid, '
...                              f'should be one of: {metadata["choices"]}')
...
...     def __post_init__(self):
...         self._validate_age()
...         self._validate_agency()



Assignments
-----------
.. literalinclude:: assignments/dataclass_field_a.py
    :caption: :download:`Solution <assignments/dataclass_field_a.py>`
    :end-before: # Solution
