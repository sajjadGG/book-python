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

    s = pd.Series([1, 2, 3])

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
        data = [1, 2, 3],
        index = [99, 88, 77])

    s
    # 99    1
    # 88    2
    # 77    3
    # dtype: int64

    s.index
    # Int64Index([99, 88, 77], dtype='int64')

    s[0]
    # KeyError: 0


String Index
============
* Also has ``RangeIndex``

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1, 3, 5],
        index = ['a', 'b', 'c'])

    s
    # a    1
    # b    3
    # c    5
    # dtype: int64

    s.index
    # Index(['a', 'b', 'c'], dtype='object')

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

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [11, 22, 33, 44, 55],
        index = ['aaa', 'bbb', 'ccc', 'ddd', 'eee'])

    s
    # aaa    11
    # bbb    22
    # ccc    33
    # ddd    44
    # eee    55
    # dtype: int64


Date Index
==========
* Also has ``RangeIndex``
* Default is "Daily"
* Works also with ISO time format ``1970-01-01T00:00:00``
* ``00:00:00`` is assumed if time is not provided

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [11, 22, 33, 44, 55],
        index = pd.date_range('1999-12-30', periods=5))

    s
    # 1999-12-30    11
    # 1999-12-31    22
    # 2000-01-01    33
    # 2000-01-02    44
    # 2000-01-03    55
    # Freq: D, dtype: int64

.. code-block:: python
    :caption: Every year

    import pandas as pd

    s = pd.Series(
        data = [11, 22, 33, 44, 55],
        index = pd.date_range('1999-12-30', periods=5, freq='Y'))

    s
    # 1999-12-31    11
    # 2000-12-31    22
    # 2001-12-31    33
    # 2002-12-31    44
    # 2003-12-31    55
    # Freq: A-DEC, dtype: int64

.. code-block:: python
    :caption: Every quarter

    import pandas as pd

    s = pd.Series(
        data=[11, 22, 33, 44, 55],
        index=pd.date_range('1999-12-30', periods=5, freq='Q'))

    s
    # 1999-12-31    11
    # 2000-03-31    22
    # 2000-06-30    33
    # 2000-09-30    44
    # 2000-12-31    55
    # Freq: Q-DEC, dtype: int64

.. code-block:: python
    :caption: Every month

    import pandas as pd

    s = pd.Series(
        data = [11, 22, 33, 44, 55],
        index = pd.date_range('1999-12-30', periods=5, freq='M'))

    s
    # 1999-12-31    11
    # 2000-01-31    22
    # 2000-02-29    33
    # 2000-03-31    44
    # 2000-04-30    55
    # Freq: M, dtype: int64

.. code-block:: python
    :caption: Every day

    import pandas as pd

    s = pd.Series(
        data = [11, 22, 33, 44, 55],
        index = pd.date_range('1999-12-30', periods=5, freq='D'))

    s
    # 1999-12-30    11
    # 1999-12-31    22
    # 2000-01-01    33
    # 2000-01-02    44
    # 2000-01-03    55
    # Freq: D, dtype: int64

.. code-block:: python
    :caption: Every two days

    import pandas as pd

    s = pd.Series(
        data = [11, 22, 33, 44, 55],
        index = pd.date_range('1999-12-30', periods=5, freq='2D'))

    s
    # 1999-12-30    11
    # 2000-01-01    22
    # 2000-01-03    33
    # 2000-01-05    44
    # 2000-01-07    55
    # Freq: 2D, dtype: int64

.. code-block:: python
    :caption: Every hour

    import pandas as pd

    s = pd.Series(
        data = [11, 22, 33, 44, 55],
        index = pd.date_range('1999-12-30', periods=5, freq='H'))

    s
    # 1999-12-30 00:00:00    11
    # 1999-12-30 01:00:00    22
    # 1999-12-30 02:00:00    33
    # 1999-12-30 03:00:00    44
    # 1999-12-30 04:00:00    55
    # Freq: H, dtype: int64

.. code-block:: python
    :caption: Every minute

    import pandas as pd

    s = pd.Series(
        data = [11, 22, 33, 44, 55],
        index = pd.date_range('1999-12-30', periods=5, freq='T'))

    s
    # 1999-12-30 00:00:00    11
    # 1999-12-30 00:01:00    22
    # 1999-12-30 00:02:00    33
    # 1999-12-30 00:03:00    44
    # 1999-12-30 00:04:00    55
    # Freq: T, dtype: int64

.. code-block:: python
    :caption: Every second

    import pandas as pd

    s = pd.Series(
        data = [11, 22, 33, 44, 55],
        index = pd.date_range('1999-12-30', periods=5, freq='S'))

    s
    # 1999-12-30 00:00:00    11
    # 1999-12-30 00:00:01    22
    # 1999-12-30 00:00:02    33
    # 1999-12-30 00:00:03    44
    # 1999-12-30 00:00:04    55
    # Freq: S, dtype: int64

.. code-block:: python
    :caption: Every business day. More in :ref:`Date and Time Frequency` and :ref:`Date and Time Calendar`

    import pandas as pd

    s = pd.Series(
        data=[11, 22, 33, 44, 55],
        index=pd.date_range('1999-12-30', periods=5, freq='B'))

    s
    # 1999-12-30    11
    # 1999-12-31    22
    # 2000-01-03    33
    # 2000-01-04    44
    # 2000-01-05    55
    # Freq: B, dtype: int64
