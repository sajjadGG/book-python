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

Logical AND
-----------
.. code-block:: python

    a = np.array([1, 3, 0], float)

    np.logical_and(a > 0, a < 3)
    # array([ True, False, False], dtype=bool)

Logical NOT
-----------
.. code-block:: python

    a = np.array([True, False, True], bool)

    np.logical_not(a)
    # array([False, True, False], dtype=bool)

Logical OR
----------
.. code-block:: python

    a = np.array([True, False, True], bool)
    b = np.array([False, True, False], bool)

    np.logical_or(a, b)
    # array([ True, True, False], dtype=bool)


Where
=====
* Single argument where ``where(boolarray)``:

    .. code-block:: python

        a = np.array([1, 3, 0], float)

        np.where(a != 0)
        # array([0, 1])  # indexes of elements


        b = np.array([1, 0, 3, 4, 0], float)
        np.where(b != 0)
        # array([0, 2, 3])

* Multiple argument where ``where(boolarray, truearray, falsearray)``:

    .. code-block:: python

        a = np.array([1, 3, 0], float)

        np.where(a != 0, a, None)  # for element ``a != 0`` return such element, otherwise ``None``
        # array([1.0, 3.0, None], dtype=object)

    .. code-block:: python

        a = np.array([1, 3, 0], float)

        np.where(a != 0, 1 / a, a)
        # array([ 1. , 0.33333333, 0. ])

    .. code-block:: python

        a = np.array([1, 3, 0], float)

        np.where(a != 0, 1 / a, a)
        # array([ 1. , 0.33333333, 0. ])

        np.where(a > 0, 3, 2)
        # array([3, 3, 2])

        a = np.array([1, -3, 3, 0], float)
        np.logical_and(a > 0, a % 3 == 0)
        # array([False, False, True, False])

Nonzero
^^^^^^^
.. code-block:: python

    a = np.array([[0, 1], [3, 0]], float)
    a.nonzero()
    # (array([0, 1]), array([1, 0]))

IsFinite and IsNaN
^^^^^^^^^^^^^^^^^^
.. code-block:: python

    a = np.array([1, np.NaN, np.Inf], float)
    # array([ 1., NaN, Inf])

    np.isnan(a)
    # array([False, True, False], dtype=bool)

    np.isfinite(a)
    # array([True, False, False], dtype=bool)


Assignments
===========
