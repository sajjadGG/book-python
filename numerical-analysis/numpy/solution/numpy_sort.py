import numpy as np
np.random.seed(0)


data = np.random.randint(0, 99, size=(3, 4))

data.sort(axis=-1)
# array([[23, 63, 64, 74],
#        [11, 24, 29, 44],
#        [45, 49, 78, 93]])

np.flip(data, axis=0)
# array([[36, 70, 87, 88],
#        [ 9, 21, 67, 83],
#        [44, 47, 64, 67]])
