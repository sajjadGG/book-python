def is_numeric(*args):
    if not args:
        return False

    for arg in args:
        if not isinstance(arg, (int, float)):
            return False

    return True
