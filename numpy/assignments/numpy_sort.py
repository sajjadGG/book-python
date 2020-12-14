"""
* Assignment: Numpy Sort
* Filename: numpy_sort.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result_sort` with sorted `DATA` by columns
    3. Define `result_flip` with flipped `DATA` by rows

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result_sort` z posortowanym `DATA` po kolumnach
    3. Zdefiniuj `result_flip` z flipniętym `DATA` po wierszach

Hints:
    * `.sort()` returns `None`

Tests:
    >>> type(result_sort) is np.ndarray
    True
    >>> type(result_flip) is np.ndarray
    True
    >>> result_sort
    array([[44, 47, 64, 67],
           [ 9, 21, 67, 83],
           [36, 70, 87, 88]])
    >>> result_flip
    array([[36, 70, 87, 88],
           [ 9, 21, 67, 83],
           [44, 47, 64, 67]])
"""


# Given
import numpy as np


DATA = np.array([[44, 47, 64, 67],
                 [67,  9, 83, 21],
                 [36, 87, 70, 88]])

result_sort = ...
result_flip = ...


# Solution
DATA.sort(axis=-1)
result_sort = DATA
result_flip = np.flip(DATA, axis=0)
