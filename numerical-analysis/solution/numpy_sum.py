import numpy as np


A = np.random.randint(10, size=(16, 16)).astype(float)
A.transpose()
print(A)

inner = A[6:10, 6:10]
print(inner)

# total = sum(inner.flatten())
total = inner.sum()
print(total)
