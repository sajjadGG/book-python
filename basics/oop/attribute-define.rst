OOP Attribute Set
=================


Syntax
------
* Optional attribute annotation

>>> class MyClass:
...     myattribute: str



Example
-------
>>> class Astronaut:
...     pass

>>> class Astronaut:
...     firstname: str
...     lastname: str


Namespace
---------
Unrelated values:

>>> x: int
>>> y: int
>>> z: int

Class creates space, in which names has meaning:

>>> class Point:
...     x: int
...     y: int
...     z: int


Different Types
---------------
>>> class Iris:
...     features: list[float]
...     label: str

>>> # doctest: +SKIP
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: float|int
...     height: float
...     weight: float
...     missions: list
...     experience: list|None


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
...     date_of_birth: Date


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


References
----------
.. [glassimg] https://media.istockphoto.com/vectors/glasses-set-for-water-glasses-full-empty-halffilled-with-water-vector-vector-id905957960?k=6&m=905957960&s=612x612&w=0&h=DE0uCDCehEA_eDHzHW38jvhl3pYjNuoqXZ_6ZzHbz0M=


Assignments
-----------
.. literalinclude:: assignments/oop_attribute_a.py
    :caption: :download:`Solution <assignments/oop_attribute_a.py>`
    :end-before: # Solution
