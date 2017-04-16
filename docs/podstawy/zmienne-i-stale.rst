****************************
Stałe, zmienne i typy danych
****************************

Stałe i zmienne
===============

Deklarowanie zmiennych
----------------------

.. code-block:: python

    moja_zmienna = 10
    moja_zmienna = 'przykladowy tekst'

Deklarowanie stałych
--------------------

.. code-block:: python

    MOJA_STALA = 10
    MOJA_STALA = 'przykladowy tekst'

Różnica między stałymi i zmiennymi
----------------------------------

Zasięg widoczności
------------------

* ``globals()``
* ``locals()``

Numeryczne typy danych
======================

``int`` - Liczba całkowita
--------------------------

Jednym z najbardziej podstawowych typów danych jest ``int``.
``int()`` jest funkcją wbudowaną, która zamieni swój argument na liczbę całkowitą.

.. code-block:: python

    age = 10
    >>> int(10)
    10
    >>> int(10.0)
    10

``float`` - Liczba zmiennoprzecinkowa
-------------------------------------

``float`` w Pythonie reprezentuje liczbę zmiennoprzecinkową. Ciekawą własnością tego typu jest możliwość reprezentacji nieskończoności za pomocą ``Infinity`` oraz minus nieskończoności ``-Infinity``. Więcej szczegółów dostępnych jest w dokumentacji dla tego `typu <https://docs.python.org/3/library/functions.html#grammar-token-infinity>`_

Podobnie jak pozostałe typy ``float()`` jest funkcją, która konwertuje swój argument na liczbę zmiennoprzecinkową.

.. code-block:: python

    >>> float(10)
    10.0
    >>> float('+1.23')
    1.23
    >>> float('   -12345\n')
    -12345.0
    >>> float('1e-003')
    0.001
    >>> float('+1E6')
    1000000.0
    >>> float('-Infinity')
    -inf

``complex`` - liczba zespolona
------------------------------

``complex`` reprezentuje typ liczby zespolonej posiadającej część rzeczywistą oraz urojoną. Należy zwrócić uwagę, że argument powinien być ciągiem znaków niezawierającym spacji. W przeciwnym przypadku otrzymamy ``ValueError``.

.. code-block:: python

    >>> complex('1+2j')
    (1+2j)
    >>> complex('1 + 2j')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: complex() arg is a malformed string


Tekstowe typy danych
====================

``str`` - Ciąg znaków
---------------------

Obiekt typu ``str`` przechowuje łańcuch znaków. ``str()`` jest także funkcją, która zwraca ciąg znaków z argumentu.

.. code-block:: python

    name1 = 'Matt'
    name2 = "Matt"
    name3 = """
    Matt
    """
    >>> str(10)
    '10'

Escape'owanie znaków
--------------------
.. code-block:: python

    """
    \xac
    \u7723
    \n
    \b
    \r
    \t
    \'
    """


Niemutowalność
--------------

Ważną cechą ciągów znakowych jest tzw. niemutowalność. Gdy wykonujemy operację na stringu tworzona jest jego nowa kopia.


Różnica między ' a "
--------------------

Python nie rozróżnia czy stosujemy pojedyncze znaki cudzysłowiu czy podwójne.
Ważne jest aby wybrać jedną konwencję i się jej konsekwentnie trzymać.

Interpreter Pythona domyślnie stosuje pojedyncze znaki cudzysłowia, z tego powodu w tym materiale będziemy trzymać się tej konwencji.

Operacje na stringach
---------------------

* ``strip()``, ``lstrip()``, ``rstrip()``
* ``join()``
* ``startswith()``
* ``title()``
* ``replace()``
* Wycinanie części stringów

.. code-block:: python

    >>> text = "Lorem ipsum"

    >>> text[2]
    'r'

    >>> text[:2]
    'Lo'

    >>> text[0:3]
    'Lor'

    >>> text[-3]
    's'

    >>> text[-3:]
    'sum'

    >>> text[-3:-1]
    'su'

    >>> text[:-2]
    'Lorem ips'


Logiczne typy danych
====================

``bool`` - Wartość logiczna
---------------------------

Obiekt typu ``bool`` może przyjąć dwie wartości logiczne:

* True
* False

Zwróć uwagę na wielkość liter!

``bool()`` to także funkcja wbudowana w język Python, która zwraca wartość logiczną wyrażenia.

``None`` - Wartość pusta
------------------------

Złożone typy danych
===================

``tuple`` - Krotka
------------------

.. code-block:: python

    a = (1, 2, 3)
    a = tuple(1, 2, 3)

    def co_ci_dalem(a, b):
        return (a, b)

    a = co_ci_dalem(10, 20)

    print(a)


``list`` - Lista
----------------

``set`` - Zbiór
---------------

``dict`` - Słownik
------------------

.. code-block:: python

    my_data = {
        "imie": "Mateusz",
        "nazwisko": 'Harasymczuk',
        'wiek': 10,
    }

    print(my_data['nazwisko'])

.. code-block:: python

    student = {'imie': 'Matt', 'nazwisko': 'H'}
    print(student)

    # will rise an exception 'KeyError'
    for ocena in student['oceny']:
        print(ocena)

    # will return None
    for ocena in student.get('oceny'):
        print(ocena)

    # will return empty list
    for ocena in student.get('oceny', []):
        print(ocena)

    try:
        oceny = student['oceny']
    except KeyError:
        student['oceny'] = []
        oceny = []

    print(oceny)
    print(student)



Dobieranie się do wartości elementów
====================================

``[...]`` i ``.get(...)``
-------------------------

Rozszerzone typy danych
=======================

Lista słowników
---------------

.. code-block:: python

    studenci = [
        {'imie': 'Mateusz'},
        {'imie': 'Angelika', 'nazwisko': 'Nowak'},
        {'imie': 'Dawid', 'nazwisko': 'Kowalski'},
        {'imie': 'Piotr', 'nazwisko': None},
        {'imie': 'Grzegorz', 'programuje w': ['python', 'java', 'c/c++']},
    ]


    dane = studenci[0]['nazwisko']
    dane = studenci[0].get('nazwisko', 'n/d')
    dane = '\n'.join(studenci[4].get('programuje w'))
    print(dane)

Listy wielowymiarowe
--------------------

Drzewa
------

Jak inicjować poszczególne typy?
================================

- ``dict()`` czy ``{}``
- ``list()`` czy ``[]``
- ``tuple()`` czy ``()``
- ``set()`` czy ``{}``
