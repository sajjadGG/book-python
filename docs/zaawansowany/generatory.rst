*******************************
Generatory i list comprehension
*******************************

Lazy evaluation
===============

.. code-block:: python

    import datetime

    now = datetime.datetime.now

    print(now())

    for i in range(0, 9999999):
        pow(i, 10)

    print(now())


List comprehension
==================

* wykonywane natychmiast

.. code-block:: python

    [x*x for x in range(0, 30) if x % 2]

.. code-block:: python

    >>> osoba = {'username': 'wykladowca1', 'czy_wykladowca': True}

    >>> out = {wartosc: klucz for klucz, wartosc in osoba.items()}

    >>> print(out)
    {'wykladowca1': 'username', True: 'czy_wykladowca'}

    >>> type(out)
    <class 'dict'>

    >>> out = {wartosc for klucz, wartosc in osoba.items()}

    >>> print(out)
    {'wykladowca1', True}

    >>> type(out)
    <class 'set'>

Generator expressions
=====================

* lazy evaluation

.. code-block:: python

    (x*x for x in range(0, 30) if x % 2)


Operator ``yield``
==================

.. code-block:: python

    osoby_w_klasie = [
        {'username': 'wykladowca1', 'czy_wykladowca': True},
        {'username': 'uczen1', 'czy_wykladowca': False},
        {'username': 'uczen2', 'czy_wykladowca': False},
        {'username': 'uczen3', 'czy_wykladowca': False},
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
        {'username': 'wykladowca1', 'czy_wykladowca': True},
        {'username': 'uczen1', 'czy_wykladowca': False},
        {'username': 'uczen2', 'czy_wykladowca': False},
        {'username': 'uczen3', 'czy_wykladowca': False},
    ]

    def uczestnicy_kursu_yield():
        for osoba in osoby_w_klasie:
            if not osoba.get('czy_wykladowca'):
                yield osoba.get('username')


    for uczestnik in uczestnicy_kursu_yield():
        print('certyfikat dla', uczestnik)


.. code-block:: python

    osoby_w_klasie = [
        {'username': 'wykladowca1', 'czy_wykladowca': True},
        {'username': 'uczen1', 'czy_wykladowca': False},
        {'username': 'uczen2', 'czy_wykladowca': False},
        {'username': 'uczen3', 'czy_wykladowca': False},
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

Reużywalność
============

.. code-block:: python

    nieparzyste_list_comp = [x*x for x in range(0, 30) if x % 2]
    print(nieparzyste_list_comp)
    print(nieparzyste_list_comp)

    print('------')

    nieparzyste_generator = (x*x for x in range(0, 30) if x % 2)
    print(list(nieparzyste_generator))
    print(list(nieparzyste_generator))

Przykład
========

.. code-block:: python

    a = [x for x in range(0, 30)]
    b = (x for x in range(0, 30))
    c = {x for x in range(0, 30)}
    d = list(x for x in range(0, 30))
    e = tuple(x for x in range(0, 30))
    f = set(x for x in range(0, 30))

    print(x for x in range(0, 30))


    ADDRESS_BOOK = [
        {'imie': 'Matt',
        'nazwisko': 'Harasymczuk',
        'ulica': 'Westpad',
        'miasto': 'Katwijk aan Zee',
        'kod_pocztowy': '2224',
        'wojewodztwo': 'Zuid-Holland',
        'panstwo': 'Netherlands'},

        {'imie': 'Angelika',
        'nazwisko': 'Jan',
        'ulica': 'Bial',
        'miasto': 'Warszawa',
        'kod_pocztowy': '02-370',
        'wojewodztwo': 'Mazowieckie',
        'panstwo': 'Polska'},
    ]

    osoby = [{'imie': x['imie'], 'nazwisko': x['nazwisko']} for x in ADDRESS_BOOK]
    print(osoby)


Przykład 2
==========

.. code-block:: python

    # List Comprehension
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


    # Generator Expressions
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


Zadania kontrolne
=================

``yield`` i ``/etc/passwd``
---------------------------

:Zadanie:
    * Przepisz program parsujący plik ``/etc/passwd`` aby wykorzystywał słówko kluczowe ``yield``.
