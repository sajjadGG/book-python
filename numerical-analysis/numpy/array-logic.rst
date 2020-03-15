***********
Array Logic
***********


Contains
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    2 in a
    # True

    0 in a
    # False

    [1, 2, 3] in a
    # True

    [1, 2] in a
    # False

    [3, 4] in a
    # False

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    b = np.array([1, 2, 3])

    np.isin(a, b)
    # array([[ True,  True,  True],
    #        [False, False, False]])


Value Comparison
================

Comparision with Scalar
-----------------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a == 2
    # array([[False,  True, False],
    #        [False, False, False]])

    a != 2
    # array([[ True, False,  True],
    #        [ True,  True,  True]])

    a > 2
    # array([[False, False,  True],
    #        [ True,  True,  True]])

    a >= 2
    # array([[False,  True,  True],
    #        [ True,  True,  True]])

    a < 2
    # array([[ True, False, False],
    #        [False, False, False]])

    a <= 2
    # array([[ True,  True, False],
    #        [False, False, False]])

Comparison with Array
---------------------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([3, 2, 1])

    a == b
    # array([False, True, False])

    a != b
    # array([ True, False,  True])

    a > b
    # array([False, False,  True])

    a >= b
    # array([False,  True,  True])

    a < b
    # array([ True, False, False])

    a <= b
    # array([True, True, False])


Boolean Logic
=============

Any
---
.. code-block:: python

    import numpy as np


    a = np.array([True, False, False])
    # array([True, False, False])

    any(a)
    # True

    a.any()
    # True

.. code-block:: python

    import numpy as np


    a = np.array([[True, False, False],
                  [True, True, True]])

    any(a)
    # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

    a.any()
    # True

    a.any(axis=0)
    # array([ True,  True,  True])

    a.any(axis=1)
    # array([ True,  True])

All
---
.. code-block:: python

    import numpy as np


    a = np.array([True, False, False])

    all(a)
    # False

    a.all()
    # False

.. code-block:: python

    import numpy as np


    a = np.array([[True, False, False],
                  [True, True, True]])

    all(a)
    # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

    a.all()
    # False

    a.all(axis=0)
    # array([ True, False, False])

    a.all(axis=1)
    # array([False,  True])

Logical NOT
-----------
* ``np.logical_not(...)``
* ``~(...)``

.. code-block:: python

    import numpy as np


    a = np.array([[True, False, False],
                  [True, True, True]])

    np.logical_not(a)
    # array([[False,  True,  True],
    #        [False, False, False]])

    ~a
    # array([[False,  True,  True],
    #        [False, False, False]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.logical_not(a > 2)
    # array([[ True,  True, False],
    #        [False, False, False]])

    ~(a > 2)
    # array([[ True,  True, False],
    #        [False, False, False]])


Logical AND
-----------
* Meets first and second condition at the same time
* ``np.logical_and(..., ...)``
* ``(...) & (...)``

.. code-block:: python

    import numpy as np


    a = np.array([True, False, False])
    b = np.array([True, True, False])

    np.logical_and(a, b)
    # array([ True, False, False])

    a & b
    # array([ True, False, False])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.logical_and(a > 2, a < 5)
    # array([[False, False,  True],
    #        [ True, False, False]])

    (a > 2) & (a < 5)
    # array([[False, False,  True],
    #        [ True, False, False]])


Logical OR
----------
* Meets first or second condition at the same time
* ``np.logical_or(..., ...)``
* ``(...) | (...)``

.. code-block:: python

    import numpy as np


    a = np.array([True, False, False])
    b = np.array([True, True, False])

    np.logical_or(a, b)
    # array([ True,  True, False])

    a | b
    # array([ True,  True, False])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.logical_or(a < 2, a > 4)
    # array([[ True, False, False],
    #        [False,  True,  True]])

    (a < 2) | (a > 4)
    # array([[ True, False, False],
    #        [False,  True,  True]])

Logical XOR
-----------
* Meets first or second condition, but not both at the same time
* ``np.logical_xor(..., ...)``
* ``(...) ^ (...)``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.logical_xor(a < 2, a > 4)
    # array([[ True, False, False],
    #        [False,  True,  True]])

    (a < 2) ^ (a > 4)
    # array([[ True, False, False],
    #        [False,  True,  True]])


Signum
======
.. code-block:: python

    import numpy as np


    a = np.array([[-2, -1, 0],
                  [0, 1, 2]])

    np.sign(a)
    # array([[-1, -1,  0],
    #        [ 0,  1,  1]])


Assignments
===========

Array Logic
-----------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/numpy_logic.py`

:English:
    #. Set random seed to zero
    #. Generate ``a: ndarray`` of 9 random integers from 0 to 100 (exclusive)
    #. Check for even numbers which are less than 50
    #. Check if all numbers matches this condition
    #. Check if any number matches this condition

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Wygeneruj ``a: ndarray`` z 9 losowymi liczbami całkowitymi od 0 do 100 (rozłącznie)
    #. Sprawdź parzyste elementy, które są mniejsze od 50
    #. Sprawdź czy wszystkie liczby spełniają ten warunek
    #. Sprawdź czy jakakolwiek liczba spełnia ten warunek

Is in Array
-----------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/numpy_isin.py`

:English:
    #. Set random seed to zero
    #. Generate ``a: ndarray`` of 50 random integers from 0 to 100 (exclusive)
    #. Generate ``b: ndarray`` with sequential powers of 2 and exponential from 0 to 6 (inclusive)
    #. Check which elements from ``a`` are present in ``b``

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Wygeneruj ``a: ndarray`` z 50 losowymi liczbami całkowitymi od 0 do 100 (rozłącznie)
    #. Wygeneruj ``b: ndarray`` z kolejnymi potęgami liczby 2, wykładnik od 0 do 6 (włącznie)
    #. Sprawdź, które elementy z ``a`` są obecne w ``b``

