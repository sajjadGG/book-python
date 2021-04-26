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

    >>> assert result_a is not Ellipsis, 'Assignment solution must be in `result_a` instead of ... (Ellipsis)'
    >>> assert result_b is not Ellipsis, 'Assignment solution must be in `result_b` instead of ... (Ellipsis)'
    >>> assert result_c is not Ellipsis, 'Assignment solution must be in `result_c` instead of ... (Ellipsis)'
    >>> assert result_d is not Ellipsis, 'Assignment solution must be in `result_d` instead of ... (Ellipsis)'
    >>> assert result_e is not Ellipsis, 'Assignment solution must be in `result_e` instead of ... (Ellipsis)'
    >>> assert type(result_a) is bool, 'Variable `result_a` has invalid type, should be bool'
    >>> assert type(result_b) is bool, 'Variable `result_b` has invalid type, should be bool'
    >>> assert type(result_c) is bool, 'Variable `result_c` has invalid type, should be bool'
    >>> assert type(result_d) is bool, 'Variable `result_d` has invalid type, should be bool'
    >>> assert type(result_e) is bool, 'Variable `result_e` has invalid type, should be bool'

    >>> bool(result_a)
    True
    >>> bool(result_b)
    False
    >>> bool(result_c)
    True
    >>> bool(result_d)
    False
    >>> bool(result_e)
    False
"""

a = ...  # bool: True
b = ...  # bool: False
c = ...  # bool: True
d = ...  # bool: False
e = ...  # bool: False

# Do not modify following lines
result_a = a is None
result_b = b is not None
result_c = bool(bool(c) is not bool(c)) == False
result_d = bool(bool(d) is not bool(d)) == False and bool(d)
result_e = (bool(bool(e) is not bool(e)) == False and bool(e)) and (e is not None)

# Solution
a = None  # bool: True
b = None  # bool: False
c = None  # bool: True
d = None  # bool: False
e = None  # bool: False

result_a = a is None
result_b = b is not None
result_c = bool(bool(c) is not bool(c)) == False
result_d = bool(bool(d) is not bool(d)) == False and bool(d)
result_e = (bool(bool(e) is not bool(e)) == False and bool(e)) and (e is not None)
