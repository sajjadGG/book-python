import numpy as np

a = np.array([[1, 0], [0, 1]])
b = [[4, 1], [2, 2]]
c = [[1, 0, 1, 0], [0, 1, 1, 0], [3, 2, 1, 0], [4, 1, 2, 0]]
d = np.array([[4, 1], [2, 2], [5, 1], [2, 3]])

a * b
# array([[4, 0],
#        [0, 2]])

b * a
# array([[4, 0],
#        [0, 2]])

a @ b
# array([[4, 1],
#        [2, 2]])

b @ a
# array([[4, 1],
#        [2, 2]])


c @ d
# array([[ 9,  2],
#        [ 7,  3],
#        [21,  8],
#        [28,  8]])

d @ c
# TypeError: unsupported operand type(s) for @: 'list' and 'list'



b @ c
# TypeError: unsupported operand type(s) for @: 'list' and 'list'

c * d
# ValueError: operands could not be broadcast together with shapes (4,4) (4,2)

d * c
# ValueError: operands could not be broadcast together with shapes (4,2) (4,4)
