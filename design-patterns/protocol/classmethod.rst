Protocol Classmethod
====================


Rationale
---------
* Using class as namespace
* Will pass class as a first argument
* ``self`` is not required

>>> class MyClass:
...     def mymethod(self):
...         pass

>>> class MyClass:
...     @staticmethod
...     def mymethod():
...         pass

>>> class MyClass:
...     @classmethod
...     def mymethod(cls):
...         pass


Example
-------
>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...
...     def from_json(self, data):
...         data = json.loads(data)
...         return User(**data)
>>>
>>>
>>> DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>>
>>> User.from_json(DATA)
Traceback (most recent call last):
TypeError: from_json() missing 1 required positional argument: 'data'
>>>
>>> User().from_json(DATA)
Traceback (most recent call last):
TypeError: __init__() missing 2 required positional arguments: 'firstname' and 'lastname'
>>>
>>> User(None, None).from_json(DATA)
User(firstname='Jan', lastname='Twardowski')

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...
...     @staticmethod
...     def from_json(data):
...         data = json.loads(data)
...         return User(**data)
>>>
>>>
>>> DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>>
>>> User.from_json(DATA)
User(firstname='Jan', lastname='Twardowski')

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     @staticmethod
...     def from_json(data):
...         data = json.loads(data)
...         return User(**data)
>>>
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>>
>>> DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>>
>>> print(User.from_json(DATA))
User(firstname='Jan', lastname='Twardowski')

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     def from_json(self, data):
...         data = json.loads(data)
...         return User(**data)
>>>
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str = None
...     lastname: str = None
>>>
>>>
>>> DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>>
>>> User.from_json(DATA)
Traceback (most recent call last):
TypeError: from_json() missing 1 required positional argument: 'data'
>>>
>>> User().from_json(DATA)
User(firstname='Jan', lastname='Twardowski')

Trying to use method with ``self``:

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     def from_json(self, data):
...         data = json.loads(data)
...         return self(**data)
>>>
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str = None
...     lastname: str = None
>>>
>>>
>>> DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>>
>>> User.from_json(DATA)
Traceback (most recent call last):
TypeError: from_json() missing 1 required positional argument: 'data'
>>>
>>> User().from_json(DATA)
Traceback (most recent call last):
TypeError: 'User' object is not callable

Trying to use method with ``self.__init__()``:

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     def from_json(self, data):
...         data = json.loads(data)
...         self.__init__(**data)
...         return self
>>>
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str = None
...     lastname: str = None
>>>
>>>
>>> DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>>
>>> User.from_json(DATA)
Traceback (most recent call last):
TypeError: from_json() missing 1 required positional argument: 'data'
>>>
>>> User().from_json(DATA)
User(firstname='Jan', lastname='Twardowski')

Trying to use methods ``self.__new__()`` and ``self.__init__()``:

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     def from_json(self, data):
...         data = json.loads(data)
...         instance = object.__new__(type(self))
...         instance.__init__(**data)
...         return instance
>>>
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str = None
...     lastname: str = None
>>>
>>>
>>> DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>>
>>> User.from_json(DATA)
Traceback (most recent call last):
TypeError: from_json() missing 1 required positional argument: 'data'
>>>
>>> User().from_json(DATA)
User(firstname='Jan', lastname='Twardowski')

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     @classmethod
...     def from_json(cls, data):
...         data = json.loads(data)
...         return cls(**data)
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>>
>>> DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>>
>>> User.from_json(DATA)
User(firstname='Jan', lastname='Twardowski')


Use Cases
---------
>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     @classmethod
...     def from_json(cls, data):
...         data = json.loads(data)
...         return cls(**data)
>>>
>>> @dataclass
... class Guest(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>> @dataclass
... class Admin(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>>
>>> DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>>
>>> Guest.from_json(DATA)
Guest(firstname='Jan', lastname='Twardowski')
>>>
>>> Admin.from_json(DATA)
Admin(firstname='Jan', lastname='Twardowski')

>>> class AbstractTime:
...     tzname: str
...     tzcode: str
...
...     def __init__(self, date, time):
...         ...
...
...     @classmethod
...     def parse(cls, text):
...         result = {'date': ..., 'time': ...}
...         return cls(**result)
>>>
>>> class MartianTime(AbstractTime):
...     tzname = 'Coordinated Mars Time'
...     tzcode = 'MTC'
>>>
>>> class LunarTime(AbstractTime):
...     tzname = 'Lunar Standard Time'
...     tzcode = 'LST'
>>>
>>> class EarthTime(AbstractTime):
...     tzname = 'Universal Time Coordinated'
...     tzcode = 'UTC'
>>>
>>>
>>> # Settings
>>> time = MartianTime
>>>
>>> # Usage
>>> from settings import time  # doctest: +SKIP
>>>
>>> UTC = '1969-07-21T02:53:07Z'
>>>
>>> dt = time.parse(UTC)
>>> print(dt.tzname)
Coordinated Mars Time


Assignments
-----------
.. literalinclude:: assignments/protocol_classmethod_a.py
    :caption: :download:`Solution <assignments/protocol_classmethod_a.py>`
    :end-before: # Solution
