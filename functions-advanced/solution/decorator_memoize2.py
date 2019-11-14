def factorial(n):
    if not hasattr(factorial, '__cache__'):
        factorial.__cache__ = {1: 1}

    if not n in factorial.__cache__:
        factorial.__cache__[n] = n * factorial(n - 1)

    return factorial.__cache__[n]


factorial(50)
print(factorial.__cache__)
# {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, ...}
