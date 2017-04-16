*******************
Wyrażenia regularne
*******************

Konstruowanie wyrażeń
=====================

Wyciąganie parametrów (zmiennych)
=================================

Najczęściej wykorzystywane funkcje
==================================

``match()``
-----------

``search()``
------------

``findall()`` i ``finditer()``
------------------------------

``compile()``
-------------

Greedy search
=============


Przykład
========

.. code-block:: python

    import re

    TEKST = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. -- Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC"""


    SLOWA_ZAWIERAJACE_IS = r'[a-zA-Z0-9]*is[a-zA-Z0-9]*'
    wynik = re.findall(SLOWA_ZAWIERAJACE_IS, TEKST)
    print(wynik)

    SLOWA_ZAWIERAJACE_IS = re.compile(r'[a-zA-Z0-9]*is[a-zA-Z0-9]*')
    SLOWA_ZAWIERAJACE_IS.findall(TEKST)
    print(wynik)

.. code-block:: python

    POPRAWNY_EMAIL = r'(^[a-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'


    def email_poprawny(email):
        if re.match(POPRAWNY_EMAIL, email):
            print('Poprawny:', email)
            return True
        else:
            print('Niepoprawny:', email)
            return False


    email_poprawny('Amatt@astrotech.io')
    email_poprawny('matt@astrotech.io')
    email_poprawny('+matt@astrotech.io')
    email_poprawny('matt+@astrotech.io')
    email_poprawny('mattastrotech@.io')
