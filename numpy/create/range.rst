Array Range
===========


SetUp
-----
>>> import numpy as np


Array range
-----------
Array from Python ``range()``:

>>> np.array(range(5))
array([0, 1, 2, 3, 4])
>>>
>>> np.array(range(5), float)
array([0., 1., 2., 3., 4.])
>>>
>>> np.array(range(5, 10))
array([5, 6, 7, 8, 9])
>>>
>>> np.array(range(5, 10), float)
array([5., 6., 7., 8., 9.])
>>>
>>> np.array(range(5, 10, 2))
array([5, 7, 9])
>>>
>>> np.array(range(5, 10, 2), float)
array([5., 7., 9.])

Array from Python comprehension:

>>> np.array([x for x in range(5)])
array([0, 1, 2, 3, 4])
>>>
>>> np.array([x for x in range(5)], float)
array([0., 1., 2., 3., 4.])
>>>
>>> np.array([x for x in range(5, 10)])
array([5, 6, 7, 8, 9])
>>>
>>> np.array([x for x in range(5, 10)], float)
array([5., 6., 7., 8., 9.])
>>>
>>> np.array([x for x in range(5, 10, 2)])
array([5, 7, 9])
>>>
>>> np.array([x for x in range(5, 10, 2)], float)
array([5., 7., 9.])

Array from ``np.arange()``:

>>> np.arange(5)
array([0, 1, 2, 3, 4])
>>>
>>> np.arange(5, dtype=float)
array([0., 1., 2., 3., 4.])
>>>
>>> np.arange(5.0)
array([0., 1., 2., 3., 4.])
>>>
>>> np.arange(5, 10)
array([5, 6, 7, 8, 9])
>>>
>>> np.arange(5, 10, step=2)
array([5, 7, 9])
>>>
>>> np.arange(start=5, stop=10, step=2)
array([5, 7, 9])
>>>
>>> np.arange(start=5, stop=10, step=2, dtype=float)
array([5., 7., 9.])
>>>
>>> np.arange(0.0, 1.0, 0.1)
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
>>>
>>> np.arange(0.0, 1.0, 0.2)
array([0. , 0.2, 0.4, 0.6, 0.8])
>>>
>>> np.arange(0.0, 1.0, 0.3)
array([0. , 0.3, 0.6, 0.9])


Linspace
--------
>>> # doctest: +SKIP
... def linspace(self,
...              start=...,
...              stop=...,
...              num=50,
...              endpoint=True,
...              retstep=False,
...              dtype=None
...              axis=0
... ) -> np.ndarray: ...

Return evenly spaced numbers over a specified interval.

>>> np.linspace(2.0, 3.0, num=5)
array([2.  , 2.25, 2.5 , 2.75, 3.  ])
>>>
>>> np.linspace(2.0, 3.0, num=5, endpoint=False)
array([2. , 2.2, 2.4, 2.6, 2.8])

>>> data, step = np.linspace(2.0, 3.0, num=5, retstep=True)
>>>
>>> data
array([2.  , 2.25, 2.5 , 2.75, 3.  ])
>>>
>>> step
0.25


Recap
-----
>>> a = np.array(range(0, 10))
>>> b = np.arange(0, 10, 2)
>>> c = np.linspace(0, 10, 100)


Assignments
-----------
.. literalinclude:: assignments/numpy_create_a.py
    :caption: :download:`Solution <assignments/numpy_create_a.py>`
    :end-before: # Solution
