.. _Generators and Comprehensions:

*****************************
Generators and Comprehensions
*****************************


Lazy evaluation
===============
* Code do not execute instantly
* Sometimes code is not executed at all!

Declaring generators
--------------------
.. code-block:: python

    # This will not execute code!
    range(0, 9_999_999)
    range(0, 9_999_999)
    range(0, 9_999_999)

.. code-block:: python

    # This will only create generator expression, but not execute it!
    numbers = range(0, 9_999_999)
    print(numbers)
    # range(0, 9999999)

Getting  values from generator
------------------------------
.. code-block:: python

    numbers = range(0, 9_999_999)
    list(range)  # Generator will execute here (not very efficient)

.. code-block:: python

    # Generator will execute once at a time, for every loop iteration
    for i in range(0, 9_999_999):
        print(i)


Generator expressions vs. Comprehensions
========================================

Generator Expressions
---------------------
* Lazy evaluation

.. code-block:: python

    (x*x for x in range(0, 30) if x % 2)

Comprehensions
--------------
* Executes instantly

.. code-block:: python

    a = [x for x in range(0, 10)]
    b = (x for x in range(0, 10))
    c = {x for x in range(0, 10)}
    d = {x: x for x in range(0, 10)}

.. code-block:: python

    a = list(x for x in range(0, 10))
    b = tuple(x for x in range(0, 10))
    c = set(x for x in range(0, 10))
    d = dict(x: x for x in range(0, 10))

What is the difference?
-----------------------
.. code-block:: python

    # tutaj nastąpi wykonanie i przypisanie
    numbers = [x**2 for x in range(0, 30) if x % 2 == 0]

    print(numbers)
    # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784]

    print(numbers)
    # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784]

.. code-block:: python

    # tu nastąpi tylko przypisanie do generatora
    numbers = (x**2 for x in range(0, 30) if x % 2 == 0)

    print(numbers)
    # <generator object <genexpr> at 0x11af5a570>

    print(list(numbers))
    # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784]

    print(list(numbers))
    # []

Which one is better?
--------------------
* Comprehensions - Using values more than one
* Generators - Using value one (for example in the loop iterator)


Operator ``yield``
==================
.. code-block:: python

    # ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
    ]

.. code-block:: python

    def get_species(species):
        output = []

        for record in DATA:
            if record[4] == species:
                output.append(record)

        return output


    data = get_species('setosa')

    print(data)
    # [(5.1, 3.5, 1.4, 0.2, 'setosa'),
    #  (4.9, 3.0, 1.4, 0.2, 'setosa'),
    #  (5.4, 3.9, 1.7, 0.4, 'setosa'),
    #  (4.6, 3.4, 1.4, 0.3, 'setosa')]


    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.9, 3.0, 1.4, 0.2, 'setosa')
    # (5.4, 3.9, 1.7, 0.4, 'setosa')
    # (4.6, 3.4, 1.4, 0.3, 'setosa')


.. code-block:: python

    def get_species(species):
        for record in DATA:
            if record[4] == species:
                yield record

    data = get_species('setosa')

    print(data)
    # <generator object get_species at 0x11af257c8>


    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.9, 3.0, 1.4, 0.2, 'setosa')
    # (5.4, 3.9, 1.7, 0.4, 'setosa')
    # (4.6, 3.4, 1.4, 0.3, 'setosa')

Przykłady
=========

Zamiana klucz wartość oraz generowanie ``dict`` i ``set``
---------------------------------------------------------
.. code-block:: python

    data = {'first_name': 'Иван', 'last_name': 'Иванович'}

    out = {v: k for k, v in data.items()}  # {'Иван': 'first_name', 'Иванович': 'last_name'}
    type(out)  # <class 'dict'>

    out = {v for k, v in data.items()}  # {'Иван', 'Иванович'}
    type(out)  # <class 'set'>

Filtrowanie wyników na liście dictów
------------------------------------
.. code-block:: python

    ADDRESS_BOOK = [
        {'imie': 'Иван',
        'nazwisko': 'Иванович',
        'ulica': 'Wochod',
        'miasto': 'Bajkonur',
        'kod_pocztowy': '101503',
        'wojewodztwo': 'Kyzyłordyńskie',
        'panstwo': 'Kazachstan'},

        {'imie': 'José',
        'nazwisko': 'Jiménez',
        'ulica': '2101 E NASA Pkwy',
        'miasto': 'Huston',
        'kod_pocztowy': '77058',
        'wojewodztwo': 'Texas',
        'panstwo': 'USA'},
    ]

    osoby = [{'imie': x['imie'], 'nazwisko': x['nazwisko']} for x in ADDRESS_BOOK]
    print(osoby)


