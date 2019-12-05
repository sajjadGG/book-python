import numpy as np
np.random.seed(0)


a = np.random.randint(0, 1025, size=(50, 50))

selection = [2**x for x in range(0, 11)]
mask = np.isin(a, selection)

b = sorted(a[mask])
b = np.flip(b)

print(b)
# [1024 1024 1024 1024 1024 1024  512  512  512  512  256  256  256  256
#   256  128  128  128  128  128   64   32   32   32   32   32   16   16
#    16   16   16   16    8    8    4    2    2    2    2    2]
