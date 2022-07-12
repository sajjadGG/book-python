"""
* Assignment: Decorator Functools Cls
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Modify code to restore docstring and name from decorated class
    2. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod aby przywrócić docstring oraz nazwę z dekorowanej klasy
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction, isclass

    >>> assert isfunction(mydecorator), \
    'Create mydecorator() function'

    >>> assert mydecorator(object), \
    'mydecorator() should take class as an argument'

    >>> assert isclass(mydecorator(object)), \
    'The result of mydecorator() should be a class'

    >>> @mydecorator
    ... class Hello:
    ...     '''Hello Docstring'''
    >>> hello = Hello()
    >>> hello.__name__
    'Hello'
    >>> hello.__doc__
    'Hello Docstring'
"""


# type: Callable[[Type], Type]
def mydecorator(cls):
    class Wrapper(cls):
        pass

    return Wrapper


# Solution
def mydecorator(cls):
    class Wrapper(cls):
        __doc__ = cls.__doc__
        __name__ = cls.__name__

    return Wrapper
