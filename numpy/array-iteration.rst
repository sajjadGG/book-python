***************
Array Iteration
***************


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    data = np.array([1, 2, 3])

    for value in data:
        print(value)

    # 1
    # 2
    # 3


2-dimensional Array
===================
.. code-block:: python

    import numpy as np


    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for value in data:
        print(value)

    # [1 2 3]
    # [4 5 6]
    # [7 8 9]

.. code-block:: python

    import numpy as np


    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for row in data:
        for value in row:
            print(value)

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
.. code-block:: python
    :caption: Flatten

    import numpy as np


    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for value in data.flatten():
        print(value)

    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

.. code-block:: python
    :caption: Ravel

    import numpy as np


    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for value in data.ravel():
        print(value)

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

    import numpy as np

    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for i, value in enumerate(data):
        print(i, value)

    # 0 [1 2 3]
    # 1 [4 5 6]
    # 2 [7 8 9]

.. code-block:: python

    import numpy as np

    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for i, value in enumerate(data.ravel()):
        print(i, value)
    # 0 1
    # 1 2
    # 2 3
    # 3 4
    # 4 5
    # 5 6
    # 6 7
    # 7 8
    # 8 9

.. code-block:: python

    import numpy as np

    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    for i, row in enumerate(data):
        for j, value in enumerate(row):
            print(i, j, value)

    # 0 0 1
    # 0 1 2
    # 0 2 3
    # 1 0 4
    # 1 1 5
    # 1 2 6
    # 2 0 7
    # 2 1 8
    # 2 2 9


Assignments
===========

.. todo:: Convert assignments to literalinclude

Numpy Iteration
---------------
* Assignment: Numpy Iteration
* Filename: :download:`assignments/numpy_iteration.py`
* Complexity: easy
* Lines of code: 9 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Use ``for`` to iterate over ``DATA``
    3. Print even numbers

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Używając ``for`` iteruj po ``DATA``
    3. Wypisz liczby parzyste

Hints:
    * ``number % 2 == 0``

Given:
    .. code-block:: python

        DATA = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

