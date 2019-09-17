def is_numeric(*args, **kwargs) -> bool:
    """
    >>> is_numeric(1)
    True
    >>> is_numeric(1.5)
    True
    >>> is_numeric('one', a=1)
    False
    >>> is_numeric([1, 1.5])
    False
    >>> is_numeric()
    False
    >>> is_numeric(True)
    False
    >>> is_numeric(a=1)
    True
    >>> is_numeric(a='one')
    False
    """
    args = args + tuple(kwargs.values())

    if len(args) == 0:
        return False

    for arg in args:
        if type(arg) not in (float, int):
            return False

    return True
