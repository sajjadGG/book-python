**************
Series Indexes
**************

Numbered
--------
* by default

.. code-block:: python

    values = [1, 3, 5, np.nan, 6, 8]

    pd.Series(values)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    NaN
    # 4    6.0
    # 5    8.0
    # dtype: float64

Alphabetic
----------
.. code-block:: python

    indexes = ['a', 'b', 'c', 'd', 'e', 'f']
    values = [1, 3, 5, np.nan, 6, 8]

    s = pd.Series(values, index=indexes)
    # a    1.0
    # b    3.0
    # c    5.0
    # d    NaN
    # e    6.0
    # f    8.0
    # dtype: float64

.. code-block:: python

    values = np.random.randn(5)

    s = pd.Series(values, index=list('abcdef'))
    # a    1.0
    # b    3.0
    # c    5.0
    # d    NaN
    # e    6.0
    # f    8.0
    # dtype: float64

Datetime
--------
* Default is "Daily"

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

Every year
^^^^^^^^^^
.. code-block:: python

    pd.date_range('1970-01-01', periods=6, freq='Y')
    # DatetimeIndex(['1970-12-31',
    #                '1971-12-31',
    #                '1972-12-31',
    #                '1973-12-31',
    #                '1974-12-31',
    #                '1975-12-31'],
    #                dtype='datetime64[ns]', freq='A-DEC')

Every month
^^^^^^^^^^^
.. code-block:: python

    pd.date_range('1970-01-01', periods=6, freq='Y')
    # DatetimeIndex(['1970-01-31',
    #                '1970-02-28',
    #                '1970-03-31',
    #                '1970-04-30',
    #                '1970-05-31',
    #                '1970-06-30'],
    #                dtype='datetime64[ns]', freq='M')

Every day
^^^^^^^^^
.. code-block:: python

    pd.date_range('1970-01-01', periods=6, freq='D')
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'],
    #                dtype='datetime64[ns]', freq='D')

Every hour
^^^^^^^^^^
* Works also with ISO time format ``1970-01-01T00:00:00``
* If time is not provided, it will start since midnight ``00:00:00``

.. code-block:: python

    pd.date_range('1970-01-01 00:00:00', periods=6, freq='H')
    # DatetimeIndex(['1970-01-01 00:00:00',
    #                '1970-01-01 01:00:00',
    #                '1970-01-01 02:00:00',
    #                '1970-01-01 03:00:00',
    #                '1970-01-01 04:00:00',
    #                '1970-01-01 05:00:00'],
    #                dtype='datetime64[ns]', freq='H')

Every minute
^^^^^^^^^^^^
* Works also with ISO time format ``1970-01-01T00:00:00``
* If time is not provided, it will start since midnight ``00:00:00``

.. code-block:: python

    pd.date_range('1970-01-01 00:00:00', periods=6, freq='T')
    # DatetimeIndex(['1970-01-01 00:00:00',
    #                '1970-01-01 00:01:00',
    #                '1970-01-01 00:02:00',
    #                '1970-01-01 00:03:00',
    #                '1970-01-01 00:04:00',
    #                '1970-01-01 00:05:00'],
    #                dtype='datetime64[ns]', freq='T')

Every second
^^^^^^^^^^^^
* Works also with ISO time format ``1970-01-01T00:00:00``
* If time is not provided, it will start since midnight ``00:00:00``

.. code-block:: python

    pd.date_range('1970-01-01 00:00:00', periods=6, freq='S')
    # DatetimeIndex(['1970-01-01 00:00:00',
    #                '1970-01-01 00:00:01',
    #                '1970-01-01 00:00:02',
    #                '1970-01-01 00:00:03',
    #                '1970-01-01 00:00:05',
    #                '1970-01-01 00:00:06'],
    #                dtype='datetime64[ns]', freq='T')

