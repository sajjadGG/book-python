OOP Method About
================
* Methods are functions in the class
* Prevents copy-paste code
* Improves readability
* Improves refactoring
* Decomposes bigger problem into smaller chunks

.. glossary::

    method
        Functions in the class which takes instance as first argument (``self``)

    self
        Instance on which method was called.


Syntax
------
>>> class MyClass:
...     def mymethod(self):
...         pass
>>>
>>>
>>> my = MyClass()
>>> my.mymethod()


Define
------
* At definition - ``self`` should always be a first parameter

>>> class Astronaut:
...     def say_hello(self):
...         print('hello')


Self
----
* At definition - ``self`` should always be a first parameter
* At call - ``self`` is not passed as an argument (Python will do that)
* Later you will learn more advanced things like static methods etc.


Call
----
* At call - ``self`` is not passed as an argument (Python will do that)


Return
------


.. todo:: Assignments
