def if_allowed(func):
    def wrapper(*args, **kwargs):
        if _allowed:
            return func(*args, **kwargs)
        else:
            raise PermissionError
    return wrapper


@if_allowed
def echo(text):
    print(text)


if __name__ == '__main__':
    _allowed = True
    echo('hello')
    # hello

    _allowed = False
    echo('hello')
    # Traceback (most recent call last):
    #     ...
    # PermissionError
