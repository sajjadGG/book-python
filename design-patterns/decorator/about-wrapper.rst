Decorator Wrapper
=================
* Wrapper function
* Wrapper lambda
* Wrapper class
* Wrapper method


Name
----
* Name ``wrapper`` is just a convention

>>> def mydecorator(obj):
...     def wrapper():
...         ...
...     return wrapper

>>> def mydecorator(obj):
...     def wrap():
...         ...
...     return wrap

Underscore ``_`` is a normal identifier name which can be used as a wrapper
name. Note, that this is a bit less readable than previous examples:

>>> def mydecorator(obj):
...     def _():
...         ...
...     return _


Wrapper Function
----------------
* ``obj`` is a decorated object
* Doesn't matter, whether is a function, class or method

>>> def mydecorator(obj):
...     def wrapper(*args, **kwargs):
...         ...
...     return wrapper


Wrapper Lambda
--------------
* ``obj`` is a decorated object
* Doesn't matter, whether is a function, class or method

>>> def mydecorator(obj):
...     return lambda *args, **kwargs: obj(*args, **kwargs)


Wrapper Class
-------------
* If ``obj`` and ``Wrapper`` are classes, ``Wrapper`` can inherit from ``obj`` (to extend it)

>>> def mydecorator(obj):
...     class Wrapper:
...         def __init__(self, *args, **kwargs):
...             ...
...     return Wrapper

>>> def mydecorator(obj):
...     class Wrapper(obj):
...         def __init__(self, *args, **kwargs):
...             ...
...     return Wrapper


Wrapper Arguments
-----------------
* If you know names of the arguments you can use it in wrapper
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

>>> def mydecorator(obj):
...     def wrapper(a, b):
...         return func(a, b)
...     return wrapper

Positional Arguments:

>>> def mydecorator(obj):
...     def wrapper(*args):
...         return func(*args)
...     return wrapper

Keyword Arguments:

>>> def mydecorator(obj):
...     def wrapper(**kwargs):
...         return func(**kwargs)
...     return wrapper

Positional and Keyword Arguments:

>>> def mydecorator(obj):
...     def wrapper(*args, **kwargs):
...         return func(*args, **kwargs)
...     return wrapper
