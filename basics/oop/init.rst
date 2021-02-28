OOP Init Method
===============


Rationale
---------
* It's a first method run after object is initiated
* All classes has default ``__init__()``

.. glossary::

    constructor
        Method called at object instantiation used to create object. Constructor is called on not fully initialized object and hence do not have access to object methods. Constructor should return ``None``.

    initializer
        Method called at object instantiation used to fill empty object with values. Initializer is called upon object initialization and hence can modify object and use its methods. Initializer should return ``None``.


Syntax
------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> print(astro.firstname)
Mark
>>> print(astro.lastname)
Watney


Initializer Method Without Arguments
------------------------------------
Initializer method without arguments:

>>> class Astronaut:
...     def __init__(self):
...         print('My name... José Jiménez')
>>>
>>>
>>> jose = Astronaut()
My name... José Jiménez


Initializer Method With Arguments
---------------------------------
Initializer method with arguments:

>>> class Astronaut:
...     def __init__(self, firstname, lastname='Unknown'):
...         print(f'My name... {firstname} {lastname}')
>>>
>>>
>>> jan = Astronaut('Jan')
My name... Jan Unknown
>>> jose = Astronaut('José', 'Jiménez')
My name... José Jiménez
>>> melissa = Astronaut('Melissa', lastname='Lewis')
My name... Melissa Lewis
>>> mark = Astronaut(firstname='José', lastname='Jiménez')
My name... José Jiménez
>>> ryan = Astronaut(lastname='Stone', firstname='Ryan')
My name... Ryan Stone
>>> ivan = Astronaut()
Traceback (most recent call last):
TypeError: __init__() missing 1 required positional argument: 'firstname'


Constant Attributes
-------------------
Init time attributes:

>>> class Astronaut:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
>>>
>>>
>>> mark = Astronaut()
>>> print(mark.firstname)
Mark
>>> print(mark.lastname)
Watney
>>> print(mark.missions)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'mission'
>>>
>>> ivan = Astronaut()
>>> print(ivan.firstname)
Mark
>>> print(ivan.lastname)
Watney
>>> print(ivan.missions)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'mission'


Variable Attributes
-------------------
>>> class Astronaut:
...     def __init__(self, a, b):
...         self.firstname = a
...         self.lastname = b
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> print(mark.firstname)
Mark
>>> print(mark.lastname)
Watney
>>>
>>> ivan = Astronaut(a='Ivan', b='Ivanovich')
>>> print(ivan.firstname)
Ivan
>>> print(ivan.lastname)
Ivanovich

Init time attributes:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> print(mark.firstname)
Mark
>>> print(mark.lastname)
Watney
>>>
>>> ivan = Astronaut(firstname='Ivan', lastname='Ivanovich')
>>> print(ivan.firstname)
Ivan
>>> print(ivan.lastname)
Ivanovich

Init time attributes:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.name = f'{firstname} {lastname}'
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>>
>>> print(mark.name)
Mark Watney
>>> print(mark.firstname)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'firstname'
>>> print(mark.lastname)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute 'lastname'

Init time attributes:

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

Init time attributes:

>>> class Iris:
...     def __init__(self, sepal_length, sepal_width,
...                  petal_length, petal_width, species):
...
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species
>>>
>>>
>>> setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
>>>
>>> print(setosa.sepal_length)
5.1
>>> print(setosa.sepal_width)
3.5
>>> print(setosa.petal_length)
1.4
>>> print(setosa.petal_width)
0.2
>>> print(setosa.species)
setosa
>>>
>>>
>>> virginica = Iris(
...     sepal_length=5.8,
...     sepal_width=2.7,
...     petal_length=5.1,
...     petal_width=1.9,
...     species='virginica')
>>>
>>> print(virginica.__dict__)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': 5.1,
 'petal_width': 1.9,
 'species': 'virginica'}

Since Python 3.7: there is a ``@dataclass`` decorator, which automatically generates ``__init__()`` arguments and fields.
More information in `OOP Dataclass`

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
>>> setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
>>>
>>> print(setosa.sepal_length)
5.1
>>> print(setosa.sepal_width)
3.5
>>> print(setosa.petal_length)
1.4
>>> print(setosa.petal_width)
0.2
>>> print(setosa.species)
setosa
>>>
>>>
>>> virginica = Iris(
...     sepal_length=5.8,
...     sepal_width=2.7,
...     petal_length=5.1,
...     petal_width=1.9,
...     species='virginica')
>>>
>>> print(virginica.__dict__)  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': 5.1,
 'petal_width': 1.9,
 'species': 'virginica'}


Checking Values
---------------
>>> class Kelvin:
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


Assignments
-----------
.. literalinclude:: assignments/oop_init_a.py
    :caption: :download:`Solution <assignments/oop_init_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_init_b.py
    :caption: :download:`Solution <assignments/oop_init_b.py>`
    :end-before: # Solution
