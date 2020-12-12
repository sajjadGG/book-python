**********************
Data Import and Export
**********************


np.loadtxt()
============
.. code-block:: python

    import numpy as np


    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris.csv'

    a = np.loadtxt(url)
    # Traceback (most recent call last):
    # ValueError: could not convert string to float: 'sepal_length,sepal_width,petal_length,petal_width,species'

    a = np.loadtxt(url, skiprows=1)
    # Traceback (most recent call last):
    # ValueError: could not convert string to float: '5.4,3.9,1.3,0.4,setosa'

    a = np.loadtxt(url, skiprows=1, delimiter=',')
    # Traceback (most recent call last):
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

    a = np.loadtxt(url, max_rows=1, delimiter=',', dtype=str, usecols=(0,1,2,3))
    # array(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], dtype='<U12')


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

    np.savetxt('/tmp/filename.csv', a, delimiter=',')
    # 5.400000000000000355e+00,3.899999999999999911e+00,1.300000000000000044e+00,4.000000000000000222e-01
    # 5.900000000000000355e+00,3.000000000000000000e+00,5.099999999999999645e+00,1.800000000000000044e+00
    # 6.000000000000000000e+00,3.399999999999999911e+00,4.500000000000000000e+00,1.600000000000000089e+00
    # 7.299999999999999822e+00,2.899999999999999911e+00,6.299999999999999822e+00,1.800000000000000044e+00
    # 5.599999999999999645e+00,2.500000000000000000e+00,3.899999999999999911e+00,1.100000000000000089e+00

    np.savetxt('/tmp/filename.csv', a, delimiter=',', fmt='%.1f')
    # 5.4,3.9,1.3,0.4
    # 5.9,3.0,5.1,1.8
    # 6.0,3.4,4.5,1.6
    # 7.3,2.9,6.3,1.8
    # 5.6,2.5,3.9,1.1

    np.savetxt('/tmp/filename.csv', a, delimiter=',', fmt='%.2f')
    # 5.40,3.90,1.30,0.40
    # 5.90,3.00,5.10,1.80
    # 6.00,3.40,4.50,1.60
    # 7.30,2.90,6.30,1.80
    # 5.60,2.50,3.90,1.10


Other
=====
.. csv-table:: NumPy Export methods
    :header: "Method", "Data Type", "Format", "Description"
    :widths: 15, 5, 5, 75

    ``np.savetxt()``, "Text", "``.csv``, ``.txt``, ``.dat``", "Save in text format, such as CSV"
    ``np.save()``, "Binary", ``.npy``, "Save in NumPy native format"
    ``np.savez()``, "Binary",``.npz``, "Save multiple arrays to native format"
    ``np.savez_compressed()``, "Compressed", ``.npz``, "Save multiple arrays to compressed native format"

.. csv-table:: NumPy Import methods
    :header: "Method", "Data Type", "Description"
    :widths: 15, 5, 85

    ``np.loadtxt()``, "Text", "Load data from text file such as ``.csv``"
    ``np.load()``, "Binary", "Load data from ``.npy`` file"
    ``np.loads()``, "Binary", "Load binary data from ``pickle`` string"
    ``np.fromstring()``, "Text", "Load data from string"
    ``np.fromregex()``, "Text", "Load data from file using regex to parse"
    ``np.genfromtxt()``, "Text", "Load data with missing values handled as specified"
    ``scipy.io.loadmat()``, "Binary", "reads MATLAB data files"

.. code-block:: python

    import numpy as np

    data = np.loadtxt('_temporary.csv', delimiter=',', usecols=1, skiprows=1, dtype=np.float16)

    small = (data < 1)
    medium = (data < 1) & (data < 2.0)
    large = (data < 2)

    np.save('/tmp/small', data[small])
    np.save('/tmp/medium', data[medium])
    np.save('/tmp/large', data[large])



Assignments
===========

.. todo:: Convert assignments to literalinclude

Numpy Loadtext
--------------
* Assignment: Numpy Loadtext
* Filename: :download:`assignments/numpy_loadtext.py`
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Load text from ``URL``
    3. From the first line select Iris species names and save as str to ``species: np.ndarray``
    4. For other lines:

        a. Read columns with data and save as float to ``features: np.ndarray``
        b. Read last column with species numbers and save as int to ``labels: np.ndarray``

    5. Print ``species``, ``labels`` and ``features``
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj tekst z ``URL``
    3. Z pierwszej linii wybierz nazwy gatunków Irysów i zapisz rezultat jako str do ``species: np.ndarray``
    4. W pozostałych linii:

        a Wczytaj kolumny z danymi i zapisz jako float do ``features: np.ndarray``
        b Wczytaj ostatnią kolumnę z numerami gatunków i zapisz jako int do ``labels: np.ndarray``

    5. Wyświetl ``species``, ``labels`` i ``features``
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        URL = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-dirty.csv'

Tests:
    .. code-block:: python

        species: np.ndarray
        # array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

        features: np.ndarray
        # array([[5.4, 3.9, 1.3, 0.4],
        #        [5.9, 3. , 5.1, 1.8],
        #        [6. , 3.4, 4.5, 1.6],
        #        [7.3, 2.9, 6.3, 1.8],
        #        ...
        #        [6.8, 3.2, 5.9, 2.3]])

        labels: np.ndarray
        # array([0, 2, 1, 2, ..., 0, 2, 2, 2])

