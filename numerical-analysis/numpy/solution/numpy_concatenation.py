import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b)).reshape(2, 3)
print(result)
# [[1 2 3]
#  [4 5 6]]
