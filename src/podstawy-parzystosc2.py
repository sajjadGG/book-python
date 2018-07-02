from typing import Union


def is_even_number(number: Union[int, float]) -> bool:
    """
    >>> is_even_number(1)
    False
    >>> is_even_number(2)
    True
    >>> is_even_number(1.5)
    False
    >>> is_even_number(0)
    True
    >>> is_even_number(-1)
    False
    >>> is_even_number(-2)
    True
    >>> is_even_number([2, 4, 6, 8])
    Traceback (most recent call last):
    ...
    TypeError
    >>> is_even_number('two')
    Traceback (most recent call last):
    ...
    TypeError
    >>> is_even_number('2')
    Traceback (most recent call last):
    ...
    TypeError
    """
    if isinstance(number, (int, float)):
        return number % 2 == 0
    else:
        raise TypeError
