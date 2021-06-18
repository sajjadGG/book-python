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


Syntax
------
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


No Inheritance
--------------
>>> class Parent:
...     pass
>>>
>>>
>>> class Child:
...     pass


Simple Inheritance
------------------
>>> class Parent:
...     pass
>>>
>>>
>>> class Child(Parent):
...     pass


Multilevel Inheritance
----------------------
>>> class Mother:
...     pass
>>>
>>>
>>> class Parent(Mother):
...     pass
>>>
>>>
>>> class Child(Parent):
...     pass


Multiple Inheritance
--------------------
>>> class Mother:
...     pass
>>>
>>>
>>> class Father:
...     pass
>>>
>>>
>>> class Child(Mother, Father):
...     pass


Use Cases
---------
>>> class Person:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
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


Assignments
-----------
.. literalinclude:: assignments/oop_inheritance_a.py
    :caption: :download:`Solution <assignments/oop_inheritance_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_b.py
    :caption: :download:`Solution <assignments/oop_inheritance_b.py>`
    :end-before: # Solution
