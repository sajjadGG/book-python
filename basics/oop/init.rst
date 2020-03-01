.. _OOP Initializer Method:

******************
Initializer Method
******************


.. highlights::
    * It's a first method run after object is initiated
    * All classes has default ``__init__()``
    * ``__init__()`` is not a constructor!


Initializer method without arguments
====================================
.. code-block:: python
    :caption: Initializer method without arguments

    class Astronaut:
        def __init__(self):
            print('My name... Jose Jimenez')


    jose = Astronaut()
    # My name... Jose Jimenez


Initializer method with arguments
=================================
.. code-block:: python
    :caption: Initializer method with arguments

    class Astronaut:
        def __init__(self, name):
            print(f'My name... {name}')


    jose = Astronaut('Jose Jimenez')
    # My name... Jose Jimenez

    mark = Astronaut(name='Mark Watney')
    # My name... Mark Watney

    ivan = Astronaut()
    # TypeError: __init__() missing 1 required positional argument: 'name'

.. code-block:: python
    :caption: Method argument with default value

    class Astronaut:
        def __init__(self, name='Unknown'):
            print(f'My name... {name}')


    jose = Astronaut('Jose Jimenez')
    # My name... Jose Jimenez

    mark = Astronaut(name='Mark Watney')
    # My name... Mark Watney

    ivan = Astronaut()
    # My name... Unknown


Initializing Attributes
=======================
.. code-block:: python
    :caption: Init time attributes

    class Astronaut:
        def __init__(self):
            self.first_name = 'Mark'
            self.last_name = 'Watney'


    mark = Astronaut()

    print(mark.first_name)      # Mark
    print(mark.last_name)       # Watney
    print(mark.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

.. code-block:: python
    :caption: Init time attributes

    class Astronaut:
        def __init__(self):
            self.first_name = 'Mark'
            self.lastname = 'Watney'


    mark = Astronaut()
    print(mark.first_name)      # Mark
    print(mark.last_name)       # Watney
    print(mark.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

    ivan = Astronaut()
    print(ivan.first_name)      # Mark
    print(ivan.last_name)       # Watney
    print(ivan.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

.. code-block:: python
    :caption: Init time attributes

    class Astronaut:
        def __init__(self, a, b):
            self.first_name = a
            self.last_name = b


    mark = Astronaut('Mark', 'Watney')
    print(mark.first_name)      # Mark
    print(mark.last_name)       # Watney
    print(mark.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

    ivan = Astronaut(firstname='Ivan', lastname='Ivanovich')
    print(ivan.first_name)      # Ivan
    print(ivan.last_name)       # Ivanovich
    print(ivan.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

.. code-block:: python
    :caption: Init time attributes

    class Astronaut:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name


    mark = Astronaut('Mark', 'Watney')
    print(mark.first_name)      # Mark
    print(mark.last_name)       # Watney
    print(mark.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

    ivan = Astronaut(firstname='Ivan', lastname='Ivanovich')
    print(ivan.first_name)      # Ivan
    print(ivan.last_name)       # Ivanovich
    print(ivan.missions)        # AttributeError: 'Astronaut' object has no attribute 'mission'

.. code-block:: python
    :caption: Init time attributes

    class Astro:
        def __init__(self, first_name, last_name):
            self.full_name = f'{first_name} {last_name}'


    mark = Astro('Mark', 'Watney')

    print(mark.full_name)       # Mark Watney
    print(mark.first_name)      # AttributeError: 'Astro' object has no attribute 'firstname'
    print(mark.last_name)       # AttributeError: 'Astro' object has no attribute 'lastname'

.. code-block:: python
    :caption: Init time attributes

    class Point:
        def __init__(self, x, y, z=0):
            self.x = x
            self.y = y
            self.z = z


    p1 = Point(10, 20)
    p2 = Point(x=10, y=20)

    p3 = Point(10, 20, 30)
    p4 = Point(10, 20, z=30)
    p5 = Point(x=10, y=20, z=30)

.. code-block:: python
    :caption: Init time attributes

    class Iris:
        def __init__(self, sepal_length, sepal_width,
                     petal_length, petal_width, species):

            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species


    setosa = Iris(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2,
        species='setosa')

    virginica = Iris(
        sepal_length=5.8,
        sepal_width=2.7,
        petal_length=5.1,
        petal_width=1.9,
        species='virginica')


    print(setosa.sepal_length)      # 5.1
    print(setosa.sepal_width)       # 3.5
    print(setosa.petal_length)      # 1.4
    print(setosa.petal_width)       # 0.2
    print(setosa.species)           # setosa

    print(virginica.sepal_length)   # 5.8
    print(virginica.sepal_width)    # 2.7
    print(virginica.petal_length)   # 5.1
    print(virginica.petal_width)    # 1.9
    print(virginica.species)        # virginica

.. note:: Since Python 3.7 there is a ``@dataclass`` decorator, which automatically generates ``__init__()`` arguments and fields. Dataclasses are described in :ref:`OOP Dataclass`.


Checking values
===============
.. code-block:: python

    class Kelvin:
        def __init__(self, value):
            if not isinstance(value, (float, int)):
                raise TypeError('Temperature must be int or float')

            if value < 0.0:
                raise ValueError('Temperature must be greater than 0')

            self.value = value


    ice = Kelvin(273.15)
    print(ice.value)
    # 273.15

    not_existing = Kelvin(-300)
    # ValueError: Temperature must be greater than 0


Assignments
===========

Classes and instances
---------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/syntax_instances.py`

:English:
    #. Create one class ``Temperature``
    #. Create three instances of ``Temperature`` class
    #. Values must be passed at the initialization
    #. At initialization instances print:

        #. Instance ``celsius`` prints temperature 36.6
        #. Instance ``fahrenheit`` prints temperature 97.88
        #. Instance ``kelvin`` prints temperature 309.75

    #. Do not convert units (print only given numbers)
    #. Do not store values in the instances (only print on instance creation)

:Polish:
    #. Stwórz jedną klasę ``Temperature``
    #. Stwórz trzy instancje klasy ``Temperature``
    #. Wartości mają być podawane przy inicjalizacji
    #. Przy inicjalizacji instancje wypisują:

        #. Instancja ``celsius`` wyświetla temperaturę 36.6
        #. Instancja ``fahrenheit`` wyświetla temperaturę 97.88
        #. Instancja ``kelvin`` wyświetla temperaturę 309.75

    #. Nie konwertuj jednostek (użyj tylko podanych numerów)
    #. Nie przechowuj informacji w instancjach (tylko wypisz przy inicjalizacji)

Data Modeling
-------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/init_model.py`

:English:
    #. Model the data using classes
    #. Create instances for each record
    #. Create instances of a first class using positional arguments
    #. Create instances of a second class using keyword arguments
    #. Using ``__dict__`` print all fields from each instance

:Polish:
    #. Zamodeluj dane za pomocą klas
    #. Stwórz instancje dla każdego wpisu
    #. Twórz instancje pierwszej klasy używając argumentów pozycyjnych
    #. Twórz instancje drugiej klasy używając argumentów nazwanych
    #. Za pomocą ``__dict__`` wypisz wszystkie pola każdej z instancji

:Input:
    .. code-block:: text

        Jan, Twardowski, 1961-04-12
        Mark, Watney, 1969-07-21
        ESA, European Space Agency, Europe
        NASA, National Aeronautics and Space Administration, USA
        POLSA, Polish Space Agency, Poland

:The whys and wherefores:
    * :ref:`OOP Classes and Instances`
    * :ref:`OOP Attributes`
