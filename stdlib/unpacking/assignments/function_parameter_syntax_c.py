"""
* Assignment: Unpacking ParameterSyntax Mixed
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min
* Warning: This assignment will work only in Python 3.8+

English:
    1. Create function `take_damage`
    2. Function takes one argument `dmg` and always returns `None`
    3. Argument must be passed only as positional
    4. Test function by running with positional arguments
    5. Test function by running with keyword arguments
    6. Run doctests - all must succeed

Polish:
    1. Stwórz funkcję `take_damage`
    2. Funkcja przyjmuje jeden argument `dmg` i zawsze zwraca `None`
    3. Argument można podawać tylko pozycyjnie
    4. Przetestuj funkcję uruchamiając z pozycyjnymi parametrami
    5. Przetestuj funkcję uruchamiając z nazwanymi parametrami
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert callable(compute)
    >>> assert isfunction(compute)

    >>> compute(1, 2, 3)
    >>> compute(1, 2, 3, func=lambda:None)

    >>> compute(1, 2)
    Traceback (most recent call last):
    TypeError: compute() missing 1 required positional argument: 'c'

    >>> compute()  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: compute() missing 3 required positional arguments: 'a', 'b',
    and 'c'

    >>> compute(1, 2, 3, lambda:None)
    Traceback (most recent call last):
    TypeError: compute() takes 3 positional arguments but 4 were given

    >>> compute(a=1, b=2, c=3)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: compute() got some positional-only arguments passed as
    keyword arguments: 'a, b, c'
"""


# callable: Argument must be passed only as positional
def compute(a, b, c, func=lambda:...):
    pass


# Solution
def compute(a, b, c, /, *, func=lambda:...):
    pass
