"""
* Assignment: Type Bool Simple
* Required: yes
* Complexity: easy
* Lines of code: 9 lines
* Time: 8 min

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

    >>> assert a is not Ellipsis, 'Assign result to variable: `a`'
    >>> assert b is not Ellipsis, 'Assign result to variable: `b`'
    >>> assert c is not Ellipsis, 'Assign result to variable: `c`'
    >>> assert d is not Ellipsis, 'Assign result to variable: `d`'
    >>> assert e is not Ellipsis, 'Assign result to variable: `e`'
    >>> assert f is not Ellipsis, 'Assign result to variable: `f`'
    >>> assert g is not Ellipsis, 'Assign result to variable: `g`'
    >>> assert h is not Ellipsis, 'Assign result to variable: `h`'
    >>> assert i is not Ellipsis, 'Assign result to variable: `i`'
    >>> assert type(a) is bool, 'Variable `a` has invalid type, should be bool'
    >>> assert type(b) is bool, 'Variable `b` has invalid type, should be bool'
    >>> assert type(c) is bool, 'Variable `c` has invalid type, should be bool'
    >>> assert type(d) is bool, 'Variable `d` has invalid type, should be bool'
    >>> assert type(e) is bool, 'Variable `e` has invalid type, should be bool'
    >>> assert type(f) is bool, 'Variable `f` has invalid type, should be bool'
    >>> assert type(g) is bool, 'Variable `g` has invalid type, should be bool'
    >>> assert type(h) is bool, 'Variable `h` has invalid type, should be bool'
    >>> assert type(i) is bool, 'Variable `i` has invalid type, should be bool'

    >>> a
    True
    >>> b
    True
    >>> c
    False
    >>> d
    True
    >>> e
    False
    >>> f
    False
    >>> g
    True
    >>> h
    True
    >>> i
    False
"""

# bool: result of `not ...` must be True
example = False

# bool: result of `True == ...` must be True
a = ...

# bool: result of `True != ...` must be True
b = ...

# bool: result of `not ...` must be True
c = ...

# bool: result of `bool(...) == True` must be True
d = ...

# bool: result of `bool(...) == False` must be True
e = ...

# bool: result of `... or False` must be False
f = ...

# bool: result of `True and ...` must be True
g = ...

# bool: result of `bool(bool(...) == ...) or False` must be True
h = ...

# bool: result of `bool(...) is not bool(False)` must be False
i = ...

# Solution
a = True
b = True
c = False
d = True
e = False
f = False
g = True
h = True
i = False
