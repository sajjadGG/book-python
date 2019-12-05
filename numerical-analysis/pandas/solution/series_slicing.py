import numpy as np
import pandas as pd
np.random.seed(0)


data = np.random.randint(10, 100, size=26)
index = list('abcdefghijklmnopqrstuvwxyz')
position = int(len(index) / 2)

series = pd.Series(data, index)
output = series[position-3:position+4]

print(output.sum())
