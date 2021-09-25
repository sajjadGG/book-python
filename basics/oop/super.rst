OOP Super
=========


Rationale
---------
* Child inherits all fields and methods from parent
* Used to avoid code duplication
* Order is important
* Raymond Hettinger - Super considered super! - PyCon 2015 [#Hettinger2015]_

.. glossary::

    overload
        When :term:`child` has method or attribute with the same name as
        :term:`parent`. In such case :term:`child` attribute will be used
        (will :term:`overload` :term:`parent`).


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


Super with Methods
------------------
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


Super with Attributes
---------------------
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


Assignments
-----------
.. literalinclude:: assignments/oop_overload_a.py
    :caption: :download:`Solution <assignments/oop_overload_a.py>`
    :end-before: # Solution
