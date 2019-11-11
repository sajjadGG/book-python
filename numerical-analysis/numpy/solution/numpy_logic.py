import numpy as np
np.random.seed(0)


a = np.array([np.random.randint(0, 100) for n in range(0, 10)])
# array([36, 34, 48, 93,  3, 98, 42, 77, 21])

b = np.logical_and(a < 50, a % 2 == 0)
# array([ True,  True,  True, False, False, False,  True, False, False])

b.all()
# False

b.any()
# True
