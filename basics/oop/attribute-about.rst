OOP Attribute About
===================


Rationale
---------
* Attributes are also known as "Properties" or "Fields"
* Attributes store information for instances
* Access field values using dot (``.``) notation

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


What are attributes?
--------------------
Identifiers and scalars creates values:

>>> point_x: int
>>> point_y: int
>>> point_z: int

Values with relations creates structure:

>>> point: tuple[int,int,int]

Data with meaning creates data:

>>> point: dict[str,int]

Information with context and relations creates information:

>>> class Point:
...     x: int
...     y: int
...     z: int


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


Use Case - Laptop
-----------------
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


Use Case - Date
---------------
>>> class Date:
...     year: int
...     month: int
...     day: int
>>>
>>>
>>> # Gagarin - first man to leave Earth
>>> gagarin = Date()
>>> gagarin.year = 1961
>>> gagarin.month = 4
>>> gagarin.day = 12
>>>
>>> # Armstrong - first man to walk on the Moon
>>> armstrong = Date()
>>> armstrong.year = 1969
>>> armstrong.month = 7
>>> armstrong.day = 21


Use Case - Relation
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
...     height: float
...     weight: float


Good Practices
--------------
* ``snake_case`` name convention
* Attributes should be defined only in ``__init__()`` method
* More information in `OOP Init Method`


References
----------
.. [glassimg] https://media.istockphoto.com/vectors/glasses-set-for-water-glasses-full-empty-halffilled-with-water-vector-vector-id905957960?k=6&m=905957960&s=612x612&w=0&h=DE0uCDCehEA_eDHzHW38jvhl3pYjNuoqXZ_6ZzHbz0M=


Assignments
-----------
.. tood:: Create assignment
