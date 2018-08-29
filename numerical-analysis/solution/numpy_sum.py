import numpy as np


A = np.random.randint(low=10, high=100, size=(16, 16)).astype(float)
print(A)

B = A.transpose()
print(B)

inner = B[6:10, 6:10]
print(inner)

# total = sum(inner.flatten())
total = inner.sum()
print(total)
