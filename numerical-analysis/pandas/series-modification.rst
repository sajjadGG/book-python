*******************
Series Modification
*******************


.. code-block:: python

    import pandas as pd

    data =  [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)
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
* Can use with ``inplace=True``

.. code-block:: python

    import pandas as pd

    data =  [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)

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

Ffill
-----
* Can use with ``inplace=True``

.. code-block:: python

    import pandas as pd

    data =  [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)

    s.ffill()
    # 0    1.0
    # 1    1.0
    # 2    5.0
    # 3    5.0
    # 4    1.0
    # 5    2.0
    # 6    1.0
    # 7    inf
    # dtype: float64

Bfill
-----
* Can use with ``inplace=True``

.. code-block:: python

    import pandas as pd

    data =  [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)

    s.bfill()
    # 0    1.0
    # 1    5.0
    # 2    5.0
    # 3    1.0
    # 4    1.0
    # 5    2.0
    # 6    1.0
    # 7    inf
    # dtype: float64

Interpolate
-----------
* ``method: str``, default ``linear``

.. list-table:: Interpolation techniques
    :widths: 25, 75
    :header-rows: 1

    * - Method
      - Description

    * - ``linear``
      - Ignore the index and treat the values as equally spaced. This is the only method supported on MultiIndexes

    * - ``time``
      - Works on daily and higher resolution data to interpolate given length of interval

    * - ``index``, ``values``
      - use the actual numerical values of the index.

    * - ``pad``
      - Fill in NaNs using existing values

    * - ``nearest``, ``zero``, ``slinear``, ``quadratic``, ``cubic``, ``spline``, ``barycentric``, ``polynomial``
      - Passed to ``scipy.interpolate.interp1d``. These methods use the numerical values of the index.  Both ``polynomial`` and ``spline`` require that you also specify an ``order`` (int), e.g. ``df.interpolate(method='polynomial', order=5)``

    * - ``krogh``, ``piecewise_polynomial``, ``spline``, ``pchip``, ``akima``
      - Wrappers around the SciPy interpolation methods of similar names

    * - ``from_derivatives``
      - Refers to ``scipy.interpolate.BPoly.from_derivatives`` which replaces ``piecewise_polynomial`` interpolation method in scipy 0.18.

.. code-block:: python

    import pandas as pd

    data =  [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)

    s.interpolate()
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    3.0
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
* Can use with ``inplace=True``

.. code-block:: python

    import pandas as pd

    data =  [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
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
---------------
* Modifies inplace

.. code-block:: python

    import pandas as pd

    data =  [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)

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

    import pandas as pd

    data =  [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
    s = pd.Series(data)

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

    import pandas as pd

    data =  [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
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

Slicing
-------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
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
