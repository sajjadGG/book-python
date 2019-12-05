**********************
DataFrame Modification
**********************

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

Adding column
-------------
.. code-block:: python

    df['Z'] = ['aa', 'bb']
    #       A     B     C   Z
    # 0   1.0   2.0   NaN  aa
    # 1   NaN   2.0   3.0  bb

Drop row if all values are ``NaN``
----------------------------------
* ``axis=0``: rows

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.dropna(how='all')
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

Drop column if all values are ``NaN``
-------------------------------------
* ``axis=1``: columns

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.dropna(how='all', axis=1)
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

Drop row if any value is ``NaN``
--------------------------------
* ``axis=0``: rows

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.dropna(how='any')
    #       A     B     C

Drop column if any value is ``NaN``
-----------------------------------
* ``axis=1``: columns

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.dropna(how='any', axis=1)
    #       B
    # 0   2.0
    # 1   2.0

Fill ``NA``/``NaN`` with specified values
-----------------------------------------
.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.fillna(0.0)
    #       A     B     C
    # 0   1.0   2.0   0.0
    # 1   0.0   2.0   3.0

Fill ``NA``/``NaN`` with values from dict with column names
-----------------------------------------------------------
.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    data = {'A': 5, 'B': 7, 'C': 9}

    df.fillna(data)
    #       A     B     C
    # 0   1.0   2.0   9.0
    # 1   5.0   2.0   3.0

Fill ``NA``/``NaN`` values from previous row
--------------------------------------------
* ``ffill``: propagate last valid observation forward to next valid backfill

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.fillna(method='ffill')
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   1.0   2.0   3.0

Fill ``NA``/``NaN`` values from next row
----------------------------------------
* ``bfill``: use NEXT valid observation to fill gap

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.fillna(method='bfill')
    #       A     B     C
    # 0   1.0   2.0   3.0
    # 1   NaN   2.0   3.0

Transpose
---------
.. code-block:: python

    import numpy as np
    import pandas as pd
    np.random.seed(0)


    data = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(data, index, columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

.. code-block:: python

    df.T
    df.transpose()
    #          1970-01-01  1970-01-02  1970-01-03  1970-01-04  1970-01-05  1970-01-06
    # Morning   -0.728881    1.242791   -0.300652    0.973488    0.527855    0.805407
    # Noon       2.452567    0.595302   -0.272770   -2.083819   -0.911698   -0.931830
    # Evening    0.911723    0.176457   -0.471503    0.402725   -0.842518   -0.063189
    # Midnight  -0.849580   -0.560606   -0.852577   -0.331235    1.653468   -0.792088

Substitute values in columns
----------------------------
.. code-block:: python

    df.loc[df['Species'] == 0, 'Species'] = 'Setosa'
    df.loc[df['Species'] == 1, 'Species'] = 'Versicolor'
    df.loc[df['Species'] == 2, 'Species'] = 'Virginica'

.. code-block:: python

    df['Species'].replace({
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }, inplace=True)


Assignments
===========

Iris Dirty
----------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/pandas_df_dirty.py`


#. Pobierz dane Irysów: :download:`data/iris-dirty.csv`
#. Mając dane Irysów przekonwertuj je na ``DataFrame``
#. Pomiń pierwszą linię z metadanymi
#. Zmień nazwy kolumn na:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

#. Podmień wartości w kolumnie species

    - 0 -> 'setosa',
    - 1 -> 'versicolor',
    - 2 -> 'virginica'

#. Ustaw wszystkie wiersze w losowej kolejności i zresetuj index
#. Wyświetl pierwsze 5 i ostatnie 3 wiersze
#. Wykreśl podstawowe statystyki opisowe

