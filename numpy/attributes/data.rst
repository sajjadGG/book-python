Array Attributes
================


Rationale
---------


SetUp
-----
>>> import numpy as np


Itemsize
--------
* ``int64`` takes 64 bits (8 bytes of memory)

.. figure:: img/array-attributes-itemsize.png

>>> a = np.array([1, 2, 3], dtype=int)
>>> a.itemsize
8
>>>
>>> b = np.array([1, 2, 3], dtype=np.int0)
>>> b.itemsize
8
>>>
>>> c = np.array([1, 2, 3], dtype=np.int8)
>>> c.itemsize
1
>>>
>>> d = np.array([1, 2, 3], dtype=np.int16)
>>> d.itemsize
2
>>>
>>> e = np.array([1, 2, 3], dtype=np.int32)
>>> e.itemsize
4
>>>
>>> f = np.array([1, 2, 3], dtype=np.int64)
>>> f.itemsize
8

>>> a = np.array([1, 2, 3], dtype=float)
>>> a.itemsize
8
>>>
>>> b = np.array([1, 2, 3], dtype=np.float16)
>>> b.itemsize
2
>>>
>>> c = np.array([1, 2, 3], dtype=np.float32)
>>> c.itemsize
4
>>>
>>> d = np.array([1, 2, 3], dtype=np.float64)
>>> d.itemsize
8


Strides
-------
* ``int64`` takes 64 bits (8 bytes of memory)
* Strides inform how many bytes numpy has to jump to access values in each dimensions

.. figure:: img/array-attributes-strides.png

>>> a = np.array([1, 2, 3])
>>>
>>> a.strides
(8,)

>>> b = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> b.strides
(24, 8)

>>> c = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> c.strides
(24, 8)

>>> d = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>>
>>> d.strides
(72, 24, 8)


Data
----
>>> a = np.array([1, 2, 3])
>>>
>>> a.data  # doctest: +ELLIPSIS
<memory at 0x...>

>>> b = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> b.data  # doctest: +ELLIPSIS
<memory at 0x...>

>>> c = np.array([[[ 1,  2,  3],
...                [ 4,  5,  6],
...                [ 5,  6,  7]],
...
...               [[11, 22, 33],
...                [44, 55, 66],
...                [77, 88, 99]]])
>>>
>>> c.data  # doctest: +ELLIPSIS
<memory at 0x...>

.. figure:: img/array-attributes-data.png


Recap
-----
.. figure:: img/array-attributes-recap.png


Assignments
-----------
.. literalinclude:: assignments/numpy_attributes_a.py
    :caption: :download:`Solution <assignments/numpy_attributes_a.py>`
    :end-before: # Solution
