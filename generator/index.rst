.. _Generators:

*******************************
Generatory i list comprehension
*******************************

Lazy evaluation
===============
.. code-block:: python

    import datetime


    print(datetime.datetime.now())

    range(0, 9_999_999)

    print(datetime.datetime.now())

    for i in range(0, 9_999_999):
        pow(i, 10)

    print(datetime.datetime.now())


List comprehension
==================

* wykonywane natychmiast

.. code-block:: python

    [x*x for x in range(0, 30) if x % 2]

Generator expressions
=====================

* lazy evaluation

.. code-block:: python

    (x*x for x in range(0, 30) if x % 2)

List comprehension vs. Generator expressions
============================================
.. code-block:: python

    print('List Comprahension')

    # tutaj nastąpi wykonanie i przypisanie
    nieparzyste_list_comp = [x * x for x in range(0, 30) if x % 2]

    print(nieparzyste_list_comp)
    # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841]

    print(nieparzyste_list_comp)
    # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841]

.. code-block:: python

    print('\nGenerator Expression')

    # tu nastąpi tylko przypisanie do generatora
    nieparzyste_generator = (x * x for x in range(0, 30) if x % 2)

    print(list(nieparzyste_generator))  # tu dopiero nastąpi wywołanie
    # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841]

    # tu już generator jest pusty
    print(list(nieparzyste_generator))
    # []



Operator ``yield``
==================

.. code-block:: python

    osoby_w_klasie = [
        {'username': 'ivan-ivanovic', 'czy_wykladowca': True},
        {'username': 'max-peck', 'czy_wykladowca': False},
        {'username': 'jose-jimenez', 'czy_wykladowca': False},
    ]


    def uczestnicy_kursu_lista():
        uczniowie = []

        for osoba in osoby_w_klasie:
            if not osoba.get('czy_wykladowca'):
                uczen = osoba.get('username')
                uczniowie.append(uczen)

        return uczniowie


    for uczestnik in uczestnicy_kursu_lista():
        print('certyfikat dla', uczestnik)

.. code-block:: python

    osoby_w_klasie = [
        {'username': 'ivan-ivanovic', 'czy_wykladowca': True},
        {'username': 'max-peck', 'czy_wykladowca': False},
        {'username': 'jose-jimenez', 'czy_wykladowca': False},
    ]

    def uczestnicy_kursu_yield():
        for osoba in osoby_w_klasie:
            if not osoba.get('czy_wykladowca'):
                yield osoba.get('username')


    for uczestnik in uczestnicy_kursu_yield():
        print('certyfikat dla', uczestnik)


.. code-block:: python

    osoby_w_klasie = [
        {'username': 'ivan-ivanovic', 'czy_wykladowca': True},
        {'username': 'max-peck', 'czy_wykladowca': False},
        {'username': 'jose-jimenez', 'czy_wykladowca': False},
    ]


    def uczestnicy_kursu(osoby):
        def jest_wykladowca(user):
            if user['czy_wykladowca']:
                return True
            else:
                return False

        for osoba in osoby:
            if not osoba['czy_wykladowca']:
                yield {
                    'wykladowcy': jest_wykladowca,
                    'uczestnicy': [x for x in osoby if not x['czy_wykladowca']],
                    'wszystkie_username': [x['username'] for x in osoby]
                }


    uczestnicy_kursu = [osoba.get('username') for osoba in osoby_w_klasie if not osoba['czy_wykladowca']]
    pprint(uczestnicy_kursu)

Przykłady
=========

Przykładowe inicjalizacje generatorów
-------------------------------------

.. code-block:: python

    a = [x for x in range(0, 30)]
    b = (x for x in range(0, 30))
    c = {x for x in range(0, 30)}
    d = list(x for x in range(0, 30))
    e = tuple(x for x in range(0, 30))
    f = set(x for x in range(0, 30))

    print(list(x for x in range(0, 30)))

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
Napisz program, który wczyta plik :numref:`listing-file-etc-passwd-2`, a następnie:

* przefiltruje linie, tak aby nie zawierały komentarzy (zaczynające się od ``#``) oraz pustych linii
* przefiltruje linie, aby wyciągnąć konta systemowe - użytkowników, którzy mają UID (trzecie pole) mniejsze niż 1000
* zwróci listę loginów takich użytkowników

* Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję.
* Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``.

* Porównaj wyniki jednego i drugiego rozwiązania przez użycie ``sys.getsizeof()``

.. literalinclude:: src/etc-passwd.txt
    :name: listing-file-etc-passwd-2
    :language: python
    :caption: ``/etc/passwd`` sample file
