Operator Comparison
===================
* ``==`` - eq
* ``!=`` - ne
* ``<`` - lt
* ``<=`` - le
* ``>`` - gt
* ``>=`` - ge
* ``in`` - contains


SetUp
-----
>>> from functools import reduce


About
-----
.. csv-table:: Comparison Operator Overload
    :header: "Operator", "Method"

    "``obj == other``",   "``obj.__eq__(other)``"
    "``obj != other``",   "``obj.__ne__(other)``"
    "``obj < other``",    "``obj.__lt__(other)``"
    "``obj <= other``",   "``obj.__le__(other)``"
    "``obj > other``",    "``obj.__gt__(other)``"
    "``obj >= other``",   "``obj.__ge__(other)``"
    "``other in obj``",       "``obj.__contains__(other)``"


Object Equality
---------------
* When you compare objects with the same fields from two different classes
* Always remember to compare classes
* This way you avoid bug, when both has the same fields and values
* Eq Works at Both Sides

>>> class Fruit:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>>
>>> a == b
False

>>> class Fruit:
...     def __init__(self, name):
...         self.name = name
...
...     def __eq__(self, other):
...         return self.name == other.name
>>>
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>>
>>> a == b
True

>>> class Fruit:
...     def __init__(self, name):
...         self.name = name
...
...     def __eq__(self, other):
...         return self.name == other.name
>>>
>>>
>>> class Company:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>> c = Company('Apple')
>>>
>>> a == b
True
>>>
>>> a == c
True

>>> class Fruit:
...     def __init__(self, name):
...         self.name = name
...
...     def __eq__(self, other):
...         return self.__class__ is other.__class__ \
...            and self.name == other.name
>>>
>>>
>>> class Company:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>> c = Company('Apple')
>>>
>>> a == b
True
>>>
>>> a == c
False

Eq Works at Both Sides:

>>> class Fruit:
...     def __init__(self, name):
...         self.name = name
>>>
>>>
>>> class Company:
...     def __init__(self, name):
...         self.name = name
...
...     def __eq__(self, other):
...         return self.__class__ is other.__class__ \
...            and self.name == other.name
>>>
>>>
>>> a = Fruit('Apple')
>>> b = Fruit('Apple')
>>> c = Company('Apple')
>>>
>>> a == b
False
>>>
>>> a == c
False


Use Case - 0x01
---------------
* Game

>>> hero < Damage(20)  # doctest: +SKIP
>>> hero > Damage(20)  # doctest: +SKIP


Use Case - 0x02
---------------
* Numpy

SetUp:

>>> import numpy as np
>>> from pprint import pprint

Python does not support element-wise comparison:

>>> data = [[1, 2, 3],
...         [4, 5, 6],
...         [7, 8, 9]]
>>>
>>>
>>> data > 2
Traceback (most recent call last):
TypeError: '>' not supported between instances of 'list' and 'int'

In Python you have to iterate over each row and each element in a row,
then to create a temporary row-result to which you append the information,
at the end, you append this temporary object to result and process next line:

>>> data = [[1, 2, 3],
...         [4, 5, 6],
...         [7, 8, 9]]
>>>
>>> result = []
>>>
>>> for row in data:
...     tmp = []
...     for number in row:
...         tmp.append(number > 2)
...     result.append(tmp)
>>>
>>>
>>> pprint(result, width=30)
[[False, False, True],
 [True, True, True],
 [True, True, True]]

Alternatively you can use nested list comprehensions to do the same:

>>> data = [[1, 2, 3],
...         [4, 5, 6],
...         [7, 8, 9]]
>>>
>>> result = [
...     [number > 2 for number in row]
...     for row in data
... ]
>>>
>>> pprint(result, width=30)
[[False, False, True],
 [True, True, True],
 [True, True, True]]

In ``numpy`` all the comparison is being done element-wise and we do not
have to worry about iteration etc. It is called vectorized operation:

>>> data = np.array([[1, 2, 3],
...                  [4, 5, 6],
...                  [7, 8, 9]])
>>>
>>> data > 2
array([[False, False,  True],
       [ True,  True,  True],
       [ True,  True,  True]])


Assignments
-----------
.. literalinclude:: assignments/operator_comparison_a.py
    :caption: :download:`Solution <assignments/operator_comparison_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operator_comparison_b.py
    :caption: :download:`Solution <assignments/operator_comparison_b.py>`
    :end-before: # Solution
