*****
Numpy
*****

NumPy jest podstawowym pakiet (dodatkowym) w Pythonie do obliczeń naukowych. Integruje on niskopoziomowe biblioteki takie jak BLAS i LAPACK lub ATLAS. Podstawowe właściwości NumPy to :

    * potężny N-wymiarowy obiekt tablicy danych
    * rozbudowane funkcje
    * narzędzia do integracji z kodem napisanym w C/C++ i Fortranie
    * narzędzia do algebry liniowej, transformaty Fouriera czy generator liczb losowych

NumPy is the fundamental package for scientific computing with Python. It contains among other things:

    * a powerful N-dimensional array object
    * sophisticated (broadcasting) functions
    * tools for integrating C/C++ and Fortran code
    * useful linear algebra, Fourier transform, and random number capabilities

Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

* http://www.numpy.org/

.. code-block:: console

    $ pip install numpy

.. code-block:: python

    import numpy as np

Data Structures:

    * Skalar - jednowymiarowa
    * Wektor - dwuwymiarowa
    * Tensor - trójwymiarowa
    * Tablica - czterowymiarowa
    * Macierz - n-wymiarowa

Performance:
    .. code-block:: python
        :caption: Results with Jupyter and ``%%timeit -n 1_000_000 -r 10``

        import numpy as np


        np.arange(0, 100, step=2, dtype=float)
        # 756 ns ± 10.3 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

        np.array(range(0, 100, 2), dtype=float)
        # 8.28 µs ± 364 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

        np.array([x for x in range(0, 100) if x % 2 == 0], dtype=float)
        # 9.76 µs ± 324 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

        np.array([float(x) for x in range(0, 100) if x % 2 == 0])
        # 12.7 µs ± 195 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

        np.array([float(x) for x in range(0, 100, 2)])
        # 8.35 µs ± 196 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)

        np.array([x for x in range(0, 100, 2)], dtype=float)
        # 5.89 µs ± 77 ns per loop (mean ± std. dev. of 10 runs, 1000000 loops each)


.. todo:: Assignments:

    * http://www.labri.fr/perso/nrougier/teaching/numpy.100/
    * https://github.com/rougier/numpy-100


References
==========
.. bibliography:: _references/bibliography.bib
    :style: plain
    :labelprefix: NP
    :all:
