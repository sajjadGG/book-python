from typing import Callable, NoReturn


def check_positional(fn: Callable, args: tuple) -> NoReturn:
    expected = fn.__annotations__.copy()
    expected.pop('return')

    for arg, exp in zip(args, expected.values()):
        if not isinstance(arg, exp):
            raise TypeError(f'Argument {arg} is {type(arg)}, but {exp} was expected')


def check_keyword(fn: Callable, kwargs: dict) -> NoReturn:
    expected = fn.__annotations__.copy()

    for argname, argvalue in kwargs.items():
        exp = expected.get(argname)
        if not isinstance(argvalue, exp):
            raise TypeError(f'Argument {argname} is {type(argname)}, but {exp} was expected')


def check_types(fn: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        check_positional(fn, args)
        check_keyword(fn, kwargs)
        return fn(*args, **kwargs)
    return wrapper


@check_types
def echo(a: str, b: int, c: int = 0) -> bool:
    return bool(a * b)


print(echo('a', 2))
print(echo('a', 2))
print(echo('b', 2))
print(echo(a='b', b=2))
print(echo(b=2, a='b'))
print(echo('b', b=2))
