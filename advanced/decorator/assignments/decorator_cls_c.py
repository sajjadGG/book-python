"""
* Assignment: Decorator Class TypeCheck
* Complexity: medium
* Lines of code: 18 lines
* Time: 13 min

English:
    1. Refactor decorator `decorator` to decorator `TypeCheck`
    2. Decorator checks types of all arguments (`*args` oraz `**kwargs`)
    3. Decorator checks return type
    4. When received type is not expected raise `TypeError` with:
        a. argument name
        b. actual type
        c. expected type
    5. Run doctests - all must succeed

Polish:
    1. Przerób dekorator `decorator` na klasę `TypeCheck`
    2. Dekorator sprawdza typy wszystkich argumentów (`*args` oraz `**kwargs`)
    3. Dekorator sprawdza typ zwracany
    4. Gdy otrzymany typ nie jest równy oczekiwanemu podnieś `TypeError` z:
        a. nazwa argumentu
        b. aktualny typ
        c. oczekiwany typ
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `echo.__annotations__`
    * `dict(zip(...))`
    * `kwargs.items()`
    * `list(kwargs.items())[:-1]`
    * `dict1 | dict2` - merging dicts since Python 3.9

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(TypeCheck), \
    'TypeCheck should be a decorator class'

    >>> assert TypeCheck(lambda: ...), \
    'TypeCheck should take function as an argument'

    >>> assert isinstance(TypeCheck(lambda: ...), TypeCheck), \
    'TypeCheck() should return an object which is an instance of TypeCheck'

    >>> @TypeCheck
    ... def echo(a: str, b: int, c: float = 0.0) -> bool:
    ...     return bool(a * b)

    >>> echo('one', 1)
    True
    >>> echo('one', 1, 1.1)
    True
    >>> echo('one', b=1)
    True
    >>> echo('one', 1, c=1.1)
    True
    >>> echo('one', b=1, c=1.1)
    True
    >>> echo(a='one', b=1, c=1.1)
    True
    >>> echo(c=1.1, b=1, a='one')
    True
    >>> echo(b=1, c=1.1, a='one')
    True
    >>> echo('one', c=1.1, b=1)
    True
    >>> echo(1, 1)
    Traceback (most recent call last):
    TypeError: "a" is <class 'int'>, but <class 'str'> was expected

    >>> echo('one', 'two')
    Traceback (most recent call last):
    TypeError: "b" is <class 'str'>, but <class 'int'> was expected

    >>> echo('one', 1, 'two')
    Traceback (most recent call last):
    TypeError: "c" is <class 'str'>, but <class 'float'> was expected

    >>> echo(b='one', a='two')
    Traceback (most recent call last):
    TypeError: "b" is <class 'str'>, but <class 'int'> was expected

    >>> echo('one', c=1.1, b=1.1)
    Traceback (most recent call last):
    TypeError: "b" is <class 'float'>, but <class 'int'> was expected

    >>> @TypeCheck
    ... def echo(a: str, b: int, c: float = 0.0) -> bool:
    ...     return str(a * b)
    >>>
    >>> echo('one', 1, 1.1)
    Traceback (most recent call last):
    TypeError: "return" is <class 'str'>, but <class 'bool'> was expected
"""
from typing import Optional


def typecheck(func):
    def validate(argname, argval):
        argtype = type(argval)
        expected = func.__annotations__[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, '
                            f'but {expected} was expected')

    def wrapper(*args, **kwargs):
        arguments = kwargs | dict(zip(func.__annotations__.keys(), args))
        [validate(k, v) for k, v in arguments.items()]
        result = func(*args, **kwargs)
        validate('return', result)
        return result

    return wrapper


# class: Refactor typecheck into class
class TypeCheck:
    ...


# Solution
class TypeCheck:
    def __init__(self, func) -> None:
        self._func = func

    def __call__(self, *args, **kwargs):
        self.check_arguments(*args, **kwargs)
        result = self._func(*args, **kwargs)
        self.check_result(result)
        return result

    def check_arguments(self, *args, **kwargs):
        arguments = kwargs | dict(zip(self._func.__annotations__.keys(), args))
        [self.validate(k, v) for k, v in arguments.items()]

    def check_result(self, result):
        self.validate('return', result)

    def validate(self, argname, argval) -> Optional[Exception]:
        argtype = type(argval)
        expected = self._func.__annotations__[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, '
                            f'but {expected} was expected')
