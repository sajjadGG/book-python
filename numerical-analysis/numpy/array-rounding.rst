**************
Array Rounding
**************


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


Round
=====
.. code-block:: python

    import numpy as np


    a = np.array([1., 1.00000001, 1.99999999])

    np.rint(a)
    # array([1., 1., 2.])


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


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.clip(2, 5)
    # array([[2, 2, 3],
    #        [4, 5, 5],
    #        [5, 5, 5]])


Assignments
===========
.. todo:: Create assignments
