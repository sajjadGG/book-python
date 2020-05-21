.. _OOP Attributes:

**********
Attributes
**********


Rationale
=========
.. highlights::
    * Attributes are also known as "Properties" or "Fields"
    * ``snake_case`` name convention
    * Attributes store information (state) for instances
    * Access field values using dot (``.``) notation
    * Attributes should be defined only in ``__init__()`` method
    * More information in :ref:`OOP Initializer Method`

.. code-block:: python

    point_x = 1
    point_y = 2
    point_z = 3

    print(point_x)
    print(point_y)
    print(point_z)

.. code-block:: python

    class Point:
        pass

    point = Point()
    point.x = 1
    point.y = 2
    point.z = 3

    print(point.x)
    print(point.y)
    print(point.z)

.. glossary::

    attribute
    field
        Variable inside the class.
        Can be used as a synonym of :term:`property` or :term:`state`.

    property
        Variable inside the class.
        Should not change during lifetime of an object.

    state
        Variable inside the class.
        Changes during lifetime of an object.
        Represents current state of an object.

.. code-block:: text
    :caption: Class example with distinction of properties and state attributes

    Bucket with Water

        Properties:
            - color
            - width
            - height
            - radius
            - capacity
            - net mass (without water)

        State:
            - volume  (how much water is currently in bucket)
            - gross mass = net mass + water mass (water mass depends on its volume used))

.. figure:: img/bucket.jpg
    :width: 30%
    :align: center


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


    jose = Astronaut()
    jose.first_name = 'José'
    jose.last_name = 'Jiménez'

    print(f'My name... {jose.first_name} {jose.last_name}')
    # My name... José Jiménez

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

    class Astronaut:
        pass


    astro = Astronaut()

    print(astro.missions)
    # AttributeError: 'Astronaut' object has no attribute 'missions'

.. code-block:: python

    class Astronaut:
        pass


    jose = Astronaut()
    mark = Astronaut()

    jose.name = 'José Jiménez'

    print(f'My name... {jose.name}')
    # My name... José Jiménez

    print(f'My name... {mark.name}')
    # AttributeError: 'Astronaut' object has no attribute 'name'


Get All Dynamic Attributes and Values
=====================================
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


Assignments
===========

Data Modeling
-------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/oop_attribute_model.py`

:English:
    #. Use data from "Input" section (see below)
    #. Model the data using classes
    #. Create instances for each record
    #. How many classes are there?
    #. How many instances are there?
    #. Print all fields from each instance

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
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
