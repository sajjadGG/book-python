Decorator About Object
======================
* Decorating function
* Decorating class
* Decorating method


Decorating Function
-------------------
* By convention ``func`` or ``fn``

>>> def mydecorator(func):
...     ...

>>> class MyDecorator:
...     def __init__(self, func):
...         ...


Decorating Class
----------------
* By convention ``cls``

>>> def mydecorator(cls):
...     ...

>>> class MyDecorator:
...     def __init__(self, cls):
...         ...


Decorating Method
-----------------
* By convention ``mth``, ``meth`` or ``method``

>>> def mydecorator(mth):
...     ...

>>> class MyDecorator:
...     def __init__(self, mth):
...         ...
