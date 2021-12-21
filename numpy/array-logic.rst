Array Logic
===========


Contains
--------
>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> 2 in a
True
>>>
>>> 0 in a
False
>>>
>>> [1, 2, 3] in a
True
>>>
>>> [1, 2] in a
False
>>>
>>> [3, 4] in a
False


Is In
-----
>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> b = np.array([1, 5, 9])
>>>
>>> np.isin(a, b)
array([[ True, False, False],
       [False,  True, False]])


Scalar Comparison
-----------------
>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a == 2
array([[False,  True, False],
       [False, False, False]])
>>>
>>> a != 2
array([[ True, False,  True],
       [ True,  True,  True]])
>>>
>>> a > 2
array([[False, False,  True],
       [ True,  True,  True]])
>>>
>>> a >= 2
array([[False,  True,  True],
       [ True,  True,  True]])
>>>
>>> a < 2
array([[ True, False, False],
       [False, False, False]])
>>>
>>> a <= 2
array([[ True,  True, False],
       [False, False, False]])


Broadcasting Comparison
-----------------------
>>> import numpy as np
>>>
>>>
>>> a = np.array([1, 2, 3])
>>> b = np.array([3, 2, 1])
>>>
>>> a == b
array([False, True, False])
>>>
>>> a != b
array([ True, False,  True])
>>>
>>> a > b
array([False, False,  True])
>>>
>>> a >= b
array([False,  True,  True])
>>>
>>> a < b
array([ True, False, False])
>>>
>>> a <= b
array([True, True, False])


Any
---
>>> import numpy as np
>>>
>>>
>>> a = np.array([True, False, False])
array([True, False, False])
>>>
>>> a.any()
True

>>> import numpy as np
>>>
>>>
>>> a = np.array([[True, False, False],
...               [True, True, True]])
>>>
>>> a.any()
True
>>>
>>> a.any(axis=0)
array([ True,  True,  True])
>>>
>>> a.any(axis=1)
array([ True,  True])


All
---
>>> import numpy as np
>>>
>>>
>>> a = np.array([True, False, False])
>>>
>>> a.all()
False

>>> import numpy as np
>>>
>>>
>>> a = np.array([[True, False, False],
...               [True, True, True]])
>>>
>>> a.all()
False
>>>
>>> a.all(axis=0)
array([ True, False, False])
>>>
>>> a.all(axis=1)
array([False,  True])


Logical NOT
-----------
* ``np.logical_not(...)``
* ``~(...)``

>>> import numpy as np
>>>
>>>
>>> a = np.array([[True, False, False],
...               [True, True, True]])
>>>
>>> np.logical_not(a)
array([[False,  True,  True],
       [False, False, False]])
>>>
>>> ~a
array([[False,  True,  True],
       [False, False, False]])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.logical_not(a > 2)
array([[ True,  True, False],
       [False, False, False]])
>>>
>>> ~(a > 2)
array([[ True,  True, False],
       [False, False, False]])


Logical AND
-----------
* Meets first and second condition at the same time
* ``np.logical_and(..., ...)``
* ``(...) & (...)``

>>> import numpy as np
>>>
>>>
>>> a = np.array([True, False, False])
>>> b = np.array([True, True, False])
>>>
>>> np.logical_and(a, b)
array([ True, False, False])
>>>
>>> a & b
array([ True, False, False])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.logical_and(a > 2, a < 5)
array([[False, False,  True],
       [ True, False, False]])
>>>
>>> (a > 2) & (a < 5)
array([[False, False,  True],
       [ True, False, False]])


Logical OR
----------
* Meets first or second condition at the same time
* ``np.logical_or(..., ...)``
* ``(...) | (...)``

>>> import numpy as np
>>>
>>>
>>> a = np.array([True, False, False])
>>> b = np.array([True, True, False])
>>>
>>> np.logical_or(a, b)
array([ True,  True, False])
>>>
>>> a | b
array([ True,  True, False])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.logical_or(a < 2, a > 4)
array([[ True, False, False],
       [False,  True,  True]])
>>>
>>> (a < 2) | (a > 4)
array([[ True, False, False],
       [False,  True,  True]])


Logical XOR
-----------
* Meets first or second condition, but not both at the same time
* ``np.logical_xor(..., ...)``
* ``(...) ^ (...)``

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.logical_xor(a < 2, a > 4)
array([[ True, False, False],
       [False,  True,  True]])
>>>
>>> (a < 2) ^ (a > 4)
array([[ True, False, False],
       [False,  True,  True]])


Good Practices
--------------
>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>>
>>> (a < 2) & (a > 4) | (a == 3)
array([[False, False,  True],
       [False, False, False]])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> lower = (a > 2)
>>> upper = (a < 6)
>>> nine = (a == 9)
>>> range = lower & upper
>>>
>>> lower & upper
array([[False, False,  True],
       [ True,  True, False],
       [False, False, False]])
>>>
>>> range | nine
array([[False, False,  True],
       [ True,  True, False],
       [False, False,  True]])
>>>
>>> lower & upper | nine
array([[False, False,  True],
       [ True,  True, False],
       [False, False,  True]])


Assignments
-----------
.. literalinclude:: assignments/numpy_logic_even.py
    :caption: :download:`Solution <assignments/numpy_logic_even.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_logic_isin.py
    :caption: :download:`Solution <assignments/numpy_logic_isin.py>`
    :end-before: # Solution
