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


    astro = Astronaut('José Jiménez')

    print(astro)        # <__main__.Astronaut object at 0x114175dd0>
    str(astro)          # '<__main__.Astronaut object at 0x114175dd0>'
    astro.__str__()     # '<__main__.Astronaut object at 0x114175dd0>'

.. code-block:: python
    :caption: Objects can verbose print if ``__str__()`` method is present

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f'My name... {self.name}'


    astro = Astronaut('José Jiménez')

    print(astro)        # My name... José Jiménez
    str(astro)          # 'My name... José Jiménez'
    astro.__str__()     # 'My name... José Jiménez'


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


     astro = Astronaut('José Jiménez')

     repr(astro)        # 'Astronaut(name="José Jiménez")'
     astro              # Astronaut(name="José Jiménez")

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
    # 1961-04-12 6:07:00.000000

    repr(datetime.datetime.now())
    # datetime.datetime(1961, 4, 12, 6, 7, 0, 000000)


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


     jose = Astronaut('José Jiménez')

     print(f'{jose:happy}')
     # Yuppi, we're going to space!

     print(f'{jose:scared}')
     # I hope we don't crash

.. code-block:: python

    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR


    class Duration:
        def __init__(self, seconds):
            self.seconds = seconds

        def __format__(self, unit):
            if unit == 'minutes':
                return str(self.seconds / MINUTE)

            if unit == 'hours':
                return str(self.seconds / HOUR)

            if unit == 'days':
                return str(round(self.seconds / DAY, 2))


    duration = Duration(seconds=3600)

    print(f'Duration was {duration:minutes} min')       # Duration was 60.0 min
    print(f'Duration was {duration:hours} hour')        # Duration was 1.0 hour
    print(f'Duration was {duration:days} day')          # Duration was 0.04 day


.. code-block:: python

    class Temperature:
        def __init__(self, kelvin):
            self.kelvin = kelvin

        def __format__(self, unit):

            if unit == 'kelvin':
                value = self.kelvin

            elif unit == 'celsius':
                value = self.kelvin - 273.15

            elif unit == 'fahrenheit':
                value = (self.kelvin-273.15) * 9/5 + 32

            value = round(value, 2)
            return str(value)


    temp = Temperature(309.75)

    print(f'Temperature is {temp:kelvin} K')       # Temperature is 309.75 K
    print(f'Temperature is {temp:celsius} C')      # Temperature is 36.6 C
    print(f'Temperature is {temp:fahrenheit} F')   # Temperature is 97.88 F

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

OOP Stringify Str
-----------------
* Complexity level: easy
* Lines of code to write: 18 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/oop_stringify_str.py`

:English:
    #. Create class ``Iris`` with ``features: List[float]`` and ``label: str`` attributes
    #. For each row in ``DATA`` create ``Iris`` instance with row values
    #. Set class attributes at the initialization from positional arguments
    #. Create method which sums values of all ``features``
    #. While printing object show: species name and a sum method result
    #. Compare result with "Output" section (see below)

:Polish:
    #. Stwórz klasę ``Iris`` z atrybutami ``features: List[float]`` i ``label: str``
    #. Dla każdego wiersza w ``DATA`` twórz instancję ``Iris`` z danymi z wiersza
    #. Ustaw atrybuty klasy przy iniclalizacji z argumentów pozycyjnych
    #. Stwórz metodę sumującą wartości wszystkich ``features``
    #. Przy wypisywaniu obiektu pokaż: nazwę gatunku i wynik metody sumującej
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
        ]

:Output:
    .. code-block:: text

        setosa 9.4
        versicolor 16.299999999999997
        virginica 19.3

OOP Stringify Repr
------------------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/oop_stringify_repr.py`

:English:
    #. Use code from "Input" section (see below)
    #. Create class ``Iris`` with ``features: List[float]`` and ``label: str`` attributes
    #. For each row in ``DATA`` create ``Iris`` instance with row values
    #. Set class attributes at the initialization from positional arguments
    #. Print representation of each instance with values (use ``repr()``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz klasę ``Iris`` z atrybutami ``features: List[float]`` i ``label: str``
    #. Dla każdego wiersza w ``DATA`` twórz instancję ``Iris`` z danymi z wiersza
    #. Ustaw atrybuty klasy przy iniclalizacji z argumentów pozycyjnych
    #. Wypisz reprezentację każdej z instancji z wartościami (użyj ``repr()``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
        ]

:Output:
    .. code-block:: text

        Iris(features=[4.7, 3.2, 1.3, 0.2], label='setosa')
        Iris(features=[7.0, 3.2, 4.7, 1.4], label='versicolor')
        Iris(features=[7.6, 3.0, 6.6, 2.1], label='virginica')

OOP Stringify Complex
---------------------
* Complexity level: medium
* Lines of code to write: 9 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/oop_stringify_complex.py`

:English:
    #. Use code from "Input" section (see below)
    #. Overload ``str`` and ``repr`` to achieve desired printing output
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Przeciąż ``str`` i ``repr`` aby osiągnąć oczekiwany rezultat wypisywania
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python
        :caption: Address Book

        class Crew:
            def __init__(self, members=()):
                self.members = list(members)

        class Astronaut:
            def __init__(self, name, experience=()):
                self.name = name
                self.experience = list(experience)

        class Mission:
            def __init__(self, year, name):
                self.year = year
                self.name = name

:Output:
    .. code-block:: python

        melissa = Astronaut('Melissa Lewis')

        print(f'Commander: \n{melissa}\n')
        # Commander:
        # Melissa Lewis

    .. code-block:: python

        mark = Astronaut('Mark Watney', experience=[
            Mission(2035, 'Ares 3'),
        ])

        print(f'Space Pirate: \n{mark}\n')
        # Space Pirate:
        # Mark Watney veteran of [
        # 	2035: Ares 3]

    .. code-block:: python

        crew = Crew([
            Astronaut('Jan Twardowski', experience=[
                Mission(1969, 'Apollo 11'),
                Mission(2024, 'Artemis 3'),
            ]),
            Astronaut('José Jiménez'),
            Astronaut('Mark Watney', experience=[
                Mission(2035, 'Ares 3'),
            ]),
        ])

        print(f'Crew: \n{crew}')
        # Crew:
        # Jan Twardowski veteran of [
        # 	1969: Apollo 11,
        # 	2024: Artemis 3]
        # José Jiménez
        # Mark Watney veteran of [
        # 	2035: Ares 3]

:The whys and wherefores:
    * :ref:`OOP Stringify Objects`

:Hint:
    * Define ``Crew.__str__()``
    * Define ``Astronaut.__str__()`` and ``Astronaut.__repr__()``
    * Define ``Mission.__repr__()``
