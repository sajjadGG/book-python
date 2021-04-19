"""
* Assignment: Type Bool True or False
* Status: required
* Complexity: easy
* Lines of code: 16 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Which variables are `True`?
    3. Which variables are `False`?

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Które zmienne są `True`?
    3. Które zmienne są `False`?

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, 'Assignment solution must be in `a` instead of ... (Ellipsis)'
    >>> assert b is not Ellipsis, 'Assignment solution must be in `b` instead of ... (Ellipsis)'
    >>> assert c is not Ellipsis, 'Assignment solution must be in `c` instead of ... (Ellipsis)'
    >>> assert d is not Ellipsis, 'Assignment solution must be in `d` instead of ... (Ellipsis)'
    >>> assert e is not Ellipsis, 'Assignment solution must be in `e` instead of ... (Ellipsis)'
    >>> assert f is not Ellipsis, 'Assignment solution must be in `f` instead of ... (Ellipsis)'
    >>> assert g is not Ellipsis, 'Assignment solution must be in `g` instead of ... (Ellipsis)'
    >>> assert h is not Ellipsis, 'Assignment solution must be in `h` instead of ... (Ellipsis)'
    >>> assert i is not Ellipsis, 'Assignment solution must be in `i` instead of ... (Ellipsis)'
    >>> assert j is not Ellipsis, 'Assignment solution must be in `j` instead of ... (Ellipsis)'
    >>> assert k is not Ellipsis, 'Assignment solution must be in `k` instead of ... (Ellipsis)'
    >>> assert l is not Ellipsis, 'Assignment solution must be in `l` instead of ... (Ellipsis)'
    >>> assert m is not Ellipsis, 'Assignment solution must be in `m` instead of ... (Ellipsis)'
    >>> assert n is not Ellipsis, 'Assignment solution must be in `n` instead of ... (Ellipsis)'
    >>> assert o is not Ellipsis, 'Assignment solution must be in `o` instead of ... (Ellipsis)'
    >>> assert n is not Ellipsis, 'Assignment solution must be in `n` instead of ... (Ellipsis)'
    >>> assert p is not Ellipsis, 'Assignment solution must be in `p` instead of ... (Ellipsis)'
    >>> assert q is not Ellipsis, 'Assignment solution must be in `q` instead of ... (Ellipsis)'
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
    >>> assert type(o) is bool, 'Variable `o` has invalid type, should be bool'
    >>> assert type(p) is bool, 'Variable `p` has invalid type, should be bool'
    >>> assert type(q) is bool, 'Variable `q` has invalid type, should be bool'

    >>> a
    False
    >>> b
    True
    >>> c
    False
    >>> d
    False
    >>> e
    False
    >>> f
    False
    >>> g
    True
    >>> h
    True
    >>> i
    True
    >>> j
    True
    >>> k
    False
    >>> l
    True
    >>> m
    False
    >>> n
    True
    >>> o
    False
    >>> p
    True
    >>> q
    False
"""

# Given
a = bool(False)
b = bool(True)

c = bool(0)
d = bool(0.0)
e = bool(-0)
f = bool(-0.0)

g = bool('a')
h = bool('.')
i = bool('0')
j = bool('0.0')
k = bool('')
l = bool(' ')

m = bool(int('0'))
n = bool(bool(str(-0)))

o = bool(-0.0 + 0.0j)
p = bool('-0.0+0.0j')
q = bool(complex('-0.0+0.0j'))

# Solution
a == False
b == True
c == False
d == False
e == False
f == False
g == True
h == True
i == True
j == True
k == False
l == True
m == False
n == False
o == False
p == True
q == False
