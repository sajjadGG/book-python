************
Series Alter
************


Drop
====
* Drop element at index
* Can use with ``inplace=True``

.. code-block:: python

    import pandas as pd

    data = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)

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
===============
* Modifies inplace

.. code-block:: python

    import pandas as pd

    data = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)

    s.drop_duplicates()
    # 0    1.0
    # 1    NaN
    # 2    5.0
    # 5    2.0
    # 7    inf
    # dtype: float64


Drop NaN
========
* can use with ``inplace=True``

.. code-block:: python

    import pandas as pd

    data = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)

    s.dropna()
    # 0    1.0
    # 2    5.0
    # 4    1.0
    # 5    2.0
    # 6    1.0
    # 7    inf
    # dtype: float64


Reset Index
===========
* ``drop=True`` to avoid the old index being added as a column

.. code-block:: python

    import pandas as pd

    data = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)
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

Update
------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/series_update.py`

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
