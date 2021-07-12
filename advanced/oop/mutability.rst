OOP Mutability
==============


Rationale
---------
* Function and method arguments should not be mutable


Immutable Types
---------------
* ``int``
* ``float``
* ``complex``
* ``bool``
* ``None``
* ``str``
* ``bytes``
* ``tuple``
* ``frozenset``
* ``mappingproxy``


Mutable Types
-------------
* ``list``
* ``set``
* ``dict``


Argument Mutability
-------------------
Note, You should not set mutable objects as a default function argument.
More information in `Argument Mutability`. This is how all dynamically typed
languages work (including PHP, Ruby, Perl etc).

>>> class Astronaut:
...     def __init__(self, name, missions=[]):
...         self.name = name
...         self.missions = missions
>>>
>>>
>>> watney = Astronaut('Mark Watney')
>>> lewis = Astronaut('Melissa Lewis')
>>>
>>> watney.missions.append('Ares 1')
>>> watney.missions.append('Ares 2')
>>> watney.missions.append('Ares 3')
>>>
>>> print(f'Name: {watney.name}, Missions: {watney.missions}')
Name: Mark Watney, Missions: ['Ares 1', 'Ares 2', 'Ares 3']
>>>
>>> print(f'Name: {lewis.name}, Missions: {lewis.missions}')
Name: Melissa Lewis, Missions: ['Ares 1', 'Ares 2', 'Ares 3']

>>> class Astronaut:
...     def __init__(self, name, missions=None):
...         self.name = name
...         self.missions = missions if missions else []
>>>
>>>
>>> watney = Astronaut('Mark Watney')
>>> lewis = Astronaut('Melissa Lewis')
>>>
>>> watney.missions.append('Ares 1')
>>> watney.missions.append('Ares 2')
>>> watney.missions.append('Ares 3')
>>>
>>> print(f'Name: {watney.name}, Missions: {watney.missions}')
Name: Mark Watney, Missions: ['Ares 1', 'Ares 2', 'Ares 3']
>>>
>>> print(f'Name: {lewis.name}, Missions: {lewis.missions}')
Name: Melissa Lewis, Missions: []


Assignments
-----------
.. todo:: Create assignments
