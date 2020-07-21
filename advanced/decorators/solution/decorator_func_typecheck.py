from typing import Callable, NoReturn



def check_types(func: Callable) -> Callable:
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

    def wrapper(*args, **kwargs):
        check_positional(func, args)
        check_keyword(func, kwargs)
        return func(*args, **kwargs)
    return wrapper


@check_types
def isworking(a: str, b: int, c: float = 0) -> bool:
    return True
