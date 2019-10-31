import numpy as np
np.random.seed(0)


a = np.random.randint(0, 10, size=(16, 16))
total = a[6:10, 6:10].sum()

print(total)
