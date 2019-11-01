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


    pd.Series([1, 2, np.nan, 4])
    # 0    1.0
    # 1    2.0
    # 2    NaN
    # 3    4.0
    # dtype: float64

.. code-block:: python

    import pandas as pd


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


Assignments
===========

Even Numbers
------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/pandas_series_even_numbers.py`

#. Stwórz ``pd.Series`` z 10 liczbami parzystymi
#. Podnieś wszystkie elementy do kwadratu
#. Dodaj 5 do każdego z elementów
