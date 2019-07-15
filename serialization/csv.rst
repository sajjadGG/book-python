.. _CSV Serialization:

*****************
CSV Serialization
*****************


Reading data from CSV files
===========================
* Good practice is to always set:

    * ``quotechar='"'``
    * ``delimiter=','``
    * ``open(FILE, encoding='utf-8')`` - especially for MS Excel exported *CSV* files

.. code-block:: python
    :caption: Zapis do plików csv używając ``csv.DictReader()``

    import csv

    FILE = r'../data/iris.csv'
    """
    sepal_length,sepal_width,petal_length,petal_width,species
    5.4,3.9,1.3,0.4,setosa
    5.9,3.0,5.1,1.8,virginica
    6.0,3.4,4.5,1.6,versicolor
    7.3,2.9,6.3,1.8,virginica
    5.6,2.5,3.9,1.1,versicolor
    5.4,3.9,1.3,0.4,setosa
    """


    with open(FILE) as file:
        data = csv.DictReader(file, delimiter=',', quotechar='"')

        for line in data:
            print(dict(line))

    # {'sepal_length': '5.4', 'sepal_width': '3.9', 'petal_length': '1.3', 'petal_width': '0.4', 'species': 'setosa'}
    # {'sepal_length': '5.9', 'sepal_width': '3.0', 'petal_length': '5.1', 'petal_width': '1.8', 'species': 'virginica'}
    # {'sepal_length': '6.0', 'sepal_width': '3.4', 'petal_length': '4.5', 'petal_width': '1.6', 'species': 'versicolor'}
    # {'sepal_length': '7.3', 'sepal_width': '2.9', 'petal_length': '6.3', 'petal_width': '1.8', 'species': 'virginica'}
    # ...


Writing to CSV files
====================
* Good practice is to always set:

    * ``quoting=csv.QUOTE_ALL``
    * ``quotechar='"'``
    * ``delimiter=','``
    * ``lineterminator='\n'``
    * ``open(FILE, encoding='utf-8')`` - especially for reading in MS Excel

