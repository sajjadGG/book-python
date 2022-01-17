Pandas Read CSV
===============


Rationale
---------
* File paths works also with URLs


SetUp
-----
>>> import pandas as pd


Header
------
>>> DATA = 'https://python.astrotech.io/_static/iris-clean.csv'
>>>
>>> header = pd.read_csv(DATA, nrows=0).columns

Label Encoder:

>>> DATA = 'https://python.astrotech.io/_static/iris-clean.csv'
>>>
>>> header = pd.read_csv(DATA, nrows=0)
>>> nrows, ncols, *class_labels = header.columns
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
>>>
>>> COLUMNS =  ['sepal_length', 'sepal_width',
...             'petal_length', 'petal_width', 'species']
>>>
>>> df = pd.read_csv(DATA)
>>> df.head(3)
   150    4  setosa  versicolor  virginica
0  5.4  3.9     1.3         0.4          0
1  5.9  3.0     5.1         1.8          2
2  6.0  3.4     4.5         1.6          1
>>>
>>> df = pd.read_csv(DATA, skiprows=1, names=COLUMNS)
>>> df.head(3)
   sepal_length  sepal_width  petal_length  petal_width  species
0           5.4          3.9           1.3          0.4        0
1           5.9          3.0           5.1          1.8        2
2           6.0          3.4           4.5          1.6        1
>>>
>>> df['species'].replace({
...     0: 'setosa',
...     1: 'versicolor',
...     2: 'virginica',
... }, inplace=True)
>>>
>>> df.head(n=3)
   sepal_length  sepal_width  petal_length  petal_width     species
0           5.4          3.9           1.3          0.4      setosa
1           5.9          3.0           5.1          1.8   virginica
2           6.0          3.4           4.5          1.6  versicolor


Compressed
----------
* If the extension is ``.gz``, ``.bz2``, ``.zip``, and ``.xz``,
  the corresponding compression method is automatically selected

>>> df = pd.read_csv('sample_file.zip', compression='zip')  # doctest: +SKIP
>>> df = pd.read_csv('sample_file.gz', compression='infer')  # doctest: +SKIP


Use Case - 0x01
---------------
>>> DATA = 'https://python.astrotech.io/_static/iris-dirty.csv'
>>>
>>> COLUMNS =  ['sepal_length', 'sepal_width',
...             'petal_length', 'petal_width', 'species']

>>> header = pd.read_csv(DATA, nrows=0)
>>> nrows, ncols, *class_labels = header.columns
>>> label_encoder = dict(enumerate(class_labels))
>>>
>>> label_encoder
{0: 'setosa', 1: 'versicolor', 2: 'virginica'}

>>> df = pd.read_csv(DATA, names=COLUMNS, skiprows=1)
>>> df['species'].replace(label_encoder, inplace=True)
>>> df.head(n=5)
   sepal_length  sepal_width  petal_length  petal_width     species
0           5.4          3.9           1.3          0.4      setosa
1           5.9          3.0           5.1          1.8   virginica
2           6.0          3.4           4.5          1.6  versicolor
3           7.3          2.9           6.3          1.8   virginica
4           5.6          2.5           3.9          1.1  versicolor


Use Case - 0x02
---------------
>>> DATA = 'https://python.astrotech.io/_static/martian-en.csv'

>>> pd.read_csv(DATA)
   id First Name   Last Name       Mission Date
0   1        Jan  Twardowski     5 January 1988
1   2       Mark      Watney      July 21, 1969
2   3       Ivan   Ivanovich      Apr 12,  1961
3   4    Melissa       Lewis  January 1st, 1970
4   5       Alex       Vogel   1968 December 25

>>> pd.read_csv(DATA, parse_dates=['Mission Date'])
   id First Name   Last Name Mission Date
0   1        Jan  Twardowski   1988-01-05
1   2       Mark      Watney   1969-07-21
2   3       Ivan   Ivanovich   1961-04-12
3   4    Melissa       Lewis   1970-01-01
4   5       Alex       Vogel   1968-12-25


Assignments
-----------
.. literalinclude:: assignments/pandas_readcsv_a.py
    :caption: :download:`Solution <assignments/pandas_readcsv_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_readcsv_b.py
    :caption: :download:`Solution <assignments/pandas_readcsv_b.py>`
    :end-before: # Solution
