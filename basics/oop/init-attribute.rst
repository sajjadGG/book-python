OOP Init Attribute
==================


Important
---------
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



Constant Attributes
-------------------
>>> class Astronaut:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
>>>
>>>
>>> mark = Astronaut()
>>> melissa = Astronaut()
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
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


Better Names
------------
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


Assignments
-----------
.. literalinclude:: assignments/oop_init_attribute_a.py
    :caption: :download:`Solution <assignments/oop_init_attribute_a.py>`
    :end-before: # Solution
