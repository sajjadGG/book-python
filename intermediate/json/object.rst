JSON Object
===========

SetUp
-----
>>> from pprint import pprint
>>> from dataclasses import dataclass
>>> import json


Encode Object
-------------
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     role: str
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', 'Botanist')
>>> data = vars(mark)
>>>
>>> json.dumps(data)
'{"firstname": "Mark", "lastname": "Watney"}'


Decode Object
-------------
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> DATA = """{
...   "firstname": "Mark",
...   "lastname": "Watney"
... }"""
>>>
>>> data = json.loads(DATA)
>>> result = Astronaut(**data)
>>>
>>> print(result)
Astronaut(firstname='Mark', lastname='Watney')


Object Encoder
--------------
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> data = Astronaut('Mark', 'Watney')
>>>
>>>
>>> def encoder(obj):
...     return vars(obj)
>>>
>>>
>>> json.dumps(data, default=encoder)
'{"firstname": "Mark", "lastname": "Watney"}'


Object Decoder
--------------
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> DATA = """{
...   "firstname": "Mark",
...   "lastname": "Watney"
... }"""
>>>
>>>
>>> def decoder(data):
...     return Astronaut(**data)
>>>
>>>
>>> json.loads(DATA, object_hook=decoder)
Astronaut(firstname='Mark', lastname='Watney')


Encode Object with Relation
---------------------------
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
...     role: str
...     missions: list[Mission]
>>>
>>>
>>> CREW = [
...     Astronaut('Mark', 'Watney', 'Botanist', missions=[
...         Mission(2035, 'Ares 3')]),
...     Astronaut('Melissa', 'Lewis', 'Commander', missions=[
...         Mission(2035, 'Ares 3'),
...         Mission(2031, 'Ares 1')]),
...     Astronaut('Rick', 'Martinez', 'Pilot', missions=[])]
>>>
>>>
>>> def encoder(obj):
...     data = {'_type': obj.__class__.__name__}
...     return data | vars(obj)
>>>
>>>
>>> result = json.dumps(CREW, default=encoder, indent=2)
>>>
>>> print(result)
[
  {
    "_type": "Astronaut",
    "firstname": "Mark",
    "lastname": "Watney",
    "role": "Botanist",
    "missions": [
      {
        "_type": "Mission",
        "year": 2035,
        "name": "Ares 3"
      }
    ]
  },
  {
    "_type": "Astronaut",
    "firstname": "Melissa",
    "lastname": "Lewis",
    "role": "Commander",
    "missions": [
      {
        "_type": "Mission",
        "year": 2035,
        "name": "Ares 3"
      },
      {
        "_type": "Mission",
        "year": 2031,
        "name": "Ares 1"
      }
    ]
  },
  {
    "_type": "Astronaut",
    "firstname": "Rick",
    "lastname": "Martinez",
    "role": "Pilot",
    "missions": []
  }
]


Decode
------
Encoding nested objects with relations to JSON:

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
...     role: str
...     missions: list[Mission]
>>>
>>>
>>> DATA = """[{"_type": "Astronaut", "firstname": "Mark", "lastname": "Watney", "role": "Botanist", "missions": [{"_type": "Mission", "year": 2035, "name": "Ares 3"}]}, {"_type": "Astronaut", "firstname": "Melissa", "lastname": "Lewis", "role": "Commander", "missions": [{"_type": "Mission", "year": 2035, "name": "Ares 3"}, {"_type": "Mission", "year": 2031, "name": "Ares 1"}]}, {"_type": "Astronaut", "firstname": "Rick", "lastname": "Martinez", "role": "Pilot", "missions": []}]"""
>>>
>>>
>>> def decoder(obj):
...     clsname = obj.pop('_type')
...     cls = globals()[clsname]
...     return cls(**obj)
>>>
>>>
>>> result = json.loads(DATA, object_hook=decoder)
>>>
>>> pprint(result, width=72)
[Astronaut(firstname='Mark',
           lastname='Watney',
           role='Botanist',
           missions=[Mission(year=2035, name='Ares 3')]),
 Astronaut(firstname='Melissa',
           lastname='Lewis',
           role='Commander',
           missions=[Mission(year=2035, name='Ares 3'),
                     Mission(year=2031, name='Ares 1')]),
 Astronaut(firstname='Rick',
           lastname='Martinez',
           role='Pilot',
           missions=[])]


Use Case - 0x01
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
.. literalinclude:: assignments/json_object_a.py
    :caption: :download:`Solution <assignments/json_object_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_object_b.py
    :caption: :download:`Solution <assignments/json_object_b.py>`
    :end-before: # Solution
