import pandas as pd
import numpy as np


data = np.random.randint(0, 9, size=100)
data = data[data % 2 == 0]
data = data[:10]

s = pd.Series(data)


## Alternative Solution
from random import randint
data = []

while len(data) < 10:
    n = randint(0, 9)
    if n % 2 == 0:
        data.append(n)

pd.Series(data)
