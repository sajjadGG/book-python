from typing import Any


def is_numeric(*args: Any) -> bool:
    if not args:
        return False

    for arg in args:
        if not isinstance(arg, (int, float)):
            return False

    return True
