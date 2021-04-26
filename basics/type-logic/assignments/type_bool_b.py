"""
* Assignment: Type Bool Simple
* Required: yes
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. What you need to put in expressions to get the expected outcome?
    2. In place of ellipsis (`...`) insert only `True` or `False`
    3. Run doctests - all must succeed

Polish:
    1. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    2. W miejsce trzech kropek (`...`) wstawiaj tylko `True` lub `False`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, 'Assignment solution must be in `a` instead of ... (Ellipsis)'
    >>> assert b is not Ellipsis, 'Assignment solution must be in `b` instead of ... (Ellipsis)'
    >>> assert c is not Ellipsis, 'Assignment solution must be in `c` instead of ... (Ellipsis)'
    >>> assert d is not Ellipsis, 'Assignment solution must be in `d` instead of ... (Ellipsis)'
    >>> assert e is not Ellipsis, 'Assignment solution must be in `e` instead of ... (Ellipsis)'
    >>> assert f is not Ellipsis, 'Assignment solution must be in `f` instead of ... (Ellipsis)'
    >>> assert g is not Ellipsis, 'Assignment solution must be in `g` instead of ... (Ellipsis)'
    >>> assert h is not Ellipsis, 'Assignment solution must be in `h` instead of ... (Ellipsis)'
    >>> assert i is not Ellipsis, 'Assignment solution must be in `i` instead of ... (Ellipsis)'
    >>> assert type(a) is bool, 'Variable `a` has invalid type, should be bool'
    >>> assert type(b) is bool, 'Variable `b` has invalid type, should be bool'
    >>> assert type(c) is bool, 'Variable `c` has invalid type, should be bool'
    >>> assert type(d) is bool, 'Variable `d` has invalid type, should be bool'
    >>> assert type(e) is bool, 'Variable `e` has invalid type, should be bool'
    >>> assert type(f) is bool, 'Variable `f` has invalid type, should be bool'
    >>> assert type(g) is bool, 'Variable `g` has invalid type, should be bool'
    >>> assert type(h) is bool, 'Variable `h` has invalid type, should be bool'
    >>> assert type(i) is bool, 'Variable `i` has invalid type, should be bool'

    >>> bool(a)
    True
    >>> bool(b)
    True
    >>> bool(c)
    False
    >>> bool(d)
    True
    >>> bool(e)
    True
    >>> bool(f)
    False
    >>> bool(g)
    True
    >>> bool(h)
    True
    >>> bool(i)
    False
"""

a = True == ...         # bool: the expression result must be True
b = True != ...         # bool: the expression result must be True
c = not ...             # bool: the expression result must be False

d = bool(...) == True   # bool: the expression result must be True
e = bool(...) == False  # bool: the expression result must be True

f = ... or ...          # bool: the expression result must be False
g = ... and ...         # bool: the expression result must be True

h = bool(bool(...) == ...) or False  # bool: the expression result must be True
i = bool(...) is not bool(False)     # bool: the expression result must be False

# Solution
a = True == True
b = True != False
c = not True
d = bool(True) == True
e = bool(False) == False
f = False or False
g = True and True
h = bool(bool(False) == False) or False
i = bool(False) is not bool(False)
