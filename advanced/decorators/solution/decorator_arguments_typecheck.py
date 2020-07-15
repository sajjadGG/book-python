from typing import Callable, NoReturn


def check_positional(func: Callable, args: tuple) -> NoReturn:
    expected = func.__annotations__.copy()
    expected.pop('return')

    for arg, exp in zip(args, expected.values()):
        if not isinstance(arg, exp):
            raise TypeError(f'Argument {arg} is {type(arg)}, but {exp} was expected')


def check_keyword(func: Callable, kwargs: dict) -> NoReturn:
    expected = func.__annotations__.copy()

    for argname, argvalue in kwargs.items():
        exp = expected.get(argname)
        if not isinstance(argvalue, exp):
            raise TypeError(f'Argument {argname} is {type(argname)}, but {exp} was expected')


def check_result(func, argvalue):
    expected = func.__annotations__['return']

    if not isinstance(argvalue, expected):
        raise TypeError(f'Return is {type(argvalue)}, but {expected} was expected')


def check_types(check_return: bool = False):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            check_positional(func, args)
            check_keyword(func, kwargs)
            result = func(*args, **kwargs)

            if check_return:
                check_result(func, result)

            return result
        return wrapper
    return decorator


@check_types(check_return=False)
def echo(a: str, b: int, c: int = 0) -> bool:
    return a * b


print(echo('a', 2))
print(echo('a', 2))
print(echo('b', 2))
print(echo(a='b', b=2))
print(echo(b=2, a='b'))
print(echo('b', b=2))
