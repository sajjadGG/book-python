import numpy as np

a = np.array([[1, 0], [0, 1]])
b = [[4, 1], [2, 2]]
c = [[1, 0, 1, 0], [0, 1, 1, 0], [3, 2, 1, 0], [4, 1, 2, 0]]
d = np.array([[4, 1], [2, 2], [5, 1], [2, 3]])

b = np.array(b)
c = np.array(c)

a @ b
# array([[4, 1],
#        [2, 2]])

a * b
# array([[4, 0],
#        [0, 2]])

c @ b
# array([[ 9,  2],
#        [ 7,  3],
#        [21,  8],
#        [28,  8]])

c * d
# ValueError: operands could not be broadcast together with shapes (4,4) (4,2)


