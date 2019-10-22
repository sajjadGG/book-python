
Comparison operators and value testing
--------------------------------------
.. code-block:: python

    a = np.array([1, 3, 0], float)
    b = np.array([0, 3, 2], float)

    a > b
    # array([ True, False, False], dtype=bool)

    a == b
    # array([False, True, False], dtype=bool)

    a <= b
    # array([False, True, True], dtype=bool)

    c = a > b
    # array([ True, False, False], dtype=bool)

.. code-block:: python

    a = np.array([1, 3, 0], float)
    a > 2
    # array([False, True, False], dtype=bool)

.. code-block:: python

    c = np.array([ True, False, False], bool)

    any(c)
    # True

    all(c)
    # False

.. code-block:: python

    a = np.array([1, 3, 0], float)

    np.logical_and(a > 0, a < 3)
    # array([ True, False, False], dtype=bool)

.. code-block:: python

    a = np.array([True, False, True], bool)

    np.logical_not(a)
    # array([False, True, False], dtype=bool)

.. code-block:: python

    a = np.array([True, False, True], bool)
    b = np.array([False, True, False], bool)

    np.logical_or(a, b)
    # array([ True, True, False], dtype=bool)

Where
^^^^^
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
