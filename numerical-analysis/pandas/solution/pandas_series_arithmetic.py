import numpy as np
import pandas as pd
np.random.seed(0)


data = [np.random.randint(0, 9) for n in range(0, 5)]
index = list('abcde')

s = pd.Series(data, index)
# a    5
# b    0
# c    3
# d    3
# e    7
# dtype: int64

s * 10
# a    50
# b     0
# c    30
# d    30
# e    70
# dtype: int64

s * 10 * s
# a    250
# b      0
# c     90
# d     90
# e    490
# dtype: int64
