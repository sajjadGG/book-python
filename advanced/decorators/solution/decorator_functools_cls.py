def mydecorator(cls):
    class Wrapper(cls):
        __doc__ = cls.__doc__
        __name__ = cls.__name__
    return Wrapper


@mydecorator
class Hello:
    """Hello Docstring"""


hello = Hello()

print('Class:', hello.__name__)
# Class: Hello

print('Doctring:', hello.__doc__)
# Doctring: Hello Docstring
