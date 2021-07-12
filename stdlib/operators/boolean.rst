Operators Boolean
=================


Rationale
---------
.. csv-table:: Boolean Operators Overload
    :header: "Operator", "Method"

    "``obj & other``",     "``obj.__and__(other)``"
    "``obj | other``",     "``obj.__or__(other)``"
    "``obj ^ other``",     "``obj.__xor__(other)``"

    "``obj &= other``",    "``obj.__iand__(other)``"
    "``obj |= other``",    "``obj.__ior__(other)``"
    "``obj ^= other``",    "``obj.__ixor__(other)``"

    "``obj << other``",    "``obj.__lshift__(other)``"
    "``obj >> other``",    "``obj.__rshift__(other)``"
    "``obj <<= other``",   "``obj.__ilshift__(other)``"
    "``obj >>= other``",   "``obj.__irshift__(other)``"


Operator Module - AND
---------------------
.. code-block:: text

    1 & 1 = 1
    1 & 0 = 0
    0 & 1 = 0
    0 & 0 = 0

>>> from operator import and_
>>>
>>>
>>> and_(True, True)
True
>>> and_(True, False)
False
>>> and_(False, True)
False
>>> and_(False, False)
False


Operator Module - OR
--------------------
.. code-block:: text

    1 | 1 = 1
    1 | 0 = 1
    0 | 1 = 1
    0 | 0 = 0

>>> from operator import or_
>>>
>>>
>>> or_(True, True)
True
>>> or_(True, False)
True
>>> or_(False, True)
True
>>> or_(False, False)
False


Operator Module - XOR
---------------------
.. code-block:: text

    1 ^ 1 = 0
    1 ^ 0 = 1
    0 ^ 1 = 1
    0 ^ 0 = 0

>>> from operator import xor
>>>
>>>
>>> xor(True, True)
False
>>> xor(True, False)
True
>>> xor(False, True)
True
>>> xor(False, False)
False


Use Case - XOR as pow
---------------------
* Excel uses ``^`` to rise number to the power of a second number

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Number:
...     value: int
...
...     def __xor__(self, other):
...         return Number(self.value ** other.value)
>>>
>>>
>>> a = Number(2)
>>> b = Number(4)
>>>
>>> a ^ b
Number(value=16)


Use Case - Numpy
----------------
>>> import numpy as np  # doctest: +SKIP
>>>
>>>
>>> a = np.array([[0, 1, 2],
...               [3, 4, 5],
...               [6, 7, 8]])  # doctest: +SKIP
>>>
>>> a > 2  # doctest: +SKIP
array([[False, False, False],
       [ True,  True,  True],
       [ True,  True,  True]])
>>>
>>> (a>2) & (a<7)  # doctest: +SKIP
array([[False, False, False],
       [ True,  True,  True],
       [ True, False, False]])
>>>
>>> (a>2) & (a<7) | (a>3)  # doctest: +SKIP
array([[False, False, False],
       [ True,  True,  True],
       [ True,  True,  True]])
>>>
>>> ~( (a>2) & (a<7) | (a>3) )  # doctest: +SKIP
array([[ True,  True,  True],
       [False, False, False],
       [False, False, False]])
