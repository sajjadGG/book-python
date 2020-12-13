"""
* Assignment: Numpy Attributes
* Filename: numpy_attributes.py
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Print:
        a. number of dimensions;
        b. number of elements;
        c. data type;
        d. element size;
        e. shape;
        f. strides.

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wypisz:
        a. liczbę wymiarów,
        b. liczbę elementów,
        c. typ danych,
        d. rozmiar elementu,
        e. kształt,
        f. przeskoki (strides).

Tests:
    >>> type(result) is dict
    True
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'number of dimensions': 2,
     'number of elements': 6,
     'data type': dtype('float64'),
     'element size': 8,
     'shape': (2, 3),
     'strides': (24, 8)}
"""

import numpy as np

a = np.array([[-1.1, 0.0, 1.1],
              [2.2, 3.3, 4.4]])

result = {
    'number of dimensions': ...,
    'number of elements': ...,
    'data type': ...,
    'element size': ...,
    'shape': ...,
    'strides': ...,
}


# Solution
result = {
    'number of dimensions': a.ndim,
    'number of elements': a.size,
    'data type': a.dtype,
    'element size': a.itemsize,
    'shape': a.shape,
    'strides': a.strides,
}
