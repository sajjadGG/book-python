Array Arithmetic
================


Rationale
---------
.. glossary::

    Scalar
        Single Value

    Vectorized Operations
        Single statement without a loop that explains a looping concept.
        Applies operation to each element.

        >>> import numpy as np
        >>>
        >>>
        >>> a = np.array([1, 2, 3])
        >>>
        >>> a + 1
        array([2, 3, 4])


Addition
--------
>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a + 2
array([[3, 4, 5],
       [6, 7, 8]])


Subtraction
-----------
>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a - 2
array([[-1,  0,  1],
       [ 2,  3,  4]])


Division
--------
>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])

True division:

>>> a / 2
array([[0.5, 1. , 1.5],
       [2. , 2.5, 3. ]])

Floor division:

>>> a // 2
array([[0, 1, 1],
       [2, 2, 3]])

Modulo:

>>> a % 2
array([[1, 0, 1],
       [0, 1, 0]])


Multiplication
--------------
* Scalar multiplication

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
>>>               [4, 5, 6]])
>>>
>>> a * 2
array([[ 2,  4,  6],
       [ 8, 10, 12]])


Power
-----
* ``np.power()``

.. todo:: Performance testing np.power(a) vs a ** 2

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
>>>               [4, 5, 6]])
>>>
>>> a ** 2
>>> # array([[ 1,  4,  9],
>>> #        [16, 25, 36]])


Roots
-----
* ``np.sqrt()``

.. todo:: Performance testing np.sqrt(a) vs a ** (1/2)

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
>>>               [4, 5, 6]])
>>>
>>> a ** (1/2)
array([[1.        , 1.41421356, 1.73205081],
       [2.        , 2.23606798, 2.44948974]])


Assignments
-----------
.. todo:: Create assignments
