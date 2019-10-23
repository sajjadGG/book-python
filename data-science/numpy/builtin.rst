*********
Built-ins
*********


Contants
========

Pi number
---------
.. code-block:: python

    import numpy as np


    np.pi
    # 3.1415926535897931

Euler number
------------
.. code-block:: python

    import numpy as np


    np.e
    # 2.7182818284590451

Not-a-Number
------------
.. code-block:: python

    import numpy as np


    np.nan
    # NaN

Infinity
--------
.. code-block:: python

    import numpy as np


    np.inf
    # inf


Functions
=========

Square Root
-----------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    np.sqrt(a)
    # array([1., 1.41421356, 1.73205081])

Rounding
--------
.. code-block:: python

    import numpy as np


    a = np.array([1., 1.41421356, 1.73205081])

    np.floor(a)
    # array([1., 1., 1.])

    np.ceil(a)
    # array([1., 2., 2.])

    np.rint(a)
    # array([1., 1., 2.])



.. code-block:: python

    a = np.array([6, 2, 5, -1, 0], float)

    sorted(a)
    # [-1.0, 0.0, 2.0, 5.0, 6.0]

    a.sort()
    # array([-1., 0., 2., 5., 6.])

.. code-block:: python

    a = np.array([6, 2, 5, -1, 0], float)

    a.clip(0, 5)
    # array([ 5., 2., 5., 0., 0.])

.. code-block:: python

    a = np.array([1, 1, 4, 5, 5, 5, 7], float)

    np.unique(a)
    # array([ 1., 4., 5., 7.])

.. code-block:: python

    a = np.array([[1, 2], [3, 4]], float)

    a.diagonal()
    # array([ 1., 4.])


Assignments
===========
