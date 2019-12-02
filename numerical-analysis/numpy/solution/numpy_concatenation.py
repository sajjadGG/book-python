import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

output = np.concatenate((a, b)).reshape(2, 3)
print(output)
# [[1 2 3]
#  [4 5 6]]
