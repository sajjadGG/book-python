def mydecorator(cls):
    class Wrapper(cls):
        attribute = 'some value...'
        __doc__ = cls.__doc__
        __name__ = cls.__name__
    return Wrapper


@mydecorator
class Hello:
    """Some documentation"""


hello = Hello()
print('Class:', hello.__name__)
print('Doctring:', hello.__doc__)
