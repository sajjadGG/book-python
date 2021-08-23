OOP Class Creation
==================


Class Definition
----------------
>>> class MyClass:
...     pass

>>> MyClass = type('MyClass', (), {})


Class Attributes
----------------
>>> class MyClass:
...     myattr = 1

>>> MyClass = type('MyClass', (), {'myattr': 1})


Class Methods
-------------
>>> class MyClass:
...     def mymethod(self):
...         pass

>>> def mymethod(self):
...     pass
>>>
>>> MyClass = type('MyClass', (), {'mymethod': mymethod})


Class Inheritance
-----------------
>>> class Parent:
...     pass
>>>
>>>
>>> class MyClass(Parent):
...     pass

>>> MyClass = type('MyClass', (Parent,), {})


Recap
-----
>>> class Parent:
...     pass
>>>
>>>
>>> class MyClass(Parent):
...     myattr = 1
...
...     def mymethod(self):
...         pass

>>> MyClass = type('MyClass', (Parent,), {'myattr': 1, 'mymethod': mymethod})


Use Case - Dynamic Class Creation
---------------------------------
>>> for classname in ['Astronaut', 'Cosmonaut', 'Taikonaut']:
...     globals()[classname] = type(classname, (), {})

