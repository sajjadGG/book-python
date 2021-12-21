Array Sort
==========


Sort
----
>>> import numpy as np
>>>
>>>
>>> a = np.array([2, 3, 1])
>>> a.sort()
>>>
>>> a
array([1, 2, 3])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[9, 7, 8],
>>>               [2, 3, 1],
>>>               [5, 6, 4]])
>>> b = a.copy()
>>> c = a.copy()
>>>
>>> a.sort()
>>> a
array([[7, 8, 9],
       [1, 2, 3],
       [4, 5, 6]])
>>>
>>> b.sort(axis=0)
>>> b
array([[2, 3, 1],
       [5, 6, 4],
       [9, 7, 8]])
>>>
>>> c.sort(axis=1)
>>> c
array([[7, 8, 9],
       [1, 2, 3],
       [4, 5, 6]])


Flip
----
* Does not modify inplace
* Returns new ``np.ndarray``
* Reverse the order of elements in an array along the given axis

>>> import numpy as np
>>>
>>>
>>> a = np.array([1, 2, 3])
array([1, 2, 3])
>>>
>>> np.flip(a)
array([3, 2, 1])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
>>>               [4, 5, 6]])
>>>
>>> a.flip()
array([[6, 5, 4],
       [3, 2, 1]])
>>>
>>> np.flip(a, axis=0)
array([[4, 5, 6],
       [1, 2, 3]])
>>>
>>> np.flip(a, axis=1)
array([[3, 2, 1],
       [6, 5, 4]])


Assignments
-----------
.. literalinclude:: assignments/numpy_sort.py
    :caption: :download:`Solution <assignments/numpy_sort.py>`
    :end-before: # Solution
