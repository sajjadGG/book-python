import numpy as np


INPUT = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

np.array([
    [INPUT[0,2], INPUT[2,2]],
    [INPUT[0,0], INPUT[1,0]],
])
# array([[3, 9],
#        [1, 4]])


output = np.zeros(shape=(2,2), dtype=float)
output[0,0] = INPUT[0,2]
output[0,1] = INPUT[2,2]
output[1,0] = INPUT[0,0]
output[1,1] = INPUT[1,0]
print(output)
# array([[3, 9],
#        [1, 4]])
