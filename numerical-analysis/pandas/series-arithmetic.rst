*****************
Series Arithmetic
*****************


.. code-block:: python

    data = np.random.randn(5)
    index = ['a', 'b', 'c', 'd', 'e']

    s = pd.Series(data, index)
    # a   -1.613898
    # b   -0.212740
    # c   -0.895467
    # d    0.386902
    # e   -0.510805
    # dtype: float64


Multiply by scalar
==================
.. code-block:: python

    data = np.random.randn(5)
    index = ['a', 'b', 'c', 'd', 'e']
    s = pd.Series(data, index)

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

    data = np.random.randn(5)
    index = ['a', 'b', 'c', 'd', 'e']
    s = pd.Series(data, index)

    s * s
    # a    2.604666
    # b    0.045258
    # c    0.801860
    # d    0.149694
    # e    0.260922
    # dtype: float64

.. code-block:: python

    data = np.random.randn(5)
    index = ['a', 'b', 'c', 'd', 'e']
    s = pd.Series(data, index)

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

    data = np.random.randn(5)
    index = ['a', 'b', 'c', 'd', 'e']
    s = pd.Series(data, index)

    s.sum()
    # -2.846007328675207

.. code-block:: python

    data = np.random.randn(5)
    index = ['a', 'b', 'c', 'd', 'e']
    s = pd.Series(data, index)

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

    a = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
    b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'x', 'y'])

    a + b
    # a    2.0
    # b    NaN
    # c    NaN
    # d    NaN
    # x    NaN
    # y    NaN
    # dtype: float64

.. code-block:: python
    :caption: ``fill_value``: If data in both corresponding ``Series`` locations is missing the result will be missing

    a = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
    b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'x', 'y'])

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

Arithmetic
----------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/series_arithmetic.py`

:English:
    #. Set random seed to zero
    #. Generate ``data: ndarray`` with 5 random digits [0, 9]
    #. Create ``index: list`` with index names as sequential letters in english alphabet
    #. Create ``s: pd.Series`` from ``data`` and ``index``
    #. Multiply ``s`` by 10
    #. Multiply ``s`` by original ``s`` values (before multiplying by 10)

:Polish:
    #. Ustaw random seed na zero
    #. Wygeneruj ``data: ndarray`` z 5 losowymi cyframi <0, 9>
    #. Stwórz ``index: list`` z indeksami jak kolejne listery alfabetu angielskiego
    #. Stwórz ``s: pd.Series`` z ``data`` oraz ``index``
    #. Pomnóż ``s`` przez 10
    #. Pomnóż ``s`` przez oryginalne wartości ``s`` (przed mnożeniem przez 10)
