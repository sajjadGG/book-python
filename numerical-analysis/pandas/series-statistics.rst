*****************
Series Statistics
*****************


.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series(
        data = [1.0, 2.0, 3.0, np.nan],
        index = ['a', 'b', 'c', 'd'])

    s
    # a    1.0
    # b    2.0
    # c    3.0
    # d    NaN
    # dtype: float64


Count
=====
.. code-block:: python

    s.count()
    # 3

Sum
===
.. code-block:: python

    s.sum()
    # 6.0

.. code-block:: python

    s.cumsum()
    # a    1.0
    # b    3.0
    # c    6.0
    # d    NaN
    # dtype: float64


Product
=======
.. code-block:: python

    s.prod()
    # 6.0

.. code-block:: python

    s.cumprod()
    # a    1.0
    # b    2.0
    # c    6.0
    # d    NaN
    # dtype: float64


Minimal
=======
.. code-block:: python

    a.min()
    # 1.0

    a.idxmin()
    # 'a'


Maximal
=======
.. code-block:: python

    a.max()
    # 3.0

    a.idxmax()
    # 'c'


Mean
====
.. code-block:: python

    a.mean()
    # 2.0

.. code-block:: python

    a.median()
    # 2.0


Standard Deviation
==================
.. code-block:: python

    a.std()
    # 1.0


Variance
========
.. code-block:: python

    s.var()
    # 1.0


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
    # 1.5

    s.quantile(.5)
    # 2.0

    s.quantile(.75)
    # 2.5


Describe
========
.. code-block:: python

    s.describe()
    # count    3.0
    # mean     2.0
    # std      1.0
    # min      1.0
    # 25%      1.5
    # 50%      2.0
    # 75%      2.5
    # max      3.0
    # dtype: float64

Assignments
===========
.. todo:: Create Assignments
