import numpy as np


# URL = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/numpy/data/iris-dirty.csv'
URL = '/Users/matt/Developer/book-python/numerical-analysis/numpy/data/iris-dirty.csv'

header = np.loadtxt(URL, max_rows=1, delimiter=',', dtype=str)
data = np.loadtxt(URL, skiprows=1, delimiter=',')

species = header[2:]
features = data[:, :-1]
# array([[5.4, 3.9, 1.3, 0.4],
#        [5.9, 3. , 5.1, 1.8],
#        [6. , 3.4, 4.5, 1.6],
#        [7.3, 2.9, 6.3, 1.8],
#        ...
#        [6.8, 3.2, 5.9, 2.3]])


labels = data[:, -1].astype(int)
# array([0, 2, 1, 2, 1, 0, 1, 1, 0, 2, 2, 0, 0, 2, 2, 1, 2, 2, 2, 1, 0, 1,
#        1, 0, 0, 0, 2, 2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2, 1, 1, 1, 2, 2,
#        0, 1, 1, 1, 1, 1, 2, 0, 2, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2, 0, 0,
#        0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 1, 2, 2, 1, 0, 2, 1, 0, 1, 0, 2, 1,
#        0, 2, 0, 2, 1, 0, 2, 1, 1, 0, 0, 1, 2, 2, 2, 1, 0, 1, 1, 1, 2, 2,
#        0, 2, 2, 0, 2, 1, 2, 0, 0, 1, 0, 2, 0, 2, 1, 2, 2, 2, 1, 0, 2, 1,
#        0, 0, 2, 0, 2, 1, 1, 1, 0, 1, 1, 2, 0, 1, 1, 0, 2, 2, 2])
