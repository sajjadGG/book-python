**********
Attributes
**********

* Fields are also known as "Properties" or "Fields"
* ``snake_case`` name convention
* Fields should be defined only in ``__init__()`` method
* Fields store information for instances
* Access field values using ``.`` (dot) notation


Constant value attributes
=========================
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


Variable value attributes
=========================
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


Access modifiers
================
* All fields are always public
* No protected i private
* ``_name`` - private fields (by convention)
* ``__name__`` - system methods
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

    print(flower._sepal_length)  # 5.1       # Good IDE will tell you, that you access protected member
    print(flower._sepal_width)   # 3.5       # Good IDE will tell you, that you access protected member
    print(flower._petal_length)  # 1.4       # Good IDE will tell you, that you access protected member
    print(flower._petal_width)   # 0.2       # Good IDE will tell you, that you access protected member
    print(flower.species)       # 'setosa'


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


    flower = Iris(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2,
        species='setosa')

    flower.__dict__
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
