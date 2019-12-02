from statistics import median_low
import string
import numpy as np
import pandas as pd
np.random.seed(0)


values = np.random.randint(10, 100, size=26)
indexes = list(string.ascii_lowercase)
median = median_low(indexes)
position = indexes.index(median)

series = pd.Series(values, index=list(indexes))
output = series[position-3:position+4]

print(output.sum())


## Alternative solution
values = np.random.randint(10, 100, size=26)
indexes = list('abcdefghijklmnopqrstuvwxyz')
position = int(len(indexes) / 2)

series = pd.Series(values, index=indexes)
output = series[position-3:position+4]

print(output.sum())
