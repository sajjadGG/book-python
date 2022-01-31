"""
* Assignment: Type Bool True or False
* Required: yes
* Complexity: easy
* Lines of code: 14 lines
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
    >>> assert j is not Ellipsis, 'Assign result to variable: `j`'
    >>> assert k is not Ellipsis, 'Assign result to variable: `k`'
    >>> assert l is not Ellipsis, 'Assign result to variable: `l`'
    >>> assert m is not Ellipsis, 'Assign result to variable: `m`'
    >>> assert n is not Ellipsis, 'Assign result to variable: `n`'
    >>> assert type(a) is bool, 'Variable `a` has invalid type, should be bool'
    >>> assert type(b) is bool, 'Variable `b` has invalid type, should be bool'
    >>> assert type(c) is bool, 'Variable `c` has invalid type, should be bool'
    >>> assert type(d) is bool, 'Variable `d` has invalid type, should be bool'
    >>> assert type(e) is bool, 'Variable `e` has invalid type, should be bool'
    >>> assert type(f) is bool, 'Variable `f` has invalid type, should be bool'
    >>> assert type(g) is bool, 'Variable `g` has invalid type, should be bool'
    >>> assert type(h) is bool, 'Variable `h` has invalid type, should be bool'
    >>> assert type(i) is bool, 'Variable `i` has invalid type, should be bool'
    >>> assert type(j) is bool, 'Variable `j` has invalid type, should be bool'
    >>> assert type(k) is bool, 'Variable `k` has invalid type, should be bool'
    >>> assert type(l) is bool, 'Variable `l` has invalid type, should be bool'
    >>> assert type(m) is bool, 'Variable `m` has invalid type, should be bool'
    >>> assert type(n) is bool, 'Variable `n` has invalid type, should be bool'

    >>> a
    True
    >>> b
    False
    >>> c
    True
    >>> d
    False
    >>> e
    True
    >>> f
    False
    >>> g
    True
    >>> h
    False
    >>> i
    True
    >>> j
    True
    >>> k
    False
    >>> l
    False
    >>> m
    True
    >>> n
    False
"""

# bool: result of bool(True)
example = True

# bool: result of bool(True)
a = ...

# bool: result of bool(False)
b = ...

# bool: result of bool(1)
c = ...

# bool: result of bool(0)
d = ...

# bool: result of bool(-1)
e = ...

# bool: result of bool(0.0)
f = ...

# bool: result of bool('a')
g = ...

# bool: result of bool('')
h = ...

# bool: result of bool(' ')
i = ...

# bool: result of bool('0')
j = ...

# bool: result of bool(int('0'))
k = ...

# bool: result of bool(-0.0+0.0j)
l = ...

# bool: result of bool('-0.0+0.0j')
m = ...

# bool: result of bool(complex('-0.0+0.0j'))
n = ...

# Solution
a = True
b = False
c = True
d = False
e = True
f = False
g = True
h = False
i = True
j = True
k = False
l = False
m = True
n = False
