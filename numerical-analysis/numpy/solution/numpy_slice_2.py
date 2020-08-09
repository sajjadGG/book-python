import numpy as np
np.random.seed(0)


data = np.random.randint(0, 10, size=(16, 16))
result = data[6:-6, 6:-6]

print(result)
# [[2 0 7 5]
#  [1 2 9 1]
#  [8 8 8 2]
#  [4 3 6 9]]
