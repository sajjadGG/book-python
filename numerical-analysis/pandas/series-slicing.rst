************
Series Slice
************


Slicing by index numbers
========================
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

    s[1]
    # -0.2127402802139687

    s[2:]
    # c   -0.895467
    # d    0.386902
    # e   -0.510805
    # dtype: float64

    s[1:-2]
    # b   -0.212740
    # c   -0.895467
    # dtype: float64


Slicing by index names
======================
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

    s['b']
    # -0.2127402802139687

    s['c':]
    # c   -0.895467
    # d    0.386902
    # e   -0.510805
    # dtype: float64

    s['b':'c']
    # b   -0.212740
    # c   -0.895467
    # dtype: float64

.. code-block:: python

    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    values = [1, 3, 5, np.nan, 6, 8]
    s = pd.Series(values, index=indexes)
    # 1970-01-01    1.0
    # 1970-01-02    3.0
    # 1970-01-03    5.0
    # 1970-01-04    NaN
    # 1970-01-05    6.0
    # 1970-01-06    8.0
    # Freq: D, dtype: float64

    s['1970-01-03':'1970-01-05']
    # 1970-01-03    5.0
    # 1970-01-04    NaN
    # 1970-01-05    6.0
    # Freq: D, dtype: float64


Assignments
===========

Slicing
-------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/pandas_series_slicing.py`

:English:
    .. todo:: Translate to English

:Polish:
    #. Stwórz ``pd.Series`` z 26 losowymi liczbami całkowitymi z przedziału ``[10, 100)``
    #. Przekształć kolejne litery alfabetu angielskiego (patrz poniżej) na nazwy kolumn
    #. Nazwij indeksy jak kolejne litery alfabetu angielskiego
    #. Za pomocą biblioteki ``statistics`` znajdź medianę alfabetu
    #. Jak znaleźć medianę dla parzystej długości listy? Użyj dolnego elementu.
    #. Jak znaleźć element w liście o zadanym indeksie?
    #. Wytnij z serii po 3 elementy w górę i w dół od wyszukanego środka
    #. Zsumuj wyniki

:Input:
    .. code-block:: python

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

:Hint:
    * ``import string``, ``string.ascii_lowercase``
    * ``import statistics``, ``statistics.median_low(...)``
    * ``list.index(...)``
