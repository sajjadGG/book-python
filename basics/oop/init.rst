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

    class Iris:
        def __init__(self):
            print('Latin name: Iris Setosa')


    flower = Iris()
    # Latin name: Iris Setosa


Initializer method with arguments
=================================
.. code-block:: python
    :caption: Initializer method with arguments

    class Iris:
        def __init__(self, species):
            print(f'Latin name: {species}')


    setosa = Iris('Iris Setosa')
    # Latin name: Iris Setosa

    virginica = Iris(species='Iris Virginica')
    # Latin name: Iris Virginica

    iris = Iris()
    # TypeError: __init__() missing 1 required positional argument: 'species'

.. code-block:: python
    :caption: Initializing fields on instance creation

    class Iris:
        def __init__(self, species):
            self.species = species


    setosa = Iris(species='setosa')
    print(setosa.species)
    # setosa

    virginica = Iris('virginica')
    print(virginica.species)
    # virginica

    versicolor = Iris()
    # TypeError: __init__() missing 1 required positional argument: 'species'

.. code-block:: python
    :caption: Method argument with default value

    class Iris:
        def __init__(self, species='versicolor'):
            self.species = species


    versicolor = Iris()
    print(versicolor.species)
    # versicolor


Initializing Attributes
=======================
.. code-block:: python
    :caption: Init time attributes

    class Iris:
        def __init__(self):
            self.sepal_length = 5.1
            self.sepal_width = 3.5
            self.petal_length = 1.4
            self.petal_width = 0.2
            self.species = 'setosa'


    setosa = Iris()

    print(setosa.sepal_length)      # 5.1
    print(setosa.sepal_width)       # 3.5
    print(setosa.petal_length)      # 1.4
    print(setosa.petal_width)       # 0.2
    print(setosa.species)           # setosa

    print(setosa.xxx)               # AttributeError: 'Iris' object has no attribute 'xxx'


.. code-block:: python
    :caption: Init time attributes

    class Iris:
        def __init__(self):
            self.sepal_length = 5.1
            self.sepal_width = 3.5
            self.petal_length = 1.4
            self.petal_width = 0.2
            self.species = 'setosa'


    setosa = Iris()
    virginica = Iris()

    print(setosa.sepal_length)      # 5.1
    print(setosa.sepal_width)       # 3.5
    print(setosa.petal_length)      # 1.4
    print(setosa.petal_width)       # 0.2
    print(setosa.species)           # setosa

    print(virginica.sepal_length)   # 5.1
    print(virginica.sepal_width)    # 3.5
    print(virginica.petal_length)   # 1.4
    print(virginica.petal_width)    # 0.2
    print(virginica.species)        # setosa

.. code-block:: python
    :caption: Init time attributes

    class Iris:
        def __init__(self, a, b, c, d, e):
            self.sepal_length = a
            self.sepal_width = b
            self.petal_length = c
            self.petal_width = d
            self.species = e


    setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
    virginica = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

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


Checking values
===============
.. code-block:: python

    class Kelvin:
        def __init__(self, value):
            if value < 0.0:
                raise ValueError('Kelvin temperature must be greater than 0')
            else:
                self.value = value

    ice = Kelvin(273.15)
    print(ice)
    # 273.15

    not_existing = Kelvin(-300)
    # ValueError: Kelvin temperature must be greater than 0'


Assignment
==========

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

    #. Do not convert units
    #. Do not store values in the instances

:Polish:
    #. Stwórz jedną klasę ``Temperature``
    #. Stwórz trzy instancje klasy ``Temperature``
    #. Wartości mają być podawane przy inicjalizacji
    #. Przy inicjalizacji instancje wypisują:

        #. Instancja ``celsius`` wyświetla temperaturę 36.6
        #. Instancja ``fahrenheit`` wyświetla temperaturę 97.88
        #. Instancja ``kelvin`` wyświetla temperaturę 309.75

    #. Nie konwertuj jednostek
    #. Nie przechowuj informacji w instancjach

Data Modeling
-------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/init_model.py`

:English:
    #. Model the data using classes
    #. Create instances for each record
    #. How many classes are there?
    #. How many instances are there?
    #. Create instances of a first class using positional arguments
    #. Create instances of a second class using keyword arguments
    #. Print first field from each instance

:Polish:
    #. Zamodeluj dane za pomocą klas
    #. Stwórz instancje dla każdego wpisu
    #. Jak wiele klas możemy wyróżnić?
    #. Jak wiele instancji możemy wyróżnić?
    #. Twórz instancje pierwszej klasy używając argumentów pozycyjnych
    #. Twórz instancje drugiej klasy używając argumentów nazwanych
    #. Wypisz pierwsze pole każdej z instancji

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
