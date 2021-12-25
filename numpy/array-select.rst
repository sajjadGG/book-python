Array Select
============


Unique
------
>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3, 1],
...               [1, 4, 5, 6]])
>>>
>>> np.unique(a)
array([1, 2, 3, 4, 5, 6])
>>>
>>> np.unique(a, axis=0)
array([[1, 2, 3, 1],
       [1, 4, 5, 6]])
>>>
>>> np.unique(a, axis=1)
array([[1, 1, 2, 3],
       [1, 6, 4, 5]])


Diagonal
--------
>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2],
...               [3, 4]])
>>>
>>> a.diagonal()
array([1, 4])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a.diagonal()
array([1, 5])

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> a.diagonal()
array([1, 5, 9])


Nonzero
-------
* Each element of the tuple contains one of the indices for each nonzero value.
* Therefore, the length of each tuple element is the number of nonzeros in the array.
* The first element of the tuple is the first index for each of the nonzero values: (``[0, 0, 1, 1]``).
* The second element of the tuple is the second index for each of the nonzero values: (``[0, 2, 0, 2]``).
* Pairs are zipped (first and second tuple):

    * ``0, 0``
    * ``0, 2``
    * ``1, 0``
    * ``1, 2``

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 0, 2],
...               [3, 0, 4]])
>>>
>>> a.nonzero()  # doctest: +NORMALIZE_WHITESPACE
(array([0, 0, 1, 1]),
 array([0, 2, 0, 2]))
>>>
>>> a[a.nonzero()]
array([1, 2, 3, 4])


Where
-----
* ``where(boolarray)``
* indexes of elements

>>> import numpy as np

Single argument:

>>> a = np.array([1, 2, 3, 4, 5, 6])
>>>
>>> np.where(a != 2)
(array([0, 2, 3, 4, 5]),)
>>>
>>> np.where(a % 2 == 0)
(array([1, 3, 5]),)
>>>
>>> np.where( (a>2) & (a<5) )
(array([2, 3]),)

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> np.where(a % 2 == 0)  # doctest: +NORMALIZE_WHITESPACE
(array([0, 1, 1, 2]),
 array([1, 0, 2, 1]))
>>>
>>> np.where( (a>2) & (a<5) )  # doctest: +NORMALIZE_WHITESPACE
(array([0, 1]),
 array([2, 0]))


Multiple argument
-----------------
* ``where(boolarray, truearray, falsearray)``:

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])

>>> np.where(a < 5, 'small', 'large')
array([['small', 'small', 'small'],
       ['small', 'large', 'large'],
       ['large', 'large', 'large']], dtype='<U5')

>>> np.where(a % 2 == 0, 'even', 'odd')
array([['odd', 'even', 'odd'],
       ['even', 'odd', 'even'],
       ['odd', 'even', 'odd']], dtype='<U4')

>>> np.where(a % 2 == 0, np.nan, a)
array([[ 1., nan,  3.],
       [nan,  5., nan],
       [ 7., nan,  9.]])


Take
----
>>> import numpy as np

>>> a = np.array([1, 2, 3])
>>> at_index = np.array([0, 0, 1, 2, 2, 1])
>>>
>>> a.take(at_index)
array([1, 1, 2, 3, 3, 2])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> at_index = np.array([0, 0, 1])
>>>
>>> a.take(at_index, axis=0)
array([[1, 2, 3],
       [1, 2, 3],
       [4, 5, 6]])
>>>
>>> a.take(at_index, axis=1)
array([[1, 1, 2],
       [4, 4, 5],
       [7, 7, 8]])


Assignments
-----------
.. literalinclude:: assignments/numpy_select_isin.py
    :caption: :download:`Solution <assignments/numpy_select_isin.py>`
    :end-before: # Solution
