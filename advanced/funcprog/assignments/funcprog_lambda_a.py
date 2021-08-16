"""
* Assignment: FuncProg Lambda Chain
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Inline functions `odd()` and `cube()` with `lambda` expressions
    2. Run doctests - all must succeed

Polish:
    1. Wciel (inline) kod `odd()` i `cube()` wykorzystując wyrażenia `lambda`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `mean = sum(...) / len(...)`
    * type cast to `list()` before calculating mean to expand generator

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is float
    True
    >>> result
    11502.0
"""


def odd(x):
    return x % 2


def cube(x):
    return x ** 3


# float: Inline lambda expressions
result = ...

result = (x for x in range(1, 34) if x % 3 == 0)
result = filter(odd, result)
result = map(cube, result)
result = list(result)
result = sum(result) / len(result)

# Solution
result = (x for x in range(1, 34) if x % 3 == 0)
result = filter(lambda x: x % 2, result)
result = map(lambda x: x ** 3, result)
result = list(result)
result = sum(result) / len(result)
