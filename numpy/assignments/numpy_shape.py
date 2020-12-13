"""
* Assignment: Numpy Shape
* Filename: numpy_shape.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result_ravel` with result of flattening `DATA` using `.ravel()` method
    3. Define `result_reshape` with result of reshaping `result_ravel` into 3x3

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result_ravel` z wynikiem spłaszczenia ``DATA`` używając metody ``.ravel()``
    3. Zdefiniuj `result_reshape` z wynikiem zmiany kształtu ``result_ravel`` na 3x3

Tests:
    >>> type(result_ravel) is np.ndarray
    True
    >>> type(result_reshape) is np.ndarray
    True
    >>> result_ravel
    array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> result_reshape
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
"""


# Given
import numpy as np


DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])


# Solution
result_ravel = DATA.ravel()
result_reshape = result_ravel.reshape(3, 3)

