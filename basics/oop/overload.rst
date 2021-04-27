OOP Overload
============


Rationale
---------
* Child inherits all fields and methods from parent
* Used to avoid code duplication

.. glossary::

    overload
        When :term:`child` has method or attribute with the same name as
        :term:`parent`. In such case :term:`child` attribute will be used
        (will overload :term:`parent`).


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
>>> Child().say_hello()
'Hello'


Super Function
--------------
>>> class A:
...     def show(self):
...         return 'a'
>>>
>>> class B(A):
...     def show(self):
...         old_value = super().show()
...         return old_value + 'b'
>>>
>>>
>>> B().show()
'ab'

>>> class Engineer:
...     def __init__(self):
...         self.education = 'Engineer'
...         self.profession = 'Engineer'
>>>
>>> class Astronaut(Engineer):
...     def __init__(self):
...         super().__init__()
...         self.profession = 'Astronaut'
>>>
>>>
>>> vars(Astronaut())  # doctest: +NORMALIZE_WHITESPACE
{'education': 'Engineer',
 'profession': 'Astronaut'}

>>> class Engineer:
...     def __init__(self):
...         self.education = 'Engineer'
...         self.profession = 'Engineer'
>>>
>>> class Astronaut(Engineer):
...     def __init__(self):
...         self.profession = 'Astronaut'
...         super().__init__()
>>>
>>>
>>> vars(Astronaut())  # doctest: +NORMALIZE_WHITESPACE
{'profession': 'Engineer',
 'education': 'Engineer'}

>>> class Engineer:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.education = 'Engineer'
...         self.profession = 'Engineer'
>>>
>>> class Astronaut(Engineer):
...     def __init__(self, firstname, lastname):
...         super().__init__(firstname, lastname)
...         self.profession = 'Astronaut'
>>>
>>>
>>> vars(Astronaut('Mark', 'Watney'))  # doctest: +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'education': 'Engineer',
 'profession': 'Astronaut'}


Inheritance vs Composition
--------------------------
>>> class Car:
...     def engine_start(self):
...         print('Starting engine...')
>>>
>>>
>>> class Truck:
...     def engine_start(self):
...         print('Starting engine...')

Simple Inheritance:

>>> class Vehicle:
...     def engine_start(self):
...         print('Starting engine...')
>>>
>>>
>>> class Car(Vehicle):
...     pass
>>>
>>> class Truck(Vehicle):
...     pass

Inheritance Problem:

>>> class Vehicle:
...     def engine_start(self):
...         print('Starting engine...')
>>>
>>>
>>> class Car(Vehicle):
...     def windows_open(self):
...         print('Opening windows...')
>>>
>>>
>>> class Truck(Vehicle):
...     def windows_open(self):
...         print('Opening windows...')
>>>
>>>
>>> class Motorcycle(Vehicle):
...     pass

Not Implemented Error:

>>> class Vehicle:
...     def engine_start(self):
...         print('Starting engine...')
...
...     def windows_open():
...         print('Opening windows...')
>>>
>>>
>>> class Car(Vehicle):
...     pass
>>>
>>> class Truck(Vehicle):
...     pass
>>>
>>> class Motorcycle(Vehicle):
...     def windows_open(self):
...         raise NotImplementedError('Has no windows')

Composition:

>>> class Vehicle:
...     def engine_start(self):
...         print('Starting engine...')
...
...     def engine_stop():
...         print('Stopping engine...')
>>>
>>>
>>> class HasWindows:
...     def windows_open(self):
...         print('Opening windows...')
>>>
>>>
>>> class Car(Vehicle, HasWindows):
...     pass
>>>
>>> class Truck(Vehicle, HasWindows):
...     pass
>>>
>>> class Motorcycle(Vehicle):
...     pass


Use Cases
---------
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
.. literalinclude:: assignments/oop_overload_a.py
    :caption: :download:`Solution <assignments/oop_overload_a.py>`
    :end-before: # Solution
