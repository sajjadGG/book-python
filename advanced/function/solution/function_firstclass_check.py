def check(func):
    def wrapper(*args, **kwargs):
        pass
    return wrapper


run = check(...)
del check
run()
