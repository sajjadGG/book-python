*******************
Series Modification
*******************

.. code-block:: python

    values = [1, 3, 5, np.nan, 6, 8]
    s = pd.Series(values)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    NaN
    # 4    6.0
    # 5    8.0
    # dtype: float64

Fill ``NaN`` values
-------------------
* can use with ``inplace=True``

.. code-block:: python

    s.fillna(0.0)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    0.0
    # 4    6.0
    # 5    8.0
    # dtype: float64

Drop rows with ``NaN`` values
-----------------------------
.. code-block:: python

    s.dropna(inplace=True)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 4    6.0
    # 5    8.0
    # dtype: float64

Reset index
-----------
* ``drop=True`` to avoid the old index being added as a column

.. code-block:: python

    s.reset_index(drop=True)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    6.0
    # 4    8.0
    # dtype: float64
