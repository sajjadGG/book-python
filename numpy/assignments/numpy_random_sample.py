"""
* Assignment: Numpy Random Sample
* Filename: numpy_random_sample.py
* Complexity: medium
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Set random seed to zero
    2. Print 6 random integers without repetition in range from 1 to 49

Polish:
    1. Ustaw ziarno losowości na zero
    2. Wyświetl 6 losowych i nie powtarzających się liczb całkowitych z zakresu od 1 do 49.

Tests:
    >>> type(result) is np.ndarray
    True
    >>> result
    array([30,  5, 27, 31, 33, 38])
"""


# Given
import numpy as np
np.random.seed(0)


# Solution
result = np.random.choice(np.arange(1, 50), size=6, replace=False)

# ## Alternative Solution
# result = np.random.choice(np.random.randint(49), size=6, replace=False)
#
# ## Alternative Solution
# a = np.random.randint(1, 49, size=100)
# result = np.random.choice(np.unique(a), size=6, replace=False)
#
# ## Alternative Solution
# result = np.random.choice(range(1, 50), size=6, replace=False)
