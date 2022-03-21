Array Sort
==========


Important
---------


SetUp
-----
>>> import numpy as np


Sort
----
Sort vector:

>>> a = np.array([2, 3, 1])
>>> a.sort()
>>>
>>> a
array([1, 2, 3])

Sort matrix:

>>> a = np.array([[9, 7, 8],
...               [2, 3, 1],
...               [5, 6, 4]])
>>> a.sort()
>>> a
array([[7, 8, 9],
       [1, 2, 3],
       [4, 5, 6]])


Sort matrix rows:

>>> a = np.array([[9, 7, 8],
...               [2, 3, 1],
...               [5, 6, 4]])
>>>
>>> a.sort(axis=0)
>>> a
array([[2, 3, 1],
       [5, 6, 4],
       [9, 7, 8]])


Sort matrix columns:

>>> a = np.array([[9, 7, 8],
...               [2, 3, 1],
...               [5, 6, 4]])
>>>
>>> a.sort(axis=1)
>>> a
array([[7, 8, 9],
       [1, 2, 3],
       [4, 5, 6]])


Flip
----
* Does not modify inplace
* Returns new ``np.ndarray``
* Reverse the order of elements in an array along the given axis

Flip vector:

>>> a = np.array([1, 2, 3])
>>>
>>> np.flip(a)
array([3, 2, 1])

Flip matrix:

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])

Flip matrix by crossline from top-left to bottom-right:

>>> np.flip(a)
array([[6, 5, 4],
       [3, 2, 1]])

Flip matrix by rows (bottom rows goes up, upper rows goes down):

>>> np.flip(a, axis=0)
array([[4, 5, 6],
       [1, 2, 3]])

Flip matrix by column (left columns from center goes right, right columns
go left):

>>> np.flip(a, axis=1)
array([[3, 2, 1],
       [6, 5, 4]])


Assignments
-----------
.. literalinclude:: assignments/numpy_sort_a.py
    :caption: :download:`Solution <assignments/numpy_sort_a.py>`
    :end-before: # Solution
