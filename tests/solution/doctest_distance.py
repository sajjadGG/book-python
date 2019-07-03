from typing import Union


def m_to_km(meters: Union[int, float]) -> float:
    """
    >>> m_to_km(1)
    0.001

    >>> m_to_km(0)
    0.0

    >>> m_to_km(-1)
    Traceback (most recent call last):
        ...
    ValueError: Argument must be positive

    >>> m_to_km([1, 2])
    Traceback (most recent call last):
        ...
    ValueError: Invalid Argument

    >>> m_to_km('one')
    Traceback (most recent call last):
        ...
    ValueError: Invalid Argument

    >>> m_to_km(1.5)
    0.0015
    """
    if not isinstance(meters, (int, float)):
        raise ValueError('Invalid Argument')

    if meters < 0:
        raise ValueError('Argument must be positive')

    return float(meters / 1000)
