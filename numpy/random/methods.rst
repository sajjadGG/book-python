Array Random
============


Random Choice (Draw)
--------------------
>>> import numpy as np
>>> np.random.seed(0)

Choice:

>>> np.random.choice([1, 2, 3])
1

>>> np.random.choice([1, 2, 3], size=2)
array([2, 1])

>>> np.random.choice([1, 2, 3], size=2)
array([2, 2])

>>> np.random.choice([1, 2, 3], 2, replace=False)
array([2, 1])


Random Sample
-------------
* Compatible with Python built-in ``random.random``

>>> import numpy as np
>>> np.random.seed(0)

Sample:

>>> np.random.sample(size=5)
array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ])

>>> np.random.sample(size=(2,3))
array([[0.64589411, 0.43758721, 0.891773  ],
       [0.96366276, 0.38344152, 0.79172504]])

>>> np.random.sample(size=(3,2))
array([[0.52889492, 0.56804456],
       [0.92559664, 0.07103606],
       [0.0871293 , 0.0202184 ]])


Shuffle
-------
* Modify sequence in-place (!!)
* Multi-dimensional arrays are only shuffled along the first axis

>>> import numpy as np
>>> np.random.seed(0)

1-dimensional Array:

>>> a = np.array([1, 2, 3])
>>>
>>> np.random.shuffle(a)
>>> a
array([3, 2, 1])

2-dimensional Array:

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> np.random.shuffle(a)
>>> a
array([[7, 8, 9],
       [1, 2, 3],
       [4, 5, 6]])


Assignments
-----------
.. literalinclude:: assignments/numpy_random_a.py
    :caption: :download:`Solution <assignments/numpy_random_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_random_b.py
    :caption: :download:`Solution <assignments/numpy_random_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_random_c.py
    :caption: :download:`Solution <assignments/numpy_random_c.py>`
    :end-before: # Solution
