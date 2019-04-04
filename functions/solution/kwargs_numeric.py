def is_numeric(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            return False
    return True


def is_numeric(*args, **kwargs):
    data = list(args) + list(kwargs.values())
    for arg in data:
        if not isinstance(arg, (int, float)):
            return False
    return True
