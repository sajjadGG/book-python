def check_types(func):
    arg_types = func.__annotations__.copy()
    arg_types.pop('return')  # not needed

    def check(*args, **kwargs):

        for i, value in enumerate(args):
            required_type = list(arg_types.values())[i]

            if type(value) is not required_type:
                raise TypeError(f'Argument ``{i}`` has to be "{required_type}"')

        for key, value in kwargs.items():
            required_type = arg_types[key]

            if type(value) is not required_type:
                raise TypeError(f'Argument ``{key}`` has to be "{required_type}"')

        return func(*args, **kwargs)
    return check


@check_types
def my_function(a: str, b: int) -> bool:
    return bool(a * b)


my_function('hello', 3.5, 3)
