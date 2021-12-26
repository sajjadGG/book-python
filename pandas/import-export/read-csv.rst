Pandas Read CSV
===============


Rationale
---------
* File paths works also with URLs


SetUp
-----
>>> import pandas as pd
>>>


Header
------
>>> DATA = 'https://python.astrotech.io/_static/iris-clean.csv'
>>>
>>> header = pd.read_csv(DATA, nrows=0).columns

Label Encoder:

>>> DATA = 'https://python.astrotech.io/_static/iris-clean.csv'
>>>
>>> header = pd.read_csv(DATA, nrows=0)
>>> class_labels = header.columns[2:]
>>> label_encoder = dict(enumerate(class_labels))


Content
-------
>>> DATA = 'https://python.astrotech.io/_static/iris-clean.csv'
>>>
>>> df = pd.read_csv(DATA)
>>> df.head(3)
   sepal_length  sepal_width  petal_length  petal_width     species
0           5.4          3.9           1.3          0.4      setosa
1           5.9          3.0           5.1          1.8   virginica
2           6.0          3.4           4.5          1.6  versicolor


Rename Columns
--------------
>>> DATA = 'https://python.astrotech.io/_static/iris-dirty.csv'
>>> COLUMNS =  ['sepal_length', 'sepal_width',
>>>             'petal_length', 'petal_width', 'species']
>>>
>>> df = pd.read_csv(DATA)
>>> df.head(3)
     150    4  setosa  versicolor  virginica
0    5.4  3.9     1.3         0.4          0
1    5.9  3.0     5.1         1.8          2
2    6.0  3.4     4.5         1.6          1
>>>
>>> df = pd.read_csv(url, skiprows=1, names=COLUMNS)
>>> df.head(3)
   sepal_length  sepal_width  petal_length  petal_width  species
0           5.4          3.9           1.3          0.4        0
1           5.9          3.0           5.1          1.8        2
2           6.0          3.4           4.5          1.6        1
>>>
>>> df['species'].replace({
>>>     0: 'setosa',
>>>     1: 'versicolor',
>>>     2: 'virginica',
>>> }, inplace=True)
   sepal_length  sepal_width  petal_length  petal_width  species
0           5.4          3.9           1.3          0.4        setosa
1           5.9          3.0           5.1          1.8        virginica
2           6.0          3.4           4.5          1.6        versicolor


Compressed
----------
* If the extension is ``.gz``, ``.bz2``, ``.zip``, and ``.xz``,
  the corresponding compression method is automatically selected

>>> df = pd.read_json('sample_file.zip', compression='zip')  # doctest: +SKIP
>>> df = pd.read_json('sample_file.gz', compression='infer')  # doctest: +SKIP


Use Case
--------
>>> DATA = 'https://python.astrotech.io/_static/iris-dirty.csv'
>>> COLUMNS =  ['sepal_length', 'sepal_width',
>>>             'petal_length', 'petal_width', 'species']
>>>
>>>
>>> header = pd.read_csv(DATA, nrows=0)
>>> class_labels = header.columns[2:]
>>> label_encoder = dict(enumerate(class_labels))
>>>
>>> df = pd.read_csv(DATA, names=COLUMNS, skiprows=1)
>>> df['species'].replace(label_encoder, inplace=True)


Assignments
-----------
.. literalinclude:: assignments/pandas_readcsv_a.py
    :caption: :download:`Solution <assignments/pandas_readcsv_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_readcsv_b.py
    :caption: :download:`Solution <assignments/pandas_readcsv_b.py>`
    :end-before: # Solution
