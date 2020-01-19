***************
DataFrame Alter
***************


Add
===

Add Column
----------
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

    df['Z'] = np.arange(7.0)
    #      A    B    C   D    Z
    # 0  1.0  1.1    a NaN  0.0
    # 1  2.0  2.2    b NaN  1.0
    # 2  NaN  NaN  NaN NaN  2.0
    # 3  NaN  NaN  NaN NaN  3.0
    # 4  3.0  3.3    c NaN  4.0
    # 5  NaN  NaN  NaN NaN  5.0
    # 6  4.0  4.4    d NaN  6.0

    df['X'] = ['a', 'b', 'c']
    # ValueError: Length of values does not match length of index

    df['X'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    #      A    B    C   D    Z  X
    # 0  1.0  1.1    a NaN  0.0  a
    # 1  2.0  2.2    b NaN  1.0  b
    # 2  NaN  NaN  NaN NaN  2.0  c
    # 3  NaN  NaN  NaN NaN  3.0  d
    # 4  3.0  3.3    c NaN  4.0  e
    # 5  NaN  NaN  NaN NaN  5.0  f
    # 6  4.0  4.4    d NaN  6.0  g

Add Row
-------
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

    df.append({'A':1, 'B':2, 'C':3, 'D':4})
    # TypeError: Can only append a Series if ignore_index=True or if the Series has a name

    df.append({'A':1, 'B':2, 'C':3, 'D':4}, ignore_index=True)
    #      A    B    C    D
    # 0  1.0  1.1    a  NaN
    # 1  2.0  2.2    b  NaN
    # 2  NaN  NaN  NaN  NaN
    # 3  NaN  NaN  NaN  NaN
    # 4  3.0  3.3    c  NaN
    # 5  NaN  NaN  NaN  NaN
    # 6  4.0  4.4    d  NaN
    # 7  1.0  2.0    3  4.0

Drop
====

Drop Columns
------------
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

    df.drop(columns=['A', 'B'])
    #      C    D
    # 0    a  NaN
    # 1    0  0.0
    # 2    0  0.0
    # 3    0  0.0
    # 4    c  NaN
    # 5  NaN  NaN
    # 6    d  NaN

Drop Row
--------
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

    df.drop(1)
    #      A    B    C    D
    # 0  1.0  1.1    a  NaN
    # 2  0.0  0.0    0  0.0
    # 3  0.0  0.0    0  0.0
    # 4  3.0  3.3    c  NaN
    # 5  NaN  NaN  NaN  NaN
    # 6  4.0  4.4    d  NaN

    df.drop([1,2,3])
    #      A    B    C   D
    # 0  1.0  1.1    a NaN
    # 4  3.0  3.3    c NaN
    # 5  NaN  NaN  NaN NaN
    # 6  4.0  4.4    d NaN


Update
======

Update Column
-------------
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
    #      A    B    C    D
    # 0  1.0  1.1    a  NaN
    # 1  2.0  2.2    b  NaN
    # 2  NaN  NaN  NaN  NaN
    # 3  NaN  NaN  NaN  NaN
    # 4  3.0  3.3    c  NaN
    # 5  NaN  NaN  NaN  NaN
    # 6  4.0  4.4    d  NaN

    df['D'] = 99
    df
    #      A    B    C   D
    # 0  1.0  1.1    a  99
    # 1  2.0  2.2    b  99
    # 2  NaN  NaN  NaN  99
    # 3  NaN  NaN  NaN  99
    # 4  3.0  3.3    c  99
    # 5  NaN  NaN  NaN  99
    # 6  4.0  4.4    d  99

Update Rows
-----------
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
    #      A    B    C    D
    # 0  1.0  1.1    a  NaN
    # 1  2.0  2.2    b  NaN
    # 2  NaN  NaN  NaN  NaN
    # 3  NaN  NaN  NaN  NaN
    # 4  3.0  3.3    c  NaN
    # 5  NaN  NaN  NaN  NaN
    # 6  4.0  4.4    d  NaN

    df[1:4] = 99

    df
    #      A     B     C     D
    # 0  1.0    1.1    a   NaN
    # 1  99.0  99.0   99  99.0
    # 2  99.0  99.0   99  99.0
    # 3  99.0  99.0   99  99.0
    # 4  3.0    3.3    c   NaN
    # 5  NaN    NaN  NaN   NaN
    # 6  4.0    4.4    d   NaN

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
.. todo:: Create assignments
