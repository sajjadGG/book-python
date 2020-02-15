************
Series Alter
************


Drop
====
* Drop element at index
* Works with ``inplace=True``

.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series([1.0, 2.0, 3.0, np.nan, 5.0])

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


Drop duplicates
===============
* Works with ``inplace=True``

.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series([1.0, 2.0, 2.0, np.nan, 5.0])

    s.drop_duplicates()
    # 0    1.0
    # 1    2.0
    # 3    NaN
    # 4    5.0
    # dtype: float64


Drop NaN
========
* Works with ``inplace=True``

.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series([1.0, 2.0, 3.0, np.nan, 5.0])

    s.dropna()
    # 0    1.0
    # 1    2.0
    # 2    2.0
    # 4    5.0
    # dtype: float64


Reset Index
===========
* Works with ``inplace=True``
* ``drop=True`` prevents the old index being added as a column

.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series([1.0, 2.0, 3.0, np.nan, 5.0])

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

    s.reset_index(drop=True)
    # 0    3.0
    # 1    NaN
    # 2    5.0
    # dtype: float64


Assignments
===========

Update
------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/series_update.py`

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
