**************
Series Getitem
**************


Numeric Index
=============
.. code-block:: python

    import pandas as pd
    import numpy as np


    s = pd.Series([1.0, 2.0, 3.0, np.nan, 5.0])

    s
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    NaN
    # 4    5.0
    # dtype: float64

    s[0]        # 1.0
    s[3]        # nan
    s[100]      # IndexError: index out of bounds

    s[-1]       # 5.0
    s[-100]     # IndexError: index out of bounds


String Index
============
.. code-block:: python

    import pandas as pd
    import numpy as np


    s = pd.Series(
        data = [1.0, 2.0, 3.0, np.nan, 5.0],
        index = ['a', 'b', 'c', 'd', 'e'])

    s
    # a    1.0
    # b    2.0
    # c    3.0
    # d    NaN
    # e    5.0
    # dtype: float64

    s['a']      # 1.0
    s['d']      # nan
    s['e']      # 5.0
    s['x']      # KeyError: 'x'

    s[0]        # 1.0
    s[3]        # nan
    s[100]      # IndexError: index out of bounds
    s[-1]       # 5.0
    s[-100]     # IndexError: index out of bounds


Date Index
==========
.. code-block:: python

    import pandas as pd
    import numpy as np


    s = pd.Series(
        data = [1.0, 2.0, 3.0, np.nan, 5.0],
        index = pd.date_range('1999-12-30', periods=5))

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # 2000-01-02    NaN
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s[0]        # 1.0
    s[3]        # nan
    s[100]      # IndexError: index out of bounds
    s[-1]       # 5.0
    s[-100]     # IndexError: index out of bounds

    s['a']      # KeyError: 'a'

    s['2000-01-03']
    # 5.0

    s['2000-01']
    # 2000-01-01    3.0
    # 2000-01-02    NaN
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s['1999']
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # Freq: D, dtype: float64


Assignments
===========

Series Getitem
--------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/series_getitem.py`

:English:
    #. Set random seed to zero
    #. Create ``pd.Series`` with 100 random numbers from standard normal distribution
    #. Series Index are following dates since 2000
    #. Print values:

        * at 2000-02-29,
        * first in the series,
        * last 5 elements in the series,
        * first two weeks in the series,
        * last month in the series,
        * three random elements,
        * middle value in the series.

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz ``pd.Series`` z 100 losowymi liczbami z rozkładu normalnego
    #. Indeksem w serii mają być kolejne dni od 2000 roku
    #. Wypisz wartości:

        * dnia 2000-02-29,
        * pierwszy w serii,
        * ostatnie 5 elementów w serii,
        * dwa pierwsze tygodnie w serii,
        * ostatni miesiąc w serii,
        * trzy losowe element,
        * środkowa wartość serii.

:Hint:
    * ``np.random.seed(0)``
    * ``np.random.randn(10)``
