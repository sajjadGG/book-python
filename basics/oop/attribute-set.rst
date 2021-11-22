OOP Attribute Set
=================


Rationale
---------
* Attributes are also known as "Properties" or "Fields"
* ``snake_case`` name convention
* Attributes store information (state) for instances
* Access field values using dot (``.``) notation
* Attributes should be defined only in ``__init__()`` method
* More information in `OOP Init Method`

.. glossary::

    attribute
        Variable inside the class.
        In Python, methods also can be described as attributes,
        but justification for that is a bit more complex which will
        be introduced later in a book.

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

Class example with distinction of properties and state attributes.

An example "Glass with Water" can illustrate the distinction of properties
and state attributes:

Properties:
    - color
    - width
    - height
    - radius
    - capacity
    - net mass (without water)

State:
    - volume  (how much water is currently in the glass)
    - gross mass = net mass + water mass (water mass depends on its volume used))

.. figure:: img/oop-classes-glass.jpg


Syntax
------
>>> class MyClass:
...     myattribute: str
>>>
>>>
>>> myobj = MyClass()
>>> myobj.myattribute = 'MyValue'
>>> print(myobj.myattribute)
MyValue


What are attributes?
--------------------
Identifiers and scalars creates values:

>>> point1_x = 1
>>> point1_y = 2
>>> point1_z = 3
>>>
>>> point2_x = 4
>>> point2_y = 5
>>> point2_z = 6

Values with relations creates data:

>>> point1 = (1, 2, 3)
>>> point2 = (4, 5, 6)

Data with meaning creates information:

>>> point1 = {'x': 1, 'y': 2, 'z': 3}
>>> point2 = {'x': 4, 'y': 5, 'z': 6}

Information with context and relations creates class:

>>> class Point:
...     x: int
...     y: int
...     z: int
>>>
>>>
>>> point1 = Point()
>>> point1.x = 1
>>> point1.y = 2
>>> point1.z = 3
>>>
>>> point2 = Point()
>>> point2.x = 4
>>> point2.y = 5
>>> point2.z = 6


Dynamic Attributes
------------------
Dynamic attributes:

>>> class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'

>>> class Astronaut:
...     name: str
>>>
>>>
>>> mark = Astronaut()
>>> jose = Astronaut()
>>> jose.name = 'José Jiménez'
>>>
>>> print(f'My name... {jose.name}')
My name... José Jiménez
>>> print(f'My name... {mark.name}')
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'name'


Namespace
---------
Unrelated values:

>>> x = 1
>>> y = 2
>>> z = 3

Class creates space, in which names has meaning:

>>> class Point:
...     x: int
...     y: int
...     z: int
>>>
>>>
>>> point = Point()
>>> point.x = 1
>>> point.y = 2
>>> point.z = 3


Different Types
---------------
>>> class Iris:
...     features: list[float]
...     label: str
>>>
>>>
>>> setosa = Iris()
>>> setosa.features = [5.1, 3.5, 1.4, 0.2]
>>> setosa.label = 'setosa'
>>>
>>> print(setosa.label)
setosa
>>> print(setosa.features)
[5.1, 3.5, 1.4, 0.2]
>>> sum(setosa.features)
10.2

>>> from typing import Union
>>>
>>>
>>> class Astronaut:
...     age: Union[float,int]
>>>
>>>
>>> jose = Astronaut()
>>> jose.age = 36
>>>
>>> mark = Astronaut()
>>> mark.age = 42.1

>>> class Astronaut:
...     pass
>>>
>>>
>>> jose = Astronaut()
>>> jose.age = 36
>>>
>>> mark = Astronaut()
>>> mark.age = 42.1


Get All Dynamic Attributes and Values
-------------------------------------
* ``vars(obj)`` - returns all fields in dict format

Getting dynamic fields and values:

>>> class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str
>>>
>>>
>>> flower = Iris()
>>> flower.sepal_length = 5.1
>>> flower.sepal_width = 3.5
>>> flower.petal_length = 1.4
>>> flower.petal_width = 0.2
>>> flower.species = 'setosa'
>>>
>>> vars(flower)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.1,
 'sepal_width': 3.5,
 'petal_length': 1.4,
 'petal_width': 0.2,
 'species': 'setosa'}


Select Attributes
-----------------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     height: float
...     weight: float
>>>
>>>
>>> astro = Astronaut()
>>> astro.firstname = 'Mark'
>>> astro.lastname = 'Watney'
>>> astro.age = 44
>>> astro.height = 185.5
>>> astro.weight = 75.5
>>>
>>> vars(astro)
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 44, 'height': 185.5, 'weight': 75.5}
>>>
>>> list(vars(mark).values())
['Mark', 'Watney', 44, 185.5, 75.5]
>>>
>>> [x for x in vars(mark).values() if type(x) is str]
['Mark', 'Watney']
>>>
>>> [x for x in vars(mark).values() if type(x) in (float, int)]
[44, 185.5, 75.5]
>>>
>>> {k:v for k,v in vars(mark).items()}
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 44, 'height': 185.5, 'weight': 75.5}
>>>
>>> {k:v for k,v in vars(mark).items() if k in ['firstname', 'lastname']}
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> {k:v for k,v in vars(mark).items() if type(v) is str}
{'firstname': 'Mark', 'lastname': 'Watney'}


Use Cases
---------
>>> class Laptop:
...     cpu: float
...     ram: int
...     ssd: int
>>>
>>>
>>> macbook = Laptop()
>>> lenovo = Laptop()
>>> hp = Laptop()
>>> asus = Laptop()

>>> class Date:
...     year: int
...     month: int
...     day: int
>>>
>>>
>>> gagarin_launch = Date()
>>> gagarin_launch.year = 1961
>>> gagarin_launch.month = 4
>>> gagarin_launch.day = 12
>>>
>>> armstrong_first_moon_step = Date()
>>> armstrong_first_moon_step.year = 1969
>>> armstrong_first_moon_step.month = 7
>>> armstrong_first_moon_step.day = 21

>>> class Date:
...     year: int
...     month: int
...     day: int
>>>
>>>
>>> class Person:
...     firstname: str
...     lastname: str
...     date_of_birth: Date
...     height: float
...     weight: float


Use Case - Astronaut
--------------------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     mission: str
...     agency: str
>>>
>>>
>>> watney = Astronaut()
>>> watney.firstname = 'Mark'
>>> watney.lastname = 'Watney'
>>> watney.mission = 'Ares 3'
>>> watney.agency = 'NASA'
>>>
>>> lewis = Astronaut()
>>> lewis.firstname = 'Melissa'
>>> lewis.lastname = 'Lewis'
>>> lewis.mission = 'Ares 3'
>>> lewis.agency = 'NASA'


References
----------
.. [glassimg] https://media.istockphoto.com/vectors/glasses-set-for-water-glasses-full-empty-halffilled-with-water-vector-vector-id905957960?k=6&m=905957960&s=612x612&w=0&h=DE0uCDCehEA_eDHzHW38jvhl3pYjNuoqXZ_6ZzHbz0M=


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_a.py
    :caption: :download:`Solution <assignments/oop_attribute_a.py>`
    :end-before: # Solution
