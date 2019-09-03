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
    :caption: Multi-word class names should use ``CamelCase``

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
    :caption: Three classes and four instances

    class IrisSetosa:
        pass

    class IrisVersicolor:
        pass

    class IrisVirginica:
        pass


    iris_setosa1 = IrisSetosa()
    iris_setosa2 = IrisSetosa()
    iris_versicolor = IrisVersicolor()
    iris_virginica = IrisVirginica()


Methods
=======
* Methods are functions in the class
* First argument is always instance (``self``)
* While calling function you never pass ``self``

Methods without arguments
-------------------------
.. code-block:: python
    :caption: Methods without arguments

    class Iris:
        def latin_name(self):
            print(f'Latin name: Iris Setosa')


    flower = Iris()

    flower.latin_name()
    # Latin name: Iris Setosa

Methods with argument
---------------------
.. code-block:: python
    :caption: Methods with arguments

    class Iris:
        def latin_name(self, species):
            print(f'Latin name: {species}')


    flower = Iris()

    flower.latin_name(species='Iris Setosa')
    # Latin name: Iris Setosa

    flower.latin_name('Iris Setosa')
    # Latin name: Iris Setosa

    flower.latin_name()
    # TypeError: latin_name() missing 1 required positional argument: 'species'

Methods with arguments with default value
-----------------------------------------
.. code-block:: python
    :caption: Methods with arguments with default value

    class Iris:
        def latin_name(self, species='unknown'):
            print(f'Latin name: Iris {species}')


    flower = Iris()

    flower.latin_name(species='Iris Setosa')
    # Latin name: Iris Setosa

    flower.latin_name('setosa')
    # Latin name: Iris Setosa

    flower.latin_name()
    # Latin name: unknown

Methods calling other methods
-----------------------------
.. code-block:: python
    :caption: Methods calling other methods

    class Iris:
        def get_name(self):
            return 'Iris Setosa'

        def latin_name(self):
            name = self.get_name()
            return f'Latin name: {name}'


    flower = Iris()

    flower.latin_name()
    # Latin name: Iris Setosa


Initializer Method
==================
* It's a first method run after object is initiated
* All classes has default ``__init__()``
* ``__init__()`` is not a constructor!

Initializer method without arguments
------------------------------------
.. code-block:: python
    :caption: Initializer method without arguments

    class Iris:
        def __init__(self):
            print('Latin name: Iris Setosa')


    flower = Iris()
    # Latin name: Iris Setosa

Initializer method with arguments
---------------------------------
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


Fields
======
* Fields are also known as "Properties" or "Attributes"
* ``snake_case`` name convention
* Fields should be defined only in ``__init__()`` method
* Fields store information for instances
* Access field values using ``.`` (dot) notation

Fields with constant values
---------------------------
.. code-block:: python
    :caption: Fields with constant values

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

Initializing fields on instance creation
----------------------------------------
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
        def __init__(self, species=None):
            self.species = species


    versicolor = Iris()
    print(versicolor.species)
    # None


Methods accessing fields
========================
.. code-block:: python
    :caption: Methods accessing fields

    class Iris:
        def __init__(self, species='unknown'):
            self.species = species

        def latin_name(self):
            print(f'Latin name is: {self.species}')


    setosa = Iris('Iris Setosa')
    setosa.latin_name()
    # Latin name is: Iris Setosa

    iris = Iris()
    iris.latin_name()
    # Latin name is: unknown


Assignments
===========

Classes and instances
---------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/syntax_instances.py`

:English:
    #. Create class ``Temperature``
    #. Class has to remember input data
    #. Create three instances of ``Temperature`` class
    #. Values had to be passed at the initialization

        #. Instance ``celsius`` with temperature 36.6
        #. Instance ``fahrenheit`` with temperature 97.88
        #. Instance ``kelvin`` with temperature 309.75

    #. Print on the screen temperatures remembered in instances

:Polish:
    #. Stwórz klasę ``Temperature``
    #. Klasa ma pamiętać wprowadzoną wartość
    #. Stwórz trzy instancje klasy ``Temperature``
    #. Wartości mają być podawane przy inicjalizacji:

        #. Instancja ``celsius`` z temperaturą 36.6
        #. Instancja ``fahrenheit`` z temperaturą 97.88
        #. Instancja ``kelvin`` z temperaturą 309.75

    #. Wypisz na ekranie temperatury zapamiętane w instancji

Data Modeling
-------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/syntax_modeling.py`

:English:
    #. Model the data using classes
    #. Create instances for each record
    #. How many classes are there?
    #. How many instances are there?

:Polish:
    #. Zamodeluj dane za pomocą klas
    #. Stwórz instancje dla każdego wpisu
    #. Jak wiele klas możemy wyróżnić?
    #. Jak wiele instancji możemy wyróżnić?

:Input:
    .. code-block:: text

        Jan, Twardowski, 1961-04-12
        Mark, Watney, 1969-07-21
        Kennedy Space Center, Merritt Island, FL
        Johnson Space Center, Houston, TX
        Jet Propulsion Laboratory, Pasadena, TX

Methods
-------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/syntax_methods.py`

:English:
    #. Create class ``Iris`` with fields from input data
    #. Create method ``total()`` which sums all the numerical attributes values
    #. Create method ``mean()`` which calculates mean of numerical attributes values
    #. Create ``setosa`` object with attributes set at the initialization (see input data)
    #. Create ``virginica`` object with attributes set at the initialization (see input data)
    #. Print on the screen species name, total and mean of each instance

:Polish:
    #. Stwórz klasę ``Iris`` z polami z danych wejściowych
    #. Napisz metodę ``total()`` wyliczającą sumę atrybutów numerycznych obiektu
    #. Napisz metodę ``mean()`` wyliczającą średnią atrybutów numerycznych obiektu
    #. Stwórz obiekt ``setosa`` z pomiarami podawanymi przy inicjalizacji (patrz dane wejściowe)
    #. Stwórz obiekt ``virginica`` z pomiarami podawanymi przy inicjalizacji (patrz dane wejściowe)
    #. Wyświetl na ekranie nazwę gatunku oraz sumę i średnią z pomiarów dla każdej instancji

:Input:
    .. code-block:: python
        :caption: Iris parameters

        sepal_length: float
        sepal_width: float
        petal_length: float
        petal_width: float
        species: str

    .. code-block:: python
        :caption: Setosa initial values

        sepal_length = 5.4
        sepal_width = 3.9
        petal_length = 1.3
        petal_width = 0.4

    .. code-block:: python
        :caption: Virginica initial values

        sepal_length = 5.8
        sepal_width = 2.7
        petal_length = 5.1
        petal_width = 1.9
