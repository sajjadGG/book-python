CSV Reader
==========


Rationale
---------
* csv.reader: list[tuple]


Reader
------
Read data from CSV file using ``csv.reader()``:

.. code-block:: python

    import csv

    FILE = r'_temporary.csv'
    # sepal_length,sepal_width,petal_length,petal_width,species
    # 5.4,3.9,1.3,0.4,setosa
    # 5.9,3.0,5.1,1.8,virginica
    # 6.0,3.4,4.5,1.6,versicolor


    with open(FILE) as file:
        result = csv.reader(file)

        for line in result:
            print(line)

    # ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    # ['5.4', '3.9', '1.3', '0.4', 'setosa']
    # ['5.9', '3.0', '5.1', '1.8', 'virginica']
    # ['6.0', '3.4', '4.5', '1.6', 'versicolor']


Assignments
-----------
.. literalinclude:: assignments/csv_reader_a.py
    :caption: :download:`Solution <assignments/csv_reader_a.py>`
    :end-before: # Solution
