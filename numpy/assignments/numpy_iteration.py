"""
* Assignment: Numpy Iteration
* Filename: numpy_iteration.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Use `for` to iterate over `DATA`
    3. Define `result: list[int]` with even numbers from `DATA`

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Używając `for` iteruj po `DATA`
    3. Zdefiniuj `result: list[int]` z liczbami parzystymi z `DATA`

Hints:
    * `number % 2 == 0`

Tests:
    >>> type(result) is list
    True
    >>> result
    [2, 4, 6, 8, 2, 4, 6, 8]
"""


# Given
import numpy as np


DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])


result = []


# Solution
for value in DATA.ravel():
    if value % 2 == 0:
        result.append(value)


## Alternative solution
for row in DATA:
    for value in row:
        if value % 2 == 0:
            result.append(value)


