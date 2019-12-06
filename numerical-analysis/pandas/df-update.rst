****************
DataFrame Update
****************


Update columns
==============
.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df['D'] = 0
    #      A    B    C  D
    # 0  1.0  1.1    a  0
    # 1  2.0  2.2    b  0
    # 2  NaN  NaN  NaN  0
    # 3  NaN  NaN  NaN  0
    # 4  3.0  3.3    c  0
    # 5  NaN  NaN  NaN  0
    # 6  4.0  4.4    d  0

Update Rows
===========
.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df[1:4] = 0

    df
    #      A    B    C    D
    # 0  1.0  1.1    a  NaN
    # 1  0.0  0.0    0  0.0
    # 2  0.0  0.0    0  0.0
    # 3  0.0  0.0    0  0.0
    # 4  3.0  3.3    c  NaN
    # 5  NaN  NaN  NaN  NaN
    # 6  4.0  4.4    d  NaN

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


Drop NaN - All
==============
* ``axis=0`` - rows
* ``axis=1`` - columns

.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df.dropna(how='all')
    #      A    B  C   D
    # 0  1.0  1.1  a NaN
    # 1  2.0  2.2  b NaN
    # 4  3.0  3.3  c NaN
    # 6  4.0  4.4  d NaN

    df.dropna(how='all', axis=0)
    #      A    B  C   D
    # 0  1.0  1.1  a NaN
    # 1  2.0  2.2  b NaN
    # 4  3.0  3.3  c NaN
    # 6  4.0  4.4  d NaN

    df.dropna(how='all', axis=1)
    #      A    B    C
    # 0  1.0  1.1    a
    # 1  2.0  2.2    b
    # 2  NaN  NaN  NaN
    # 3  NaN  NaN  NaN
    # 4  3.0  3.3    c
    # 5  NaN  NaN  NaN
    # 6  4.0  4.4    d

    df.dropna(how='all', axis='rows')
    #      A    B  C   D
    # 0  1.0  1.1  a NaN
    # 1  2.0  2.2  b NaN
    # 4  3.0  3.3  c NaN
    # 6  4.0  4.4  d NaN

    df.dropna(how='all', axis='columns')
    #      A    B    C
    # 0  1.0  1.1    a
    # 1  2.0  2.2    b
    # 2  NaN  NaN  NaN
    # 3  NaN  NaN  NaN
    # 4  3.0  3.3    c
    # 5  NaN  NaN  NaN
    # 6  4.0  4.4    d

    df.dropna(how='all', axis=-1)
    # ValueError: No axis named -1 for object type <class 'pandas.core.frame.DataFrame'>


Drop NaN - Any
==============
* ``axis=0`` - rows
* ``axis=1`` - columns

.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df.dropna(how='any')
    # Empty DataFrame
    # Columns: [A, B, C, D]
    # Index: []

    df.dropna(how='any', axis=0)
    # Empty DataFrame
    # Columns: [A, B, C, D]
    # Index: []

    df.dropna(how='any', axis=1)
    # Empty DataFrame
    # Columns: []
    # Index: [0, 1, 2, 3, 4, 5, 6]

    df.dropna(how='any', axis='rows')
    # Empty DataFrame
    # Columns: [A, B, C, D]
    # Index: []

    df.dropna(how='any', axis='columns')
    # Empty DataFrame
    # Columns: []
    # Index: [0, 1, 2, 3, 4, 5, 6]

    df.dropna(how='any', axis=-1)
    # ValueError: No axis named -1 for object type <class 'pandas.core.frame.DataFrame'>


Fill NaN - scalar value
=======================
* ``axis=0`` - rows
* ``axis=1`` - columns

.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df.fillna(0.0)
    #      A    B  C    D
    # 0  1.0  1.1  a  0.0
    # 1  2.0  2.2  b  0.0
    # 2  0.0  0.0  0  0.0
    # 3  0.0  0.0  0  0.0
    # 4  3.0  3.3  c  0.0
    # 5  0.0  0.0  0  0.0
    # 6  4.0  4.4  d  0.0


