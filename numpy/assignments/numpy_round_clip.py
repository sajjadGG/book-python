"""
* Assignment: Numpy Round Clip
* Complexity: medium
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create `result: np.ndarray` copy of `DATA`
    3. Clip numbers only in first column to 50 (inclusive) to 80 (exclusive)
    4. Print `result`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `result: np.ndarray` z kopią danych z `DATA`
    3. Przytnij liczby w pierwszej kolumnie od 50 (włącznie) do 80 (rozłącznie)
    4. Wypisz `result`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `result[:, 0]`

Tests:
    >>> type(result) is np.ndarray
    True
    >>> result
    array([[50, 47, 64],
           [67, 67,  9],
           [80, 21, 36],
           [80, 70, 88],
           [80, 12, 58],
           [65, 39, 87],
           [50, 88, 81]])
"""


# Given
import numpy as np


DATA = np.array([[44, 47, 64],
                 [67, 67,  9],
                 [83, 21, 36],
                 [87, 70, 88],
                 [88, 12, 58],
                 [65, 39, 87],
                 [46, 88, 81]])

result = ...


# Solution
result = DATA
result[:, 0] = result[:, 0].clip(50, 80)

