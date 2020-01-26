***
CSV
***


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

    * ``delimiter=','`` to  ``csv.DictReader()`` object
    * ``quotechar='"'`` to ``csv.DictReader()`` object
    * ``quoting=csv.QUOTE_ALL`` to ``csv.DictReader()`` object
    * ``lineterminator='\n'`` to ``csv.DictReader()`` object
    * ``encoding='utf-8'`` to ``open()`` function (especially when working with Microsoft Excel)

* Microsoft Excel 2016 uses:

    * ``quotechar='"'``
    * ``delimiter=','``
    * ``lineterminator='\n'``
    * ``encoding='...'`` - depends on Windows version and settings

* Encoding:

    * ``utf-8`` - international standard (should be always used!)
    * ``iso-8859-1`` - ISO standard for Western Europe and USA
    * ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
    * ``cp1250`` or ``windows-1250`` - Polish encoding on Windows
    * ``cp1251`` or ``windows-1251`` - Russian encoding on Windows
    * ``cp1252`` or ``windows-1252`` - Western European encoding on Windows
    * ``ASCII`` - ASCII characters only


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


Assignments
===========

Read and parse data from CSV file
---------------------------------
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/csv_dictreader.py`

:English:
    #. Download :download:`data/iris.csv` file
    #. Save data to ``iris.csv`` in your script folder
    #. Using ``csv.DictReader`` read the content
    #. Use explicit ``encoding``, ``delimiter`` and ``quotechar``
    #. Replace column names (see output data)
    #. Skip the first line (header)
    #. Print rows

:Polish:
    #. Pobierz plik :download:`data/iris.csv`
    #. Zapisz jego zawartość na dysku w miejscu gdzie masz skrypty
    #. Korzystając z ``csv.DictReader`` wczytaj zawartość pliku
    #. Podaj jawnie ``encoding``, ``delimiter`` oraz ``quotechar``
    #. Podmień nazwy kolumn (patrz dane wyjściowe)
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
    #. Using ``csv.DictWriter()`` save ``INPUT`` (see below) to file
    #. Open file in your spreadsheet program like Microsoft Excel / Libre Office / Numbers etc.
    #. Open file in simple in your IDE and simple text editor (like Notepad, vim, gedit)

:Polish:
    #. Za pomocą ``csv.DictWriter()`` zapisz ``INPUT`` (patrz sekcja input) do pliku
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
* Complexity level: medium
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/csv_dictwriter_variable.py`

:English:
    #. Using ``csv.DictWriter()`` write variable schema data to CSV file
    #. ``fieldnames`` must be automatically generated from ``INPUT``
    #. ``fieldnames`` must always be in the same order

:Polish:
    #. Za pomocą ``csv.DictWriter()`` zapisz do pliku CSV dane o zmiennej strukturze
    #. ``fieldnames`` musi być generowane automatycznie na podstawie ``INPUT``
    #. ``fieldnames`` ma być zawsze w takiej samej kolejności

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
            {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
            {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
        ]

:Output:
    .. csv-table:: Output
        :header: "Petal length", "Petal width", "Sepal length", "Sepal width", "Species"

        "", "", "5.1", "3.5", "setosa"
        "4.1", "1.3", "", "", "versicolor"
        "", "1.8", "6.3", "", "virginica"
        "", "0.2", "5.0", "", "setosa"
        "4.1", "", "", "2.8", "versicolor"
        "", "1.8", "", "2.9", "virginica"

Object serialization to CSV
---------------------------
* Complexity level: hard
* Lines of code to write: 60 lines
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
            def __init__(self, location, city):
                self.location = location
                self.city = city


        INPUT = [
            Contact(first_name='Jan', last_name='Twardowski', addresses=(
                Address(location='Johnson Space Center', city='Houston, TX'),
                Address(location='Kennedy Space Center', city='Merritt Island, FL'),
                Address(location='Jet Propulsion Laboratory', city='Pasadena, CA'),
            )),
            Contact(first_name='Mark', last_name='Watney'),
            Contact(first_name='Melissa', last_name='Lewis', addresses=()),
        ]
