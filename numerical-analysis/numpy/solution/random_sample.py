import numpy as np
np.random.seed(0)


np.random.choice(range(1, 49), size=6, replace=False)

a = np.random.randint(1, 49, size=100)
np.random.choice(np.unique(a), size=6, replace=False)


# Alternative Solution
# a = np.array([], int)
#
# while a.size <= 6:
#     number = np.random.randint(1, 50)
#
#     if number not in a:
#         a = np.append(a, number)
#
# print(a)
