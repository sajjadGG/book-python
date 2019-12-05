import numpy as np
np.random.seed(0)


a = np.random.randint(0, 10, size=(16, 16))

print(a.shape)
print(a.ndim)
print('Size:', a.size)
print('Itemsize:', a.itemsize)
