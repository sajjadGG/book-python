***********
Array Index
***********


Selecting items
===============

1-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a[0]        # 1
    a[1]        # 2
    a[2]        # 3
    a[3]        # IndexError: index 3 is out of bounds for axis 0 with size 3
    a[-1]       # 3

2-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a[0]        # array([1, 2, 3])
    a[1]        # array([4, 5, 6])
    a[2]        # IndexError: index 2 is out of bounds for axis 0 with size 2

    a[0,0]      # 1
    a[0,1]      # 2
    a[0,2]      # 3

    a[1,0]      # 4
    a[1,1]      # 5
    a[1,2]      # 6

    a[2,0]      # IndexError: index 2 is out of bounds for axis 0 with size 2


Substituting items
==================

1-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a[0] = 99
    # array([99,  2,  3])

    a[-1] = 88
    # array([99,  2,  88])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3], float)
    # array([1., 2., 3.])

    a[0] = 99.9
    # array([99.9,  2.,  3.])

    a[-1] = 11.1
    # array([99.9,  2.,  11.1])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3], int)
    # array([1, 2, 3])

    a[0] = 99.9
    # array([99,  2,  3])

    a[-1] = 11.1
    # array([99,  2,  11])

2-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a[0,0] = 99
    # array([[99,  2,  3],
    #        [ 4,  5,  6]])

    a[1,2]
    # array([[99,  2,  3],
    #        [ 4,  5, 88]])


Assignments
===========

Index
-----
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_index.py`

:English:
    #. Create ``OUTPUT: ndarray``
    #. Add to ``OUTPUT`` elements from ``INPUT`` (see below) at indexes:

        - row 0, column 2
        - row 2, column 2
        - row 0, column 0
        - row 1, column 0

    #. ``OUTPUT`` size must be 2x2

:Polish:
    #. Stwórz ``OUTPUT: ndarray``
    #. Dodaj do ``OUTPUT`` elementy z ``INPUT`` (patrz poniżej) o indeksach:

        - wiersz 0, kolumna 2
        - wiersz 2, kolumna 2
        - wiersz 0, kolumna 0
        - wiersz 1, kolumna 0

    #. Rozmiar ``OUTPUT`` musi być 2x2

:Input:
    .. code-block:: python

        INPUT = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

:The whys and wherefores:
    * Defining ``np.array``
    * Indexing ``np.array``

:Hint:
    * ``np.zeros(shape, dtype)``
