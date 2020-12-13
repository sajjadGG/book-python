"""
* Assignment: Numpy Slice 1
* Filename: numpy_slice_1.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Print inner 2x2 elements
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wybierz wewnętrzne 2x2 elementy
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result) is np.ndarray
    True
    >>> result
    array([[8, 4],
           [5, 2]])
"""

# Given
import numpy as np


DATA = np.array([
    [2, 8, 1, 5],
    [8, 8, 4, 4],
    [5, 5, 2, 5],
    [1, 0, 6, 0],
])


# Solution
result = DATA[1:3, 1:3]
