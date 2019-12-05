*************
Series Create
*************


Creating
========

``int``
-------
* From Python sequence (``list``, ``tuple``, ``set``)
* From Python range
* From Numpy ``ndarray`` - most efficient

.. code-block:: python

    import pandas as pd


    pd.Series([1, 2, 3, 4])
    # 0    1
    # 1    2
    # 2    3
    # 3    4
    # dtype: int64

.. code-block:: python

    import pandas as pd
    import numpy as np


    pd.Series(range(4))
    # 0    0
    # 1    1
    # 2    2
    # 3    3
    # dtype: int64

.. code-block:: python

    import pandas as pd
    import numpy as np


    pd.Series(np.arange(4))
    # 0    0
    # 1    1
    # 2    2
    # 3    3
    # dtype: int64

``float``
---------
* From Python sequence (``list``, ``tuple``, ``set``)
* From Numpy ``ndarray`` - most efficient

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


    pd.Series(np.arange(4.0))
    # 0    0.0
    # 1    1.0
    # 2    2.0
    # 3    3.0
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


    pd.Series([1, 2, np.inf, 4])
    # 0    1.0
    # 1    2.0
    # 2    inf
    # 3    4.0
    # dtype: float64

``str``
-------
* From Python sequence (``list``, ``tuple``, ``set``)
* From Numpy ``ndarray`` - most efficient
* From ``list(str)``

.. code-block:: python

    import pandas as pd


    pd.Series(['a', 'b', 'c', 'd'])
    # 0    a
    # 1    b
    # 2    c
    # 3    d
    # dtype: object

.. code-block:: python

    import pandas as pd


    pd.Series(list('abcd'))
    # 0    a
    # 1    b
    # 2    c
    # 3    d
    # dtype: object

dates
-----
* From ``pd.Timestamp``
* From ``pd.daterange()``

.. code-block:: python

    import pandas as pd


    apollo11 = pd.date_range(start='1969-07-16', end='1969-07-24')

    pd.Series(apollo11)
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


Assignments
===========

Create Int
----------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/series_create_int.py`

:English:
    #. Set random seed to zero
    #. Create ``pd.Series`` with 10 even numbers in range ``[0,9]`` (inclusive)

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz ``pd.Series`` z 10 liczbami parzystymi z zakresu ``<0;9>`` (włącznie)

:Hint:
    * ``np.random.seed(0)``
    * ``np.random.randint(0, 9, size=10)``
    * ``a[a % 2 == 0]``

Create Date
-----------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/series_create_date.py`

:English:
    #. Gagarin flown to space on 1961-04-12
    #. Armstrong set foot on the Moon on 1969-07-21
    #. Create ``pd.Series`` with days between Gagarin's launch and Armstrong's first step
    #. How many days passed?

:Polish:
    #. Gagarin poleciał w kosmos w 1961-04-12
    #. Armstrong postawił stopę na Księżycu w 1969-07-21
    #. Stwórz ``pd.Series`` z dniami pomiędzy startem Gagarina a pierwszym krokiem Armstronga
    #. Jak wiele dni upłynęło?
