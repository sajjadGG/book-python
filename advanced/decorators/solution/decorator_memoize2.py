def cache(fn):
    def wrapper(n):
        cache = getattr(wrapper, '__cache__', {})
        if n not in cache:
            print(f'"n={n}" Not in cache. Calculating...')
            cache[n] = fn(n)
            setattr(wrapper, '__cache__', cache)
        else:
            print(f'"n={n}" Found in cache. Fetching...')
        return cache[n]
    return wrapper


@cache
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))
# "n=3" Not in cache. Calculating...
# "n=2" Not in cache. Calculating...
# "n=1" Not in cache. Calculating...
# "n=0" Not in cache. Calculating...
# 6

print(factorial.__cache__)
# {3: 6}

print(factorial(5))
# "n=5" Not in cache. Calculating...
# "n=4" Not in cache. Calculating...
# "n=3" Found in cache. Fetching...
# 120

print(factorial.__cache__)
# {3: 6, 4: 24, 5: 120}

print(factorial(6))
# "n=6" Not in cache. Calculating...
# "n=5" Found in cache. Fetching...
# 720

print(factorial.__cache__)
# {3: 6, 4: 24, 5: 120, 6: 720}

print(factorial(4))
# "n=4" Found in cache. Fetching...
# 24

print(factorial.__cache__)
# {3: 6, 4: 24, 5: 120, 6: 720}
