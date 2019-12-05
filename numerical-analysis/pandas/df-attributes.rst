********************
DataFrame Attributes
********************

.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    data = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(data, index, columns)
    #                 Morning        Noon    Evening   Midnight
    # 1970-01-01     2.269755   -1.454366   0.045759  -0.187184
    # 1970-01-02     1.532779    1.469359   0.154947   0.378163
    # 1970-01-03    -0.887786   -1.980796  -0.347912   0.156349
    # 1970-01-04     1.230291    1.202380  -0.387327  -0.302303
    # 1970-01-05    -1.048553   -1.420018  -1.706270   1.950775
    # 1970-01-06    -0.509652   -0.438074  -1.252795   0.777490


Indexes
=======
.. code-block:: python

    df.index
    # DatetimeIndex(['1970-01-01', '1970-01-02', '1970-01-03', '1970-01-04', '1970-01-05', '1970-01-06'],
    #               dtype='datetime64[ns]', freq='D')


Columns
=======
.. code-block:: python

    df.columns
    # Index(['Morning', 'Noon', 'Evening', 'Midnight'], dtype='object')


Assignments
===========
.. todo:: Create assignments
