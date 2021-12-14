JSON Decoder
============


Problem
-------
* Problem with ``date``, ``datetime``, ``time``, ``timedelta``
* Python does not decode values automatically

>>> from datetime import date
>>> import json
>>>
>>>
>>> DATA = """
...     {"firstname": "Mark",
...      "lastname": "Watney",
...      "born": "1994-10-12"}"""
>>>
>>>
>>> result = json.loads(DATA)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'born': '1994-10-12'}


Function Decoder
----------------
>>> from datetime import date
>>> import json
>>>
>>>
>>> DATA = """
...     {"firstname": "Mark",
...      "lastname": "Watney",
...      "born": "1994-10-12"}"""
>>>
>>>
>>> def decoder(data: dict) -> dict:
...     for field, value in data.items():
...         if field == 'born':
...             data[field] = date.fromisoformat(value)
...     return data
>>>
>>>
>>> result = json.loads(DATA, object_hook=decoder)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'born': datetime.date(1994, 10, 12)}


Context Dependency Injection
----------------------------
>>> from datetime import date
>>> import json
>>>
>>>
>>> DATA = """
...     {"firstname": "Mark",
...      "lastname": "Watney",
...      "born": "1994-10-12"}"""
>>>
>>>
>>> class Decoder(json.JSONDecoder):
...     def __init__(self):
...         super().__init__(object_hook=self.default)
...
...     def default(self, data: dict) -> dict:
...         for field, value in data.items():
...             if field == 'born':
...                 data[field] = date.fromisoformat(value)
...         return data
>>>
>>>
>>> result = json.loads(DATA, cls=Decoder)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'born': datetime.date(1994, 10, 12)}


Use Case - 0x01
---------------
>>> from datetime import datetime, date, time, timedelta
>>> import json
>>>
>>>
>>> DATA = """
...     {"name": "Mark Watney",
...      "born": "1994-10-12",
...      "launch": "1969-07-21T02:56:15",
...      "landing": "12:30:00",
...      "duration": 13}"""
>>>
>>>
>>> class MyDecoder(json.JSONDecoder):
...     def __init__(self):
...         super().__init__(object_hook=lambda data: {
...                 field: self.default(field, value)
...                 for field, value in data.items()})
...
...     def default(self, field, value):
...         result = {
...             'born': lambda x: date.fromisoformat(x),
...             'launch': lambda x: datetime.fromisoformat(x),
...             'landing': lambda x: time.fromisoformat(x),
...             'duration': lambda x: timedelta(days=x),
...         }.get(field, value)
...         return result(value) if callable(result) else result
>>>
>>>
>>> result = json.loads(DATA, cls=MyDecoder)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'name': 'Mark Watney',
 'born': datetime.date(1994, 10, 12),
 'launch': datetime.datetime(1969, 7, 21, 2, 56, 15),
 'landing': datetime.time(12, 30),
 'duration': datetime.timedelta(days=13)}


Use Case - 0x02
---------------
>>> from datetime import date, time, datetime, timedelta
>>> import json
>>>
>>>
>>> DATA = """
...     {"name": "Mark Watney",
...      "born": "1994-10-12",
...      "launch": "1969-07-21T02:56:15",
...      "landing": "12:30:00",
...      "duration": 13}"""
>>>
>>> class MyDecoder(json.JSONDecoder):
...      name: str
...      born: date
...      launch: datetime
...      landing: time
...      duration: timedelta
...
...      def __init__(self) -> None:
...          super().__init__(object_hook=lambda data: {
...                  field: getattr(self, method)(value)
...                  for field, value in data.items()
...                  if (method := self.__annotations__.get(field, str).__name__)})
...
...      def datetime(self, value: str) -> date:
...          return datetime.fromisoformat(value)
...
...      def date(self, value: str) -> date:
...          return date.fromisoformat(value)
...
...      def time(self, value: str) -> date:
...          return time.fromisoformat(value)
...
...      def timedelta(self, value: str) -> date:
...          return timedelta(days=value)
...
...      def str(self, value: str) -> str:
...          return str(value)
>>>
>>>
>>> result = json.loads(DATA, cls=MyDecoder)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'name': 'Mark Watney',
 'born': datetime.date(1994, 10, 12),
 'launch': datetime.datetime(1969, 7, 21, 2, 56, 15),
 'landing': datetime.time(12, 30),
 'duration': datetime.timedelta(days=13)}


Use Case - 0x03
---------------
>>> import json
>>> from dataclasses import dataclass, field
>>> from pprint import pprint
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
...     lastname: str
...     firstname: str
...     missions: list[Mission] = field(default_factory=list)
>>>
>>>
>>> CREW = [
...     Astronaut('Mark', 'Watney', missions=[
...         Mission(1973, 'Apollo18'),
...         Mission(2035, 'Ares3'),
...     ]),
...
...     Astronaut('Melissa', 'Lewis', missions=[
...         Mission(2035, 'Ares3'),
...     ]),
...
...     Astronaut('Rick', 'Martinez'),
... ]
>>>
>>>
>>> class MyEncoder(json.JSONEncoder):
...     def default(self, obj):
...         data = vars(obj)
...         data['__clsname__'] = obj.__class__.__name__
...         return data
>>>
>>>
>>> class MyDecoder(json.JSONDecoder):
...     def __init__(self):
...         super().__init__(object_hook=self.default)
...
...     def default(self, data: dict) -> dict:
...         clsname = data.pop('__clsname__')
...         cls = globals()[clsname]
...         return cls(**data)

>>> result = json.dumps(CREW, cls=MyEncoder)
>>>
>>> pprint(result, width=72)
('[{"lastname": "Mark", "firstname": "Watney", "missions": [{"year": '
 '1973, "name": "Apollo18", "__clsname__": "Mission"}, {"year": 2035, '
 '"name": "Ares3", "__clsname__": "Mission"}], "__clsname__": '
 '"Astronaut"}, {"lastname": "Melissa", "firstname": "Lewis", '
 '"missions": [{"year": 2035, "name": "Ares3", "__clsname__": '
 '"Mission"}], "__clsname__": "Astronaut"}, {"lastname": "Rick", '
 '"firstname": "Martinez", "missions": [], "__clsname__": '
 '"Astronaut"}]')

>>> result = json.loads(result, cls=MyDecoder)
>>>
>>> pprint(result)  # doctest: +NORMALIZE_WHITESPACE
[Astronaut(lastname='Mark',
           firstname='Watney',
           missions=[Mission(year=1973, name='Apollo18'),
                     Mission(year=2035, name='Ares3')]),
 Astronaut(lastname='Melissa',
           firstname='Lewis',
           missions=[Mission(year=2035, name='Ares3')]),
 Astronaut(lastname='Rick', firstname='Martinez', missions=[])]


Assignments
-----------
.. literalinclude:: assignments/json_decoder_a.py
    :caption: :download:`Solution <assignments/json_decoder_a.py>`
    :end-before: # Solution
