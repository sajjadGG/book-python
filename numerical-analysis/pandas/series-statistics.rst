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


Extremes
========

Minimum
-------
.. code-block:: python

    s.min()
    # 1.0

.. code-block:: python

    s.idxmin()
    # 'a'

Maximum
-------
.. code-block:: python

    s.max()
    # 5.0

.. code-block:: python

    s.idxmax()
    # 'e'


Average
=======

Mean
----
.. code-block:: python

    s.mean()
    # 2.75

Median
------
.. code-block:: python

    s.median()
    # 2.5

Standard Deviation
------------------
.. code-block:: python

    s.std()
    # 1.707825127659933


Distribution
============

Quantile
--------
* A.K.A. Percentile

.. code-block:: python

    s.quantile(.3)
    # 1.9

    s.quantile([.25, .5, .75])
    # 0.25    1.75
    # 0.50    2.50
    # 0.75    3.50
    # dtype: float64

Variance
--------
.. code-block:: python

    s.var()
    # 2.9166666666666665

Correlation Coefficient
-----------------------
.. code-block:: python

    s.corr(s)
    # 1.0


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


Other methods
=============
.. csv-table:: Descriptive statistics
    :header: "Function", "Description"
    :widths: 10, 90


    "``count``", "Number of non-null observations"
    "``sum``", "Sum of values"
    "``mean``", "Mean of values"
    "``mad``", "Mean absolute deviation"
    "``median``", "Arithmetic median of values"
    "``min``", "Minimum"
    "``max``", "Maximum"
    "``mode``", "Mode"
    "``abs``", "Absolute Value"
    "``prod``", "Product of values"
    "``std``", "Unbiased standard deviation"
    "``var``", "Unbiased variance"
    "``sem``", "Unbiased standard error of the mean"
    "``skew``", "Unbiased skewness (3rd moment)"
    "``kurt``", "Unbiased kurtosis (4th moment)"
    "``quantile``", "Sample quantile (value at %)"
    "``cumsum``", "Cumulative sum"
    "``cumprod``", "Cumulative product"
    "``cummax``", "Cumulative maximum"
    "``cummin``", "Cumulative minimum"


Assignments
===========
.. todo:: Create Assignments
