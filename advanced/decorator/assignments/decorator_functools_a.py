"""
* Assignment: Decorator Functools Func
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

    >>> assert isfunction(mydecorator(lambda: ...)), \
    'mydecorator() should take function as an argument'

    >>> @mydecorator
    ... def hello():
    ...     '''Hello Docstring'''

    >>> hello.__name__
    'hello'
    >>> hello.__doc__
    'Hello Docstring'
"""

from functools import wraps


# type: Callable[[Callable], Callable]
def mydecorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


# Solution
def mydecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
