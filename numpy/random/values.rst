Random Values
=============


Generate Integer
----------------
* Random ``int`` from low (inclusive) to high (exclusive)

>>> import numpy as np
>>> np.random.seed(0)

Generate pseudorandom ``int``:

>>> np.random.randint(0, 10)
5

>>> np.random.randint(0, 10, size=5)
array([0, 3, 3, 7, 9])

>>> np.random.randint(0, 10, size=(2,3))
array([[3, 5, 2],
       [4, 7, 6]])


Generate Float
--------------
* Random ``float`` in the half-open interval ``[0.0, 1.0)``

>>> import numpy as np
>>> np.random.seed(0)

Generate pseudorandom ``float``:

>>> np.random.random()
0.5488135039273248

>>> np.random.random(size=5)
array([0.71518937, 0.60276338, 0.54488318, 0.4236548 , 0.64589411])

>>> np.random.random(size=(2,3))
array([[0.43758721, 0.891773  , 0.96366276],
       [0.38344152, 0.79172504, 0.52889492]])


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
