import numpy as np


a = np.random.randint(0, 10, size=(16, 16))

print('Ndim:', a.ndim)
print('Size:', a.size)
print('Dtype:', a.dtype)
print('Itemsize:', a.itemsize)
print('Shape:', a.shape)
print('Strides:', a.strides)
