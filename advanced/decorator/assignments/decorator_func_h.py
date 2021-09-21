"""
* Assignment: Decorator Function TypeCheck
* Complexity: hard
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Modify decorator `typecheck`
    2. Decorator checks types of all arguments (`*args` oraz `**kwargs`)
    3. Decorator checks return type
    4. When received type is not expected raise `TypeError` with:
       a. argument name
       b. actual type
       c. expected type
    5. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj dekorator `typecheck`
    2. Dekorator sprawdza typy wszystkich argumentów (`*args` oraz `**kwargs`)
    3. Dekorator sprawdza typ zwracany
    4. Gdy otrzymany typ nie jest równy oczekiwanemu podnieś `TypeError` z:
       a. nazwa argumentu
       b. aktualny typ
       c. oczekiwany typ
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Merge dict since Python 3.9: `dict1 | dict2`
    * Merge dict in Python 3.7, 3.8: `{**dict1, **dict2)}`
    * Convert args into dict: `dict(zip(func.__annotations__.keys(), args))`
    * `echo.__annotations__`
    # {'a': <class 'str'>,
    #  'b': <class 'int'>,
    #  'c': <class 'float'>,
    #  'return': <class 'bool'>}
    * `dict(zip(...))`
    * `kwargs.items()`
    * `list(kwargs.items())[:-1]`
    * `dict1 | dict2` - merging dicts since Python 3.9

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(typecheck), \
    'Create typecheck() function'

    >>> assert isfunction(typecheck(lambda: ...)), \
    'typecheck() should take function as an argument'

    >>> @typecheck
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

    >>> @typecheck
    ... def echo(a: str, b: int, c: float = 0.0) -> bool:
    ...     return str(a * b)
    >>>
    >>> echo('one', 1, 1.1)
    Traceback (most recent call last):
    TypeError: "return" is <class 'str'>, but <class 'bool'> was expected
"""


def typecheck(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


# Solution
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
