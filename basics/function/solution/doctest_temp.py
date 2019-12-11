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
    if type(degrees) in (int, float):
        return 273.15 + degrees

    if type(degrees) is tuple:
        return tuple(x+273.15 for x in degrees)

    if type(degrees) is list:
        return list(x+273.15 for x in degrees)

    if type(degrees) is set:
        return set(x+273.15 for x in degrees)

    raise TypeError('Invalid argument')

    ## Alternative solution
    # if type(degrees) in (int, float):
    #     return 273.15 + degrees
    #
    # if type(degrees) in (list, tuple, set):
    #     cls = type(degrees)
    #     return cls(x+273.15 for x in degrees)
    #
    # raise TypeError('Invalid argument')