Zaawansowane wykorzystanie `List Comprehension`
-----------------------------------------------

.. code-block:: python

    def parzyste_f1(x):
        if x % 2 == 0:
            return True
        else:
            return False

    def parzyste_f2(x):
        return x % 2 == 0

    parzyste1 = [float(x) for x in range(0, 30) if x % 2 == 0]
    parzyste2 = [float(x) for x in range(0, 30) if parzyste_f1(x)]
    parzyste3 = []

    for x in range(0, 30):
        if x % 2 == 0:
            parzyste3.append(float(x))

    def parzyste_f3():
        parzyste = []

        for x in range(0, 30):
            if x % 2 == 0:
                parzyste.append(float(x))

        return parzyste

    a = range(0, 30)

Zaawansowane wykorzystanie `Generator Expressions`
--------------------------------------------------

.. code-block:: python

    liczby = (x for x in range(0, 30))
    parzyste1 = (x for x in range(0, 30) if x % 2 == 0)

    MAX = 30
    parzyste1 = (x for x in range(0, MAX) if x % 2 == 0)

    p = lambda a: (x for x in range(0, a) if x % 2 == 0)

    def xxx(a):
        return (x for x in range(0, a) if x % 2 == 0)

    p(2)
    xxx(2)

    parzyste2 = (x for x in range(0, a) if x % 2 == 0)

.. code-block:: python

    DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Max', 'last_name': 'Peck'},
        {'first_name': 'Иван'},
        {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
        {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961, 'first_step': 1969},
    ]


    # Wykorzystując listę
    fieldnames = []

    for record in DATA:
        for key in record.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    print('list():', fieldnames)


    # set(), podejście 1
    # Wykorzystując zbiór, który deduplikuje za nas
    fieldnames = set()

    for record in DATA:
        for key in record.keys():
            fieldnames.add(key)

    print('set(), podejście 1:', fieldnames)


    # set(), podejście 2
    # Wykorzystując zbiór, który deduplikuje za nas
    fieldnames = set()

    for key in [record.keys() for record in DATA]:
        fieldnames.update(key)

    print('set(), podejście 2:', fieldnames)


    # set(), podejście 3
    # Wykorzystując zbiór, który deduplikuje za nas
    fieldnames = set()

    for record in DATA:
        fieldnames.update(record.keys())

    print('set(), podejście 3:', fieldnames)


Nested list comprahension
-------------------------
.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Max', 'last_name': 'Peck'},
        {'first_name': 'Иван'},
        {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
        {'first_name': 'Max', 'last_name': 'Peck', 'first_step': 1969},
    ]

    # set(), podejście 4
    # Wykorzystując zbiór, który deduplikuje za nas
    fieldnames = set()
    fieldnames.update(key for record in DATA for key in record.keys())
    print('set(), podejście 4:', fieldnames)

Uwaga, czytelność kodu ma znaczenie
-----------------------------------
.. literalinclude:: src/generator-clean-code.py
    :name: listing-generator-clean-code
    :language: python
    :caption: Clean Code in generator


Assignments
===========

Generatory vs. Przetwarzanie Listy
----------------------------------
#. Napisz program, który wczyta plik :numref:`listing-file-etc-passwd-2`
#. Przefiltruj linie, tak aby nie zawierały komentarzy (zaczynające się od ``#``) oraz pustych linii
#. Przefiltruj linie, aby wyciągnąć konta systemowe - użytkowników, którzy mają UID (trzecie pole) mniejsze niż 1000
#. Zwróć listę loginów użytkowników systemowych
#. Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję
#. Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``
#. Porównaj wyniki jednego i drugiego rozwiązania przez użycie ``sys.getsizeof()``

:About:
    * Filename: ``generator_size.py``
    * Lines of code to write: 40 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Wykorzystanie generatorów
    * Odbieranie danych z lazy evaluation
    * Porównanie wielkości struktur danych
    * Parsowanie pliku
    * Filtrowanie treści w locie

.. literalinclude:: src/etc-passwd.txt
    :name: listing-file-etc-passwd-2
    :language: text
    :caption: ``/etc/passwd`` sample file
