******************
DataFrame Indexing
******************


.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    df = pd.DataFrame(
        columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
        index = pd.date_range('1999-12-30', periods=7),
        data = np.random.randn(7, 4))

    df
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Rows
====

Range Index
-----------
.. code-block:: python

    df.iloc[0]
    # Morning     1.764052
    # Noon        0.400157
    # Evening     0.978738
    # Midnight    2.240893
    # Name: 1999-12-30 00:00:00, dtype: float64

    df.iloc[[1,3]]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674

    df[0]
    # KeyError: 0

    df.loc[0]
    # KeyError: 0

Date Index
----------
.. code-block:: python

    df.loc['2000-01-05']
    # Morning     2.269755
    # Noon       -1.454366
    # Evening     0.045759
    # Midnight   -0.187184
    # Name: 2000-01-05 00:00:00, dtype: float64

.. code-block:: python

    df['2000-01-05']
    # KeyError: '2000-01-05'

    df[pd.Timestamp('2000-01-05')]
    # KeyError: Timestamp('2000-01-05 00:00:00')

.. code-block:: python

    df.loc[['2000-01-02', '2000-01-05']]
    # KeyError: "None of [Index(['2000-01-02', '2000-01-05'], dtype='object')] are in the [index]"

    df.loc[[pd.Timestamp('2000-01-02'), pd.Timestamp('2000-01-05')]]
    #                  Morning      Noon   Evening  Midnight
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

.. code-block:: python

    date1 = pd.Timestamp('2000-01-02')
    date2 = pd.Timestamp('2000-01-05')

    df.loc[[date1, date2]]
    #                  Morning      Noon   Evening  Midnight
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Columns
=======

Single Column
-------------
.. code-block:: python

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

    df[['Morning', 'Evening']]
    #               Morning    Evening
    # 1970-01-01  -0.438232  -1.113116
    # 1970-01-02  -1.798254  -0.946041
    # 1970-01-03  -0.802938  -0.258279
    # 1970-01-04   0.820863  -0.901532
    # 1970-01-05   1.800466   0.611194
    # 1970-01-06   0.141029  -0.046938

Columns by Index
----------------
.. code-block:: python

    df.iloc[:, 1]
    # 1970-01-01    0.400157
    # 1970-01-02   -0.977278
    # 1970-01-03    0.410599
    # 1970-01-04    0.121675
    # 1970-01-05   -0.205158
    # 1970-01-06    0.653619
    # Freq: D, Name: Noon, dtype: float64

    df.iloc[:, [1,2]]
    #                  Noon   Evening
    # 1970-01-01   0.400157  0.978738
    # 1970-01-02  -0.977278  0.950088
    # 1970-01-03   0.410599  0.144044
    # 1970-01-04   0.121675  0.443863
    # 1970-01-05  -0.205158  0.313068
    # 1970-01-06   0.653619  0.864436
