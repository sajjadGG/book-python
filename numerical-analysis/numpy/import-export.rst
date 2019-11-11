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

    a = np.loadtxt(url, skiprows=1, max_rows=3, delimiter=',', usecols=(0,1,2,3))
    # array([[5.4, 3.9, 1.3, 0.4],
    #        [5.9, 3. , 5.1, 1.8],
    #        [6. , 3.4, 4.5, 1.6]])

    a = np.loadtxt(url, skiprows=1, max_rows=3, delimiter=',', usecols=(0,1,2,3))
    # array([[5.4, 3.9, 1.3, 0.4],
    #        [5.9, 3. , 5.1, 1.8],
    #        [6. , 3.4, 4.5, 1.6]])


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


Assignments
===========

Load Dirty CSV
--------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_loadtext.py`

:English:
    #. Load text from URL given as input (see below)
    #. Read first line with ``dtype=str`` and save as ``header: ndarray``
    #. Read other lines with ``dtype=float`` and save as ``data: ndarray``
    #. From ``header`` slice Iris species names and save result as ``species: ndarray``
    #. In ``data`` split measurements from species number (last column)
    #. Measurements save as ``features: ndarray`` as type ``float``
    #. Species numbers save as ``labels: ndarray`` as type ``int``
    #. Print ``species``, ``labels`` and ``features``

:Polish:
    #. Wczytaj tekst z URL podanego na wejściu (patrz poniżej)
    #. Przeczytaj pierwszą linię jako ``dtype=str`` i zapisz do ``header: ndarray``
    #. Przeczytaj pozostałe linie jako ``dtype=float`` i zapisz jako ``data: ndarray``
    #. Z ``header`` wytnij nazwy gatunków Irysów i zapisz rezultat jako ``species: ndarray``
    #. W ``data`` oddziel pomiary od numerów gatunków (ostatnia kolumna)
    #. Pomiary zapisz do ``features: ndarray`` jako typ ``float``
    #. Gatunki zapisz do ``labels: ndarray`` jako typ ``int``
    #. Wyświetl ``species``, ``labels`` i ``features``

:Input:
    .. code-block:: text

        https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/numpy/data/iris-dirty.csv

:Output:

    species: ndarray
    # array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

:Hint:
    * ``np.loadtext(..., dtype=str)``
    * ``header[2:]``
    * ``ndarray.astype(int)``
    * ``data[:, :-1]``
    * ``data[:, -1]``
