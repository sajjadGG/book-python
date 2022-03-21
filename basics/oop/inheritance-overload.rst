OOP Inheritance Overload
========================


Important
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


Overload Attribute
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


.. todo:: Assignments
