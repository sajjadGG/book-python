***********
Array Logic
***********


Contains
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    2 in a
    # True

    0 in a
    # False

    [1, 2, 3] in a
    # True

    [1, 2] in a
    # False

    [3, 4] in a
    # False

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([1, 2, 3])

    np.isin(a, b)
    # array([[ True,  True,  True],
    #        [False, False, False]])


Value Comparison
================

Comparision with Scalar
-----------------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a == 2
    # array([[False,  True, False],
    #        [False, False, False]])

    a != 2
    # array([[ True, False,  True],
    #        [ True,  True,  True]])

    a > 2
    # array([[False, False,  True],
    #        [ True,  True,  True]])

    a >= 2
    # array([[False,  True,  True],
    #        [ True,  True,  True]])

    a < 2
    # array([[ True, False, False],
    #        [False, False, False]])

    a <= 2
    # array([[ True,  True, False],
    #        [False, False, False]])

Comparison with Array
---------------------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([3, 2, 1])

    a == b
    # array([False, True, False])

    a != b
    # array([ True, False,  True])

    a > b
    # array([False, False,  True])

    a >= b
    # array([False,  True,  True])

    a < b
    # array([ True, False, False])

    a <= b
    # array([True, True, False])


Boolean Logic
=============

Any
---
.. code-block:: python

    import numpy as np


    a = np.array([True, False, False])
    # array([True, False, False])

    any(a)
    # True

    a.any()
    # True

.. code-block:: python

    import numpy as np


    a = np.array([[True, False, False], [True, True, True]])
    # array([[ True, False, False],
    #        [ True,  True,  True]])

    any(a)
    # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

    a.any()
    # True

    a.any(axis=0)
    # array([ True,  True,  True])

    a.any(axis=1)
    # array([ True,  True])

All
---
.. code-block:: python

    import numpy as np


    a = np.array([True, False, False])
    # array([True, False, False])

    all(a)
    # False

    a.all()
    # False

.. code-block:: python

    import numpy as np


    a = np.array([[True, False, False], [True, True, True]])
    # array([[ True, False, False],
    #        [ True,  True,  True]])

    all(a)
    # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

    a.all()
    # False

    a.all(axis=0)
    # array([ True, False, False])

    a.all(axis=1)
    # array([False,  True])

Logical NOT
-----------
.. code-block:: python

    import numpy as np


    a = np.array([True, False, False])

    np.logical_not(a)
    # array([False,  True,  True])

.. code-block:: python

    import numpy as np


    a = np.array([[True, False, False], [True, True, True]])
    # array([[ True, False, False],
    #        [ True,  True,  True]])

    np.logical_not(a)
    # array([[False,  True,  True],
    #        [False, False, False]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.logical_not(a == 2)
    # array([[ True, False,  True],
    #        [ True,  True,  True]])

    np.logical_not(a > 2)
    # array([[ True,  True, False],
    #        [False, False, False]])

Logical AND
-----------
.. code-block:: python

    import numpy as np


    a = np.array([True, False, False])
    b = np.array([True, True, False])

    np.logical_and(a, b)
    # array([ True, False, False])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.logical_and(a > 2, a < 5)
    # array([[False, False,  True],
    #        [ True, False, False]])

Logical OR
----------
.. code-block:: python

    import numpy as np


    a = np.array([True, False, False])
    b = np.array([True, True, False])

    np.logical_or(a, b)
    # array([ True,  True, False])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.logical_or(a < 2, a > 4)
    # array([[ True, False, False],
    #        [False,  True,  True]])


Infinite
========
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, np.Inf])
    # array([ 1.,  2., inf])

    np.isfinite(a)
    # array([ True,  True, False])

    np.isinf(a)
    # array([False, False,  True])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, np.Inf])
    # array([ 1.,  2., inf])

    np.isnan(a)
    # array([False, False, False])


Not-a-Number
============
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, np.NaN])
    # array([ 1.,  2., nan])

    np.isnan(a)
    # array([False, False,  True])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, np.NaN])
    # array([ 1.,  2., nan])

    np.isfinite(a)
    # array([ True,  True, False])

    np.isinf(a)
    # array([False, False, False])


Assignments
===========
.. todo:: Create assignments
