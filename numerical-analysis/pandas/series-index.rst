************
Series Index
************


Index Types
===========
* Range Index
* Numeric Index
* String Index
* Date Index


Range Index
===========
* Default

.. code-block:: python

    import pandas as pd

    s = pd.Series([1.0, 2.0, 3.0])

    s
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # dtype: float64

    s.index
    # RangeIndex(start=0, stop=3, step=1)

.. code-block:: python

    import pandas as pd

    s = pd.Series(['a', 'b', 'c'])

    s
    # 0    a
    # 1    b
    # 2    c
    # dtype: object

    s.index
    # RangeIndex(start=0, stop=3, step=1)


Numeric Index
=============
.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0],
        index = [99, 88, 77])

    s
    # 99    1.0
    # 88    2.0
    # 77    3.0
    # dtype: float64

    s.index
    # Int64Index([99, 88, 77], dtype='int64')


String Index
============
* Also has ``RangeIndex``

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = ['a', 'b', 'c', 'd', 'e'])

    s
    # a    1.0
    # b    2.0
    # c    3.0
    # d    4.0
    # e    5.0
    # dtype: float64

    s.index
    # Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    s = pd.Series(
        data = np.random.randn(3),
        index = list('abc'))

    s
    # a    1.764052
    # b    0.400157
    # c    0.978738
    # dtype: float64

    s.index
    # Index(['a', 'b', 'c'], dtype='object')

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = ['aaa', 'bbb', 'ccc', 'ddd', 'eee'])

    s
    # aaa    1.0
    # bbb    2.0
    # ccc    3.0
    # ddd    4.0
    # eee    5.0
    # dtype: float64

    s.index
    # Index(['aaa', 'bbb', 'ccc', 'ddd', 'eee'], dtype='object')


Date Index
==========
* Also has ``RangeIndex``
* Default is "Daily"
* Works also with ISO time format ``1970-01-01T00:00:00``
* ``00:00:00`` is assumed if time is not provided

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5))

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-01',
    #                '2000-01-02', '2000-01-03'],
    #               dtype='datetime64[ns]', freq='D')

.. code-block:: python
    :caption: Every year

    import pandas as pd

    s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='Y'))

    s
    # 1999-12-31    1.0
    # 2000-12-31    2.0
    # 2001-12-31    3.0
    # 2002-12-31    4.0
    # 2003-12-31    5.0
    # Freq: A-DEC, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-31', '2000-12-31', '2001-12-31',
    #                '2002-12-31', '2003-12-31'],
    #               dtype='datetime64[ns]', freq='A-DEC')

.. code-block:: python
    :caption: Every quarter

    import pandas as pd

    s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index=pd.date_range('1999-12-30', periods=5, freq='Q'))

    s
    # 1999-12-31    1.0
    # 2000-03-31    2.0
    # 2000-06-30    3.0
    # 2000-09-30    4.0
    # 2000-12-31    5.0
    # Freq: Q-DEC, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-31', '2000-03-31', '2000-06-30',
    #                '2000-09-30', '2000-12-31'],
    #               dtype='datetime64[ns]', freq='Q-DEC')

.. code-block:: python
    :caption: Every month

    import pandas as pd

    s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='M'))

    s
    # 1999-12-31    1.0
    # 2000-01-31    2.0
    # 2000-02-29    3.0
    # 2000-03-31    4.0
    # 2000-04-30    5.0
    # Freq: M, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-31', '2000-01-31', '2000-02-29',
    #                '2000-03-31', '2000-04-30'],
    #               dtype='datetime64[ns]', freq='M')

.. code-block:: python
    :caption: Every day

    import pandas as pd

    s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='D'))

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-01',
    #                '2000-01-02', '2000-01-03'],
    #               dtype='datetime64[ns]', freq='D')

.. code-block:: python
    :caption: Every two days

    import pandas as pd

    s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='2D'))

    s
    # 1999-12-30    1.0
    # 2000-01-01    2.0
    # 2000-01-03    3.0
    # 2000-01-05    4.0
    # 2000-01-07    5.0
    # Freq: 2D, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-30', '2000-01-01', '2000-01-03',
    #                '2000-01-05', '2000-01-07'],
    #               dtype='datetime64[ns]', freq='2D')

.. code-block:: python
    :caption: Every hour

    import pandas as pd

    s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='H'))

    s
    # 1999-12-30 00:00:00    1.0
    # 1999-12-30 01:00:00    2.0
    # 1999-12-30 02:00:00    3.0
    # 1999-12-30 03:00:00    4.0
    # 1999-12-30 04:00:00    5.0
    # Freq: H, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-30 00:00:00', '1999-12-30 01:00:00',
    #                '1999-12-30 02:00:00', '1999-12-30 03:00:00',
    #                '1999-12-30 04:00:00'],
    #               dtype='datetime64[ns]', freq='H')

.. code-block:: python
    :caption: Every minute

    import pandas as pd

    s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='T'))

    s
    # 1999-12-30 00:00:00    1.0
    # 1999-12-30 00:01:00    2.0
    # 1999-12-30 00:02:00    3.0
    # 1999-12-30 00:03:00    4.0
    # 1999-12-30 00:04:00    5.0
    # Freq: T, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-30 00:00:00', '1999-12-30 00:01:00',
    #                '1999-12-30 00:02:00', '1999-12-30 00:03:00',
    #                '1999-12-30 00:04:00'],
    #               dtype='datetime64[ns]', freq='T')

.. code-block:: python
    :caption: Every second

    import pandas as pd

    s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5, freq='S'))

    s
    # 1999-12-30 00:00:00    1.0
    # 1999-12-30 00:00:01    2.0
    # 1999-12-30 00:00:02    3.0
    # 1999-12-30 00:00:03    4.0
    # 1999-12-30 00:00:04    5.0
    # Freq: S, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-30 00:00:00', '1999-12-30 00:00:01',
    #                '1999-12-30 00:00:02', '1999-12-30 00:00:03',
    #                '1999-12-30 00:00:04'],
    #               dtype='datetime64[ns]', freq='S')

.. code-block:: python
    :caption: Every business day. More in :ref:`Date and Time Frequency` and :ref:`Date and Time Calendar`

    import pandas as pd

    s = pd.Series(
        data=[1.0, 2.0, 3.0, 4.0, 5.0],
        index=pd.date_range('1999-12-30', periods=5, freq='B'))

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-03    3.0
    # 2000-01-04    4.0
    # 2000-01-05    5.0
    # Freq: B, dtype: float64

    s.index
    # DatetimeIndex(['1999-12-30', '1999-12-31', '2000-01-03',
    #                '2000-01-04', '2000-01-05'],
    #               dtype='datetime64[ns]', freq='B')
