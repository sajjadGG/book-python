OOP Method About
================


Rationale
---------


Method Names
------------
* ``name(self)`` - public method
* ``_name(self)`` - protected method (non-public by convention)
* ``__name(self)`` - private method (name mangling)
* ``__name__(self)`` - system method
* ``name_(self)`` - avoid name collision with built-ins


Method Types
------------
Dynamic methods:

>>> class MyClass:
...     def mymethod(self):
...         pass

Static methods:

>>> class MyClass:
...     @staticmethod
...     def mymethod():
...         pass

Class methods:

>>> class MyClass:
...     @classmethod
...     def mymethod(cls):
...         pass
