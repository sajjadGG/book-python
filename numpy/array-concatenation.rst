*******************
Array Concatenation
*******************


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    np.concatenate(a, b)
    # Traceback (most recent call last):
    # TypeError: only integer scalar arrays can be converted to a scalar index

    np.concatenate((a, b))
    # array([1, 2, 3, 4, 5, 6])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = np.array([7, 8, 9])

    np.concatenate((a, b, c))
    # array([1, 2, 3, 4, 5, 6, 7, 8, 9])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([2, 3, 4])

    np.concatenate((a, b))
    # array([1, 2, 3, 2, 3, 4])


2-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    np.concatenate((a, b))
    # array([[1, 2],
    #        [3, 4],
    #        [5, 6],
    #        [7, 8]])

    np.concatenate((a, b), axis=0)
    # array([[1, 2],
    #        [3, 4],
    #        [5, 6],
    #        [7, 8]])

    np.concatenate((a, b), axis=1)
    # array([[1, 2, 5, 6],
    #        [3, 4, 7, 8]])


Assignments
===========

.. todo:: Convert assignments to literalinclude

Numpy Concatenation
-------------------
* Assignment: Numpy Concatenation
* Filename: :download:`assignments/numpy_concatenation.py`
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Given are one-dimensional: ``a: np.ndarray``, ``b: np.ndarray``
    3. Concatenate them as ``result: np.ndarray``
    4. Reshape ``result`` into two rows and three columns
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dane są jednowymiarowe: ``a: np.ndarray``, ``b: np.ndarray``
    3. Połącz je ze sobą jako ``result: np.ndarray``
    4. Przekształć ``result`` w dwa wiersze na trzy kolumny
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])

Tests:
    >>> result
    array([[1, 2, 3],
           [4, 5, 6]])
