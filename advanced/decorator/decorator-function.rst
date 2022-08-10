Decorator Function
==================
* ``func`` is a reference to function which is being decorated
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments
* By calling ``func(*args, **kwargs)`` you actually run original (wrapped) function with it's original arguments

Definition:

>>> def mydecorator(func):
...     def wrapper(*args, **kwargs):
...         return func(*args, **kwargs)
...     return wrapper

Usage:

>>> @mydecorator
... def say_hello():
...     return 'hello'
>>>
>>>
>>> say_hello()
'hello'


Assignments
-----------
.. literalinclude:: assignments/decorator_function_a.py
    :caption: :download:`Solution <assignments/decorator_function_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/decorator_function_b.py
    :caption: :download:`Solution <assignments/decorator_function_b.py>`
    :end-before: # Solution
