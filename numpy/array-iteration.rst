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
Flatten:

.. code-block:: python

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

Ravel:

.. code-block:: python

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
.. literalinclude:: assignments/numpy_iteration.py
    :caption: :download:`Solution <assignments/numpy_iteration.py>`
    :end-before: # Solution
