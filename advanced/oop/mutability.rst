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


Assignments
-----------
.. todo:: Create assignments
