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


Overload Method
---------------
>>> class Parent:
...     def say_hello(self):
...         print('Parent says good morning')
>>>
>>>
>>> class Child(Parent):
...     def say_hello(self):
...         print('Child says wassup')
>>>
>>>
>>> obj = Child()
>>> obj.say_hello()
Child says wassup


Overload Attribute
------------------
>>> class Parent:
...     def __init__(self):
...         self.firstname = 'Melissa'
...         self.lastname = 'Lewis'
>>>
>>>
>>> class Child(Parent):
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.job = 'astronaut'
>>>
>>>
>>> obj = Child()
>>> vars(obj)
{'firstname': 'Mark', 'lastname': 'Watney', 'job': 'astronaut'}


.. todo:: Assignments
