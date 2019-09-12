CACHE = {}
#
#
# def factorial(n: int) -> int:
#     if n not in CACHE:
#
#         if n == 0:
#             return 1
#         else:
#             CACHE[n] = n * factorial(n-1)
#
#     return CACHE[n]



def cache(func):
    def wrapper(n):
        if n not in CACHE:
            CACHE[n] = func(n)
        return CACHE[n]
    return wrapper


@cache
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



out = factorial(5)
print(out)
