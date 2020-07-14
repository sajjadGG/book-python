from timeit import timeit
import sys

sys.setrecursionlimit(5000)


_CACHE = {}


def cache(func):
    def wrapper(n):
        if n not in _CACHE:
            _CACHE[n] = func(n)
        return _CACHE[n]
    return wrapper


@cache
def fn1(n):
    if n == 0:
        return 1
    else:
        return n * fn1(n-1)


def fn2(n):
    if n == 0:
        return 1
    else:
        return n * fn2(n-1)


duration_cache = timeit(stmt='fn1(500); fn1(400); fn1(450); fn1(350)', globals=globals(), number=100_000)
duration_nocache = timeit(stmt='fn2(500); fn2(400); fn2(450); fn2(350)', globals=globals(), number=100_000)
duration_ratio = duration_nocache / duration_cache

print(f'With Cache time: {duration_cache:.4f} seconds')
print(f'Without Cache time: {duration_nocache:.3f} seconds')
print(f'Cached solution is {duration_ratio:.1f} times faster')
