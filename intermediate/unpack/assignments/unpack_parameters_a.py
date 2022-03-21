"""
* Assignment: Unpack Parameters Define
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Create function `mean()`, which calculates arithmetic mean
    2. Function can have arbitrary number of positional arguments
    3. Do not import any libraries and modules
    4. Use builtin functions `sum()` and `len()`
    5. Run doctests - all must succeed

Polish:
    1. Napisz funkcję `mean()`, wyliczającą średnią arytmetyczną
    2. Funkcja przyjmuje dowolną ilość pozycyjnych argumentów
    3. Nie importuj żadnych bibliotek i modułów
    4. Użyj wbudowanych funkcji `sum()` i `len()`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `sum(...) / len(...)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mean(1)
    1.0
    >>> mean(1, 3)
    2.0
    >>> mean()
    Traceback (most recent call last):
    ValueError: At least one argument is required
"""


# Solution
def mean(*args):
    if not args:
        raise ValueError('At least one argument is required')
    return sum(args) / len(args)


# %%timeit -r 1000 -n 1000
# >>> def mean(*args):
# ...     if not args:
# ...         return 0
# ...     return sum(args) / len(args)
# ...
# ... mean()
# 165 ns ± 28.5 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

# >>> %%timeit -r 1000 -n 1000
# ... def mean(*args):
# ...     if len(args) == 0:
# ...         return 0
# ...     return sum(args) / len(args)
# ...
# ... mean()
# 174 ns ± 29.2 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

# >>> %%timeit -r 1000 -n 1000
# ... def mean(*args):
# ...     try:
# ...         return sum(args) / len(args)
# ...     except ZeroDivisionError:
# ...         return 0
# ...
# ... mean()
# 395 ns ± 65.6 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)
