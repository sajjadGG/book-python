.. _OOP Attributes:

**************
OOP Attributes
**************


.. highlights::
    * Attributes are also known as "Properties" or "Fields"
    * ``snake_case`` name convention
    * Attributes should be defined only in ``__init__()`` method
    * Attributes store information (state) for instances
    * Access field values using dot (``.``) notation


Setting attributes
==================

Runtime attributes
------------------
.. code-block:: python
    :caption: Dynamic attributes

    class Iris:
        pass


    setosa = Iris()

    setosa.sepal_length = 5.1
    setosa.sepal_width = 3.5
    setosa.petal_length = 1.4
    setosa.petal_width = 0.2
    setosa.species = 'setosa'

    print(setosa.sepal_length)      # 5.1
    print(setosa.sepal_width)       # 3.5
    print(setosa.petal_length)      # 1.4
    print(setosa.petal_width)       # 0.2
    print(setosa.species)           # setosa

    print(setosa.xxx)               # AttributeError: 'Iris' object has no attribute 'xxx'

Init time attributes
--------------------
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

Variable value attributes
-------------------------
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
        def __init__(self, species='unknown'):
            self.species = species


    versicolor = Iris()
    print(versicolor.species)
    # unknown


Access modifiers
================
.. highlights::
    * All fields are always public
    * No protected i private
    * ``_name`` - protected field (by convention)
    * ``__name__`` - system field
    * ``name_`` - used while name collision

.. code-block:: python
    :caption: Access modifiers

    class Iris:
        def __init__(self):
            self._sepal_length = 5.1
            self._sepal_width = 3.5
            self._petal_length = 1.4
            self._petal_width = 0.2
            self.species = 'setosa'


    flower = Iris()

    print(flower._sepal_length)     # 5.1       # IDE should warn, that you access protected member
    print(flower._sepal_width)      # 3.5       # IDE should warn, that you access protected member
    print(flower._petal_length)     # 1.4       # IDE should warn, that you access protected member
    print(flower._petal_width)      # 0.2       # IDE should warn, that you access protected member
    print(flower.species)           # setosa


``__dict__`` - Getting dynamic fields and values
================================================
.. code-block:: python
    :caption: ``__dict__`` - Getting dynamic fields and values

    class Iris:
        def __init__(self, sepal_length, sepal_width,
                     petal_length, petal_width, species):

            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species


    flower = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')

    print(flower.__dict__)
    # {'sepal_length': 5.1,
    # 'sepal_width': 3.5,
    # 'petal_length': 1.4,
    # 'petal_width': 0.2,
    # 'species': 'setosa'}


Assignment
==========

Data Modeling
-------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/attribute_modeling.py`

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
        Jet Propulsion Laboratory, Pasadena, CA

:The whys and wherefores:
    * :ref:`OOP Classes and Instances`
    * :ref:`OOP Attributes`
