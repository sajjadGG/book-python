OOP Init Validation
===================
* It's a first method run after object is initiated
* All classes has default ``__init__()``

.. glossary::

    constructor
        Method called at object instantiation used to create object.
        Constructor is called on not fully initialized object and hence do
        not have access to object methods. Constructor should return
        ``None``.

    initializer
        Method called at object instantiation used to fill empty object with
        values. Initializer is called upon object initialization and hence
        can modify object and use its methods. Initializer should return
        ``None``.


Syntax
------
>>> class MyClass:
...     myattribute: str
...
...     def __init__(self, myvar):
...         self.myattribute = myvar
>>>
>>>
>>> myobj = MyClass('myvalue')
>>>
>>> print(myobj.myattribute)
myvalue


Initializer Method Without Arguments
------------------------------------
Initializer method without arguments:

>>> class Astronaut:
...     def __init__(self):
...         print('Hello')
>>>
>>>
>>> astro = Astronaut()
Hello


Initializer Method With Arguments
---------------------------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> astro = Astronaut()
Traceback (most recent call last):
TypeError: Astronaut.__init__() missing 2 required positional arguments: 'firstname' and 'lastname'

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
Hello Mark Watney
>>>
>>> astro = Astronaut(firstname='Mark', lastname='Watney')
Hello Mark Watney

>>> class Astronaut:
...     def __init__(self, firstname, lastname='Unknown'):
...         print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
Hello Mark Watney
>>>
>>> astro = Astronaut('Mark')
Hello Mark Unknown


Constant Attributes
-------------------
>>> class Astronaut:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
>>>
>>>
>>> mark = Astronaut()
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> melissa = Astronaut()
>>> vars(melissa)
{'firstname': 'Mark', 'lastname': 'Watney'}


Variable Attributes
-------------------
>>> class Astronaut:
...     def __init__(self, a, b):
...         self.firstname = a
...         self.lastname = b
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> ivan = Astronaut(a='Ivan', b='Ivanovich')
>>> vars(ivan)
{'firstname': 'Ivan', 'lastname': 'Ivanovich'}

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> ivan = Astronaut(firstname='Ivan', lastname='Ivanovich')
>>> vars(ivan)
{'firstname': 'Ivan', 'lastname': 'Ivanovich'}


Combine Attributes
------------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.name = f'{firstname} {lastname}'
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>>
>>> print(mark.name)
Mark Watney
>>>
>>> print(mark.firstname)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'firstname'
>>>
>>> print(mark.lastname)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'lastname'


Validate
--------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...
...     def __init__(self, firstname, lastname='asd', age=0):
...         if not 30 <= age < 50:
...             raise ValueError('Astronauts are selected between age of 30-50 years')
...         self.firstname = firstname
...         self.lastname = lastname
...         self.age = age
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', age=40)
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>>
>>> mark = Astronaut('Mark', 'Watney', age=60)
Traceback (most recent call last):
ValueError: Astronauts are selected between age of 30-50 years


Validate
--------
* Those are static attributes
* Usefully for string configuration values
* Do not modify those values later in a code (keep them constant / final)
* More information in `OOP Static Attributes`.

>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     AGE_MIN: int = 30  # const / final
...     AGE_MAX: int = 50  # const / final
...
...     def __init__(self, firstname, lastname='asd', age=0):
...         if not self.AGE_MIN <= age < self.AGE_MAX:
...             raise ValueError('Astronauts are selected between age of 30-50 years')
...         self.firstname = firstname
...         self.lastname = lastname
...         self.age = age
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', age=40)
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>>
>>> mark = Astronaut('Mark', 'Watney', age=60)
Traceback (most recent call last):
ValueError: Astronauts are selected between age of 30-50 years


Example
-------
>>> class Point:
...     def __init__(self, x, y, z=0):
...         self.x = x
...         self.y = y
...         self.z = z
>>>
>>>
>>> p1 = Point(10, 20)
>>> p2 = Point(x=10, y=20)
>>> p3 = Point(10, 20, 30)
>>> p4 = Point(10, 20, z=30)
>>> p5 = Point(x=10, y=20, z=30)