Fill NaN - dict values
======================
* ``axis=0`` - rows
* ``axis=1`` - columns

.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df.fillna({
        'A': 99,
        'B': 88,
        'C': 77
    })
    #       A     B   C   D
    # 0   1.0   1.1   a NaN
    # 1   2.0   2.2   b NaN
    # 2  99.0  88.0  77 NaN
    # 3  99.0  88.0  77 NaN
    # 4   3.0   3.3   c NaN
    # 5  99.0  88.0  77 NaN
    # 6   4.0   4.4   d NaN


Fill NaN - Forward Fill
=======================
* Values from previous row
* ``ffill``: propagate last valid observation forward

.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df.fillna(method='ffill')
    #      A    B  C   D
    # 0  1.0  1.1  a NaN
    # 1  2.0  2.2  b NaN
    # 2  2.0  2.2  b NaN
    # 3  2.0  2.2  b NaN
    # 4  3.0  3.3  c NaN
    # 5  3.0  3.3  c NaN
    # 6  4.0  4.4  d NaN


Fill NaN - Backward Fill
========================
* Values from next row
* ``bfill``: use NEXT valid observation to fill gap

.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df.fillna(method='bfill')
    #      A    B  C   D
    # 0  1.0  1.1  a NaN
    # 1  2.0  2.2  b NaN
    # 2  3.0  3.3  c NaN
    # 3  3.0  3.3  c NaN
    # 4  3.0  3.3  c NaN
    # 5  4.0  4.4  d NaN
    # 6  4.0  4.4  d NaN


Fill NaN - Interpolate
======================
.. code-block:: python

    import pandas as pd
    import numpy as np


    df = pd.DataFrame({
        'A': [1, 2, np.nan, np.nan, 3, np.nan, 4],
        'B': [1.1, 2.2, np.nan, np.nan, 3.3, np.nan, 4.4],
        'C': ['a', 'b', np.nan, np.nan, 'c', np.nan, 'd'],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    })

    df
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 1  2.0  2.2    b NaN
    # 2  NaN  NaN  NaN NaN
    # 3  NaN  NaN  NaN NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN

    df.interpolate()
    #           A         B    C   D
    # 0  1.000000  1.100000    a NaN
    # 1  2.000000  2.200000    b NaN
    # 2  2.333333  2.566667  NaN NaN
    # 3  2.666667  2.933333  NaN NaN
    # 4  3.000000  3.300000    c NaN
    # 5  3.500000  3.850000  NaN NaN
    # 6  4.000000  4.400000    d NaN


Transpose
=========
.. code-block:: python

    import numpy as np
    import pandas as pd
    np.random.seed(0)


    data = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1970-01-01', periods=6)
    df = pd.DataFrame(data, index, columns)

    df
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

    df.T
    #          1970-01-01  1970-01-02  1970-01-03  1970-01-04  1970-01-05  1970-01-06
    # Morning   -0.728881    1.242791   -0.300652    0.973488    0.527855    0.805407
    # Noon       2.452567    0.595302   -0.272770   -2.083819   -0.911698   -0.931830
    # Evening    0.911723    0.176457   -0.471503    0.402725   -0.842518   -0.063189
    # Midnight  -0.849580   -0.560606   -0.852577   -0.331235    1.653468   -0.792088

    df.transpose()
    #          1970-01-01  1970-01-02  1970-01-03  1970-01-04  1970-01-05  1970-01-06
    # Morning   -0.728881    1.242791   -0.300652    0.973488    0.527855    0.805407
    # Noon       2.452567    0.595302   -0.272770   -2.083819   -0.911698   -0.931830
    # Evening    0.911723    0.176457   -0.471503    0.402725   -0.842518   -0.063189
    # Midnight  -0.849580   -0.560606   -0.852577   -0.331235    1.653468   -0.792088


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

