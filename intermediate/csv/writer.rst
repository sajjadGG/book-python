CSV Writer
==========
* csv.writer: list[tuple]


Writer
------
Writing data to CSV file using ``csv.writer()``:

.. code-block:: python

    import csv

    FILE = r'/tmp/myfile.csv'

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor')]

    with open(FILE, mode='w') as file:
        result = csv.writer(file)
        result.writerows(DATA)

    # Sepal length,Sepal width,Petal length,Petal width,Species
    # 5.8,2.7,5.1,1.9,virginica
    # 5.1,3.5,1.4,0.2,setosa
    # 5.7,2.8,4.1,1.3,versicolor


Assignments
-----------
.. literalinclude:: assignments/csv_writer_a.py
    :caption: :download:`Solution <assignments/csv_writer_a.py>`
    :end-before: # Solution
