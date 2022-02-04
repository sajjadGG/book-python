OOP Attribute Define
====================


No Attribute Definition
-----------------------
>>> class Astronaut:
...     pass


Attribute Annotation
--------------------
* Optional
* Good practice

Basic Types:

>>> class Astronaut:
...     firstname: str
...     lastname: str

Sequences:

>>> class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[str]

Union:

>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int | float

Optionals:

>>> class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list | None


Relation One to One
-------------------
>>> class Date:
...     year: int
...     month: int
...     day: int
>>>
>>>
>>> class Person:
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


Good Practices
--------------
* ``snake_case`` name convention
* Attributes should be defined only in ``__init__()`` method
* More information in `OOP Init Method`



>>> class Astronaut:
...     firstname: str
...     lastname: str
...     age: int | float
...     height: float
...     weight: float
...     missions: list
...     experience: list | None

>>> class Iris:
...     features: list[float]
...     label: str


>>> class Point:
...     x: int
...     y: int
...     z: int


Use Case - 0x01
---------------
>>> class Laptop:
...     cpu: float
...     ram: int
...     ssd: int


Use Case - 0x02
---------------
>>> class Date:
...     year: int
...     month: int
...     day: int


Use Case - 0x03
---------------
* Relation

>>> class Date:
...     year: int
...     month: int
...     day: int
>>>
>>>
>>> class Person:
...     firstname: str
...     lastname: str
...     born: Date
...     height: float
...     weight: float


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_define_a.py
    :caption: :download:`Solution <assignments/oop_attribute_define_a.py>`
    :end-before: # Solution
