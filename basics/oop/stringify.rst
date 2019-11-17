.. _OOP Stringify objects:

*********************
OOP Stringify objects
*********************


``__str__()``
=============
.. highlights::
    * for end-user
    * ``print`` converts it's arguments to ``str()`` before printing

.. code-block:: python
    :caption: Object without ``__str__()`` method overloaded prints their memory address

    class Iris:
        def __init__(self, species):
            self.species = species


    flower = Iris('setosa')

    str(flower)       # <__main__.Iris object at 0x112b366d8>
    print(flower)     # <__main__.Iris object at 0x112b366d8>

.. code-block:: python
    :caption: Objects can verbose print if ``__str__()`` method is present

    class Iris:
        def __init__(self, species):
            self.species = species

        def __str__(self):
            return f'Species: {self.species}'


    flower = Iris('setosa')

    str(flower)       # Species: setosa
    print(flower)     # Species: setosa


``__repr__()``
==============
.. highlights::
    * for developers
    * object representation
    * copy-paste for creating object with the same values
    * useful for debugging
    * printing ``list`` will call ``__repr__`` on each element

.. code-block:: python
    :caption: Using ``__repr__()`` on a class

    class Iris:
        def __init__(self, species):
            self.species = species

        def __repr__(self):
            return f'Iris(species="{self.species}")'


     flower = Iris(species='setosa')

     repr(point)    # Iris(species="setosa")
     point          # Iris(species="setosa")


.. code-block:: python
    :caption: printing ``list`` will call ``__repr__`` on each element

    class Astronaut:
        def __init__(self, name):
            self.name = name

    crew = [
        Astronaut('Jan Twardowski'),
        Astronaut('Mark Watney'),
        Astronaut('Melissa Lewis'),
    ]

    print(crew)
    # [
    #   <__main__.Astronaut object at 0x107871160>,
    #   <__main__.Astronaut object at 0x107c422e8>,
    #   <__main__.Astronaut object at 0x108156be0>
    # ]

.. code-block:: python
    :caption: printing ``list`` will call ``__repr__`` on each element

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f'{self.name}'

    crew = [
        Astronaut('Jan Twardowski'),
        Astronaut('Mark Watney'),
        Astronaut('Melissa Lewis'),
    ]

    print(crew)
    # [Jan Twardowski, Mark Watney, Melissa Lewis]


``__str__()`` vs. ``__repr__()``
================================
.. code-block:: python
    :caption: ``__str__`` and ``__repr__``

    import datetime

    str(datetime.datetime.now())
    # 2019-01-05 20:15:00.927387

    repr(datetime.datetime.now())
    # datetime.datetime(2019, 1, 5, 20, 15, 0, 684972)


``__format__()``
================
.. highlights::
    * Used for advanced formatting

.. code-block:: python

    class Point:
        def __init__(self, x, y, z=0):
            self.x = x
            self.y = y
            self.z = z

        def __format__(self, name):

            if name == '2D':
                return f"({self.x}, {self.y})"

            elif name == '3D':
                return f"({self.x}, {self.y}, {self.z})"

            elif name == 'dict':
                return str(self.__dict__)

            elif name == 'tuple':
                return str(tuple(self.__dict__.values()))

            elif name == 'json':
                import json
                return json.dumps(self.__dict__)

            else:
                raise ValueError


    point = Point(x=1, y=2)

    f'{point:2D}'           # '(1, 2)'
    f'{point:3D}'           # '(1, 2, 0)'
    f'{point:tuple}'        # '(1, 2, 0)'
    f'{point:dict}'         # "{'x': 1, 'y': 2, 'z': 0}"
    f'{point:json}'         # '{"x": 1, "y": 2, "z": 0}'


Assignments
===========

Address Book from API
---------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/syntax_stringify.py`

:English:
    #. Modify code from input data (see below)
    #. Overload ``str`` and ``repr`` to achieve result of printing

:Polish:
    #. Zmodyfikuj kod z danych wejściowych (patrz poniżej)
    #. Przeciąż ``str`` i ``repr`` aby osiągnąć rezultat wyświetlania

:The whys and wherefores:
    * :ref:`Stringify objects`

:Input:
    .. code-block:: python
        :caption: Address Book

        class Crew:
            def __init__(self, members=()):
                self.members = list(members)

        class Astronaut:
            def __init__(self, first_name, last_name, locations=()):
                self.first_name = first_name
                self.last_name = last_name
                self.locations = list(locations)

        class Location:
            def __init__(self, name):
                self.name = name


        melissa = Astronaut(first_name='Melissa', last_name='Lewis')
        print(f'Commander: \n{melissa}\n')

        mark = Astronaut(first_name='Mark', last_name='Watney', locations=[Location('Johnson Space Center'), Location('Kennedy Space Center')])
        print(f'Space Pirate: \n{mark}\n')

        crew = Crew([
            Astronaut(first_name='Jan', last_name='Twardowski', locations=[
                Location('Johnson Space Center'),
                Location('Kennedy Space Center'),
                Location('Jet Propulsion Laboratory'),
                Location('Armstrong Flight Research Center'),
            ]),
            Astronaut(first_name='José', last_name='Jiménez'),
            Astronaut(first_name='Иван', last_name='Иванович', locations=[]),
        ])

        print(f'Crew: {crew}')

:Output:
    .. code-block:: text

        Commander:
        Melissa Lewis

        Space Pirate:
        Mark Watney [Johnson Space Center, Kennedy Space Center]

        Crew: [
          José Jiménez,
          Иван Иванович,
          Jan Twardowski [
              Johnson Space Center,
              Kennedy Space Center,
              Jet Propulsion Laboratory,
              Armstrong Flight Research Center]
        ]
