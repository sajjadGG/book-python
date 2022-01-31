"""
* Assignment: Type None
* Required: yes
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. What you need to put in expressions to get the expected outcome?
    2. Run doctests - all must succeed

Polish:
    1. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, 'Assign result to variable: `a`'
    >>> assert b is not Ellipsis, 'Assign result to variable: `b`'
    >>> assert c is not Ellipsis, 'Assign result to variable: `c`'

    >>> assert type(a) is type(None), \
    'Variable `a` has invalid type, should be NoneType'
    >>> assert type(b) is type(None), \
    'Variable `b` has invalid type, should be NoneType'
    >>> assert type(c) is type(None), \
    'Variable `c` has invalid type, should be NoneType'

    >>> a is None
    True
    >>> b is not None
    False
    >>> bool(c) is not bool(c) == False
    False
"""

# bool: result of `... is None` must be True
a = ...

# bool: result of `... is not None` must be False
b = ...

# bool: result of `bool(...) is not bool(...) == False` must be True
c = ...


# Solution
a = None
b = None
c = None
