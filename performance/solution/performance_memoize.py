from timeit import timeit
CACHE = {}


def factorial_nocache(n: int) -> int:
    if n == 0:
        return 1
    else:
        result = n * factorial_nocache(n-1)
        return result


def factorial_cache(n: int) -> int:
    result = CACHE.get(n)

    if result:
        return result

    if n == 0:
        return 1
    else:
        result = n * factorial_cache(n-1)
        CACHE[n] = result
        return result


duration_cache = timeit(
    stmt='factorial_cache(500); factorial_cache(400); factorial_cache(450); factorial_cache(350)',
    globals=globals(),
    number=10000,
)

duration_nocache = timeit(
    stmt='factorial_nocache(500); factorial_nocache(400); factorial_nocache(450); factorial_nocache(350)',
    globals=globals(),
    number=10000
)

print(f'factorial_cache time: {duration_cache}')
print(f'factorial_nocache time: {duration_nocache}')
print(f'Cached solution is {int(duration_nocache / duration_cache)} times faster')
