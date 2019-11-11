import numpy as np


a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

a = a.ravel()
print(a)
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])

a = a.reshape(3, 3)
print(a)
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
