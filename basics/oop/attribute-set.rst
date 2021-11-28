OOP Attribute Set
=================


Syntax
------
>>> class MyClass:
...     myattribute: str
>>>
>>>
>>> myobj = MyClass()
>>> myobj.myattribute = 'MyValue'


Example
-------
>>> class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = Astronaut()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'


Attributes and Instances
------------------------
Dynamic attributes:

>>> class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = Astronaut()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>>
>>> melissa = Astronaut()
>>> melissa.firstname = 'Melissa'
>>> melissa.lastname = 'Lewis'
>>>
>>> rick = Astronaut()
>>> rick.firstname = 'Rick'
>>> rick.lastname = 'Martinez'


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

>>> # doctest: +SKIP
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: float|int
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


Use Case - 0x01
---------------
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


Use Case - 0x02
---------------
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


Use Case - 0x03
---------------
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


Use Case - 0x04
---------------
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
