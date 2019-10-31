**********
Statistics
**********


Mean
====
* Compute the arithmetic mean along the specified axis.
* The arithmetic mean is the sum of the elements along the axis divided by the number of elements.
* The average is taken over the flattened array by default, otherwise over the specified axis.

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2], [3, 4]])

    np.mean(a)
    # 2.5

    np.mean(a, axis=0)
    # array([2., 3.])

    np.mean(a, axis=1)
    # array([1.5, 3.5])


Average
=======
* Compute the weighted average along the specified axis.

.. code-block:: python

    import numpy as np


    a = np.average([1, 2, 3])

    np.average(a)
    # 2.0

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    np.average(a)
    # 5.0

    np.average(a, axis=0)
    # array([4., 5., 6.])

    np.average(a, axis=1)
    # array([2., 5., 8.])

.. code-block:: python

    import numpy as np


    a = np.average([1, 2, 3])

    np.average(a, weights=[1, 1, 2])
    # 2.25


Median
======
* Compute the median along the specified axis

.. code-block:: python

    import numpy as np


    a = np.array([1, 4, 3, 8, 9, 2, 3], float)

    np.median(a)
    # 3.0


Variance
========
* Compute the variance along the specified axis.
* Variance of the array elements is a measure of the spread of a distribution.
* The variance is the average of the squared deviations from the mean, i.e., ``var = mean(abs(x - x.mean())**2)``
* The variance is computed for the flattened array by default, otherwise over the specified axis.

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2], [3, 4]])

    np.var(a)
    # 1.25

    np.var(a, axis=0)
    # array([1.,  1.])

    np.var(a, axis=1)
    # array([0.25,  0.25])


Standard Deviation
==================
* Compute the standard deviation along the specified axis.
* Standard deviation is a measure of the spread of a distribution, of the array elements.
* The standard deviation is the square root of the average of the squared deviations from the mean, i.e., ``std = sqrt(mean(abs(x - x.mean())**2))``
* The standard deviation is computed for the flattened array by default, otherwise over the specified axis.

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2], [3, 4]])

    np.std(a)
    # 1.1180339887498949    # may vary

    np.std(a, axis=0)
    # array([1.,  1.])

    np.std(a, axis=1)
    # array([0.5,  0.5])


Covariance
==========
* Estimate a covariance matrix, given data and weights
* Covariance indicates the level to which two variables vary together.


.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 1, 3],
                  [5, 3, 1, 8]], float)

    np.cov(a)
    # array([[ 0.91666667, 2.08333333],
    #        [ 2.08333333, 8.91666667]])

    np.cov(a, ddof=0)               # ddof - Delta Degrees of Freedom
    # array([[0.6875, 1.5625],
    #       [1.5625, 6.6875]])


Correlation coefficient
=======================
* measure of the linear correlation between two variables X and Y
* Pearson correlation coefficient (PCC)
* Pearson product-moment correlation coefficient (PPMCC)
* bivariate correlation

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 1, 3],
                  [5, 3, 1, 8]], float)

    np.corrcoef(a)
    # array([[ 1. , 0.72870505],
    #        [ 0.72870505, 1. ]])

.. figure:: img/correlation-coefficient.png
    :scale: 100%
    :align: center

    Examples of scatter diagrams with different values of correlation coefficient (ρ) :cite:`PearsonCorrelationCoefficient`


Assignments
===========
.. todo:: Create assignments
