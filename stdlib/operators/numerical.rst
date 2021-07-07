Operators Numerical
===================


Rationale
---------
.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj + other``",     "``obj.__add__(other)``"
    "``obj - other``",     "``obj.__sub__(other)``"
    "``obj * other``",     "``obj.__mul__(other)``"
    "``obj / other``",     "``obj.__truediv__(other)``"
    "``obj // other``",    "``obj.__floordiv__(other)``"
    "``obj ** other``",    "``obj.__pow__(other)``"
    "``obj % other``",     "``obj.__mod__(other)``"
    "``obj @ other``",     "``obj.__matmul__(other)``"

    "``obj += other``",    "``obj.__iadd__(other)``"
    "``obj -= other``",    "``obj.__isub__(other)``"
    "``obj *= other``",    "``obj.__imul__(other)``"
    "``obj /= other``",    "``obj.__idiv__(other)``"
    "``obj //= other``",   "``obj.__itruediv__(other)``"
    "``obj **= other``",   "``obj.__ipow__(other)``"
    "``obj %= other``",    "``obj.__imod__(other)``"
    "``obj @= other``",    "``obj.__imatmul__(other)``"

``%`` (``__mod__``) operator behavior for ``int`` and ``str``:


Example
-------
>>> class Int:
...     def __mod__(self, other):
...         """modulo division"""
>>>
>>> 3 % 2
1
>>> 4 % 2
0


Use Case
--------
>>> class Str:
...     def __mod__(self, other):
...         """str substitute"""
...
...         if type(other) is str:
...             ...
...         if type(other) is tuple:
...             ...
...         if type(other) is dict:
...             ...

>>> 'Echo' % 2
Traceback (most recent call last):
TypeError: not all arguments converted during string formatting
>>> 'Echo %s' % 2
'Echo 2'
>>> 'Echo %d' % 2
'Echo 2'
>>> 'Echo %f' % 2
'Echo 2.000000'
>>> 'Echo %s %s' % (1, 2)
'Echo 1 2'
>>> 'Echo %s %d %f' % (1, 2, 3)
'Echo 1 2 3.000000'
>>>
>>> 'Echo %(firstname)s %(lastname)s' % {'firstname': 'Mark', 'lastname': 'Watney'}
'Echo Mark Watney'
>>>
>>> 'Echo %(name)s %(age)d' % {'name': 'Mark Watney', 'age': 44}
'Echo Mark Watney 44'

``%s``, ``%d``, ``%f`` is currently deprecated in favor of ``f'...'`` string formatting.
More information in `Builtin Printing`


Assignments
-----------
.. literalinclude:: assignments/operators_numerical_a.py
    :caption: :download:`Solution <assignments/operators_numerical_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operators_numerical_b.py
    :caption: :download:`Solution <assignments/operators_numerical_b.py>`
    :end-before: # Solution
