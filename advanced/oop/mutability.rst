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
Bad:

.. code-block:: python

    class Astronaut:
        def __init__(self, name, missions=[]):
            self.name = name
            self.missions = missions


    watney = Astronaut('Mark Watney')
    watney.missions.append('Ares 3')
    print('Watney:', watney.missions)
    # Watney: ['Ares 3']

    twardowski = Astronaut('Jan Twardowski')
    print('Twardowski:', twardowski.missions)
    # 'Twardowski:' ['Ares 3']

Good:

.. code-block:: python

    class Astronaut:
        def __init__(self, name, missions=()):
            self.name = name
            self.missions = list(missions)


    watney = Astronaut('Mark Watney')
    watney.missions.append('Ares 3')
    print('Watney:', watney.missions)
    # Watney: ['Ares 3']

    twardowski = Astronaut('Jan Twardowski')
    print('Twardowski:', twardowski.missions)
    # 'Twardowski:' []

.. code-block:: python

    from typing import Optional


    class Astronaut:
        def __init__(self, firstname, lastname, missions: Optional[list[str]] = None):
            self.firstname = firstname
            self.lastname = lastname
            self.missions = missions if missions else []


    watney = Astronaut('Mark', 'Watney')
    watney.missions.append('Ares 3')
    watney.missions.append('Apollo 18')
    print('Watney:', watney.missions)


    twardowski = Astronaut('Jan', 'Twardowski')
    print('Twardowski:', twardowski.missions)

>>> from typing import Optional
>>>
>>>
>>> class Astronaut:
...     def __init__(self, firstname, lastname, missions: Optional[list[str]] = None):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.missions = missions if missions else []
>>>
>>>
>>> watney = Astronaut('Mark', 'Watney')
>>> watney.missions.append('Ares 3')
>>> watney.missions.append('Apollo 18')
>>> print('Watney:', watney.missions)
>>>
>>>
>>> twardowski = Astronaut('Jan', 'Twardowski')
>>> print('Twardowski:', twardowski.missions)


Assignments
-----------
.. todo:: Create assignments
