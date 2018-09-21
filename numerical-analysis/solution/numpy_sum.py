import numpy as np


A = np.random.randint(low=10, high=100, size=(16, 16)).astype(float)
print('Matrix:')
print(A)

B = A.transpose()
print('Transposed:')
print(B)

inner = B[6:10, 6:10]
print('Inner:')
print(inner)

# total = sum(inner.flatten())
total = inner.sum()
print(f'Sum: {total}')
