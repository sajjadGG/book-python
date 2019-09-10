.. _CSV Serialization:

*****************
CSV Serialization
*****************


Dialects
========
.. code-block:: python

    import csv

    csv.list_dialects()
    # ['excel', 'excel-tab', 'unix']

* CSV quoting options:

    * ``csv.QUOTE_ALL``
    * ``csv.QUOTE_MINIMAL``
    * ``csv.QUOTE_NONE``
    * ``csv.QUOTE_NONNUMERIC``

* Good practice is to always specify:

    * ``quoting=csv.QUOTE_ALL`` to ``csv.DictReader()`` object
    * ``quotechar='"'`` to ``csv.DictReader()`` object
    * ``delimiter=','`` to  ``csv.DictReader()`` object
    * ``lineterminator='\n'`` to ``csv.DictReader()`` object
    * ``encoding='utf-8'`` to ``open()`` function (especially when working with Microsoft Excel)

* Microsoft Excel uses:

    * ``quotechar='"'``
    * ``delimiter=';'``
    * ``lineterminator='\r\n'``
    * ``encoding='...'`` - depends on Windows version and settings

* Encoding:

    * ``utf-8`` - international standard (should be always used!)
    * ``iso-8859-1`` - ISO standard for Western Europe and USA
    * ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
    * ``cp1250`` or ``windows-1250`` - Polish encoding on Windows
    * ``cp1251`` or ``windows-1251`` - Russian encoding on Windows
    * ``cp1252`` or ``windows-1252`` - Western European encoding on Windows

Read data from CSV file
=======================
.. code-block:: python
    :caption: Read data from CSV file using ``csv.DictReader()``

    import csv

    FILE = r'iris.csv'
    # sepal_length,sepal_width,petal_length,petal_width,species
    # 5.4,3.9,1.3,0.4,setosa
    # 5.9,3.0,5.1,1.8,virginica
    # 6.0,3.4,4.5,1.6,versicolor


    with open(FILE) as file:
        data = csv.DictReader(file, delimiter=',', quotechar='"')

        for line in data:
            print(dict(line))

    # {'sepal_length': '5.4', 'sepal_width': '3.9', 'petal_length': '1.3', 'petal_width': '0.4', 'species': 'setosa'}
    # {'sepal_length': '5.9', 'sepal_width': '3.0', 'petal_length': '5.1', 'petal_width': '1.8', 'species': 'virginica'}
    # {'sepal_length': '6.0', 'sepal_width': '3.4', 'petal_length': '4.5', 'petal_width': '1.6', 'species': 'versicolor'}


Write data to CSV file
======================
* Remember to add ``mode='w'`` to ``open()`` function

