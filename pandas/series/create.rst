Series Create
*************


From Python sequence
====================
* ``list``
* ``tuple``
* ``set``
* ``frozenset``

.. code-block:: python

    import pandas as pd
    import numpy as np


    pd.Series([1, 2, 3, 4])
    # 0    1
    # 1    2
    # 2    3
    # 3    4
    # dtype: int64

    pd.Series([1., 2., 3., 4.])
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # dtype: float64

    pd.Series([1, 2, None, 4])
    # 0    1.0
    # 1    2.0
    # 2    NaN
    # 3    4.0
    # dtype: float64

    pd.Series(['a', 'b', 'c', 'd'])
    # 0    a
    # 1    b
    # 2    c
    # 3    d
    # dtype: object

.. code-block:: python

    import pandas as pd

    list('abcd')
    # ['a', 'b', 'c', 'd']

    pd.Series(list('abcd'))
    # 0    a
    # 1    b
    # 2    c
    # 3    d
    # dtype: object


From Python range
=================
.. code-block:: python

    import pandas as pd

    pd.Series(range(4))
    # 0    0
    # 1    1
    # 2    2
    # 3    3
    # dtype: int64


From Numpy ``ndarray``
======================
.. code-block:: python

    import pandas as pd
    import numpy as np

    pd.Series(np.arange(4.0))
    # 0    0.0
    # 1    1.0
    # 2    2.0
    # 3    3.0
    # dtype: float64


From Date Range
===============
* From ``pd.Timestamp``
* From ``pd.date_range()``
* More information in `Date and Time Types`

.. code-block:: python

    import pandas as pd


    pd.Series(pd.date_range(start='1969-07-16', end='1969-07-24'))
    # 0   1969-07-16
    # 1   1969-07-17
    # 2   1969-07-18
    # 3   1969-07-19
    # 4   1969-07-20
    # 5   1969-07-21
    # 6   1969-07-22
    # 7   1969-07-23
    # 8   1969-07-24
    # dtype: datetime64[ns]


Length
======
.. code-block:: python

    import pandas as pd

    s = pd.Series([1, 2, 3, 4])

    len(s)
    # 9


Assignments
===========
.. literalinclude:: assignments/pandas_series_create_float.py
    :caption: :download:`Solution <assignments/pandas_series_create_float.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_series_create_randint.py
    :caption: :download:`Solution <assignments/pandas_series_create_randint.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_series_create_even.py
    :caption: :download:`Solution <assignments/pandas_series_create_even.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_series_create_dates.py
    :caption: :download:`Solution <assignments/pandas_series_create_dates.py>`
    :end-before: # Solution
