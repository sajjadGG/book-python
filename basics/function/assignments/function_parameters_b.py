"""
* Assignment: Function Parameters Echo
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define function `echo` with two parameters
    2. Parameter `a` is required
    3. Parameter `b` is required
    4. Return `a` and `b` as a `tuple`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj funkcję `echo` z dwoma parametrami
    2. Parametr `a` jest wymagany
    3. Parametr `b` jest wymagany
    4. zwróć `a` i `b` jako `tuple`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isfunction
    >>> isfunction(echo)
    True
    >>> type(echo(0,0)) is tuple
    True
    >>> echo(1, 2)
    (1, 2)
    >>> echo(3, 4)
    (3, 4)
"""


# Solution
def echo(a, b):
    return a, b
