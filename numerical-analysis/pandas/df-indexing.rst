******************
DataFrame Indexing
******************

Rows
====
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

    df.iloc[0]
    # Morning     1.764052
    # Noon        0.400157
    # Evening     0.978738
    # Midnight    2.240893
    # Name: 1970-01-01 00:00:00, dtype: float64

    df.loc['1970-01-02']
    # Morning     1.867558
    # Noon       -0.977278
    # Evening     0.950088
    # Midnight   -0.151357
    # Name: 1970-01-02 00:00:00, dtype: float64

    df['1970-01-02']
    # KeyError: '1970-01-02'

    df[0]
    # KeyError: 0

    df.loc[0]
    # KeyError: 0

    df.iloc[[1, 3]]
    #               Morning      Noon   Evening   Midnight
    # 1970-01-02  1.867558  -0.977278  0.950088  -0.151357
    # 1970-01-04  0.761038   0.121675  0.443863   0.333674

    df.loc[['1970-01-02', '1970-01-05']]
    # KeyError: "None of [Index(['1970-01-02', '1970-01-05'], dtype='object')] are in the [index]"


Columns
=======

Single Column
-------------
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

    df.Morning
    # 1970-01-01   -0.438232
    # 1970-01-02   -1.798254
    # 1970-01-03   -0.802938
    # 1970-01-04    0.820863
    # 1970-01-05    1.800466
    # 1970-01-06    0.141029
    # Freq: D, Name: Morning, dtype: float64

    df['Morning']
    # 1970-01-01   -0.438232
    # 1970-01-02   -1.798254
    # 1970-01-03   -0.802938
    # 1970-01-04    0.820863
    # 1970-01-05    1.800466
    # 1970-01-06    0.141029
    # Freq: D, Name: Morning, dtype: float64

Multiple columns
----------------
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

    df[['Morning', 'Evening']]
    #               Morning    Evening
    # 1970-01-01  -0.438232  -1.113116
    # 1970-01-02  -1.798254  -0.946041
    # 1970-01-03  -0.802938  -0.258279
    # 1970-01-04   0.820863  -0.901532
    # 1970-01-05   1.800466   0.611194
    # 1970-01-06   0.141029  -0.046938
