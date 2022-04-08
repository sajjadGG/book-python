OOP Attribute Define
====================
* Attribute Annotation is optional, but a good practice


No Attribute Definition
-----------------------
>>> class Astronaut:
...     pass


Basic Types
-----------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int


Union
-----
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int | float


Optional
--------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int | float
...     height: float | None
...     weight: float | None


Sequences
---------
* Since Python 3.9 you can use ``list[str]``
* Before Python 3.9 use ``list`` without specifying type of elements inside

>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int
...     missions: list[str]


Relation One to One
-------------------
>>> class Date:
...     year: int
...     month: int
...     day: int
>>>
>>>
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     born: Date


Relation One to Many
--------------------
>>> class Mission:
...     year: int
...     name: str
>>>
>>>
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[Mission]


Example
-------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     agency: str
...     flown: bool
...     age: int | float
...     height: float | None
...     weight: float | None
...     missions: list[str] | None
...     friends: list['Astronaut'] | None


Good Practices
--------------
* ``snake_case`` name convention
* Attributes should be defined only in ``__init__()`` method
* More information in `OOP Init Method`


Use Case - 0x01
---------------
>>> class Point:
...     x: int
...     y: int
...     z: int


Use Case - 0x02
---------------
>>> class Date:
...     year: int
...     month: int
...     day: int


Use Case - 0x03
---------------
>>> class Laptop:
...     cpu: str
...     ram: str
...     ssd: str


Use Case - 0x04
---------------
>>> class Iris:
...     features: list[float]
...     label: str


Use Case - 0x05
---------------
>>> class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_define_a.py
    :caption: :download:`Solution <assignments/oop_attribute_define_a.py>`
    :end-before: # Solution
