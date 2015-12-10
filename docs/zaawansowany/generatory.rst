*******************************
Generatory i list comprehension
*******************************


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


Operator ``yield``
==================

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
