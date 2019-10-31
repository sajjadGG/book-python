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


    a = np.array([1, 2, 3])

    np.mean(a)
    # 2.0

    np.mean(a, axis=0)
    # array([2., 3.])

    np.mean(a, axis=1)
    # IndexError: tuple index out of range

.. code-block:: python

    import numpy as np


    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.mean(b)
    # 3.5

    np.mean(b, axis=0)
    # array([2.5, 3.5, 4.5])

    np.mean(b, axis=1)
    # array([2., 5.])

.. code-block:: python

    import numpy as np


    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.mean(c)
    # 5.0

    np.mean(c, axis=0)
    # array([4., 5., 6.])

    np.mean(c, axis=1)
    # array([2., 5., 8.])


Average
=======
* Compute the weighted average along the specified axis.

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    np.average(a)
    # 2.0

    np.average(a, axis=0)
    # 2.0

    np.average(a, axis=1)
    # IndexError: tuple index out of range

    np.average(a, weights=[1, 1, 2])
    # 2.25

.. code-block:: python

    import numpy as np


    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.average(b)
    # 3.5

    np.average(b, axis=0)
    # array([2.5, 3.5, 4.5])

    np.average(b, axis=1)
    # array([2., 5.])

    np.average(b, weights=[[1, 1, 2],
                           [2, 1, 1]])
    # 3.5

.. code-block:: python

    import numpy as np


    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.average(c)
    # 5.0

    np.average(c, axis=0)
    # array([4., 5., 6.])

    np.average(c, axis=1)
    # array([2., 5., 8.])

    np.average(c, weights=[[1, 1, 2],
                           [2, 1, 1],
                           [1./4, 1./2, 1./3]])
    # 4.045871559633027


Median
======
* Compute the median along the specified axis

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    np.median(a)
    # 2.0

    np.median(a, axis=0)
    # 2.0

    np.median(a, axis=1)
    # numpy.AxisError: axis 1 is out of bounds for array of dimension 1


.. code-block:: python

    import numpy as np


    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.median(b)
    # 3.5

    np.median(b, axis=0)
    # array([2.5, 3.5, 4.5])

    np.median(b, axis=1)
    # array([2., 5.])

.. code-block:: python

    import numpy as np


    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.median(c)
    # 5.0

    np.median(c, axis=0)
    # array([4., 5., 6.])

    np.median(c, axis=1)
    # array([2., 5., 8.])

.. code-block:: python

    import numpy as np


    a1 = np.array([1, 2, 3, 4])

    np.median(a1)
    # 2.5

Variance
========
* Compute the variance along the specified axis.
* Variance of the array elements is a measure of the spread of a distribution.
* The variance is the average of the squared deviations from the mean, i.e., ``var = mean(abs(x - x.mean())**2)``
* The variance is computed for the flattened array by default, otherwise over the specified axis.

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    np.var(a)
    # 0.6666666666666666

    np.var(a, axis=0)
    # 0.6666666666666666

    np.var(a, axis=1)
    # IndexError: tuple index out of range

.. code-block:: python

    import numpy as np


    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.var(b)
    # 2.9166666666666665

    np.var(b, axis=0)
    # array([2.25, 2.25, 2.25])

    np.var(b, axis=1)
    # array([0.66666667, 0.66666667])

.. code-block:: python

    import numpy as np


    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.var(c)
    # 6.666666666666667

    np.var(c, axis=0)
    # array([6., 6., 6.])

    np.var(c, axis=1)
    # array([0.66666667, 0.66666667, 0.66666667])


Standard Deviation
==================
* Compute the standard deviation along the specified axis.
* Standard deviation is a measure of the spread of a distribution, of the array elements.
* The standard deviation is the square root of the average of the squared deviations from the mean, i.e., ``std = sqrt(mean(abs(x - x.mean())**2))``
* The standard deviation is computed for the flattened array by default, otherwise over the specified axis.

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    np.std(a)
    # 0.816496580927726

    np.std(a, axis=0)
    # 0.816496580927726

    np.std(a, axis=1)
    # IndexError: tuple index out of range

.. code-block:: python

    import numpy as np


    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.std(b)
    # 1.707825127659933

    np.std(b, axis=0)
    # array([1.5, 1.5, 1.5])

    np.std(b, axis=1)
    # array([0.81649658, 0.81649658])

.. code-block:: python

    import numpy as np


    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.std(c)
    # 2.581988897471611

    np.std(c, axis=0)
    # array([2.44948974, 2.44948974, 2.44948974])

    np.std(c, axis=1)
    # array([0.81649658, 0.81649658, 0.81649658])


Covariance
==========
* Estimate a covariance matrix, given data and weights
* Covariance indicates the level to which two variables vary together
* ``ddof`` - Delta Degrees of Freedom

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    np.cov(a)
    # array(1.)

    np.cov(a, ddof=0)
    # array(0.66666667)

    np.cov(a, ddof=1)
    # array(1.)

.. code-block:: python

    import numpy as np


    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.cov(b)
    # array([[1., 1.],
    #        [1., 1.]])

    np.cov(b, ddof=0)
    # array([[0.66666667, 0.66666667],
    #        [0.66666667, 0.66666667]])

    np.cov(b, ddof=1)
    # array([[1., 1.],
    #        [1., 1.]])

.. code-block:: python

    import numpy as np


    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.cov(c)
    # array([[1., 1., 1.],
    #        [1., 1., 1.],
    #        [1., 1., 1.]])

    np.cov(c, ddof=0)
    # array([[0.66666667, 0.66666667, 0.66666667],
    #        [0.66666667, 0.66666667, 0.66666667],
    #        [0.66666667, 0.66666667, 0.66666667]])

    np.cov(c, ddof=1)
    # array([[1., 1., 1.],
    #        [1., 1., 1.],
    #        [1., 1., 1.]])


Correlation coefficient
=======================
* measure of the linear correlation between two variables X and Y
* Pearson correlation coefficient (PCC)
* Pearson product-moment correlation coefficient (PPMCC)
* bivariate correlation

.. figure:: img/correlation-coefficient.png
    :scale: 75%
    :align: center

    Examples of scatter diagrams with different values of correlation coefficient (ρ) :cite:`PearsonCorrelationCoefficient`

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    np.corrcoef(a)
    # 1.0

.. code-block:: python

    import numpy as np


    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.corrcoef(b)
    # array([[1., 1.],
    #        [1., 1.]])

.. code-block:: python

    import numpy as np


    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    np.corrcoef(c)
    # array([[1., 1., 1.],
    #        [1., 1., 1.],
    #        [1., 1., 1.]])

.. code-block:: python

    import numpy as np


    b1 = np.array([[1, 2, 1],
                   [5, 4, 3]])

    np.corrcoef(b1)
    # array([[1., 0.],
    #        [0., 1.]])

.. code-block:: python

    import numpy as np


    b2 = np.array([[3, 1, 3],
                   [5, 5, 3]])

    np.corrcoef(b2)
    # array([[ 1. , -0.5],
    #        [-0.5,  1. ]])

.. code-block:: python

    import numpy as np


    b3 = np.array([[5, 2, 1],
                   [2, 4, 5]])

    np.corrcoef(b3)
    # array([[ 1.        , -0.99587059],
    #        [-0.99587059,  1.        ]])


Assignments
===========
.. todo:: Create assignments
