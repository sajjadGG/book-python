import numpy as np
np.random.seed(0)

data = np.random.randint(0, 99, size=12).reshape((3, 4))

data[:, -1].fill(0)
data = data.transpose()
data = data.astype(float)
data[0].fill(np.nan)

print(data)
