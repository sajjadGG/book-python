import numpy as np
np.random.seed(0)

a = np.random.randint(0, 99, size=12).reshape((3, 4))

a[:, -1].fill(0)
a = a.transpose()
a = a.astype(float)
a[0].fill(np.nan)

print(a)
