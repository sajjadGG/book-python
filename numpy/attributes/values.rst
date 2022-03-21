Array Attributes
================


Important
---------


SetUp
-----
>>> import numpy as np


Size
----
* Number of elements

.. figure:: img/array-attributes-size.png

>>> a = np.array([1, 2, 3])
>>>
>>> a.size
3

>>> b = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> b.size
6

>>> c = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> c.size
9

>>> d = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>>
>>> d.size
18


Shape
-----
.. figure:: img/array-attributes-shape.png

>>> a = np.array([1, 2, 3])
>>>
>>> a.shape
(3,)

>>> b = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> b.shape
(2, 3)

>>> c = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> c.shape
(3, 3)

>>> d = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>>
>>> d.shape
(2, 3, 3)


NDim
----
* Number of Dimensions
* ``len(ndarray.shape)``

.. figure:: img/array-attributes-ndim.png

>>> a = np.array([1, 2, 3])
>>>
>>> a.ndim
1

>>> b = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> b.ndim
2

>>> c = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> c.ndim
2

>>> d = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>>
>>> d.ndim
3


Length
------
* Number of elements in first dimension
* ``ndarray.shape[0]``

>>> import numpy as np
>>>
>>>
>>> a = np.array([1, 2, 3])
>>>
>>> len(a)
3

>>> b = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> len(b)
2

>>> c = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> len(c)
3

>>> d = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>>
>>> len(d)
2


Recap
-----
.. figure:: img/array-attributes-recap.png


Assignments
-----------
.. literalinclude:: assignments/numpy_attributes_a.py
    :caption: :download:`Solution <assignments/numpy_attributes_a.py>`
    :end-before: # Solution
