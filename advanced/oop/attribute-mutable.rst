OOP Attribute Mutable/Immutable
===============================


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


Problem
-------
Let's define a class:

>>> class Astronaut:
...     def __init__(self, name, missions=[]):
...         self.name = name
...         self.missions = missions

Now, we create an instance of a class:

>>> watney = Astronaut('Mark Watney')
>>> lewis = Astronaut('Melissa Lewis')

Check missions for both Astronauts:

>>> watney.missions
[]
>>>
>>> lewis.missions
[]

We will send Mark Watney to three missions: Ares1, Ares2, Ares3:

>>> watney.missions.append('Ares1')
>>> watney.missions.append('Ares2')
>>> watney.missions.append('Ares3')

Now, check the missions once again:

>>> watney.missions
['Ares1', 'Ares2', 'Ares3']
>>>
>>> lewis.missions
['Ares1', 'Ares2', 'Ares3']

This is not a mistake. Both astronauts Mark and Melissa has the same missions
despite the fact, that we set values only for Mark! This is because both
both Mark and Melissa has attribute missions pointing to the same memory
address:

>>> watney.missions == lewis.missions
True
>>>
>>> watney.missions is lewis.missions
True


Why?
----
Note, You should not set mutable objects as a default function argument.
More information in `Argument Mutability`. This is how all dynamically typed
languages work (including PHP, Ruby, Perl etc).

The problem lays in ``__init__()`` method signature. It consist a reference
to the mutable object: ``list``. Python will create a new ``list`` instance
on class creation, not an instance creation. Therefore each astronaut will
reference to the same ``list`` which was created when Python interpreted class.

>>> class Astronaut:
...     def __init__(self, name, missions=[]):
...         self.name = name
...         self.missions = missions

However method body is not interpreted on class creation. This is done in a
runtime. Creating a new ``list`` in method's body will instantiate a new
sequence each time the new instance is created. Consider the following code:

>>> class Astronaut:
...     def __init__(self, name, missions=None):
...         self.name = name
...         self.missions = missions if missions else []

``None`` object is a singleton, which can be reused. Also is not a problematic,
because we will not append or modify anything to the ``None`` itself. As soon
as the new instance is created, the ``__init__()`` body is evaluated and
``self.missions`` is assigned to newly created ``list`` instance.


Fix
---
>>> class Astronaut:
...     def __init__(self, name, missions=None):
...         self.name = name
...         self.missions = missions if missions else []
>>>
>>>
>>> watney = Astronaut('Mark Watney')
>>> lewis = Astronaut('Melissa Lewis')
>>>
>>> print(f'Name: {watney.name}, Missions: {watney.missions}')
Name: Mark Watney, Missions: []
>>>
>>> print(f'Name: {lewis.name}, Missions: {lewis.missions}')
Name: Melissa Lewis, Missions: []
>>>
>>> watney.missions.append('Ares1')
>>> watney.missions.append('Ares2')
>>> watney.missions.append('Ares3')
>>>
>>> print(f'Name: {watney.name}, Missions: {watney.missions}')
Name: Mark Watney, Missions: ['Ares1', 'Ares2', 'Ares3']
>>>
>>> print(f'Name: {lewis.name}, Missions: {lewis.missions}')
Name: Melissa Lewis, Missions: []
>>>
>>> watney.missions == lewis.missions
False
>>>
>>> watney.missions is lewis.missions
False


.. todo:: Assignments
