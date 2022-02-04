OOP Inheritance Define
======================


Inheritance
-----------
>>> class Parent:
...     pass
>>>
>>>
>>> class Child(Parent):
...     pass


Methods
-------
>>> class Parent:
...     def say_hello(self):
...         return 'Hello'
>>>
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
>>> class Parent:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
>>>
>>>
>>> class Child(Parent):
...     pass
>>>
>>>
>>> obj = Child()
>>> vars(obj)
{'firstname': 'Mark', 'lastname': 'Watney'}


Use Case - 0x01
---------------
>>> class Person:
...     pass
>>>
>>>
>>> class Astronaut(Person):
...     pass
>>>
>>> class Cosmonaut(Person):
...     pass


Use Case - 0x02
---------------
>>> class Person:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...
...     def say_hello(self):
...         return 'hello'
>>>
>>>
>>> class Astronaut(Person):
...     pass
>>>
>>> class Cosmonaut(Person):
...     pass


Use Case - 0x03
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
.. literalinclude:: assignments/oop_inheritance_define_a.py
    :caption: :download:`Solution <assignments/oop_inheritance_define_a.py>`
    :end-before: # Solution
