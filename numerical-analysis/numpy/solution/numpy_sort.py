import numpy as np
np.random.seed(0)


a = np.random.randint(0, 99, size=(3, 4))

a.sort(axis=-1)
# array([[23, 63, 64, 74],
#        [11, 24, 29, 44],
#        [45, 49, 78, 93]])
