from statistics import median_low
import string
import numpy as np
import pandas as pd
np.random.seed(0)


data =  np.random.randint(10, 100, size=26)
index = list(string.ascii_lowercase)
median = median_low(index)
position = index.index(median)

series = pd.Series(data, index=index)
output = series[position-3:position+4]

print(output.sum())


## Alternative solution
data =  np.random.randint(10, 100, size=26)
index = list('abcdefghijklmnopqrstuvwxyz')
position = int(len(index) / 2)

series = pd.Series(data, index)
output = series[position-3:position+4]

print(output.sum())
