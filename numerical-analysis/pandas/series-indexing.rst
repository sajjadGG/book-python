***************
Series Indexing
***************


Numeric Index
=============
.. code-block:: python

    import pandas as pd
    import numpy as np

    data = [1.1, 2.2, np.nan, 4.4]
    s = pd.Series(data)

    s
    # 0    1.1
    # 1    2.2
    # 2    NaN
    # 3    4.4
    # dtype: float64

    s[0]        # 1.1
    s[1]        # 2.2
    s[2]        # nan
    s[3]        # 4.4

String Index
============
.. code-block:: python

    import pandas as pd
    import numpy as np

    data = [1.1, 2.2, np.nan, 4.4]
    index = ['a', 'b', 'c', 'd']
    s = pd.Series(data, index)

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
    import numpy as np

    data = list('abcdef')
    index = pd.date_range('1999-12-28', freq='D', periods=len(data))
    s = pd.Series(data, index)

    s
    # 1999-12-28    a
    # 1999-12-29    b
    # 1999-12-30    c
    # 1999-12-31    d
    # 2000-01-01    e
    # 2000-01-02    f
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
    # 'f'

    s['2000-01-02']
    # 'f'

    s['2000-01']
    # 2000-01-01    e
    # 2000-01-02    f
    # Freq: D, dtype: object

    s['2000']
    # 2000-01-01    e
    # 2000-01-02    f
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
