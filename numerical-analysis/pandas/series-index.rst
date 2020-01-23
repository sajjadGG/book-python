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
    import numpy as np

    data = [1, 3, 5, np.nan, 6, 8]
    s = pd.Series(data)

    s
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    NaN
    # 4    6.0
    # 5    8.0
    # dtype: float64

    s.index
    # RangeIndex(start=0, stop=6, step=1)

.. code-block:: python

    import pandas as pd

    data = ['a', 'b', 'c']
    s = pd.Series(data)

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

    data = [1, 2, 3]
    index = [99, 88, 77]
    s = pd.Series(data, index)

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
    import numpy as np


    data = [1, 3, 5, np.nan, 6, 8]
    index = ['a', 'b', 'c', 'd', 'e', 'f']
    s = pd.Series(data, index)

    s
    # a    1.0
    # b    3.0
    # c    5.0
    # d    NaN
    # e    6.0
    # f    8.0
    # dtype: float64

    s.index
    # Index(['a', 'b', 'c', 'd', 'e', 'f'], dtype='object')

.. code-block:: python

    import pandas as pd
    import numpy as np


    data = np.random.randn(5)
    index = list('abcde')
    s = pd.Series(data, index)

    s
    # a    1.0
    # b    3.0
    # c    5.0
    # d    NaN
    # e    6.0
    # dtype: float64

.. code-block:: python

    import pandas as pd
    import numpy as np


    data = [11, 22, 33, 44, 55]
    index = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
    s = pd.Series(data, index)

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
    import numpy as np

    data = [1, 3, 5, np.nan, 6, 8]
    index = pd.date_range('1970-01-01', periods=data.size)

    s = pd.Series(data, index)
    # 1970-01-01    1.0
    # 1970-01-02    3.0
    # 1970-01-03    5.0
    # 1970-01-04    NaN
    # 1970-01-05    6.0
    # 1970-01-06    8.0
    # Freq: D, dtype: float64

.. code-block:: python
    :caption: Every year

    import pandas as pd
    import numpy as np

    data = [1, 3, 5, np.nan, 6, 8]
    index = pd.date_range('1970-01-01', freq='Y', periods=data.size)
    s = pd.Series(data, index)

    s
    # 1970-12-31    1.0
    # 1971-12-31    3.0
    # 1972-12-31    5.0
    # 1973-12-31    NaN
    # 1974-12-31    6.0
    # 1975-12-31    8.0
    # Freq: A-DEC, dtype: float64

.. code-block:: python
    :caption: Every month

    import pandas as pd
    import numpy as np

    data = [1, 3, 5, np.nan, 6, 8]
    index = pd.date_range('1970-01-01', freq='M', periods=data.size)
    s = pd.Series(data, index)

    s
    # 1970-01-31    1.0
    # 1970-02-28    3.0
    # 1970-03-31    5.0
    # 1970-04-30    NaN
    # 1970-05-31    6.0
    # 1970-06-30    8.0
    # Freq: M, dtype: float64

.. code-block:: python
    :caption: Every day

    import pandas as pd
    import numpy as np

    data = [1, 3, 5, np.nan, 6, 8]
    index = pd.date_range('1970-01-01', freq='D', periods=data.size)
    s = pd.Series(data, index)

    s
    # 1970-01-01    1.0
    # 1970-01-02    3.0
    # 1970-01-03    5.0
    # 1970-01-04    NaN
    # 1970-01-05    6.0
    # 1970-01-06    8.0
    # Freq: D, dtype: float64

.. code-block:: python
    :caption: Every two days

    import pandas as pd
    import numpy as np

    data = [1, 3, 5, np.nan, 6, 8]
    index = pd.date_range('1970-01-01', freq='2D', periods=data.size)
    s = pd.Series(data, index)

    s
    # 1970-01-01    1.0
    # 1970-01-03    3.0
    # 1970-01-05    5.0
    # 1970-01-07    NaN
    # 1970-01-09    6.0
    # 1970-01-11    8.0
    # Freq: 2D, dtype: float64

.. code-block:: python
    :caption: Every hour

    import pandas as pd
    import numpy as np

    data = [1, 3, 5, np.nan, 6, 8]
    index = pd.date_range('1970-01-01', freq='H', periods=data.size)
    s = pd.Series(data, index)

    s
    # 1970-01-01 00:00:00    1.0
    # 1970-01-01 01:00:00    3.0
    # 1970-01-01 02:00:00    5.0
    # 1970-01-01 03:00:00    NaN
    # 1970-01-01 04:00:00    6.0
    # 1970-01-01 05:00:00    8.0
    # Freq: H, dtype: float64

.. code-block:: python
    :caption: Every minute

    import pandas as pd
    import numpy as np

    data = [1, 3, 5, np.nan, 6, 8]
    index = pd.date_range('1970-01-01', freq='T', periods=data.size)
    s = pd.Series(data, index)

    s
    # 1970-01-01 00:00:00    1.0
    # 1970-01-01 00:01:00    3.0
    # 1970-01-01 00:02:00    5.0
    # 1970-01-01 00:03:00    NaN
    # 1970-01-01 00:04:00    6.0
    # 1970-01-01 00:05:00    8.0
    # Freq: T, dtype: float64

.. code-block:: python
    :caption: Every second

    import pandas as pd
    import numpy as np

    data = [1, 3, 5, np.nan, 6, 8]
    index = pd.date_range('1970-01-01', freq='S', periods=data.size)
    s = pd.Series(data, index)

    s
    # 1970-01-01 00:00:00    1.0
    # 1970-01-01 00:00:01    3.0
    # 1970-01-01 00:00:02    5.0
    # 1970-01-01 00:00:03    NaN
    # 1970-01-01 00:00:04    6.0
    # 1970-01-01 00:00:05    8.0
    # Freq: S, dtype: float64
