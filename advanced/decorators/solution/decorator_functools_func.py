from functools import wraps


def mydecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@mydecorator
def hello(name):
    """Some documentation"""
    return f'My name... {name}'


hello('José Jiménez')

print('Function:', hello.__name__)
print('Doctring:', hello.__doc__)
