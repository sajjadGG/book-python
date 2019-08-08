from typing import Any


def is_numeric(*args: Any) -> bool:
    """
    >>> is_numeric(1)
    True
    >>> is_numeric(1, 1.5)
    True
    >>> is_numeric(True)
    False
    >>> is_numeric('one', 1)
    False
    >>> is_numeric()
    False
    >>> is_numeric([])
    False
    >>> is_numeric([1, 1.5])
    False
    """
    if not args:
        return False

    for arg in args:
        if not type(arg) in {int, float}:
        # if not isinstance(arg, (int, float)):
            return False

    return True
