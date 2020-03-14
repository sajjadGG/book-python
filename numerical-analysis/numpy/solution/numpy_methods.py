import numpy as np
np.random.seed(0)


a = np.random.randint(0, 99, size=(3, 4))

print(a.transpose())
# array([[23, 11, 45],
#        [63, 24, 49],
#        [64, 29, 78],
#        [74, 44, 93]])
