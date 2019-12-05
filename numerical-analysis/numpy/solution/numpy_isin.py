import numpy as np
np.random.seed(0)


a = np.random.randint(0, 100, size=50)
b = 2 ** np.arange(7)

# Alternative
b = np.array([np.power(2, x) for x in range(0, 7)])

print(np.isin(a, b))
# [False False  True False False False False False False False False False
#  False False False False False False False False False False False False
#  False False False False False False False  True False False False False
#  False False False False False  True False False False  True False False
#  False False]

print(np.isin(b, a))
# [False False False False False  True  True]

a[ np.isin(a, b) ]
# array([64, 64, 32, 32])

b[ np.isin(b, a) ]
# array([32, 64])
