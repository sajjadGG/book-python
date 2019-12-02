*******************
Series Modification
*******************


.. code-block:: python

    values = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(values)
    # 0    1.0
    # 1    NaN
    # 2    5.0
    # 3    NaN
    # 4    1.0
    # 5    2.0
    # 6    1.0
    # 7    inf
    # dtype: float64

Fill
====

Fill ``NaN`` values
-------------------
* can use with ``inplace=True``

.. code-block:: python

    values = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(values)

    s.fillna(0.0)
    # 0    1.0
    # 1    0.0
    # 2    5.0
    # 3    0.0
    # 4    1.0
    # 5    2.0
    # 6    1.0
    # 7    inf
    # dtype: float64


Drop
====

Drop
----
* Drop element at index

.. code-block:: python

    values = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(values)

    s.drop(1)
    # 0    1.0
    # 2    5.0
    # 3    NaN
    # 4    1.0
    # 5    2.0
    # 6    1.0
    # 7    inf
    # dtype: float64

Drop duplicates
---------------
.. code-block:: python

    values = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(values)

    s.drop_duplicates()
    # 0    1.0
    # 1    NaN
    # 2    5.0
    # 5    2.0
    # 7    inf
    # dtype: float64

Drop rows with ``NaN`` values
-----------------------------
* can use with ``inplace=True``

.. code-block:: python

    values = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(values)

    s.dropna()
    # 0    1.0
    # 2    5.0
    # 4    1.0
    # 5    2.0
    # 6    1.0
    # 7    inf
    # dtype: float64


Index
=====

Reset index
-----------
* ``drop=True`` to avoid the old index being added as a column

.. code-block:: python

    values = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(values)
    s = s.drop_duplicates()
    # 0    1.0
    # 1    NaN
    # 2    5.0
    # 5    2.0
    # 7    inf
    # dtype: float64

    s.reset_index()
    #    index    0
    # 0      0  1.0
    # 1      1  NaN
    # 2      2  5.0
    # 3      5  2.0
    # 4      7  inf

    s.reset_index(drop=True)
    # 0    1.0
    # 1    NaN
    # 2    5.0
    # 3    2.0
    # 4    inf
    # dtype: float64


Assignments
===========

Slicing
-------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/pandas_series_modification.py`

:English:
    #. From input data create ``pd.Series``
    #. Fill empty values with zero
    #. Drop values at index 2, 4, 6
    #. Drop duplicates
    #. Reindex series (without old copy)
    #. Print series

:Polish:
    #. Z danych wejściowych stwórz ``pd.Series``
    #. Wypełnij puste wartości zerami
    #. Usuń wartości na indeksach 2, 4, 6
    #. Usuń duplikujące się wartości
    #. Zresetuj indeks (bez kopii starego)
    #. Wypisz serię

:Input:
    .. code-block:: python

        [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
