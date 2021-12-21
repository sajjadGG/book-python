Array Getitem
=============


.. todo:: Split chapters GetItem and Slice by __getitem__ argument type.


Rationale
---------
* ``int``
* ``list[int]``
* ``list[bool]``

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a[ 0 ]              # int
array([1, 2, 3])
>>>
>>> a[ [0,2] ]          # list[int]
array([[1, 2, 3],
       [7, 8, 9]])
>>>
>>> a[ [True,False,True] ]   # list[bool]
array([[1, 2, 3],
       [7, 8, 9]])


Index
-----
>>> import numpy as np
>>>
>>>
>>> a = np.array([1, 2, 3])
>>>
>>>
>>> a.flat[0]
1
>>> a.flat[1]
2
>>> a.flat[2]
3
>>> a.flat[4]
Traceback (most recent call last):
IndexError: index 4 is out of bounds for axis 0 with size 3

Flat:

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a.flat[0]
1
>>> a.flat[1]
2
>>> a.flat[2]
3
>>> a.flat[3]
4
>>> a.flat[4]
5
>>> a.flat[5]
6

Multidimensional:

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a[0][0]
1
>>> a[0][1]
2
>>> a[0][2]
3
>>> a[1][0]
4
>>> a[1][1]
5
>>> a[1][2]
6
>>> a[2]
Traceback (most recent call last):
IndexError: index 2 is out of bounds for axis 0 with size 2
>>>
>>> a[-1][-1]
6
>>> a[-3]
Traceback (most recent call last):
IndexError: index -3 is out of bounds for axis 0 with size 2
>>>
>>> a[0,0]
1
>>> a[0,1]
2
>>> a[0,2]
3
>>> a[1,0]
4
>>> a[1,1]
5
>>> a[1,2]
6


Selecting items
---------------
1-dimensional Array:

>>> import numpy as np
>>>
>>>
>>> a = np.array([1, 2, 3])
array([1, 2, 3])
>>>
>>> a[0]
1
>>> a[1]
2
>>> a[2]
3
>>> a[3]
Traceback (most recent call last):
IndexError: index 3 is out of bounds for axis 0 with size 3
>>> a[-1]
3

2-dimensional Array:

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a[0]
array([1, 2, 3])
>>> a[1]
array([4, 5, 6])
>>> a[2]
Traceback (most recent call last):
IndexError: index 2 is out of bounds for axis 0 with size 2
>>>
>>> a[0,0]
1
>>> a[0,1]
2
>>> a[0,2]
3
>>>
>>> a[1,0]
4
>>> a[1,1]
5
>>> a[1,2]
6
>>>
>>> a[2,0]
Traceback (most recent call last):
IndexError: index 2 is out of bounds for axis 0 with size 2

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a[0]
array([1, 2, 3])
>>> a[1]
array([4, 5, 6])
>>> a[2]
Traceback (most recent call last):
IndexError: index 2 is out of bounds for axis 0 with size 2
>>>
>>> a[0,0]
1
>>> a[0,1]
2
>>> a[0,2]
3
>>>
>>> a[1,0]
4
>>> a[1,1]
5
>>> a[1,2]
6
>>>
>>> a[2,0]
7
>>> a[2,1]
8
>>> a[2,2]
9

3-dimensional Array:

>>> import numpy as np
>>>
>>>
>>> a = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>>
>>> a[0,0,0]
1
>>> a[0,0,1]
2
>>> a[0,0,2]
3
>>> a[0,0,3]
Traceback (most recent call last):
IndexError: index 3 is out of bounds for axis 2 with size 3
>>>
>>> a[0,1,2]
6
>>> a[0,2,1]
6
>>> a[2,1,0]
Traceback (most recent call last):
IndexError: index 2 is out of bounds for axis 0 with size 2


Substituting items
------------------
>>> import numpy as np

1-dimensional Array:

* Will type cast values to ``np.ndarray.dtype``

>>> a = np.array([1, 2, 3])
>>>
>>> a[0] = 99
array([99,  2,  3])
>>>
>>> a[-1] = 11
array([99,  2,  11])

>>> a = np.array([1, 2, 3], float)
>>>
>>> a[0] = 99.9
array([99.9,  2.,  3.])
>>>
>>> a[-1] = 11.1
array([99.9,  2.,  11.1])

>>> a = np.array([1, 2, 3], int)
>>>
>>> a[0] = 99.9
array([99,  2,  3])
>>>
>>> a[-1] = 11.1
array([99,  2,  11])

2-dimensional Array:

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a[0,0] = 99
array([[99,  2,  3],
       [ 4,  5,  6]])
>>>
>>> a[1,2] = 11
array([[99,  2,  3],
       [ 4,  5, 11]])


Multi-indexing
--------------
>>> import numpy as np
>>>
>>>
>>> a = np.array([1, 2, 3])
>>>
>>> a[0], a[2], a[-1]
(1, 3, 3)
>>>
>>> a[[0,2,-1]]
array([1, 3, 3])
>>>
>>> a[[True, False, True]]
array([1, 3])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a[[0,1]]
array([[1, 2, 3],
       [4, 5, 6]])
>>>
>>> a[[0,2,-1]]
array([[1, 2, 3],
       [7, 8, 9],
       [7, 8, 9]])
>>>
>>> a[[True, False, True]]
array([[1, 2, 3],
       [7, 8, 9]])


Assignments
-----------
.. literalinclude:: assignments/numpy_indexing.py
    :caption: :download:`Solution <assignments/numpy_indexing.py>`
    :end-before: # Solution
