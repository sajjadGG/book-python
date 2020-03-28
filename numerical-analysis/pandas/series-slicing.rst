**************
Series Slicing
**************


Numeric Index
=============
.. code-block:: python

    import pandas as pd

    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])

    s
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # 4    5.0
    # dtype: float64

    s[:2]
    # 0    1.0
    # 1    2.0
    # dtype: float64

    s[2:]
    # 2    3.0
    # 3    4.0
    # 4    5.0
    # dtype: float64

    s[1:-2]
    # 1    2.0
    # 2    3.0
    # dtype: float64

    s[::2]
    # 0    1.0
    # 2    3.0
    # 4    5.0
    # dtype: float64

    s[1::2]
    # 1    2.0
    # 3    4.0
    # dtype: float64


String Index
============
* Using string index upper and lower bound are inclusive!
* String indexes has also numeric index underneath

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

    s['a':'d']
    # a    1.0
    # b    2.0
    # c    3.0
    # d    4.0
    # dtype: float64

    s['a':'d':2]
    # a    1.0
    # c    3.0
    # dtype: float64

    s['a':'d':'b']
    # TypeError: '>=' not supported between instances of 'str' and 'int'

    s['d':'a']
    # Series([], dtype: float64)

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

    s[:2]
    # a    1.0
    # b    2.0
    # dtype: float64

    s[2:]
    # c    3.0
    # d    4.0
    # e    5.0
    # dtype: float64

    s[1:-2]
    # b    2.0
    # c    3.0
    # dtype: float64

    s[::2]
    # a    1.0
    # c    3.0
    # e    5.0
    # dtype: float64

    s[1::2]
    # b    2.0
    # d    4.0
    # dtype: float64

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

    s['a':'b']
    # aaa    1.0
    # dtype: float64

    s['a':'c']
    # aaa    1.0
    # bbb    2.0
    # dtype: float64


Date Index
==========
.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5))

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s['2000-01-02':'2000-01-04']
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s['2000-01-02':'2000-01-04':2]
    # 2000-01-02    4.0
    # Freq: 2D, dtype: float64

    s['2000-01-02':'2000-01-04':-1]
    # Series([], Freq: -1D, dtype: float64)

    s['2000-01-04':'2000-01-02':-1]
    # 2000-01-03    5.0
    # 2000-01-02    4.0
    # Freq: -1D, dtype: float64

    s['1999-12':'1999-12']
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # Freq: D, dtype: float64

    s['2000-01':'2000-01-05']
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0
    # Freq: D, dtype: float64

    s[:'2000-01-05':2]
    # 1999-12-30    1.0
    # 2000-01-01    3.0
    # 2000-01-03    5.0
    # Freq: 2D, dtype: float64

    s[:'2000-01-03':-1]
    # 2000-01-03    5.0
    # Freq: -1D, dtype: float64

.. code-block:: python

    import pandas as pd

    s = pd.Series(
        data = [1.0, 2.0, 3.0, 4.0, 5.0],
        index = pd.date_range('1999-12-30', periods=5))

    s
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # 2000-01-02    4.0
    # 2000-01-03    5.0

    s[1:3]
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # Freq: D, dtype: float64

    s[:3]
    # 1999-12-30    1.0
    # 1999-12-31    2.0
    # 2000-01-01    3.0
    # Freq: D, dtype: float64

    s[:3:2]
    # 1999-12-30    1.0
    # 2000-01-01    3.0
    # Freq: 2D, dtype: float64

    s[::-1]
    # 2000-01-03    5.0
    # 2000-01-02    4.0
    # 2000-01-01    3.0
    # 1999-12-31    2.0
    # 1999-12-30    1.0
    # Freq: -1D, dtype: float64


Assignments
===========

Series Slicing
--------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/series_slicing_dates.py`

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
* Estimated time of completion: 15 min
* Solution: :download:`solution/series_slicing_string.py`

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