.. code-block:: python
    :caption: Zapis do plików csv używając ``csv.DictWriter()``

    import csv


    DATA = [
        {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
        {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'},
        {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'},
        {'sepal_length': 7.3, 'sepal_width': 2.9, 'petal_length': 6.3, 'petal_width': 1.8, 'species': 'virginica'},
        {'sepal_length': 5.6, 'sepal_width': 2.5, 'petal_length': 3.9, 'petal_width': 1.1, 'species': 'versicolor'},
        {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
    ]


    with open(r'filename.csv', mode='w') as file:
        writer = csv.DictWriter(
            f=file,
            fieldnames=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'],
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL,
            lineterminator='\n')

        writer.writeheader()

        for row in DATA:
            writer.writerow(row)


Parsing non-CSV files with ``csv.DictReader()``
===============================================

Parsing ``/etc/passwd``
-----------------------
.. code-block:: python
    :caption: Parsing ``/etc/passwd`` file with ``csv.DictReader()``

    import csv


    FIELDNAMES = ['username', 'password', 'uid', 'gid', 'full_name', 'home', 'shell']
    FILE = r'../data/etc-passwd.txt'
    """
    root:x:0:0:root:/root:/bin/bash
    watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
    jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
    twardowski:x:1002:1002:Иван Иванович:/home/twardowski:/bin/bash
    """


    with open(FILE) as file:
        data = csv.DictReader(file, fieldnames=FIELDNAMES, delimiter=':')

        for line in data:
            print(dict(line))

    # {'username': 'root', 'password': 'x', 'uid': '0',...}
    # {'username': 'watney', 'password': 'x', 'uid': '1000',...}
    # {'username': 'jimenez', 'password': 'x', 'uid': '1001',...}
    # {'username': 'twardowski', 'password': 'x', 'uid': '1002',...}


Parsing Java properties file
----------------------------
.. code-block:: python
    :caption: Parsing ``sonar-project.properties`` file with  ``csv.DictReader()``

    import csv

    FILE = r'../data/sonar-project.properties'
    """
    sonar.projectKey=habitatOS
    sonar.projectName=habitatOS
    sonar.language=py
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true
    """

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

.. code-block:: python

    import pandas as pd

    url = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'
    columns = [
        'Sepal length',
        'Sepal width',
        'Petal length',
        'Petal width',
        'Species'
    ]

    df = pd.read_csv(url, skiprows=1, names=columns)

    df.head(5)
    #   Sepal length  Sepal width  Petal length  Petal width  Species
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

    df.Species.replace(to_replace={
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }, inplace=True)

    df = df.sample(frac=1.0).reset_index(drop=True)
    #      Sepal length  Sepal width     ...      Petal width     Species
    # 0             5.0          2.0     ...              1.0  versicolor
    # 1             6.4          2.7     ...              1.9   virginica
    # 2             5.6          3.0     ...              1.5  versicolor
    # 3             5.7          2.6     ...              1.0  versicolor
    # 4             6.4          3.1     ...              1.8   virginica
    # 5             4.6          3.6     ...              0.2      setosa
    # 6             5.9          3.0     ...              1.5  versicolor

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


Assignments
===========

Reading ``csv``
---------------
* Filename: :download:`solution/csv_dictreader.py`
* Lines of code to write: 20 lines
* Estimated time of completion: 10 min
* Input data: https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.csv

#. Otwórz w przeglądarce podany powyżej URL
#. Zapisz jego zawartość na dysku w miejscu gdzie masz skrypty w pliku ``iris.csv``
#. Korzystając z ``csv.DictReader`` wczytaj zawartość pliku
#. Podaj jawnie ``encoding``, ``delimiter`` oraz ``quotechar``
#. Nazwy poszczególnych kolumn:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

#. Wypisz wiersze na ekranie

Writing ``csv`` - fixed schema
------------------------------
* Filename: :download:`solution/csv_dictwriter_fixed.py`
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min
* Input data: :numref:`listing-csv-dictwriter-fixed`

.. code-block:: python
    :name: listing-csv-dictwriter-fixed
    :caption: Create ``fieldnames: Set[str]`` with unique keys

    DATA = [
        {'first_name': 'Jan',  'last_name': 'Twardowski'},
        {'first_name': 'José', 'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван', 'last_name': 'Иванович'},
        {'first_name': 'Alex', 'last_name': 'Vogel'},
    ]

#. Za pomocą ``csv.DictWriter()`` zapisz do pliku *CSV* dane o stałej strukturze
#. Wszystkie pola muszą być zawsze w cudzysłowach i oddzielone średnikami, kodowanie UTF-8, a na końcu linii Unix newline.
#. Spróbuj otworzyć plik w MS Excel i w Notatniku, porównaj wyniki
#. Jeżeli będziesz otwierał plik w MS Excel, to zwróć uwagę, że ten program oczekuje innego kodowania ("windows-1250")

Writing ``csv`` - variable schema
---------------------------------
* Filename: :download:`solution/csv_dictwriter_variable.py`
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min
* Input data: :numref:`listing-csv-dictwriter-variable`

.. code-block:: python
    :name: listing-csv-dictwriter-variable
    :caption: Create ``fieldnames: Set[str]`` with unique keys

    DATA = [
        {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
        {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
        {'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
        {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
    ]

#. Za pomocą ``csv.DictWriter()`` zapisz do pliku CSV dane o zmiennej strukturze
#. Wszystkie pola muszą być zawsze w cudzysłowach
#. Pola mają być oddzielone średnikami
#. Kodowanie pliku kodowanie UTF-8
#. Na końcu linii Unix newline.
#. ``fieldnames`` musi być generowane automatycznie na podstawie ``DATA``
#. Rezultat powinien wyglądać tak:

    .. csv-table:: Result of variable schema CSV file generation
        :header: "Petal width", "Petal length", "Sepal length", "Sepal width", "Species"

        "", "", "5.1", "3.5", "setosa"
        "1.3", "4.1", "", "", "versicolor"
        "1.8", "", "6.3", "", "virginica"
        "0.2", "1.4", "", "", "setosa"
        "", "4.1", "", "2.8", "versicolor"
        "1.8", "", "", "2.9", "virginica"

:The whys and wherefores:
    * Umiejętność korzystania z modułu ``csv``
    * Umiejętność iteracji po złożonych strukturach danych
    * Dynamiczne generowanie struktur danych na podstawie innych

:Hints:
    * To jest bardzo często występujący i użyteczny przykład

Object serialization to CSV
---------------------------
* Filename: :download:`solution/csv_relations.py`
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Input data: :numref:`listing-csv-addressbook`

.. code-block:: python
    :name: listing-csv-addressbook
    :caption: Address book

    class Contact:
        def __init__(self, first_name, last_name, addresses=()):
            self.first_name = first_name
            self.last_name = last_name
            self.addresses = addresses


    class Address:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)


    addressbook = [
        Contact(first_name='Jan', last_name='Twardowski', addresses=[
            Address(street='2101 E NASA Pkwy', city='Houston', state='Texas', code='77058', country='USA'),
            Address(street=None, city='Kennedy Space Center', code='32899', country='USA'),
            Address(street='4800 Oak Grove Dr', city='Pasadena', code='91109', country='USA'),
            Address(street='2825 E Ave P', city='Palmdale', state='California', code='93550', country='USA', data_urodzenia=None),
        ]),
        Contact(first_name='José', last_name='Jiménez'),
        Contact(first_name='Иван', last_name='Иванович', addresses=[]),
    ]

#. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
#. Wszystkie pola muszą być zawsze w cudzysłowach i oddzielone średnikami, kodowanie UTF-8, a na końcu linii Unix newline.
#. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku
