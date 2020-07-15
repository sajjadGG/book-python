from typing import Callable


class CheckType:
    def __init__(self, func: Callable) -> None:
        self._func = func

    def __call__(self, *args, **kwargs):
        self.check_positional(self._func, args)
        self.check_keyword(self._func, kwargs)
        return self._func(*args, **kwargs)

    def check_positional(self, func: Callable, args: tuple):
        expected = func.__annotations__.copy()
        expected.pop('return')

        for arg, exp in zip(args, expected.values()):
            if not isinstance(arg, exp):
                raise TypeError(f'Argument {arg} is {type(arg)}, but {exp} was expected')

    def check_keyword(self, func: Callable, kwargs: dict):
        expected = func.__annotations__.copy()

        for argname, argvalue in kwargs.items():
            exp = expected.get(argname)
            if not isinstance(argvalue, exp):
                raise TypeError(f'Argument {argname} is {type(argname)}, but {exp} was expected')


@CheckType
def echo(a: str, b: int, c: int = 0) -> bool:
    return a * b


print(echo('a', 2))
print(echo('a', 2))
print(echo('b', 2))
print(echo(a='b', b=2))
print(echo(b=2, a='b'))
print(echo('b', b=2))
