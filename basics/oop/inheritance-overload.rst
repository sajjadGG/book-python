OOP Inheritance Overload
========================
* Child inherits all fields and methods from parent
* Used to avoid code duplication
* When child has method or attribute with the same name as parent
* In such case child attribute will be used (will overload parent)

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
...         self.firstname = 'Junior'
...         self.lastname = 'Watney'
>>>
>>>
>>> obj = Child()
>>> vars(obj)
{'firstname': 'Junior', 'lastname': 'Watney'}


.. todo:: Assignments
