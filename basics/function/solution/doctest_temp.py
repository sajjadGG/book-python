def celsius_to_kelvin(degrees):
    """
    >>> celsius_to_kelvin(0)
    273.15
    >>> celsius_to_kelvin(1)
    274.15
    >>> celsius_to_kelvin(-1)
    272.15
    >>> celsius_to_kelvin('a')
    Traceback (most recent call last):
        ...
    TypeError: Invalid argument
    >>> celsius_to_kelvin([0, 1])
    [273.15, 274.15]
    >>> celsius_to_kelvin((0, 1))
    (273.15, 274.15)
    >>> celsius_to_kelvin({0, 1})
    {273.15, 274.15}
    """
    if isinstance(degrees, (int, float)):
        return 273.15 + degrees
    elif isinstance(degrees, tuple):
        return tuple(x + 273.15 for x in degrees)
    elif isinstance(degrees, list):
        return list(x + 273.15 for x in degrees)
    elif isinstance(degrees, set):
        return set(x + 273.15 for x in degrees)
    else:
        raise TypeError('Invalid argument')

    ## Alternative solution
    # if isinstance(degrees, (int, float)):
    #     return 273.15 + degrees
    #
    # elif isinstance(degrees, (list, tuple, set)):
    #     cls = type(degrees)
    #     return cls(x + 273.15 for x in degrees)
    #
    # else:
    #     raise TypeError('Invalid argument')
