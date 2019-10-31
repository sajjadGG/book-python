*****
Numpy
*****

NumPy jest podstawowym pakiet (dodatkowym) w Pythonie do obliczeń naukowych. Integruje on niskopoziomowe biblioteki takie jak BLAS i LAPACK lub ATLAS. Podstawowe właściwości NumPy to :

    - potężny N-wymiarowy obiekt tablicy danych
    - rozbudowane funkcje
    - narzędzia do integracji z kodem napisanym w C/C++ i Fortranie
    - narzędzia do algebry liniowej, transformaty Fouriera czy generator liczb losowych

NumPy is the fundamental package for scientific computing with Python. It contains among other things:

    - a powerful N-dimensional array object
    - sophisticated (broadcasting) functions
    - tools for integrating C/C++ and Fortran code
    - useful linear algebra, Fourier transform, and random number capabilities

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

.. toctree::
    :maxdepth: 2

    builtin.rst

    array-create.rst
    array-attributes.rst
    array-shape.rst
    array-index.rst
    array-slice.rst
    array-iteration.rst
    array-rounding.rst
    array-methods.rst
    array-arithmetic.rst
    array-concatenation.rst
    array-serialize.rst
    array-statistics.rst
    array-logic.rst
    array-select.rst

    statistics.rst
    random.rst
    trigonometry.rst
    polynomial.rst
    algebra.rst

.. todo:: Assignments:

    * http://www.labri.fr/perso/nrougier/teaching/numpy.100/
    * https://github.com/rougier/numpy-100


Bibliography
============
.. bibliography:: bibliography.bib
    :style: alpha
    :all:
