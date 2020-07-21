from functools import wraps


def mydecorator(happy=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


@mydecorator(happy=False)
def hello():
    """Hello Docstring"""
    pass


print('Function:', hello.__name__)
# Function: hello

print('Doctring:', hello.__doc__)
# Doctring: Hello Docstring
