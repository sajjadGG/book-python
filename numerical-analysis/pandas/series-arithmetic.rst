*****************
Series Arithmetic
*****************

.. code-block:: python

    values = np.random.randn(5)
    indexes = ['a', 'b', 'c', 'd', 'e']

    s = pd.Series(values, index=indexes)
    # a   -1.613898
    # b   -0.212740
    # c   -0.895467
    # d    0.386902
    # e   -0.510805
    # dtype: float64

Multiply by scalar
------------------
.. code-block:: python

    s * 5
    # a   -8.069489
    # b   -1.063701
    # c   -4.477333
    # d    1.934512
    # e   -2.554026
    # dtype: float64

Multiply by itself
------------------
.. code-block:: python

    s * s
    # a    2.604666
    # b    0.045258
    # c    0.801860
    # d    0.149694
    # e    0.260922
    # dtype: float64

.. code-block:: python

    s ** 3
    # a   -4.203665
    # b   -0.009628
    # c   -0.718039
    # d    0.057917
    # e   -0.133280
    # dtype: float64

Sum elements
------------
.. code-block:: python

    s.sum()
    # -2.846007328675207

.. code-block:: python

    sum(s)
    # -2.846007328675207

Add values
----------
* Uses inner join
* ``fill_value``: If data in both corresponding ``Series`` locations is missing the result will be missing

.. code-block:: python

    import numpy as np

    a = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
    # a    1.0
    # b    1.0
    # c    1.0
    # d    NaN
    # dtype: float64

    b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'x', 'y'])
    # a    1.0
    # b    NaN
    # x    1.0
    # y    NaN
    # dtype: float64

.. code-block:: python

    a + b
    # a    2.0
    # b    NaN
    # c    NaN
    # d    NaN
    # x    NaN
    # y    NaN
    # dtype: float64

.. code-block:: python

    # ``fill_value``: If data in both corresponding ``Series`` locations is missing the result will be missing

    a.add(b, fill_value=0)
    # a    2.0
    # b    1.0
    # c    1.0
    # d    NaN
    # x    1.0
    # y    NaN
    # dtype: float64


Assignments
===========
.. todo:: Create assignments
