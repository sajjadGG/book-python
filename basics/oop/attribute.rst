.. _OOP Attributes:

**********
Attributes
**********


About
=====
.. highlights::
    * Attributes are also known as "Properties" or "Fields"
    * ``snake_case`` name convention
    * Attributes store information (state) for instances
    * Access field values using dot (``.``) notation
    * Attributes should be defined only in ``__init__()`` method (covered in :ref:`OOP Initializer Method`)

.. glossary::

    property
    attribute
    field
    state
        Variable inside the class.


Dynamic Attributes
==================
.. code-block:: python
    :caption: Dynamic attributes

    class Temperature:
        pass


    temp = Temperature()
    temp.kelvin = 10

    print(temp.kelvin)
    # 10

.. code-block:: python
    :caption: Dynamic attributes

    class Astronaut:
        pass


    astro = Astronaut()
    astro.first_name = 'Jose'
    astro.last_name = 'Jimenez'

    print(f'My name... {astro.first_name} {astro.last_name}')
    # My name... Jose Jimenez

.. code-block:: python
    :caption: Dynamic attributes

    class Iris:
        pass


    setosa = Iris()
    setosa.features = [5.1, 3.5, 1.4, 0.2]
    setosa.label = 'setosa'

    print(setosa.label)
    # setosa

    sum(setosa.features)
    # 10.2

.. code-block:: python
    :caption: Accessing not existing attributes

    class MyClass:
        pass


    my_instance = MyClass()
    print(my_instance.xxx)
    # AttributeError: 'MyClass' object has no attribute 'xxx'


Get all dynamic fields and values
=================================
* ``obj.__dict__``

.. code-block:: python
    :caption: ``__dict__`` - Getting dynamic fields and values

    class Iris:
        pass


    flower = Iris()
    flower.sepal_length = 5.1
    flower.sepal_width = 3.5
    flower.petal_length = 1.4
    flower.petal_width = 0.2
    flower.species = 'setosa'

    print(flower.__dict__)
    # {'sepal_length': 5.1,
    #  'sepal_width': 3.5,
    #  'petal_length': 1.4,
    #  'petal_width': 0.2,
    #  'species': 'setosa'}


Assignment
==========

Data Modeling
-------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/attribute_model.py`

:English:
    #. Model the data using classes
    #. Create instances for each record
    #. How many classes are there?
    #. How many instances are there?
    #. Print all fields from each instance

:Polish:
    #. Zamodeluj dane za pomocą klas
    #. Stwórz instancje dla każdego wpisu
    #. Jak wiele klas możemy wyróżnić?
    #. Jak wiele instancji możemy wyróżnić?
    #. Wypisz wszystkie pola każdej z instancji

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
