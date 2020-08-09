import numpy as np


data = np.random.randint(0, 10, size=(16, 16))

print('Ndim:', data.ndim)
print('Size:', data.size)
print('Dtype:', data.dtype)
print('Itemsize:', data.itemsize)
print('Shape:', data.shape)
print('Strides:', data.strides)
