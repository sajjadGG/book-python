Built-ins
=========


SetUp
-----
>>> import numpy as np


Pi number
---------
>>> np.pi
3.141592653589793


Euler number
------------
>>> np.e
2.718281828459045


Infinite
--------
Numpy built-in:

>>> np.inf
inf
>>>
>>> np.Infinity
inf
>>>
>>> np.Inf
inf
>>>
>>> np.PINF
inf
>>>
>>> np.NINF
-inf
>>>
>>> -np.inf
-inf
>>>
>>> -np.Inf
-inf
>>>
>>> -np.Infinity
-inf

Python built-in:

>>> float('Inf')
inf
>>>
>>> float('Infinity')
inf
>>>
>>> float('inf')
inf
>>>
>>> np.inf == float('inf')
True
>>>
>>> np.inf is float('inf')
False

Mathematical operations:

>>> np.inf + 1
inf
>>> np.inf + np.inf
inf
>>> np.inf - np.inf
nan
>>> np.inf - np.nan
nan
>>>
>>> np.inf * np.inf
inf
>>> np.inf / np.inf
nan
>>>
>>> 0 / np.inf
0.0
>>> np.inf / 0
Traceback (most recent call last):
ZeroDivisionError: float division by zero

Check for infinite values:

>>> a = np.array([1, 2, np.inf])
>>>
>>> np.isfinite(a)
array([ True,  True, False])
>>>
>>> np.isinf(a)
array([False, False,  True])


Not-a-Number
------------
* Special ``float`` value
* Propagates in calculations

Numpy built-in:

>>> np.NaN
nan
>>>
>>> np.NAN
nan
>>>
>>> np.nan
nan

Python built-in:

>>> float('nan')
nan
>>>
>>> np.nan is float('nan')
False
>>>
>>> np.nan == float('nan')
False
>>>
>>> np.nan is None
False
>>>
>>> np.nan == None
False

Boolean value of NaN:

>>> bool(None)
False
>>>
>>> bool(np.nan)
True

Mathematical operations:

>>> np.nan + 1
nan
>>> np.nan + np.nan
nan
>>> np.nan - np.nan
nan
>>> np.nan - np.inf
nan
>>>
>>> np.nan / np.nan
nan
>>> 0 / np.nan
nan
>>> np.nan / 0
Traceback (most recent call last):
ZeroDivisionError: float division by zero

Check for NaN values:

>>> a = np.array([1, 2, np.nan])
>>>
>>> np.isnan(a)
array([False, False,  True])


Isinf vs Isnan
--------------
>>> a = np.array([1, 2, np.inf])
>>>
>>> np.isnan(a)
array([False, False, False])

>>> a = np.array([1, 2, np.nan])
>>>
>>> np.isfinite(a)
array([ True,  True, False])
>>>
>>> np.isinf(a)
array([False, False, False])


Assignments
-----------
.. todo:: Create assignments
