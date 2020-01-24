***************
Series Indexing
***************


Numeric Index
=============
.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series([1.1, 2.2, np.nan, 4.4])

    s
    # 0    1.1
    # 1    2.2
    # 2    NaN
    # 3    4.4
    # dtype: float64

    s[0]        # 1.1
    s[1]        # 2.2
    s[2]        # NaN
    s[3]        # 4.4


String Index
============
.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series(
        data = [1.1, 2.2, np.nan, 4.4],
        index = ['a', 'b', 'c', 'd'])

    s
    # a    1.1
    # b    2.2
    # c    NaN
    # d    4.4
    # dtype: float64

    s['a']      # 1.1
    s['b']      # 2.2
    s['c']      # nan
    s['d']      # 4.4

    s[0]        # 1.1
    s[1]        # 2.2
    s[2]        # nan
    s[3]        # 4.4


Date Index
==========
.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = list('abcde'),
        index = pd.date_range('1999-12-30', periods=5))

    s
    # 1999-12-30    a
    # 1999-12-31    b
    # 2000-01-01    c
    # 2000-01-02    d
    # 2000-01-03    e
    # Freq: D, dtype: object

    s['a']
    # KeyError: 'a'

    s[0]
    # 'a'

    s[1]
    # 'b'

    s[2]
    # 'c'

    s[-1]
    # 'e'

    s['2000-01-03']
    # 'e'

    s['2000-01']
    # 2000-01-01    c
    # 2000-01-02    d
    # 2000-01-03    e
    # Freq: D, dtype: object

    s['1999']
    # 1999-12-30    a
    # 1999-12-31    b
    # Freq: D, dtype: object


Assignments
===========

Indexing Dates
--------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/series_index.py`

:English:
    #. Set random seed to zero
    #. Create ``pd.Series`` with 100 random numbers from standard distribution
    #. Series Index are following dates since 2000
    #. Print values:

        * at 2000-01-05,
        * at 2000-02-29,
        * first in the series,
        * last in the series,
        * middle value in the series.

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz ``pd.Series`` z 100 losowymi liczbami z rozkładu normalnego
    #. Indeksem w serii mają być kolejne dni od 2000 roku
    #. Wypisz wartości:

        * dnia 2000-01-05,
        * dnia 2000-02-29,
        * pierwszy w serii,
        * ostatni w serii,
        * środkowa wartość serii.

:Hint:
    * ``np.random.seed(0)``
    * ``np.random.randn(10)``
