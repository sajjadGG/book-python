def check_types(func):
    arg_types = func.__annotations__.copy()
    return_type = arg_types.pop('return')



    def check(*args, **kwargs):

        for i, value in enumerate(args):
            required_type = list(arg_types.values())[i]

            if not isinstance(value, required_type):
                raise TypeError(f'Argument ``{i}`` has to be "{required_type}"')

        for arg, value in kwargs.items():
            required_type = arg_types[arg]

            if not isinstance(value, required_type):
                raise TypeError(f'Argument ``{arg}`` has to be "{required_type}"')

        return func(*args, **kwargs)

    return check


@check_types
def function(a: str, b: int) -> bool:
    return bool(a * b)


out = function('hello', 3.5, 3)

print(out)
