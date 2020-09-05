import pandas as pd
import numpy as np


data = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
s = pd.Series(data)

s.fillna(0, inplace=True)
s.drop(2, inplace=True)
s.drop(4, inplace=True)
s.drop(6, inplace=True)
s.drop_duplicates(inplace=True)
s.reset_index(drop=True)
# 0    1.0
# 1    0.0
# 2    2.0
# 3    inf
# dtype: float64

# Alternative
# s.drop([2, 4, 6], inplace=True)


## Solution 1
DATA = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]

s = pd.Series(DATA)
s = s.fillna(0)
s = s.drop([2,4,6])
s = s.drop_duplicates()
s.reset_index(drop=True)


## Solution 2
DATA = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]

s = (pd.Series(DATA)
    .fillna(0)
    .drop([2,4,6])
    .drop_duplicates()
    .reset_index(drop=True))
