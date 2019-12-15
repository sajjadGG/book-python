.. _OOP Stringify Objects:

*****************
Stringify Objects
*****************


``__str__()``
=============
.. highlights::
    * for end-user
    * ``print`` converts it's arguments to ``str()`` before printing

.. code-block:: python
    :caption: Object without ``__str__()`` method overloaded prints their memory address

    class Astronaut:
        def __init__(self, name):
            self.name = name


    astro = Astronaut('Jose Jimenez')

    str(astro)          # '<__main__.Astronaut object at 0x114175dd0>'
    print(astro)        # <__main__.Astronaut object at 0x114175dd0>

.. code-block:: python
    :caption: Objects can verbose print if ``__str__()`` method is present

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f'My name... {self.name}'


    astro = Astronaut('Jose Jimenez')

    str(astro)          # 'My name... Jose Jimenez'
    print(astro)        # My name... Jose Jimenez


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

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f'Astronaut(name="{self.name}")'


     astro = Astronaut('Jose Jimenez')

     repr(astro)        # 'Astronaut(name="Jose Jimenez")'
     astro              # Astronaut(name="Jose Jimenez")

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

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __format__(self, mood):
            if mood == 'happy':
                return f"Yuppi, we're going to space!"
            elif mood == 'scared':
                return f"I hope we don't crash"


     astro = Astronaut('Jose Jimenez')

     print(f'{astro:happy}')
     # Yuppi, we're going to space!

     print(f'{astro:scared}')
     # I hope we don't crash

.. code-block:: python

    class Point:
        def __init__(self, x, y, z=0):
            self.x = x
            self.y = y
            self.z = z

        def __format__(self, name):

            if name == 'in_2D':
                return f"({self.x}, {self.y})"

            if name == 'in_3D':
                return f"({self.x}, {self.y}, {self.z})"

            if name == 'as_dict':
                return str(self.__dict__)

            if name == 'as_tuple':
                return str(tuple(self.__dict__.values()))

            if name == 'as_json':
                import json
                return json.dumps(self.__dict__)


    point = Point(x=1, y=2)

    print(f'{point:in_2D}')           # '(1, 2)'
    print(f'{point:in_3D}')           # '(1, 2, 0)'
    print(f'{point:as_tuple}')        # '(1, 2, 0)'
    print(f'{point:as_dict}')         # "{'x': 1, 'y': 2, 'z': 0}"
    print(f'{point:as_json}')         # '{"x": 1, "y": 2, "z": 0}'


Assignments
===========

Stringify Object
----------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/syntax_stringify.py`

:English:
    #. Modify code from input data (see below)
    #. Overload ``str`` and ``repr`` to achieve result of printing

:Polish:
    #. Zmodyfikuj kod z danych wejściowych (patrz sekcja input)
    #. Przeciąż ``str`` i ``repr`` aby osiągnąć rezultat wyświetlania

:The whys and wherefores:
    * :ref:`OOP Stringify Objects`

:Input:
    .. code-block:: python
        :caption: Address Book

        class Crew:
            def __init__(self, members=()):
                self.members = list(members)

        class Astronaut:
            def __init__(self, name, locations=()):
                self.name = first_name
                self.locations = list(locations)

        class Location:
            def __init__(self, name):
                self.name = name

:Output:
    .. code-block:: python

        melissa = Astronaut('Melissa Lewis')

        print(f'Commander: \n{melissa}\n')
        # Commander:
        # Melissa Lewis

    .. code-block:: python

        mark = Astronaut('Mark Watney', locations=[
            Location('Johnson Space Center'),
            Location('Kennedy Space Center')
        ])

        print(f'Space Pirate: \n{mark}\n')
        # Space Pirate:
        # Mark Watney [
        # 	Johnson Space Center,
        # 	Kennedy Space Center]

    .. code-block:: python

        crew = Crew([
            Astronaut('Jan Twardowski', locations=[
                Location('Johnson Space Center'),
                Location('Kennedy Space Center'),
                Location('Jet Propulsion Laboratory'),
                Location('Armstrong Flight Research Center'),
            ]),
            Astronaut('José Jiménez'),
            Astronaut('Иван Иванович', locations=[]),
        ])

        print(f'Crew: \n{crew}')
        # Crew:
        # Jan Twardowski [
        # 	Johnson Space Center,
        # 	Kennedy Space Center,
        # 	Jet Propulsion Laboratory,
        # 	Armstrong Flight Research Center]
        # José Jiménez
        # Иван Иванович
