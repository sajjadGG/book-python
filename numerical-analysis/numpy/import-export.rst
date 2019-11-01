**********************
Data Import and Export
**********************


np.loadtxt()
============
.. code-block:: python

    import numpy as np


    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/numpy/data/iris.csv'

    a = np.loadtxt(url)
    # ValueError: could not convert string to float: 'sepal_length,sepal_width,petal_length,petal_width,species'

    a = np.loadtxt(url, skiprows=1)
    # ValueError: could not convert string to float: '5.4,3.9,1.3,0.4,setosa'

    a = np.loadtxt(url, skiprows=1, delimiter=',')
    # ValueError: could not convert string to float: 'setosa'

    a = np.loadtxt(url, skiprows=1, delimiter=',', usecols=(0,1,2,3))
    # array([[5.4, 3.9, 1.3, 0.4],
    #        [5.9, 3. , 5.1, 1.8],
    #        [6. , 3.4, 4.5, 1.6],
    #        [7.3, 2.9, 6.3, 1.8],
    #        [5.6, 2.5, 3.9, 1.1],
    #        ...,
    # ])


np.savetxt()
============

``int``
-------
.. code-block:: python

    import numpy as np


    a = np.array([[1,2,3],
                  [4,5,6]])

    np.savetxt('/tmp/filename.csv', a, delimiter=',')
    # 1.000000000000000000e+00,2.000000000000000000e+00,3.000000000000000000e+00
    # 4.000000000000000000e+00,5.000000000000000000e+00,6.000000000000000000e+00

.. code-block:: python

    import numpy as np


    a = np.array([[1,2,3],
                  [4,5,6]])

    np.savetxt('/tmp/filename.csv', a, delimiter=',', fmt='%d')
    # 1,2,3
    # 4,5,6

``float``
---------
.. code-block:: python

    import numpy as np


    a = np.array([[5.4, 3.9, 1.3, 0.4],
                  [5.9, 3. , 5.1, 1.8],
                  [6. , 3.4, 4.5, 1.6],
                  [7.3, 2.9, 6.3, 1.8],
                  [5.6, 2.5, 3.9, 1.1]])

    np.savetxt('/tmp/filename.csv', a, delimiter=',', fmt='%.2f')
    # 5.40,3.90,1.30,0.40
    # 5.90,3.00,5.10,1.80
    # 6.00,3.40,4.50,1.60
    # 7.30,2.90,6.30,1.80
    # 5.60,2.50,3.90,1.10


Other
=====
* ``np.load()``, ``np.loads()`` - ``pickle``
* ``np.fromstring()``
* ``np.fromregex()``
* ``np.genfromtxt()`` - Load data with missing values handled as specified
* ``scipy.io.loadmat()`` - reads MATLAB data files


