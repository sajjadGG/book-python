Data Import and Export
======================



SetUp
-----
>>> import numpy as np


np.savetxt()
------------
Save integers:

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.savetxt('myfile.csv', a, delimiter=',')  # doctest: +SKIP
1.000000000000000000e+00,2.000000000000000000e+00,3.000000000000000000e+00
4.000000000000000000e+00,5.000000000000000000e+00,6.000000000000000000e+00
>>>
>>> np.savetxt('myfile.csv', a, delimiter=',', fmt='%d')  # doctest: +SKIP
1,2,3
4,5,6

Save floats:

>>> a = np.array([[5.4, 3.9, 1.3, 0.4],
...               [5.9, 3. , 5.1, 1.8],
...               [6. , 3.4, 4.5, 1.6],
...               [7.3, 2.9, 6.3, 1.8],
...               [5.6, 2.5, 3.9, 1.1]])
>>>
>>> np.savetxt('myfile.csv', a, delimiter=',')  # doctest: +SKIP
5.400000000000000355e+00,3.899999999999999911e+00,1.300000000000000044e+00,4.000000000000000222e-01
5.900000000000000355e+00,3.000000000000000000e+00,5.099999999999999645e+00,1.800000000000000044e+00
6.000000000000000000e+00,3.399999999999999911e+00,4.500000000000000000e+00,1.600000000000000089e+00
7.299999999999999822e+00,2.899999999999999911e+00,6.299999999999999822e+00,1.800000000000000044e+00
5.599999999999999645e+00,2.500000000000000000e+00,3.899999999999999911e+00,1.100000000000000089e+00
>>>
>>> np.savetxt('myfile.csv', a, delimiter=',', fmt='%.1f')  # doctest: +SKIP
5.4,3.9,1.3,0.4
5.9,3.0,5.1,1.8
6.0,3.4,4.5,1.6
7.3,2.9,6.3,1.8
5.6,2.5,3.9,1.1
>>>
>>> np.savetxt('myfile.csv', a, delimiter=',', fmt='%.2f')  # doctest: +SKIP
5.40,3.90,1.30,0.40
5.90,3.00,5.10,1.80
6.00,3.40,4.50,1.60
7.30,2.90,6.30,1.80
5.60,2.50,3.90,1.10


Other
-----
.. csv-table:: NumPy Export methods
    :header: "Method", "Data Type", "Format", "Description"
    :widths: 15, 5, 5, 75

    ``np.savetxt()``, "Text", "``.csv``, ``.txt``, ``.dat``", "Save in text format, such as CSV"
    ``np.save()``, "Binary", ``.npy``, "Save in NumPy native format"
    ``np.savez()``, "Binary",``.npz``, "Save multiple arrays to native format"
    ``np.savez_compressed()``, "Compressed", ``.npz``, "Save multiple arrays to compressed native format"

>>> # doctest: +SKIP
... data = np.loadtxt('myfile.csv', delimiter=',', usecols=1, skiprows=1, dtype=np.float16)
...
... small = (data < 1)
... medium = (data < 1) & (data < 2.0)
... large = (data < 2)
...
... np.save('/tmp/small', data[small])
... np.save('/tmp/medium', data[medium])
... np.save('/tmp/large', data[large])


Assignments
-----------
.. literalinclude:: assignments/numpy_importexport_a.py
    :caption: :download:`Solution <assignments/numpy_importexport_a.py>`
    :end-before: # Solution
