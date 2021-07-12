Dataclass Inheritance
=====================


Rationale
---------
* Dataclasses can inherit from other classes
* Superclass not necessarily has to be dataclass
* If parent is dataclass the init will be joined
  (all parameters from parent and child will be set)


Inheritance
-----------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Person:
...     name: str
...     job: str = None
>>>
>>>
>>> @dataclass
... class Astronaut(Person):
...     job: str = 'Astronaut'
...     agency: str = 'NASA'
>>>
>>>

Will generate ``def __init__(self, name: str, job: str = 'Astronaut', agency: str = 'NASA')``


Post Init Inheritance
---------------------
