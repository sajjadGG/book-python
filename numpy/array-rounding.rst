Array Rounding
==============


Rationale
-------------------------------------------------------------------------------
* ``np.ceil(n)`` - rounds `n` up to nearest ``int``
* ``np.floor(n)`` - rounds `n` down to nearest ``int``
* ``np.rint(n)`` - rounds `n` to nearest ``int``
* ``np.round(n, [prec])`` - rounds `n` with precision `prec`
* ``np.clip(low, high)`` - trims values to `low` and `high`


Floor
-------------------------------------------------------------------------------
.. code-block:: python

    import numpy as np


    a = np.array([1., 1.00000001, 1.99999999])

    np.floor(a)
    # array([1., 1., 1.])


Ceil
-------------------------------------------------------------------------------
.. code-block:: python

    import numpy as np


    a = np.array([1., 1.00000001, 1.99999999])

    np.ceil(a)
    # array([1., 2., 2.])


Rint
-------------------------------------------------------------------------------
* Round elements of the array to the nearest integer.

.. code-block:: python

    import numpy as np


    a = np.array([1., 1.00000001, 1.99999999])

    np.rint(a)
    # array([1., 1., 2.])


Round
-------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------
.. literalinclude:: assignments/numpy_round_rint.py
    :caption: :download:`Solution <assignments/numpy_round_rint.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_round_ceilfloor.py
    :caption: :download:`Solution <assignments/numpy_round_ceilfloor.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_round_clip.py
    :caption: :download:`Solution <assignments/numpy_round_clip.py>`
    :end-before: # Solution
