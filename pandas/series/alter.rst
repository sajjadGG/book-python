************
Series Alter
************


Drop Rows
=========
* Drop element at index
* Works with ``inplace=True``

.. code-block:: python

    import pandas as pd

    s = pd.Series([1.0, 2.0, 3.0, None, 5.0])

    s.drop(1)
    # 0    1.0
    # 2    3.0
    # 3    NaN
    # 4    5.0
    # dtype: float64

    s.drop([0,2,4])
    # 1    2.0
    # 3    NaN
    # dtype: float64


Drop Duplicates
===============
* Works with ``inplace=True``

.. code-block:: python

    import pandas as pd

    s = pd.Series([1.0, 2.0, 2.0, None, 5.0])

    s.drop_duplicates()
    # 0    1.0
    # 1    2.0
    # 3    NaN
    # 4    5.0
    # dtype: float64


Reset Index
===========
* Works with ``inplace=True``
* ``drop=True`` prevents the old index being added as a column

.. code-block:: python

    import pandas as pd

    s = pd.Series([1.0, 2.0, 3.0, None, 5.0])

    s.drop([0,1], inplace=True)
    # 2    3.0
    # 3    NaN
    # 4    5.0
    # dtype: float64

    s.reset_index()
    #    index    0
    # 0      2  3.0
    # 1      3  NaN
    # 2      4  5.0

    s.reset_index(drop=True, inplace=True)
    # 0    3.0
    # 1    NaN
    # 2    5.0
    # dtype: float64


Assignments
===========

.. todo:: Convert assignments to literalinclude

Series Alter
------------
* Assignment: Series Alter
* Filename: :download:`assignments/series_alter.py`
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. From input data create ``pd.Series``
    3. Drop values at index 2, 4, 6
    4. Drop duplicates
    5. Reindex series (without old copy)
    6. Print series

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Z danych wejściowych stwórz ``pd.Series``
    3. Usuń wartości na indeksach 2, 4, 6
    4. Usuń duplikujące się wartości
    5. Zresetuj indeks (bez kopii starego)
    6. Wypisz serię

Given:
    .. code-block:: python

        DATA = [1, None, 5, None, 1, 2, 1]

Tests:
    .. code-block:: python

        s: pd.Series
        # 0    1.0
        # 1    NaN
        # 2    2.0
        # dtype: float64
