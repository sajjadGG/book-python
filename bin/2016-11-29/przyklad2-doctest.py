
def foo1():
    """
    >>> foo()
    'asd'
    """
    napis = 'asd'
    return napis


def foo2():
    """
    >>> foo()
    asd
    """
    napis = 'asd'
    print(napis)


if __name__ == '__main__':
    import doctest
    doctest.testmod()