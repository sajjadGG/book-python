*************
Series Create
*************


Creating
========
* 1-dimensional data structure similar to ``ndarray``
* Has numerical index

``int``
-------
.. code-block:: python

    import pandas as pd


    pd.Series([1, 2, 3])
    # 0    1
    # 1    2
    # 2    3
    # 3    4
    # dtype: int64

``float``
---------
.. code-block:: python

    import pandas as pd


    pd.Series([1., 2., 3., 4.])
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # dtype: float64

.. code-block:: python

    import pandas as pd
    import numpy as np


    pd.Series([1, 2, np.nan, 4])
    # 0    1.0
    # 1    2.0
    # 2    NaN
    # 3    4.0
    # dtype: float64

.. code-block:: python

    import pandas as pd
    import numpy as np


    pd.Series([1, 2, np.nan, 4])
    # 0    1.0
    # 1    2.0
    # 2    NaN
    # 3    4.0
    # dtype: float64

``str``
-------
.. code-block:: python

    import pandas as pd


    pd.Series(['a', 'b', 'c'])
    # 0    a
    # 1    b
    # 2    c
    # dtype: object

dates
-----
.. code-block:: python

    import pandas as pd


    data = pd.date_range(start='2020-01-01', end='2020-01-06')

    pd.Series(data)
    # 0   2020-01-01
    # 1   2020-01-02
    # 2   2020-01-03
    # 3   2020-01-04
    # 4   2020-01-05
    # 5   2020-01-06
    # dtype: datetime64[ns]


Assignments
===========

Even Numbers
------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/pandas_series_even_numbers.py`

:English:
    #. Set random seed to zero
    #. Generate list of 10 even numbers in range [0,9]
    #. Create ``pd.Series`` from those numbers

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz listę 10 liczb parzystych z zakresu <0;9>
    #. Stwórz ``pd.Series`` z tych liczb

:Hint:
    * ``np.random.seed(0)``
    * ``np.random.randint(0, 9)``
    *
    * ``number % 2 == 0``
