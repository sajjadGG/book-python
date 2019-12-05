**************
Array Rounding
**************


Floor
=====
.. code-block:: python

    import numpy as np


    a = np.array([1., 1.00000001, 1.99999999])

    np.floor(a)
    # array([1., 1., 1.])


Ceil
====
.. code-block:: python

    import numpy as np


    a = np.array([1., 1.00000001, 1.99999999])

    np.ceil(a)
    # array([1., 2., 2.])


Round
=====
* Round elements of the array to the nearest integer.
* There is no ``np.round()`` method
* Only ``np.rint()``

.. code-block:: python

    import numpy as np


    a = np.array([1., 1.00000001, 1.99999999])

    np.rint(a)
    # array([1., 1., 2.])


Clip
====
* Increase smaller values to lower bound
* Decrease higher values to upper bound

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.clip(2, 5)
    # array([2, 2, 3])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.clip(2, 5)
    # array([[2, 2, 3],
    #        [4, 5, 5]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.clip(2, 5)
    # array([[2, 2, 3],
    #        [4, 5, 5],
    #        [5, 5, 5]])


Assignments
===========

Clip
----
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_clip.py`

:English:
    #. Set random seed to zero
    #. Generate ``a: ndarray`` of 21 random integers from 0 to 100 (exclusive)
    #. Change shape to 7x3
    #. Clip numbers only in first column to 50 (inclusive) to 80 (exclusive)
    #. Print ``a``

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Wygeneruj ``a: ndarray`` z 21 losowymi liczbami całkowitymi od 0 do 100 (rozłącznie)
    #. Zmień kształt na 7x3
    #. Przytnij liczby w pierwszej kolumnie od 50 (włącznie) do 80 (rozłącznie)
    #. Wypisz ``a``

:Output:
    .. code-block:: python

        a: ndarray
        # array([[50, 47, 64],
        #        [67, 67,  9],
        #        [79, 21, 36],
        #        [79, 70, 88],
        #        [79, 12, 58],
        #        [65, 39, 87],
        #        [50, 88, 81]])
