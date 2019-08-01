*******************
Objects and Classes
*******************


Object Paradigm
===============
* Model world as objects that interacts with each other

.. glossary::

    class
        Templates for objects.

    instance
    object
        Object created from class.

    method
        Function inside the class.

    property
    attribute
    field
        Variable inside the class.


Classes
=======
* Capitalized ``CamelCase`` name convention
* Classes are templates for objects

.. code-block:: python
    :caption: Defining class. Classes should have capitalized name

    class Iris:
        pass

.. code-block:: python
    :caption: Classes should have ``CamelCase`` names

    class IrisSetosa:
        pass

Classes vs Instances
--------------------
* Instances are also known as Objects
* Two newlines between class and code
* ``snake_case`` names

.. figure:: img/blueprint.png
    :scale: 8%
    :align: center

    Intuition definition: Class is a blueprint, instances are homes made from this plan. Image source: :cite:`FigureBlueprintHouse`

.. code-block:: python
    :caption: One class and one instance

    class Iris:
        pass


    flower = Iris()

.. code-block:: python
    :caption: One class and three instances

    class Iris:
        pass


    setosa = Iris()
    versicolor = Iris()
    virginica = Iris()

.. code-block:: python
    :caption: Three classes and three instances

    class IrisSetosa:
        pass

    class IrisVersicolor:
        pass

    class IrisVirginica:
        pass


    iris_setosa = IrisSetosa()
    iris_versicolor = IrisVersicolor()
    iris_virginica = IrisVirginica()


Fields
======
* Fields are also known as "Properties" or "Attributes"
* ``snake_case`` name convention
* Fields are defined in ``__init__()`` method
* Fields store information for instances

.. code-block:: python
    :caption: Classes can have multiple fields. All fields should be initialized in ``__init__()`` method.

    class Iris:
        def __init__(self):
            self.sepal_length = 5.1
            self.sepal_width = 3.5
            self.petal_length = 1.4
            self.petal_width = 0.2
            self.species = 'setosa'


    flower = Iris()

    print(flower.sepal_length)  # 5.1
    print(flower.sepal_width)   # 3.5
    print(flower.species)       # 'setosa'


Initializer Method
==================
* ``__init__()`` is not a constructor!
* It's a first method run after object is initiated
* All classes has default ``__init__()``
* Initialize all fields only in ``__init__``

.. code-block:: python
    :caption: Class initialization

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
        def __init__(self, species=None):
            self.species = species


    setosa = Iris(species='setosa')
    print(setosa.species)
    # setosa

    virginica = Iris('virginica')
    print(virginica.species)
    # virginica

    versicolor = Iris()
    print(versicolor.species)
    # None


Methods
=======
* Methods are functions in the class
* First argument is always instance (``self``)
* While calling function you never pass ``self``

Simple Methods
--------------
.. code-block:: python
    :caption: Simple Methods

    class Iris:
        def __init__(self):
            self.species = 'setosa'

        def latin_name(self):
            print(f'Latin name is: Iris setosa')


    flower = Iris()
    flower.latin_name()
    # Latin name is: Iris setosa

Methods accessing fields
------------------------
.. code-block:: python
    :caption: Methods accessing fields

    class Iris:
        def __init__(self):
            self.species = 'setosa'

        def latin_name(self):
            print(f'Latin name is: Iris {self.species}')


    flower = Iris()
    flower.latin_name()
    # Latin name is: Iris setosa

Methods with argument
---------------------
.. code-block:: python
    :caption: Methods with arguments

    class Iris:
        def latin_name(self, species):
            print(f'Iris {species}')


    flower = Iris()

    flower.latin_name(species='setosa')  # Iris setosa
    flower.latin_name('setosa')          # Iris setosa
    flower.latin_name()                  # TypeError: latin_name() missing 1 required positional argument: 'species'

Methods with arguments with default value
-----------------------------------------
.. code-block:: python
    :caption: Methods with default arguments

    class Iris:
        def latin_name(self, species='unknown'):
            print(f'Iris {species}')


    flower = Iris()

    flower.latin_name(species='setosa')  # Iris setosa
    flower.latin_name('setosa')          # Iris setosa
    flower.latin_name()                  # Iris unknown

Methods calling other methods
-----------------------------
.. code-block:: python
    :caption: Methods call other methods

    class Iris:
        def __init__(self):
            self.sepal_length = 5.1
            self.sepal_width = 3.5
            self.petal_length = 1.4
            self.petal_width = 0.2
            self.species = 'setosa'

        def sepal_area(self):
            return self.sepal_length * self.sepal_width

        def petal_area(self):
            return self.petal_length * self.petal_width

        def total_area(self):
            area = self.sepal_area() + self.petal_area()
            print(f'Total area is: {area:.1f}')


    flower = Iris()
    flower.total_area()
    # Total area is: 18.1


Assignments
===========

Classes and instances
---------------------
* Filename: :download:`solution/introduction_instances.py`
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Zamodelu dane w programie za pomocą klas i stwórz instancje:

    * Jan, Twardowski, 1961-04-12
    * Mark, Watney, 1969-07-21
    * Kennedy Space Center, Merritt Island, Florida
    * Johnson Space Center, Houston, Texas
    * Jet Propulsion Laboratory, Pasadena, Texas

Fields
------
* Filename: :download:`solution/introduction_temperature.py`
* Lines of code to write: 12 lines
* Estimated time of completion: 5 min

#. Stwórz klasę ``Temperature``
#. Klasa ma pamiętać wprowadzoną wartość
#. Stwórz instancje:

    * ``celsius`` z temperaturą 36.6
    * ``fahrenheit`` z temperaturą 97.88
    * ``kelvin`` z temperaturą 309.75

#. Wypisz temperaturę na ekranie

Methods
-------
* Filename: :download:`solution/introduction_iris.py`
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Stwórz klasę ``Iris`` z polami:

    - ``sepal_length: float``,
    - ``sepal_width: float``,
    - ``petal_length: float``,
    - ``petal_width: float``,
    - ``species: str``.

#. Napisz metodę ``total()`` wyliczającą sumę dla pól numerycznych obiektu (``sepal_length``, ``sepal_width``, ``petal_length``, ``petal_width``)
#. Napisz metodę ``average()`` wyliczającą średnią dla powyższych pól
#. Stwórz obiekt ``setosa`` z pomiarami podawanymi przy inicjalizacji:

    * sepal_length: 5.4
    * sepal_width: 3.9
    * petal_length: 1.3
    * petal_width: 0.4

#. Stwórz drugi obiekt ``virginica`` z pomiarami podawanymi przy inicjalizacji:

    * sepal_length: 5.8
    * sepal_width: 2.7
    * petal_length: 5.1
    * petal_width: 1.9

#. Wyświetl na ekranie nazwę gatunku oraz sumę i średnią z pomiarów dla obu instancji.

Credit Scoring
--------------
* Filename: :download:`solution/introduction_credit_scoring.py`
* Lines of code to write: 30 lines
* Estimated time of completion: 20 min

#. Stwórz klasę opisującą klienta banku
#. Stwórz klasę konto bankowe
#. Stwórz konta walutowe, oszczędnościowe, emerytalne i bieżące
#. Wylicz scoring kredytowy na podstawie informacji:

    - czy klient ma żonę/męża
    - czy klient ma dzieci
    - czy klient ma umowę o pracę
    - suma środków zgromadzonych na wszystkich kontach
    - wiek

#. Przedstaw scoring
