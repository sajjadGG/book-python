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


Rint
====
* Round elements of the array to the nearest integer.

.. code-block:: python

    import numpy as np


    a = np.array([1., 1.00000001, 1.99999999])

    np.rint(a)
    # array([1., 1., 2.])


Round
=====
* Round elements of the array to the precision

.. code-block:: python

    import numpy as np


    a = np.array([1.23, 1.456, 1.789])


    np.round(a)
    # array([1., 1., 2.])

    np.round(a, 1)
    # array([1.2, 1.5, 1.8])

    np.round(a, 2)
    # array([1.23, 1.46, 1.79])

    np.round(a, 3)
    # array([1.23 , 1.456, 1.789])


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


    a = np.array([[-2, -1, 0],
                  [0, 1, 2]])


    a.astype(bool)
    # array([[ True,  True, False],
    #        [False,  True,  True]])

    a.clip(0, 1)
    # array([[0, 0, 0],
    #        [0, 1, 1]])

    a.clip(0, 1).astype(bool)
    # array([[False, False, False],
    #        [False,  True,  True]])


Assignments
===========

Numpy Round Rint
----------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/numpy_round_rint.py`

:English:
    #. Set random seed to zero
    #. Generate ``result: ndarray`` of 21 random numbers from range ``<0.0; 1.1)``
    #. Round values to integers
    #. Convert data type to ``np.int8``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Wygeneruj ``result: ndarray`` z 21 losowymi liczbami z przedziału ``<0.0; 1.1)``
    #. Zaokrąglij wartości do pełnych liczb całkowitych
    #. Przekonwertuj typ danych do ``np.int8``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        result: ndarray
        # array([1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1], dtype=int8)

Numpy Round Floor and Ceil
--------------------------
* Complexity level: medium
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/numpy_round_ceilfloor.py`

:English:
    #. Set random seed to zero
    #. Generate ``data: ndarray`` of 21 random numbers from range ``<0.0; 1.1)``
    #. Ceil round ``data`` values and print them
    #. Floor round ``data`` values and print them
    #. Round ``data`` values and print them
    #. Compare result with "Output" section (see below)

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Wygeneruj ``data: ndarray`` z 21 losowymi liczbami z przedziału ``<0.0; 1.1)``
    #. Zaokrąglij wartości ``data`` w górę (ceil) i je wypisz
    #. Zaokrąglij wartości ``data`` w dół (floor) i je wypisz
    #. Zaokrąglij wartości ``data`` i je wypisz
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        ceil: ndarray
        # array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        #        1., 1., 1., 1.])

        floor: ndarray
        # array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        #        0., 0., 0., 0.])

        round: ndarray
        # array([1., 1., 1., 1., 0., 1., 0., 1., 1., 0., 1., 1., 1., 1., 0., 0., 0.,
        #        1., 1., 1., 1.])

Numpy Round Clip
----------------
* Complexity level: medium
* Lines of code to write: 3 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/numpy_round_clip.py`

:English:
    #. Set random seed to zero
    #. Generate ``result: ndarray`` of 21 random integers from 0 to 100 (exclusive)
    #. Change shape to 7x3
    #. Clip numbers only in first column to 50 (inclusive) to 80 (exclusive)
    #. Print ``result``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Wygeneruj ``result: ndarray`` z 21 losowymi liczbami całkowitymi od 0 do 100 (rozłącznie)
    #. Zmień kształt na 7x3
    #. Przytnij liczby w pierwszej kolumnie od 50 (włącznie) do 80 (rozłącznie)
    #. Wypisz ``result``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

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
