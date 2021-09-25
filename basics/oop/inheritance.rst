OOP Inheritance
===============


Rationale
---------
* Child inherits all fields and methods from parent
* Used to avoid code duplication

.. glossary::

    parent
    superclass
    base class
        Class from other classes inherits

    child
    subclass
        Class which inherits from :term:`parent`

    inherit
    derive
        Class takes attributes and methods from parent.


Methods
-------
>>> class Parent:
...     def say_hello(self):
...         return 'Hello'
>>>
>>> class Child(Parent):
...     pass
>>>
>>>
>>> obj = Child()
>>> obj.say_hello()
'Hello'


Attributes
----------
>>> class Person:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> class Astronaut(Person):
...     pass
>>>
>>> class Cosmonaut(Person):
...     pass
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> ivan = Cosmonaut('Ivan', 'Ivanovic')


Use Case - Iris
---------------
>>> class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str
...
...     def __init__(self, sepal_length, sepal_width,
...                  petal_length, petal_width, species):
...         self.sepal_length = sepal_length
...         self.sepal_width = sepal_width
...         self.petal_length = petal_length
...         self.petal_width = petal_width
...         self.species = species
>>>
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>> class Versicolor(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
>>>
>>>
>>> setosa = Setosa(
...     sepal_length=5.1,
...     sepal_width=3.5,
...     petal_length=1.4,
...     petal_width=0.2,
...     species='setosa')


References
----------
.. [#Hettinger2015] https://www.youtube.com/watch?v=EiOglTERPEo


Assignments
-----------
.. literalinclude:: assignments/oop_inheritance_a.py
    :caption: :download:`Solution <assignments/oop_inheritance_a.py>`
    :end-before: # Solution
