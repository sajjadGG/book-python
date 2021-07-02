CSV DictWriter
==============


Rationale
---------
* csv.DictWriter: list[dict]


DictWriter
----------
* Remember to add ``mode='w'`` to ``open()`` function
* Default encoding is ``encoding='utf-8'``

.. code-block:: python

    import csv

    FILE = r'_temporary.csv'

    DATA = [{'Sepal Length': 5.4, 'Sepal Width': 3.9, 'Petal Length': 1.3, 'Petal Width': 0.4, 'Species': 'setosa'},
            {'Sepal Length': 5.9, 'Sepal Width': 3.0, 'Petal Length': 5.1, 'Petal Width': 1.8, 'Species': 'virginica'},
            {'Sepal Length': 6.0, 'Sepal Width': 3.4, 'Petal Length': 4.5, 'Petal Width': 1.6, 'Species': 'versicolor'}]

    header = DATA[0].keys()

    with open(FILE, mode='w') as file:
        result = csv.DictWriter(file, fieldnames=header)
        result.writeheader()
        result.writerows(DATA)


    # Sepal Length,Sepal Width,Petal Length,Petal Width,Species
    # 5.4,3.9,1.3,0.4,setosa
    # 5.9,3.0,5.1,1.8,virginica
    # 6.0,3.4,4.5,1.6,versicolor

Write data to CSV file using ``csv.DictWriter()``:

.. code-block:: python

    import csv

    FILE = r'_temporary.csv'

    DATA = [{'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
            {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'},
            {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'}]

    FIELDNAMES = ['sepal_length', 'sepal_width', 'petal_length',
                  'petal_width', 'species']

    with open(FILE, mode='w', encoding='utf-8') as file:
        result = csv.DictWriter(
            f=file,
            fieldnames=FIELDNAMES,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL,
            lineterminator='\n')

        result.writeheader()
        result.writerows(DATA)

    # "sepal_length","sepal_width","petal_length","petal_width","species"
    # "5.4","3.9","1.3","0.4","setosa"
    # "5.9","3.0","5.1","1.8","virginica"
    # "6.0","3.4","4.5","1.6","versicolor"


Assignments
-----------
.. literalinclude:: assignments/csv_dictwriter_a.py
    :caption: :download:`Solution <assignments/csv_dictwriter_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_dictwriter_b.py
    :caption: :download:`Solution <assignments/csv_dictwriter_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_dictwriter_c.py
    :caption: :download:`Solution <assignments/csv_dictwriter_c.py>`
    :end-before: # Solution
