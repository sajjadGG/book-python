***************
Array Iteration
***************


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    for obj in a:
        print(obj)

    # 1
    # 2
    # 3


2-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    for obj in a:
        print(obj)

    # [1 2 3]
    # [4 5 6]
    # [7 8 9]

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    for row in a:
        for obj in row:
            print(obj)

    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

Flat
====

Flatten
-------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    for obj in a.flatten():
        print(obj)

    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

Ravel
-----
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    for obj in a.ravel():
        print(obj)

    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

Enumerate
=========
.. code-block:: python

    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    for i, obj in enumerate(a):
        print(i, obj)

    # 0 [1 2 3]
    # 1 [4 5 6]
    # 2 [7 8 9]


Assignments
===========

Iteration
---------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/numpy_iteration.py`

:English:
    #. Given ``a: ndarray`` (see below)
    #. Use ``for`` to iterate over ``a``
    #. Print even numbers

:Polish:
    #. Dany ``a: ndarray`` (patrz sekcja input)
    #. Używając ``for`` iteruj po ``a``
    #. Wypisz liczby parzyste

:Input:
    .. code-block:: python

        a = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

:The whys and wherefores:
    * Iterating 2-dimensional ``ndarray``

:Hint:
    * ``element % 2 == 0``
