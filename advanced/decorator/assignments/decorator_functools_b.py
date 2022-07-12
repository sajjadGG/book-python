"""
* Assignment: Decorator Functools Args
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `functools.wraps` in correct place
    2. Run doctests - all must succeed

Polish:
    1. Użyj `functools.wraps` w odpowiednim miejscu
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(mydecorator), \
    'Create mydecorator() function'

    >>> assert isfunction(mydecorator(True)), \
    'mydecorator() should take one positional argument'

    >>> assert isfunction(mydecorator(happy=True)), \
    'mydecorator() should take one keyword argument'

    >>> assert isfunction(mydecorator(happy=True)(lambda: ...)), \
    'The result of mydecorator() should take function as an argument'

    >>> @mydecorator(happy=False)
    ... def hello():
    ...     '''Hello Docstring'''
    >>> hello.__name__
    'hello'
    >>> hello.__doc__
    'Hello Docstring'
"""

from functools import wraps


# type: Callable[[bool], Callable]
def mydecorator(happy=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Solution
def mydecorator(happy=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator
