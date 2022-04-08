"""
* Assignment: Function Generator Chain
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Use `range()` to get numbers:
       a. from 0 (inclusive)
       b. to 10 (exclusive)
    2. Redefine `result` with odd numbers from `result`
    3. Redefine `result` with cubed numbers from `result`
    4. Redefine `result` with evaluated `result`
    5. Run doctests - all must succeed

Polish:
    1. Użyj `range()` aby otrzymać liczby:
       a. od 0 (włącznie)
       b. do 10 (rozłącznie)
    2. Przedefiniuj `result` z nieparzystymi liczbami z `result`
    3. Przedefiniuj `result` z podniesionymi do sześcianiu liczbami z `result`
    4. Przedefiniuj `result` z ewaluaownym `result`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * range()
    * map()
    * filter()
    * list()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(odd)
    >>> assert isfunction(cube)
    >>> assert type(result) is list
    >>> assert all(type(x) is int for x in result)

    >>> result
    [1, 27, 125, 343, 729]
"""

def odd(x):
    return x % 2


def cube(x):
    return x ** 3


# Range from 0 to 10 (exclusive)
# type: Iterator[int]
result = ...

# Filter odd numbers
# type: Iterator[int]
result = ...

# Cube result
# type: Iterator[int]
result = ...

# Get list of results
# type: list[int]
result = ...


# Solution
result = range(0, 10)
result = filter(odd, result)
result = map(cube, result)
result = list(result)
