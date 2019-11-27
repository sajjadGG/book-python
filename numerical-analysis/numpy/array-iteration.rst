***************
Array Iteration
***************


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    for element in a:
        print(element)

    # 1
    # 2
    # 3


2-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    for element in a:
        print(element)

    # [1 2 3]
    # [4 5 6]

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    for element in a:
        print(element)

    # [1 2 3]
    # [4 5 6]
    # [7 8 9]


Assignments
===========

Iteration
---------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_iteration.py`

:English:
    #. Given ``a: ndarray`` (see below)
    #. Iterate over ``a``
    #. Print even numbers

:Polish:
    #. Dany ``a: ndarray`` (patrz sekcja input)
    #. Iteruj po ``a``
    #. Wypisz liczby parzyste

:Input:
    .. code-block:: python

        a = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

:The whys and wherefores:
    * Iterating 2-dimensional ``ndarray``

:Hint:
    ``element % 2 == 0``
