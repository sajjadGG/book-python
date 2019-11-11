import numpy as np
np.random.seed(0)


a = np.array([np.random.randint(0, 100) for n in range(0, 21)])
a = a.reshape(7, 3)

a[:, 0] = a[:, 0].clip(50, 80)

print(a)
# [[50 47 64]
#  [67 67  9]
#  [80 21 36]
#  [80 70 88]
#  [80 12 58]
#  [65 39 87]
#  [50 88 81]]
