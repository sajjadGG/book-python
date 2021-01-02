OOP Attributes
==============


Rationale
---------
* Attributes are also known as "Properties" or "Fields"
* ``snake_case`` name convention
* Attributes store information (state) for instances
* Access field values using dot (``.``) notation
* Attributes should be defined only in ``__init__()`` method (More information in :ref:`OOP Init Method`)

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

    namespace
        Container for storing related data

Class example with distinction of properties and state attributes:

.. code-block:: text

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


Syntax
------
.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str


    astro = Astronaut()

    astro.firstname = 'Mark'
    astro.lastname = 'Watney'

    print(astro.firstname)
    print(astro.lastname)


Dynamic Attributes
------------------
Dynamic attributes:

.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str


    jose = Astronaut()
    jose.firstname = 'José'
    jose.lastname = 'Jiménez'

    print(f'My name... {jose.firstname} {jose.lastname}')
    # My name... José Jiménez

Accessing not existing attributes:

.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str


    astro = Astronaut()

    print(astro.missions)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'missions'

.. code-block:: python

    class Astronaut:
        name: str


    jose = Astronaut()
    mark = Astronaut()

    jose.name = 'José Jiménez'

    print(f'My name... {jose.name}')
    # My name... José Jiménez

    print(f'My name... {mark.name}')
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'name'

Namespace
---------
.. code-block:: python

    point_x = 1
    point_y = 2
    point_z = 3

    print(point_x)
    print(point_y)
    print(point_z)

.. code-block:: python

    class Point:
        x: int
        y: int
        z: int


    point = Point()
    point.x = 1
    point.y = 2
    point.z = 3

    print(point.x)
    print(point.y)
    print(point.z)


Different Types
---------------
.. code-block:: python

    class Iris:
        features: list[float]
        label: str


    setosa = Iris()
    setosa.features = [5.1, 3.5, 1.4, 0.2]
    setosa.label = 'setosa'

    print(setosa.label)
    # setosa

    print(setosa.features)
    # [5.1, 3.5, 1.4, 0.2]

    sum(setosa.features)
    # 10.2

.. code-block:: python

    from typing import Union

    class Astronaut:
        age: Union[float,int]


    jose = Astronaut()
    jose.age = 36

    mark = Astronaut()
    mark.age = 42.1

.. code-block:: python

    class Astronaut:
        pass


    jose = Astronaut()
    jose.age = 36

    mark = Astronaut()
    mark.age = 42.1


Get All Dynamic Attributes and Values
-------------------------------------
* ``obj.__dict__``

``__dict__`` - Getting dynamic fields and values:

.. code-block:: python

    class Iris:
        sepal_length: float
        sepal_width: float
        petal_length: float
        petal_width: float
        species: str


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


Use Cases
---------
.. code-block:: python

    class Laptop:
        cpu: float
        ram: int
        ssd: int


    macbook = Laptop()
    lenovo = Laptop()
    hp = Laptop()
    asus = Laptop()

.. code-block:: python

    class Date:
        year: int
        month: int
        day: int


    gagarin_launch = Date()
    gagarin_launch.year = 1961
    gagarin_launch.month = 4
    gagarin_launch.day = 12

    armstrong_first_moon_step = Date()
    armstrong_first_moon_step.year = 1969
    armstrong_first_moon_step.month = 7
    armstrong_first_moon_step.day = 21

.. code-block:: python

    class Date:
        year: int
        month: int
        day: int


    class Person:
        firstname: str
        lastname: str
        date_of_birth: Date
        height: float
        weight: float

.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str


    watney = Astronaut()
    watney.firstname = 'Mark'
    watney.lastname = 'Watney'

    lewis = Astronaut()
    lewis.firstname = 'Melissa'
    lewis.lastname = 'Lewis'
    lewis.address = 'Ćwiartki 3/4'

    print(watney.address)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'address'

    print(lewis.address)
    # Ćwiartki 3/4

.. code-block:: python

    watney_firstname = 'Mark'
    watney_lastname = 'Watney'
    watney_mission = 'Ares 3'
    watney_agency = 'NASA'

    lewis_firstname = 'Melissa'
    lewis_lastname = 'Lewis'
    lewis_mission = 'Ares 3'
    lewis_agency = 'NASA'

.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str
        mission: str
        agency: str


    watney = Astronaut()
    watney.firstname = 'Mark'
    watney.lastname = 'Watney'
    watney.mission = 'Ares 3'
    watney.agency = 'NASA'

    lewis = Astronaut()
    lewis.firstname = 'Melissa'
    lewis.lastname = 'Lewis'
    lewis.mission = 'Ares 3'
    lewis.agency = 'NASA'

    watney.__dict__
    # {'firstname': 'Mark',
    #  'lastname': 'Watney',
    #  'mission': 'Ares 3',
    #  'agency': 'NASA'}

    lewis.__dict__
    # {'firstname': 'Melissa',
    #  'lastname': 'Lewis',
    #  'mission': 'Ares 3',
    #  'agency': 'NASA'}


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_model.py
    :caption: :download:`Solution <assignments/oop_attribute_model.py>`
    :end-before: # Solution
