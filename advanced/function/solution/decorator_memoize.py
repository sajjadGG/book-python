from timeit import timeit
import sys

sys.setrecursionlimit(5000)

# Decorator
CACHE = {}


def cache(func):
    def wrapper(n):
        if n not in CACHE:
            CACHE[n] = func(n)
        return CACHE[n]
    return wrapper


@cache
def factorial_decorator(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_decorator(n - 1)


def factorial_nocache(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_nocache(n - 1)


duration_decorator = timeit(
    stmt='factorial_decorator(500); factorial_decorator(400); factorial_decorator(450); factorial_decorator(350)',
    globals=globals(),
    number=100_000
)

duration_nocache = timeit(
    stmt='factorial_nocache(500); factorial_nocache(400); factorial_nocache(450); factorial_nocache(350)',
    globals=globals(),
    number=100_000
)

print(f'factorial_decorator time: {round(duration_decorator, 4)} seconds')
print(f'factorial_nocache time: {round(duration_nocache, 3)} seconds')
print(f'Cached solution is {round(duration_nocache / duration_decorator, 1)} times faster')

