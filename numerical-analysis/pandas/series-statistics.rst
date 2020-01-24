*****************
Series Statistics
*****************


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


Count
=====
.. code-block:: python

    s.count()
    # 4

Sum
===
.. code-block:: python

    s.sum()
    # 11.0

.. code-block:: python

    s.cumsum()
    # a    1.0
    # b    3.0
    # c    6.0
    # d    NaN
    # e    11.0
    # dtype: float64


Product
=======
.. code-block:: python

    s.prod()
    # 30.0

.. code-block:: python

    s.cumprod()
    # a    1.0
    # b    2.0
    # c    6.0
    # d    NaN
    # e    30.0
    # dtype: float64


Minimal
=======
.. code-block:: python

    s.min()
    # 1.0

    s.idxmin()
    # 'a'


Maximal
=======
.. code-block:: python

    s.max()
    # 5.0

    s.idxmax()
    # 'e'


Average
=======
.. code-block:: python

    s.mean()
    # 2.75

.. code-block:: python

    s.median()
    # 2.5


Standard Deviation
==================
.. code-block:: python

    s.std()
    # 1.707825127659933


Variance
========
.. code-block:: python

    s.var()
    # 2.9166666666666665


Correlation Coefficient
=======================
.. code-block:: python

    s.corr(s)
    # 1.0


Quantile
========
* A.K.A. Percentile

.. code-block:: python

    s.quantile(.25)
    # 1.75

    s.quantile(.5)
    # 2.5

    s.quantile(.75)
    # 3.5


Describe
========
.. code-block:: python

    s.describe()
    # count    4.000000
    # mean     2.750000
    # std      1.707825
    # min      1.000000
    # 25%      1.750000
    # 50%      2.500000
    # 75%      3.500000
    # max      5.000000
    # dtype: float64


Assignments
===========
.. todo:: Create Assignments