Checking Values
---------------
>>> class Point:
...     x: int
...     y: int
...
...     def __init__(self, x, y):
...         if x < 0 or y < 0:
...             raise ValueError('Coordinate cannot be negative')
...         self.x = x
...         self.y = y
>>>
>>>
>>> point1 = Point(x=1, y=2)
>>> vars(point1)
{'x': 1, 'y': 2}
>>>
>>> point2 = Point(x=-1, y=-2)
Traceback (most recent call last):
ValueError: Coordinate cannot be negative


Use Case - 0x01
---------------
>>> class Iris:
...     def __init__(self, sepal_length, sepal_width,
...                  petal_length, petal_width, species):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species
>>>
>>>
>>> setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
>>>
>>> vars(setosa)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.1,
 'sepal_width': 3.5,
 'petal_length': 1.4,
 'petal_width': 0.2,
 'species': 'setosa'}


Use Case - 0x02
---------------
>>> class Iris:
...     def __init__(self, sepal_length, sepal_width,
...                  petal_length, petal_width, species):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species
>>>
>>>
>>> virginica = Iris(
...     sepal_length=5.8,
...     sepal_width=2.7,
...     petal_length=5.1,
...     petal_width=1.9,
...     species='virginica')
>>>
>>> vars(virginica)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': 5.1,
 'petal_width': 1.9,
 'species': 'virginica'}


Use Case - 0x03
---------------
* Dataclasses

Since Python 3.7: there is a ``@dataclass`` decorator, which automatically
generates ``__init__()`` arguments and fields. More information in
`OOP Dataclass`.

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str = 'Iris'
>>>
>>>
>>> virginica = Iris(
...     sepal_length=5.8,
...     sepal_width=2.7,
...     petal_length=5.1,
...     petal_width=1.9,
...     species='virginica')
>>>
>>> vars(virginica)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': 5.1,
 'petal_width': 1.9,
 'species': 'virginica'}


Use Case - 0x04
---------------
>>> class Kelvin:
...     value: float
...     MINIMAL_VALUE = 0.0
...
...     def __init__(self, value):
...         if value < self.MINIMAL_VALUE:
...             raise ValueError('Temperature must be greater than 0')
...         self.value = value
>>>
>>>
>>> t1 = Kelvin(273.15)
>>> print(t1.value)
273.15
>>>
>>> t2 = Kelvin(-300)
Traceback (most recent call last):
ValueError: Temperature must be greater than 0


Use Case - 0x05
---------------
* Boundaries

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     def __init__(self, x, y, z):
...         if not 0 <= x < 1024:
...             raise ValueError(f'{x} is out of boundary')
...         elif not 0 <= y < 1024:
...             raise ValueError(f'{y} is out of boundary')
...         elif not 0 <= z < 1024:
...             raise ValueError(f'{z} is out of boundary')
...         else:
...             self.x = x
...             self.y = y
...             self.z = z
>>>
>>>
>>> point1 = Point(x=-10, y=1, z=0)
Traceback (most recent call last):
ValueError: -10 is out of boundary


Use Case - 0x06
---------------
* Parametrized Boundaries

>>> class Point:
...     x: int
...     y: int
...     z: int
...
...     X_MIN: int = 0
...     X_MAX: int = 1024
...     Y_MIN: int = 0
...     Y_MAX: int = 1024
...     Z_MIN: int = 20
...     Z_MAX: int = 500
...
...     def __init__(self, x: int, y: int, z: int):
...         if not self.X_MIN <= x < self.X_MAX:
...             raise ValueError(f'{x=} is out of boundary {self.X_MIN}, {self.X_MAX}')
...         elif not self.Y_MIN <= y < self.Y_MAX:
...             raise ValueError(f'{y=} is out of boundary {self.Y_MIN}, {self.Y_MAX}')
...         elif not self.Z_MIN <= z < self.Z_MAX:
...             raise ValueError(f'{z=} is out of boundary {self.Z_MIN}, {self.Z_MAX}')
...         else:
...             self.x = x
...             self.y = y
...             self.z = z
>>>
>>>
>>> point1 = Point(x=-10, y=1, z=0)
Traceback (most recent call last):
ValueError: x=-10 is out of boundary 0, 1024


Assignments
-----------
.. literalinclude:: assignments/oop_init_a.py
    :caption: :download:`Solution <assignments/oop_init_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_init_b.py
    :caption: :download:`Solution <assignments/oop_init_b.py>`
    :end-before: # Solution
