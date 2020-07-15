from functools import wraps


def mydecorator(happy=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


@mydecorator(happy=False)
def hello(name):
    """Hello docstring"""
    return f'My name is... {name}'


name = hello('José Jiménez')

print(hello.__doc__)
print(hello.__name__)
