"""
* Assignment: Numpy Dtype Astype
* Filename: numpy_astype.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Given `a: np.ndarray` (see below)
    3. Convert to `int` and save result as `a`
    4. Convert to `bool` and save result as `b`
    5. What happened in each of those steps?

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dany `a: np.ndarray` (patrz sekcja input)
    3. Przekonwertuj do typu `int` i wynik zapisz jako `a`
    4. Przekonwertuj do typu `bool` i wynik zapisz jako `b`
    5. Co się stało w każdym z tych kroków?

Tests:
    >>> type(a) is np.ndarray
    True
    >>> type(b) is np.ndarray
    True
    >>> a
    array([[-1,  0,  1],
           [ 2,  3,  4]])
    >>> b
    array([[ True, False,  True],
           [ True,  True,  True]])
"""


# Given
import numpy as np


data = np.array([[-1.1, 0.0, 1.1],
                 [2.2, 3.3, 4.4]])


# Solution
a = data.astype(int)
b = data.astype(bool)

