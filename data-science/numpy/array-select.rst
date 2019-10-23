************
Array Select
************


Where
=====

Single argument
---------------
* ``where(boolarray)``
* indexes of elements

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    np.where(a != 2)
    # (array([0, 2]),)

    np.where(a > 1)
    # (array([1, 2]),)

    np.where(a % 2 != 0)
    # (array([0, 2]),)


.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.where(a != 3)
    # (array([0, 0, 1, 1, 1]), array([0, 1, 0, 1, 2]))

    np.where(a % 2 != 0)
    # (array([0, 0, 1]), array([0, 2, 1]))

Multiple argument
-----------------
* ``where(boolarray, truearray, falsearray)``:

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.where(a % 2, 'odd', 'even')
    # array([['odd', 'even', 'odd'],
    #        ['even', 'odd', 'even']], dtype='<U4')

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.where(a > 4, 99, 77)
    # array([[77, 77, 77],
    #        [77, 99, 99]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.where(a != 3, a, None)       # for element ``a != 3`` return such element, otherwise ``None``
    # array([[1, 2, None],
    #        [4, 5, 6]], dtype=object)

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    b = np.logical_and(a > 0, a % 3 == 0)
    # array([[False, False,  True],
    #        [False, False,  True]])

    a[b]
    # array([3, 6])


Nonzero
=======
.. code-block:: python

    import numpy as np


    a = np.array([[1, 0, 2], [3, 0, 4]])
    # array([[1, 0, 2],
    #        [3, 0, 4]])

    a.nonzero()
    # (array([0, 0, 1, 1]), array([0, 2, 0, 2]))


Assignments
===========
