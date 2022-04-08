"""
* Assignment: Function Return Capture
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result` with result of `compute` function call
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result` z wynikiem wywołania funkcji `compute`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(compute)
    True
    >>> result
    3
"""


def compute():
    return 1 + 2


# Result of `compute` function call
# type: int
result = ...

# Solution
result = compute()
