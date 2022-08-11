"""
* Assignment: FuncProg Callable Define
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define function `wrapper`, which returns 'hello from wrapper'
    2. Define function `check`
    3. Function `check` must return `wrapper: Callable`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `wrapper`, która zwraca 'hello from wrapper'
    2. Zdefiniuj funkcję `check`
    3. Funkcja `check` ma zwracać `wrapper: Callable`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(check)
    >>> assert isfunction(wrapper)
    >>> assert isfunction(check())

    >>> wrapper()
    'hello from wrapper'

    >>> check()()
    'hello from wrapper'
"""


# Returns 'hello from wrapper'
# type: Callable[[], str]
def wrapper():
    ...


# Takes `func` as an argument, returns wrapper function
# type: Callable[[Callable], Callable]
def check():
    ...


# Solution
def wrapper():
    return 'hello from wrapper'


def check():
    return wrapper
