from typing import Union


def kilometers_from_meters(km: Union[int, float]) -> float:
    """
    >>> kilometers_from_meters(1)
    1000.0

    >>> kilometers_from_meters(0)
    0.0

    >>> kilometers_from_meters(-1)
    Traceback (most recent call last):
        ...
    ValueError: Argument must be positive

    >>> kilometers_from_meters([1, 2])
    Traceback (most recent call last):
        ...
    ValueError: Invalid Argument

    >>> kilometers_from_meters('one')
    Traceback (most recent call last):
        ...
    ValueError: Invalid Argument

    >>> kilometers_from_meters(1.5)
    1500.0
    """
    if not isinstance(km, (int, float)):
        raise ValueError('Invalid Argument')

    if km < 0:
        raise ValueError('Argument must be positive')

    return float(1000 * km)
