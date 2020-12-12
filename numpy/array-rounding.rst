**************
Array Rounding
**************


Rationale
=========
* ``np.ceil(n)`` - rounds `n` up to nearest ``int``
* ``np.floor(n)`` - rounds `n` down to nearest ``int``
* ``np.rint(n)`` - rounds `n` to nearest ``int``
* ``np.round(n, [prec])`` - rounds `n` with precision `prec`
* ``np.clip(low, high)`` - trims values to `low` and `high`


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

.. code-block:: python

    import numpy as np

    data = 3.1415

    np.round(data, 2)
    # 3.14

.. code-block:: python

    import numpy as np

    data = np.array([[3.1415, 2.7182],
                     [3.1415, 2.7182]])

    np.round(data, 2)
    # array([3.14, 2.72])

.. code-block:: python

    import numpy as np

    data = np.array([[3.1415, 2.7182],
                     [3.1415, 2.7182]])

    np.round(data, 2)
    # array([[3.14, 2.72],
    #        [3.14, 2.72]])


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

.. todo:: Convert assignments to literalinclude

Numpy Round Rint
----------------
* Assignment: Numpy Round Rint
* Filename: :download:`assignments/numpy_round_rint.py`
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Round values to integers
    3. Convert data type to ``np.int8``
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zaokrąglij wartości do pełnych liczb całkowitych
    3. Przekonwertuj typ danych do ``np.int8``
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = np.array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
                         0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152,
                         0.79172504, 0.52889492, 0.56804456, 0.92559664, 0.07103606,
                         0.0871293 , 0.0202184 , 0.83261985, 0.77815675, 0.87001215,
                         0.97861834])

Tests:
    >>> type(result)
    np.ndarray
    >>> result
    array([1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1], dtype=int8)

Numpy Round Floor and Ceil
--------------------------
* Assignment: Numpy Round Floor and Ceil
* Filename: :download:`assignments/numpy_round_ceilfloor.py`
* Complexity: medium
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Ceil round ``data`` values and print them
    3. Floor round ``data`` values and print them
    4. Round ``data`` values and print them
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zaokrąglij wartości ``data`` w górę (ceil) i je wypisz
    3. Zaokrąglij wartości ``data`` w dół (floor) i je wypisz
    4. Zaokrąglij wartości ``data`` i je wypisz
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = np.array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
                         0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152,
                         0.79172504, 0.52889492, 0.56804456, 0.92559664, 0.07103606,
                         0.0871293 , 0.0202184 , 0.83261985, 0.77815675, 0.87001215,
                         0.97861834])

Tests:
    .. code-block:: python

        ceil: np.ndarray
        # array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        #        1., 1., 1., 1.])

        floor: np.ndarray
        # array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        #        0., 0., 0., 0.])

        round: np.ndarray
        # array([1., 1., 1., 1., 0., 1., 0., 1., 1., 0., 1., 1., 1., 1., 0., 0., 0.,
        #        1., 1., 1., 1.])

Numpy Round Clip
----------------
* Assignment: Numpy Round Clip
* Filename: :download:`assignments/numpy_round_clip.py`
* Complexity: medium
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Create ``result: np.ndarray`` copy of ``DATA``
    3. Clip numbers only in first column to 50 (inclusive) to 80 (exclusive)
    4. Print ``result``
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz ``result: np.ndarray`` z kopią danych z ``DATA``
    3. Przytnij liczby w pierwszej kolumnie od 50 (włącznie) do 80 (rozłącznie)
    4. Wypisz ``result``
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = np.array([[44, 47, 64],
                         [67, 67,  9],
                         [83, 21, 36],
                         [87, 70, 88],
                         [88, 12, 58],
                         [65, 39, 87],
                         [46, 88, 81]])

Tests:
    >>> type(result)
    np.ndarray
    >>> result
    # array([[50, 47, 64],
    #        [67, 67,  9],
    #        [79, 21, 36],
    #        [79, 70, 88],
    #        [79, 12, 58],
    #        [65, 39, 87],
    #        [50, 88, 81]])
