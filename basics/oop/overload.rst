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
>>> class Person:
...     def say_hello(self):
...         print('Hello Person')
>>>
>>>
>>> class Astronaut(Person):
...     def say_hello(self):
...         print('Hello Astronaut')
>>>
>>>
>>> a = Astronaut()
>>> a.say_hello()
Hello Astronaut


Super Method
------------
>>> class Person:
...     def say_hello(self):
...         print('Hello Person')
>>>
>>>
>>> class Astronaut(Person):
...     def say_hello(self):
...         print('Hello Astronaut')
...         super().say_hello()
>>>
>>>
>>> a = Astronaut()
>>> a.say_hello()
Hello Astronaut
Hello Person

>>> class Person:
...     def say_hello(self):
...         print('Hello Person')
>>>
>>>
>>> class Astronaut(Person):
...     def say_hello(self):
...         super().say_hello()
...         print('Hello Astronaut')
>>>
>>>
>>> a = Astronaut()
>>> a.say_hello()
Hello Person
Hello Astronaut


Super Attributes
----------------
Call to __init__ of super class is missed:

>>> class Person:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         self.job = 'astronaut'
>>>
>>>
>>> astro = Astronaut()
>>> print(vars(astro))
{'job': 'astronaut'}

Call ``super().__init__()`` after initialization:

>>> class Person:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.job = 'unemployed'
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         self.job = 'astronaut'
...         super().__init__()
>>>
>>>
>>> astro = Astronaut()
>>> print(vars(astro))
{'job': 'unemployed', 'firstname': 'Mark', 'lastname': 'Watney'}

Call ``super().__init__()`` before initialization:

>>> class Person:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         super().__init__()
...         self.job = 'astronaut'
>>>
>>>
>>> astro = Astronaut()
>>> print(vars(astro))
{'firstname': 'Mark', 'lastname': 'Watney', 'job': 'astronaut'}


Inheritance Problem
-------------------
>>> class Car:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>> class Truck:
...     def engine_start(self): ...
...     def engine_stop(self): ...

Simple Inheritance:

>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>>
>>> class Car(Vehicle):
...     pass
>>>
>>> class Truck(Vehicle):
...     pass


>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>>
>>> class Car(Vehicle):
...     pass
>>>
>>> class Truck(Vehicle):
...     pass
>>>
>>> class Motorcycle(Vehicle):
...     pass

.. figure:: img/uml-relations-inheritance-simple.png

Inheritance Problem:

>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>>
>>> class Car(Vehicle):
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>>
>>> class Truck(Vehicle):
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>>
>>> class Motorcycle(Vehicle):
...     pass

Not Implemented Error:

>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>>
>>> class Car(Vehicle):
...     pass
>>>
>>> class Truck(Vehicle):
...     pass
>>>
>>> class Motorcycle(Vehicle):
...     def windows_open(self): raise NotImplementedError
...     def windows_close(self): raise NotImplementedError

Multilevel Inheritance:

>>> class Vehicle:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>> class VehicleWithWindows(Vehicle):
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>>
>>> class Car(VehicleWithWindows):
...     pass
>>>
>>> class Truck(VehicleWithWindows):
...     pass
>>>
>>> class Motorcycle(Vehicle):
...     pass

.. figure:: img/uml-relations-inheritance-multilevel.png

Mixin Classes:

>>> class HasEngine:
...     def engine_start(self): ...
...     def engine_stop(self): ...
>>>
>>> class HasWindows:
...     def window_open(self): ...
...     def window_close(self): ...
>>>
>>>
>>> class Car(HasEngine, HasWindows):
...     pass
>>>
>>> class Truck(HasEngine, HasWindows):
...     pass
>>>
>>> class Motorcycle(HasEngine):
...     pass

.. figure:: img/uml-relations-mixin.png


Assignments
-----------
.. literalinclude:: assignments/oop_overload_a.py
    :caption: :download:`Solution <assignments/oop_overload_a.py>`
    :end-before: # Solution
