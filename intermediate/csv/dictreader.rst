CSV DictReader
==============


Rationale
---------
* csv.DictReader: list[dict]


Example
-------
>>> import csv
>>>
>>> FILE = r'_temporary.csv'
>>> DATA = """sepal_length,sepal_width,petal_length,petal_width,species
... 5.4,3.9,1.3,0.4,setosa
... 5.9,3.0,5.1,1.8,virginica
... 6.0,3.4,4.5,1.6,versicolor"""
>>>
>>> with open(FILE, mode='w') as file:
...     _ = file.write(DATA)
>>>
>>>
>>> with open(FILE) as file:
...     result = csv.DictReader(file)
...
...     for line in result:
...         print(line)
{'sepal_length': '5.4', 'sepal_width': '3.9', 'petal_length': '1.3', 'petal_width': '0.4', 'species': 'setosa'}
{'sepal_length': '5.9', 'sepal_width': '3.0', 'petal_length': '5.1', 'petal_width': '1.8', 'species': 'virginica'}
{'sepal_length': '6.0', 'sepal_width': '3.4', 'petal_length': '4.5', 'petal_width': '1.6', 'species': 'versicolor'}

Read data from CSV file using ``csv.DictReader()``. While giving custom names note, that first line (typically a header) will be treated like normal data. Therefore we skip it using ``header = file.readline()``:

.. code-block:: text

    sepal_length,sepal_width,petal_length,petal_width,species
    5.4,3.9,1.3,0.4,setosa
    5.9,3.0,5.1,1.8,virginica
    6.0,3.4,4.5,1.6,versicolor

>>> import csv
>>>
>>> FILE = r'_temporary.csv'
>>> DATA = """sepal_length,sepal_width,petal_length,petal_width,species
... 5.4,3.9,1.3,0.4,setosa
... 5.9,3.0,5.1,1.8,virginica
... 6.0,3.4,4.5,1.6,versicolor"""
>>>
>>> with open(FILE, mode='w') as file:
...     _ = file.write(DATA)
>>>
>>>
>>> FIELDNAMES = ['Sepal Length', 'Sepal Width',
...               'Petal Length', 'Petal Width', 'Species']
>>>
>>>
>>> with open(FILE) as file:
...     result = csv.DictReader(file, fieldnames=FIELDNAMES, delimiter=',')
...     header = file.readline()  # skip the first line (old header)
...
...     for line in result:
...         print(line)
{'Sepal Length': '5.4', 'Sepal Width': '3.9', 'Petal Length': '1.3', 'Petal Width': '0.4', 'Species': 'setosa'}
{'Sepal Length': '5.9', 'Sepal Width': '3.0', 'Petal Length': '5.1', 'Petal Width': '1.8', 'Species': 'virginica'}
{'Sepal Length': '6.0', 'Sepal Width': '3.4', 'Petal Length': '4.5', 'Petal Width': '1.6', 'Species': 'versicolor'}


Use Cases
---------
.. code-block:: text

    'sepal_length';'sepal_width';'petal_length';'petal_width';'species'
    '5,4';'3,9';'1,3';'0,4';'setosa'
    '5,9';'3,0';'5,1';'1,8';'virginica'
    '6,0';'3,4';'4,5';'1,6';'versicolor'

>>> import csv
>>>
>>>
>>> FILE = r'_temporary.csv'
>>> DATA = """'sepal_length';'sepal_width';'petal_length';'petal_width';'species'
... '5,4';'3,9';'1,3';'0,4';'setosa'
... '5,9';'3,0';'5,1';'1,8';'virginica'
... '6,0';'3,4';'4,5';'1,6';'versicolor'"""
>>>
>>> with open(FILE, mode='w') as file:
...     _ = file.write(DATA)
>>>
>>>
>>> def isnumeric(value):
...     try:
...         float(value)
...         return True
...     except ValueError:
...         return False
>>>
>>>
>>> def clean(line):
...     return {key: float(v) if isnumeric(v) else v
...             for key, value in line.items()
...             if (v := value.replace(',', '.'))}
>>>
>>>
>>> with open(FILE) as file:
...     result = csv.DictReader(file, delimiter=';', quotechar="'")
...
...     for line in result:
...         print(clean(line))
{'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'}
{'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'}
{'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'}


Assignments
-----------
.. literalinclude:: assignments/csv_dictreader_a.py
    :caption: :download:`Solution <assignments/csv_dictreader_a.py>`
    :end-before: # Solution
