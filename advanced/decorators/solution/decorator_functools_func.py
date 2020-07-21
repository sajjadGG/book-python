from functools import wraps


def mydecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@mydecorator
def hello():
    """Hello Docstring"""
    pass


print('Function:', hello.__name__)
# Function: hello

print('Doctring:', hello.__doc__)
# Doctring: Hello Docstring
