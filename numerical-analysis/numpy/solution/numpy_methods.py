import numpy as np
np.random.seed(0)


a = np.array([np.random.randint(0, 100) for n in range(0, 12)])
a = a.reshape(3,4)
a.sort(axis=0)
a = a.transpose()

print(a)
# [[36 44 67]
#  [ 9 47 87]
#  [64 70 83]
#  [21 67 88]]
