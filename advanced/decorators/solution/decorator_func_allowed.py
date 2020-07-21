_allowed = True

def check(func):
    def wrapper(*args, **kwargs):
        if _allowed:
            return func(*args, **kwargs)
        else:
            raise PermissionError
    return wrapper
