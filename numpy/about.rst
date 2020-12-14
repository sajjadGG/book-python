*****
Numpy
*****


NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.


Rationale
=========
NumPy is the fundamental package for scientific computing with Python. It contains among other things:

    * a powerful N-dimensional array object
    * sophisticated (broadcasting) functions
    * tools for integrating C/C++ and Fortran code
    * useful linear algebra, Fourier transform, and random number capabilities

Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

* http://www.numpy.org/


Installation
============
.. code-block:: console
    :caption: Installation

    $ pip install numpy

.. code-block:: console
    :caption: Upgrade

    $ pip install --upgrade numpy

.. code-block:: python
    :caption: Check version

    import numpy as np

    np.__version__
    # '1.19.1'


Further Reading
===============
* http://www.labri.fr/perso/nrougier/teaching/numpy.100/
* https://github.com/rougier/numpy-100


References
==========
.. bibliography:: _references/bibliography.bib
    :labelprefix: Numpy
    :cited:
