import pandas as pd
import numpy as np


data = np.random.randint(0, 9, size=100)
data = data[data % 2 == 0][:10]

s = pd.Series(data)
# 0    8
# 1    2
# 2    0
# 3    8
# 4    0
# 5    0
# 6    8
# 7    8
# 8    2
# 9    6
# dtype: int64


## Alternative Solution
from random import randint
data = []

while len(data) < 10:
    n = randint(0, 9)
    if n % 2 == 0:
        data.append(n)

pd.Series(data)
