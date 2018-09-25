C2K_OFFSET = 273.15


def c_to_k(degrees):
    """
    >>> c_to_k(0)
    273.15
    >>> c_to_k(1)
    274.15
    >>> c_to_k(-1)
    272.15
    >>> c_to_k('a')
    Traceback (most recent call last):
        ...
    TypeError: Invalid argument
    >>> c_to_k([0, 1])
    [273.15, 274.15]
    >>> c_to_k((0, 1))
    (273.15, 274.15)
    >>> c_to_k({0, 1})
    {273.15, 274.15}
    """
    if isinstance(degrees, (int, float)):
        return C2K_OFFSET + degrees
    elif isinstance(degrees, (list, tuple, set)):
        what = type(degrees)
        return what(x + C2K_OFFSET for x in degrees)

        # elif isinstance(degrees, tuple):
        #     return tuple(x + C2K_OFFSET for x in degrees)
        # elif isinstance(degrees, list):
        #     return list(x + C2K_OFFSET for x in degrees)
        # elif isinstance(degrees, set):
        #     return set(x + C2K_OFFSET for x in degrees)
    else:
        raise TypeError('Invalid argument')
