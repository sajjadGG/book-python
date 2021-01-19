"""
* Assignment: Series Create Even
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Create `result: pd.Series` with 10 even numbers

Polish:
    1. Stwórz `result: pd.Series` z 10 liczbami parzystymi

Tests:
    >>> type(result) is pd.Series
    True
    >>> result
    0     0
    1     2
    2     4
    3     6
    4     8
    5    10
    6    12
    7    14
    8    16
    9    18
    dtype: int64
"""


# Given
import pandas as pd
import numpy as np
np.random.seed(0)


# Solution
data = np.arange(0, 20, 2)
result = pd.Series(data)


# Alternative Solution
# s = pd.Series(range(0, 20, 2))


# Alternative Solution
# s = pd.Series([x for x in range(0, 20) if x % 2 == 0])
