Decorator Wrapper
=================
* ``func`` is a reference to function which is being decorated
* Name ``wrapper`` is just a convention
* Wrapper can be: function, method, lambda or class
* If you know names of the arguments you can use it in wrapper
* Use ``*args``, ``**kwargs`` if you don't know the number of arguments


Names
-----
* ``func`` is a reference to function which is being decorated
* Name ``wrapper`` is just a convention

>>> def mydecorator(func):
...     def wrapper():
...         ...
...     return wrapper

>>> def mydecorator(func):
...     def wrap():
...         ...
...     return wrap

Underscore ``_`` is a normal identifier name which can be used as a wrapper
name. Note, that this is a bit less readable than previous examples:

>>> def mydecorator(func):
...     def _():
...         ...
...     return _


Arguments
---------
* If you know names of the arguments you can use it in wrapper
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

>>> def mydecorator(func):
...     def wrapper(a, b):
...         return func(a, b)
...     return wrapper

Positional Arguments:

>>> def mydecorator(func):
...     def wrapper(*args):
...         return func(*args)
...     return wrapper

Keyword Arguments:

>>> def mydecorator(func):
...     def wrapper(**kwargs):
...         return func(**kwargs)
...     return wrapper

Positional and Keyword Arguments:

>>> def mydecorator(func):
...     def wrapper(*args, **kwargs):
...         return func(*args, **kwargs)
...     return wrapper


Types
-----
Function:

>>> def mydecorator(func):
...     def wrapper(*args, **kwargs):
...         return func(*args, **kwargs)
...     return wrapper

Lambda:

>>> def mydecorator(func):
...     return lambda *args, **kwargs: func(*args, **kwargs)

Class:

>>> def mydecorator(func):
...     class Wrapper:
...         def __init__(self, *args, **kwargs):
...             ...
...     return Wrapper

Method:

>>> class MyDecorator:
...     def __init__(self, obj):
...         ...
...
...     def __call__(self, *args, **kwargs):  # wrapper
...         ...
