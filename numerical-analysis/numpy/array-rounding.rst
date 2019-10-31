**************
Array Rounding
**************


Floor
=====
.. code-block:: python

    import numpy as np


    a = np.array([1., 1.41421356, 1.73205081])

    np.floor(a)
    # array([1., 1., 1.])


Ceil
====
.. code-block:: python

    import numpy as np


    a = np.array([1., 1.41421356, 1.73205081])

    np.ceil(a)
    # array([1., 2., 2.])


Round
=====
.. code-block:: python

    import numpy as np


    a = np.array([1., 1.41421356, 1.73205081])

    np.rint(a)
    # array([1., 1., 2.])


Clip
====
* Increase smaller values to lower bound
* Decrease higher values to upper bound

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6])

    a.clip(2, 5)
    # array([2, 2, 3, 4, 5, 5])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])

    a.clip(2, 5)
    # array([[2, 2, 3],
    #        [4, 5, 5]])
