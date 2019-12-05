import numpy as np
np.random.seed(0)


a = np.array([np.random.randint(0, 100) for n in range(0, 21)])
a = a.reshape(7, 3)

a[:, 0] = a[:, 0].clip(50, 80)

print(a)
# [[50 73 89]
#  [79 91 73]
#  [50 81 58]
#  [50 86 63]
#  [50 36 94]
#  [50 63 67]
#  [51  8 56]]
