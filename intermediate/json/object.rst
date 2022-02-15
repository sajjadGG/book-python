JSON Object
===========


Encode Simple Object
--------------------
>>> from dataclasses import dataclass
>>> import json
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     role: str
>>>
>>>
>>> DATA = Astronaut('Mark', 'Watney', 'Botanist')
>>>
>>> result = json.dumps(vars(DATA))
>>>
>>> print(result)
{"firstname": "Mark", "lastname": "Watney", "role": "Botanist"}


Decode Simple Object
--------------------
>>> from dataclasses import dataclass
>>> import json
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     role: str
>>>
>>> DATA = '{"firstname": "Mark", "lastname": "Watney", "role": "Botanist"}'
>>>
>>> data = json.loads(DATA)
>>> result = Astronaut(**data)
>>>
>>> print(result)
Astronaut(firstname='Mark', lastname='Watney', role='Botanist')


Encode Object with Relation
---------------------------
>>> from dataclasses import dataclass
>>> import json
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
>>> class MyEncoder(json.JSONEncoder):
...     def default(self, obj):
...         result = vars(obj)
...         result['__type__'] = obj.__class__.__name__
...         return result
>>>
>>>
>>> result = json.dumps(CREW, cls=MyEncoder)
>>>
>>> print(result)
[{"firstname": "Mark", "lastname": "Watney", "role": "Botanist", "missions": [{"year": 2035, "name": "Ares 3", "__type__": "Mission"}], "__type__": "Astronaut"}, {"firstname": "Melissa", "lastname": "Lewis", "role": "Commander", "missions": [{"year": 2035, "name": "Ares 3", "__type__": "Mission"}, {"year": 2031, "name": "Ares 1", "__type__": "Mission"}], "__type__": "Astronaut"}, {"firstname": "Rick", "lastname": "Martinez", "role": "Pilot", "missions": [], "__type__": "Astronaut"}]


Decode
------
 Encoding nested objects with relations to JSON:

>>> from dataclasses import dataclass
>>> import json
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
...     role: str
...     missions: list[Mission]
>>>
>>>
>>> DATA = """[{"firstname": "Mark", "lastname": "Watney", "role": "Botanist", "missions": [{"year": 2035, "name": "Ares 3", "__type__": "Mission"}], "__type__": "Astronaut"}, {"firstname": "Melissa", "lastname": "Lewis", "role": "Commander", "missions": [{"year": 2035, "name": "Ares 3", "__type__": "Mission"}, {"year": 2031, "name": "Ares 1", "__type__": "Mission"}], "__type__": "Astronaut"}, {"firstname": "Rick", "lastname": "Martinez", "role": "Pilot", "missions": [], "__type__": "Astronaut"}]"""
>>>
>>>
>>> class MyDecoder(json.JSONDecoder):
...     def __init__(self):
...         super().__init__(object_hook=self.default)
...
...     def default(self, obj):
...         clsname = obj.pop('__type__')
...         cls = globals()[clsname]
...         return cls(**obj)
>>>
>>>
>>> result = json.loads(DATA, cls=MyDecoder)
>>>
>>> print(result)
[Astronaut(firstname='Mark', lastname='Watney', role='Botanist', missions=[Mission(year=2035, name='Ares 3')]), Astronaut(firstname='Melissa', lastname='Lewis', role='Commander', missions=[Mission(year=2035, name='Ares 3'), Mission(year=2031, name='Ares 1')]), Astronaut(firstname='Rick', lastname='Martinez', role='Pilot', missions=[])]


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
