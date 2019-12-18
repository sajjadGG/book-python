def cache(fn):
    def wrapper(n):
        cache = getattr(wrapper, '__cache__', {})
        if n not in cache:
            cache[n] = fn(n)
            setattr(wrapper, '__cache__', cache)
        return cache[n]
    return wrapper

@cache
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(50))
# 30414093201713378043612608166064768844377641568960512000000000000

print(factorial.__cache__)
# {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, ...}

# def factorial(n):
#     if not hasattr(factorial, '__cache__'):
#         factorial.__cache__ = {1: 1}
#
#     if not n in factorial.__cache__:
#         factorial.__cache__[n] = n * factorial(n - 1)
#
#     return factorial.__cache__[n]
#
#
# factorial(50)
# print(factorial.__cache__)
# # {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, ...}
