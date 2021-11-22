OOP Inheritance Overload
========================


Rationale
---------
* Child inherits all fields and methods from parent
* Used to avoid code duplication

.. glossary::

    overload
        When :term:`child` has method or attribute with the same name as
        :term:`parent`. In such case :term:`child` attribute will be used
        (will :term:`overload` :term:`parent`).


Method Overload
---------------
>>> class Parent:
...     def say_hello(self):
...         print('hello')
>>>
>>>
>>> class Child(Parent):
...     def say_hello(self):
...         print('yo')
>>>
>>>
>>> obj = Child()
>>> obj.say_hello()
yo


super()
-------
* Calls a method from superclass
* Order/location is important
* Raymond Hettinger - Super considered super! - PyCon 2015 [#Hettinger2015]_


Super With Methods
------------------
>>> class Parent:
...     def say_hello(self):
...         print('hello')
>>>
>>>
>>> class Child(Parent):
...     def say_hello(self):
...         super().say_hello()
...         print('yo')
>>>
>>>
>>> obj = Child()
>>> obj.say_hello()
hello
yo

Order of ``super()`` is important:

>>> class Parent:
...     def say_hello(self):
...         print('hello')
>>>
>>>
>>> class Child(Parent):
...     def say_hello(self):
...         print('yo')
...         super().say_hello()
>>>
>>>
>>> obj = Child()
>>> obj.say_hello()
yo
hello


Attribute Overload
------------------
>>> class Parent:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
>>>
>>>
>>> class Child(Parent):
...     def __init__(self):
...         self.job = 'astronaut'
>>>
>>>
>>> obj = Child()
>>> vars(obj)
{'job': 'astronaut'}


Super With Attributes
---------------------
>>> class Parent:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
>>>
>>>
>>> class Child(Parent):
...     def __init__(self):
...         super().__init__()
...         self.job = 'astronaut'
>>>
>>>
>>> obj = Child()
>>> vars(obj)
{'firstname': 'Mark', 'lastname': 'Watney', 'job': 'astronaut'}


Super Attributes Problem
------------------------
Note, that the problem exists when Parent and a Child defines attribute with the
same name. Than while calling ``super()`` it will overload field value.

>>> class Parent:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.job = 'unemployed'
>>>
>>>
>>> class Child(Parent):
...     def __init__(self):
...         super().__init__()
...         self.job = 'astronaut'
>>>
>>>
>>> obj = Child()
>>> vars(obj)
{'firstname': 'Mark', 'lastname': 'Watney', 'job': 'astronaut'}

>>> class Parent:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.job = 'unemployed'
>>>
>>>
>>> class Child(Parent):
...     def __init__(self):
...         self.job = 'astronaut'
...         super().__init__()
>>>
>>>
>>> obj = Child()
>>> vars(obj)
{'job': 'unemployed', 'firstname': 'Mark', 'lastname': 'Watney'}


Assignments
-----------
.. literalinclude:: assignments/oop_overload_a.py
    :caption: :download:`Solution <assignments/oop_overload_a.py>`
    :end-before: # Solution
