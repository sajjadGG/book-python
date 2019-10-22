Polynomial mathematics
======================

Defining polynomial
-------------------
.. code-block:: text

    Ax^3 + Bx^2 + Cx^1 + D

.. code-block:: python

    np.poly([-1, 1, 1, 10])
    # array([ 1, -11, 9, 11, -10])

Roots of a polynomial
---------------------
.. code-block:: python

    np.roots([1, 4, -2, 3])
    # array([-4.57974010+0.j , 0.28987005+0.75566815j, 0.28987005-0.75566815j])

    np.roots([ 1, -11, 9, 11, -10])
    #array([10.+0.0000000e+00j, -1.+0.0000000e+00j,
    #       1.+9.6357437e-09j, 1.-9.6357437e-09j])

Antiderivative (indefinite integral) of a polynomial
----------------------------------------------------
.. code-block:: python

    np.polyint([1, 1, 1, 1])
    # array([ 0.25 , 0.33333333, 0.5 , 1. , 0. ])

Derivatives
-----------
.. code-block:: python

    np.polyder([1./4., 1./3., 1./2., 1., 0.])
    # array([ 1., 1., 1., 1.])

Evaluate a polynomial at specific values
----------------------------------------
.. code-block:: python

    np.polyval([1, -2, 0, 2], 4)
    # 34

Least squares polynomial fit
----------------------------
.. code-block:: python

    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [0, 2, 1, 3, 7, 10, 11, 19]

    np.polyfit(x, y, 2)
    # array([ 0.375 , -0.88690476, 1.05357143])

Polynomial Arithmetic
---------------------
* ``np.polyadd()``
* ``np.polysub()``
* ``np.polymul()``
* ``np.polydiv()``


Find the sum of two polynomials:
    .. code-block:: python

        np.polyadd([1, 2], [9, 5, 4])
        # array([9, 6, 6])