.. code-block:: python
    :caption: Write data to CSV file using ``csv.DictWriter()``

    import csv

    FILE = r'iris.csv'
    INPUT = [
        {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
        {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'},
        {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'},
    ]


    with open(FILE, mode='w') as file:
        writer = csv.DictWriter(
            f=file,
            fieldnames=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'],
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL,
            lineterminator='\n')

        writer.writeheader()

        for row in INPUT:
            writer.writerow(row)


Parsing non-CSV files
=====================

Parsing ``/etc/passwd``
-----------------------
.. code-block:: python
    :caption: Parsing ``/etc/passwd`` file with ``csv.DictReader()``

    import csv


    FILE = r'etc-passwd.txt'
    # root:x:0:0:root:/root:/bin/bash
    # watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
    # jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
    # twardowski:x:1002:1002:Jan Twardowski:/home/twardowski:/bin/bash

    with open(FILE) as file:
        data = csv.DictReader(
            file,
            fieldnames=['username', 'password', 'uid', 'gid', 'full_name', 'home', 'shell'],
            delimiter=':',
            lineterminator='\n',
            quoting=csv.QUOTE_NONE)

        for line in data:
            print(dict(line))

    # {'username': 'root', 'password': 'x', 'uid': '0',...}
    # {'username': 'watney', 'password': 'x', 'uid': '1000',...}
    # {'username': 'jimenez', 'password': 'x', 'uid': '1001',...}
    # {'username': 'twardowski', 'password': 'x', 'uid': '1002',...}

Parsing Java properties file
----------------------------
.. code-block:: python
    :caption: Parsing Java properties file with ``csv.DictReader()``

    import csv


    FILE = r'sonar-project.properties'
    # sonar.projectKey=habitatOS
    # sonar.projectName=habitatOS
    # sonar.language=py
    # sonar.sourceEncoding=UTF-8
    # sonar.verbose=true

    with open(FILE) as file:

        data = csv.DictReader(
            file,
            fieldnames=['property', 'value'],
            delimiter='=',
            lineterminator='\n',
            quoting=csv.QUOTE_NONE)

        for line in data:
            print(dict(line))

    # {'property': 'sonar.projectKey', 'value': 'habitatOS'}
    # {'property': 'sonar.projectName', 'value': 'habitatOS'}
    # {'property': 'sonar.language', 'value': 'py'}
    # {'property': 'sonar.sourceEncoding', 'value': 'UTF-8'}
    # {'property': 'sonar.verbose', 'value': 'true'}


Pandas
======
* External library
* Installation: ``pip install pandas``

.. code-block:: python

    import pandas as pd


    FILE = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'

    df = pd.read_csv(FILE, skiprows=1)

    df.head(5)
    #      5.1  3.5  1.4  0.2  0
    # 0    4.9  3.0  1.4  0.2  0
    # 1    4.7  3.2  1.3  0.2  0
    # 2    4.6  3.1  1.5  0.2  0
    # 3    5.0  3.6  1.4  0.2  0
    # 4    5.4  3.9  1.7  0.4  0

    df.columns = [
        'Sepal length',
        'Sepal width',
        'Petal length',
        'Petal width',
        'Species'
    ]

    df.head(5)
    #    Sepal length  Sepal width  Petal length  Petal width  Species
    # 0           5.1          3.5           1.4          0.2        0
    # 1           4.9          3.0           1.4          0.2        0
    # 2           4.7          3.2           1.3          0.2        0
    # 3           4.6          3.1           1.5          0.2        0
    # 4           5.0          3.6           1.4          0.2        0

    df.tail(3)
    #      Sepal length  Sepal width  Petal length  Petal width  Species
    # 147           6.5          3.0           5.2          2.0        2
    # 148           6.2          3.4           5.4          2.3        2
    # 149           5.9          3.0           5.1          1.8        2

    df['Species'].replace({
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }, inplace=True)

    df = df.sample(frac=1.0)
    #      Sepal length  Sepal width  Petal length  Petal width     Species
    # 120           5.6          2.8           4.9          2.0   virginica
    # 9             5.4          3.7           1.5          0.2      setosa
    # 54            5.7          2.8           4.5          1.3  versicolor
    # 46            4.6          3.2           1.4          0.2      setosa
    # 2             4.6          3.1           1.5          0.2      setosa
    # ...

    df.reset_index(drop=True)
    #      Sepal length  Sepal width     ...      Petal width     Species
    # 0             5.0          2.0     ...              1.0  versicolor
    # 1             6.4          2.7     ...              1.9   virginica
    # 2             5.6          3.0     ...              1.5  versicolor
    # 3             5.7          2.6     ...              1.0  versicolor
    # 4             6.4          3.1     ...              1.8   virginica
    # ...

    df.describe()
    #        Sepal length  Sepal width  Petal length  Petal width
    # count    150.000000   150.000000    150.000000   150.000000
    # mean       5.843333     3.057333      3.758000     1.199333
    # std        0.828066     0.435866      1.765298     0.762238
    # min        4.300000     2.000000      1.000000     0.100000
    # 25%        5.100000     2.800000      1.600000     0.300000
    # 50%        5.800000     3.000000      4.350000     1.300000
    # 75%        6.400000     3.300000      5.100000     1.800000
    # max        7.900000     4.400000      6.900000     2.500000

Hist
----
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd


    FILE = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'

    df = pd.read_csv(FILE)
    df.hist()
    plt.show()

.. figure:: img/matplotlib-pd-hist.png
    :scale: 100%
    :align: center

    Vizualization using hist

Density
-------
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd


    FILE = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'

    df = pd.read_csv(FILE)
    df.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
    plt.show()

.. figure:: img/matplotlib-pd-density.png
    :scale: 100%
    :align: center

    Vizualization using density

Box
---
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd


    FILE = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'

    df = pd.read_csv(url)
    df.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
    plt.show()

.. figure:: img/matplotlib-pd-box.png
    :scale: 100%
    :align: center

    Vizualization using density

Scatter matrix
--------------
* The in ``pandas`` version ``0.22`` plotting module has been moved from ``pandas.tools.plotting`` to ``pandas.plotting``
* As of version ``0.19``, the ``pandas.plotting`` library did not exist

.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd
    from pandas.plotting import scatter_matrix


    FILE = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'

    df = pd.read_csv(url)
    scatter_matrix(df)
    plt.show()

.. figure:: img/matplotlib-pd-scatter-matrix.png
    :scale: 100%
    :align: center

    Vizualization using density

Descriptive statistics
----------------------
.. csv-table:: Descriptive statistics
    :header: "Function", "Description"

    "``count``", "Number of non-null observations"
    "``sum``", "Sum of values"
    "``mean``", "Mean of values"
    "``mad``", "Mean absolute deviation"
    "``median``", "Arithmetic median of values"
    "``min``", "Minimum"
    "``max``", "Maximum"
    "``mode``", "Mode"
    "``abs``", "Absolute Value"
    "``prod``", "Product of values"
    "``std``", "Unbiased standard deviation"
    "``var``", "Unbiased variance"
    "``sem``", "Unbiased standard error of the mean"
    "``skew``", "Unbiased skewness (3rd moment)"
    "``kurt``", "Unbiased kurtosis (4th moment)"
    "``quantile``", "Sample quantile (value at %)"
    "``cumsum``", "Cumulative sum"
    "``cumprod``", "Cumulative product"
    "``cummax``", "Cumulative maximum"
    "``cummin``", "Cumulative minimum"


Assignments
===========

Read and parse data from CSV file
---------------------------------
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/csv_dictreader.py`

:English:
    #. Download :download:`data/iris-clean.csv` file
    #. Save data to ``iris-clean.csv`` in your script folder
    #. Using ``csv.DictReader`` read the content
    #. Use explicit ``encoding``, ``delimiter`` and ``quotechar``
    #. Replace column names (see output data)
    #. Skip the first line (header)
    #. Print rows

:Polish:
    #. Pobierz plik :download:`data/iris-clean.csv`
    #. Zapisz jego zawartość na dysku w miejscu gdzie masz skrypty
    #. Korzystając z ``csv.DictReader`` wczytaj zawartość pliku
    #. Podaj jawnie ``encoding``, ``delimiter`` oraz ``quotechar``
    #. Nazwy poszczególnych kolumn (patrz dane wyjściowe)
    #. Pomiń pierwszą linię (nagłówek)
    #. Wypisz wiersze

:Output:
    .. code-block:: python

        {'Sepal length': '5.4', 'Sepal width': '3.9', 'Petal length': '1.3', 'Petal width': '0.4', 'Species': 'setosa'}
        {'Sepal length': '5.9', 'Sepal width': '3.0', 'Petal length': '5.1', 'Petal width': '1.8', 'Species': 'virginica'}
        {'Sepal length': '6.0', 'Sepal width': '3.4', 'Petal length': '4.5', 'Petal width': '1.6', 'Species': 'versicolor'}

Write fixed schema data to CSV file
-----------------------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/csv_dictwriter_fixed.py`

:English:
    #. Using ``csv.DictWriter()`` save ``DATA`` to file
    #. Open file in your spreadsheet program like Microsoft Excel / Libre Office / Numbers etc.
    #. Open file in simple in your IDE and simple text editor (like Notepad, vim, gedit)

:Polish:
    #. Za pomocą ``csv.DictWriter()`` zapisz do pliku *CSV* dane o stałej strukturze
    #. Spróbuj otworzyć plik w arkuszu kalkulacyjnym tj. Microsoft Excel / Libre Office / Numbers itp
    #. Spróbuj otworzyć plik w IDE i prostym edytorze tekstu tj. Notepad, vim lub gedit

:Non functional requirements:
    #. All fields must be enclosed by double quote ``"`` character
    #. Use ``;`` to separate columns
    #. Use ``utf-8`` encoding
    #. Use Unix newline

:Input:
    .. code-block:: python

        INPUT = [
            {'first_name': 'Jan',  'last_name': 'Twardowski'},
            {'first_name': 'Jose', 'last_name': 'Jimenez'},
            {'first_name': 'Mark', 'last_name': 'Watney'},
            {'first_name': 'Ivan', 'last_name': 'Ivanovic'},
            {'first_name': 'Melissa', 'last_name': 'Lewis'},
        ]

:Output:
    .. code-block:: text

        "first_name";"last_name"
        "Jan";"Twardowski"
        "Jose";"Jimenez"
        "Mark";"Watney"
        "Ivan";"Ivanovic"
        "Melissa";"Lewis"

Write variable schema data to file
----------------------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/csv_dictwriter_variable.py`

:English:
    #. Using ``csv.DictWriter()`` write variable schema data to CSV file
    #. ``fieldnames`` must be automatically generated from ``DATA``
    #. ``fieldnames`` must always be in the same order

:Polish:
    #. Za pomocą ``csv.DictWriter()`` zapisz do pliku CSV dane o zmiennej strukturze
    #. ``fieldnames`` musi być generowane automatycznie na podstawie ``DATA``
    #. ``fieldnames`` ma być zawsze w takiej samej kolejności
    #. Rezultat powinien wyglądać tak:

:Non functional requirements:
    #. All fields must be enclosed by double quote ``"`` character
    #. Use ``;`` to separate columns
    #. Use ``utf-8`` encoding
    #. Use Unix newline

:The whys and wherefores:
    * Ability to use ``csv`` module to write data
    * Ability to iterate over nested data structures
    * Dynamically generate data structures from other

:Input:
    .. code-block:: python

        INPUT = [
            {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
            {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
            {'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
            {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
        ]

:Output:
    .. csv-table:: Output
        :header: "Petal length", "Petal width", "Sepal length", "Sepal width", "Species"

        "", "", "5.1", "3.5", "setosa"
        "4.1", "1.3", "", "", "versicolor"
        "", "1.8", "6.3", "", "virginica"
        "1.4", "0.2", "", "", "setosa"
        "4.1", "", "", "2.8", "versicolor"
        "", "1.8", "", "2.9", "virginica"

Object serialization to CSV
---------------------------
* Complexity level: hard
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/csv_relations.py`

:English:
    #. Using ``csv.DictWriter()`` save contacts from addressbook to CSV file
    #. How to write relations to CSV file (contact has many addresses)?
    #. Recreate object structure from CSV file

:Polish:
    #. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
    #. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
    #. Odtwórz strukturę obiektów na podstawie danych odczytanych z pliku

:Non functional requirements:
    #. All fields must be enclosed by double quote ``"`` character
    #. Use ``;`` to separate columns
    #. Use ``utf-8`` encoding
    #. Use Unix newline

:Input:
    .. code-block:: python

        class Contact:
            def __init__(self, first_name, last_name, addresses=()):
                self.first_name = first_name
                self.last_name = last_name
                self.addresses = addresses


        class Address:
            def __init__(self, center, location):
                self.center = center
                self.location = location


        INPUT = [
            Contact(first_name='Jan', last_name='Twardowski', addresses=(
                Address(center='Johnson Space Center', location='Houston, TX'),
                Address(center='Kennedy Space Center', location='Merritt Island, FL'),
                Address(center='Jet Propulsion Laboratory', location='Pasadena, CA'),
            )),
            Contact(first_name='Mark', last_name='Watney'),
            Contact(first_name='Melissa', last_name='Lewis', addresses=()),
        ]
