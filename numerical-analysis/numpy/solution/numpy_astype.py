import numpy as np


a = np.array([[-1.1, 0.0, 1.1],
              [2.2, 3.3, 4.4]])

a = a.astype(int)
a = a.astype(bool)

print(a)
# [[ True False  True]
#  [ True  True  True]]
