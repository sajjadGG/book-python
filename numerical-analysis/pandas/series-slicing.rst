**************
Series Slicing
**************


Numeric Index
=============
.. code-block:: python

    import pandas as pd
    import numpy as np

    data = [11, 22, 33, 44, 55]
    s = pd.Series(data)

    s
    # 0    11
    # 1    22
    # 2    33
    # 3    44
    # 4    55
    # dtype: int64

    s[:2]
    # 0    11
    # 1    22
    # dtype: int64

    s[2:]
    # 2    33
    # 3    44
    # 4    55
    # dtype: int64

    s[1:-2]
    # 1    22
    # 2    33
    # dtype: int64

    s[::2]
    # 0    11
    # 2    33
    # 4    55
    # dtype: int64

    s[1::2]
    # 1    22
    # 3    44
    # dtype: int64


String Index
============
* Using string index upper and lower bound are inclusive!
* String indexes has also numeric index underneath

.. code-block:: python

    import pandas as pd
    import numpy as np

    data = [11, 22, 33, 44, 55]
    index = ['a', 'b', 'c', 'd', 'e']
    s = pd.Series(data, index)

    s
    # a    11
    # b    22
    # c    33
    # d    44
    # e    55
    # dtype: int64

    s['a':'b']
    # a    11
    # b    22
    # dtype: int64

    s['a':'d']
    # a    11
    # b    22
    # c    33
    # d    44
    # dtype: int64

    s['a':'d':2]
    # a    11
    # c    33
    # dtype: int64

    s['a':'d':'b']
    # TypeError: '>=' not supported between instances of 'str' and 'int'

    s['d':'a']
    # Series([], dtype: int64)

.. code-block:: python

    import pandas as pd
    import numpy as np

    data = [11, 22, 33, 44, 55]
    index = ['a', 'b', 'c', 'd', 'e']
    s = pd.Series(data, index)

    s
    # a    11
    # b    22
    # c    33
    # d    44
    # e    55
    # dtype: int64

    s[:2]
    # a    11
    # b    22
    # dtype: int64

    s[2:]
    # c    33
    # d    44
    # e    55
    # dtype: int64

    s[1:-2]
    # b    22
    # c    33
    # dtype: int64

    s[::2]
    # a    11
    # c    33
    # e    55
    # dtype: int64

    s[1::2]
    # b    22
    # d    44
    # dtype: int64

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

    s['a':'b']
    # aaa    11
    # dtype: int64

    s['a':'c']
    # aaa    11
    # bbb    22
    # dtype: int64


Date Index
==========
.. code-block:: python

    import pandas as pd
    import numpy as np

    data = [11, 22, 33, 44, 55]
    index = pd.date_range('1970-01-01', periods=5, freq='D')
    s = pd.Series(data, index)

    s
    # 1970-01-01    11
    # 1970-01-02    22
    # 1970-01-03    33
    # 1970-01-04    44
    # 1970-01-05    55
    # Freq: D, dtype: int64

    s['1970-01-02':'1970-01-04']
    # 1970-01-02    22
    # 1970-01-03    33
    # 1970-01-04    44
    # Freq: D, dtype: int64

    s['1970-01-02':'1970-01-04':2]
    # 1970-01-02    22
    # 1970-01-04    44
    # Freq: 2D, dtype: int64

    s['1970-01-02':'1970-01-04':-1]
    # Series([], Freq: -1D, dtype: int64)

    s['1970-01-04':'1970-01-02':-1]
    # 1970-01-04    44
    # 1970-01-03    33
    # 1970-01-02    22
    # Freq: -1D, dtype: int64

    s['1970-01':'1970-01-04']
    # 1970-01-01    11
    # 1970-01-02    22
    # 1970-01-03    33
    # 1970-01-04    44
    # Freq: D, dtype: int64

    s[:'1970-01-05']
    # 1970-01-01    11
    # 1970-01-02    22
    # 1970-01-03    33
    # 1970-01-04    44
    # 1970-01-05    55
    # Freq: D, dtype: int64

    s[:'1970-01-05':2]
    # 1970-01-01    11
    # 1970-01-03    33
    # 1970-01-05    55
    # Freq: 2D, dtype: int64

    s[:'1970-01-03':-1]
    # 1970-01-05    55
    # 1970-01-04    44
    # 1970-01-03    33
    # Freq: -1D, dtype: int64

.. code-block:: python

    import pandas as pd
    import numpy as np

    data = [11, 22, 33, 44, 55]
    index = pd.date_range('1970-01-01', periods=5, freq='D')
    s = pd.Series(data, index)

    s
    # 1970-01-01    11
    # 1970-01-02    22
    # 1970-01-03    33
    # 1970-01-04    44
    # 1970-01-05    55
    # Freq: D, dtype: int64

    s[1:3]
    # 1970-01-02    22
    # 1970-01-03    33
    # Freq: D, dtype: int64

    s[:3]
    # 1970-01-01    11
    # 1970-01-02    22
    # 1970-01-03    33
    # Freq: D, dtype: int64

    s[:3:2]
    # 1970-01-01    11
    # 1970-01-03    33
    # Freq: 2D, dtype: int64

    s[::-1]
    # 1970-01-05    55
    # 1970-01-04    44
    # 1970-01-03    33
    # 1970-01-02    22
    # 1970-01-01    11
    # Freq: -1D, dtype: int64


Assignments
===========

Slice Dates
-----------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/series_slicing_dates.py`

:English:
    #. Set random seed to zero
    #. Create ``pd.Series`` with 100 random numbers from standard distribution
    #. Series Index are following dates since 2000
    #. Slice dates from 2000-02-14 to end of February 2000
    #. Print results

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz ``pd.Series`` z 100 losowymi liczbami z rozkładu normalnego
    #. Indeksem w serii mają być kolejne dni od 2000 roku
    #. Wytnij daty od 2000-02-14 do końca lutego 2000
    #. Wypisz wyniki

:Hint:
    * ``np.random.seed(0)``
    * ``np.random.randn(10)``

Slicing Alphabet
----------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/series_slicing_string.py`

:English:
    #. Create ``pd.Series`` with 26 random integers in range ``[10, 100)``
    #. Name indexes like letters from english alphabet
    #. Using ``statistics`` library find median of alphabet
    #. How to find median for even number of elements? (Use lower of pair)
    #. How to find index of element on the list?
    #. Slice from series 3 elements up and down from middle
    #. Sum results

:Polish:
    #. Stwórz ``pd.Series`` z 26 losowymi liczbami całkowitymi z przedziału ``<10; 100)``
    #. Nazwij indeksy jak kolejne litery alfabetu angielskiego
    #. Za pomocą biblioteki ``statistics`` znajdź medianę alfabetu
    #. Jak znaleźć medianę dla parzystej długości listy? (Użyj dolnego elementu)
    #. Jak znaleźć element w liście o zadanym indeksie?
    #. Wytnij z serii po 3 elementy w górę i w dół od wyszukanego środka
    #. Zsumuj wyniki

:Input:
    .. code-block:: python

        ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

:Hint:
    * ``np.random.randint(..., ..., size=...)``
    * ``from string import ascii_lowercase``
    * ``from statistics import median_low``
    * ``list.index(...)``
