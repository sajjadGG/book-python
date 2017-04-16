****************************
Stałe, zmienne i typy danych
****************************

Stałe i zmienne
===============

Deklarowanie zmiennych
----------------------

.. code-block:: python

    my_variable = 10
    my_variable = 'ehlo world'

Deklarowanie stałych
--------------------

.. code-block:: python

    MY_CONSTANT = 10
    MY_CONSTANT = 'ehlo world'

Różnica między stałymi i zmiennymi
----------------------------------

Jedyną różnicą jest konwencja nazewnicza:

* stałe zapisujemy dużymi literami
* zmienne zapisujemy małymi literami

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

    >>> age = 10

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

    >>> name1 = 'Matt'
    'Matt'

    >>> name2 = "Matt"
    'Matt'

    >>> print("""
    ... Matt
    ... """)
    '\nMatt\n'

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


Pojedynczy czy podwójny cudzysłów
---------------------------------

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

* ``True``
* ``False``

Zwróć uwagę na wielkość liter!

``bool()`` to także funkcja wbudowana w język Python, która zwraca wartość logiczną wyrażenia.

``None`` - Wartość pusta
------------------------

Ważne: nie jest to wartość ``False`` ani ``0``.
Wyobraź sobie, że masz bazę danych z użytkownikami.
Gdy użytkownik nie poda wieku, to jest to wartość ``None``.

.. code-block:: python

    wiek = None

    if not wiek:
        print('użytkownik nie podał wieku')


Zbiory
======

``tuple`` - Krotka
------------------

.. code-block:: python

    a = (1, 2, 3)
    a = tuple(1, 2, 3)

.. code-block:: python

    >>> def return_arguments(a, b):
    ...    return (a, b)

    >>> out = return_arguments(10, 20)
    >>> print(out)
    (10, 20)


``list`` - Lista
----------------

.. code-block:: python

    my_list = []
    my_list = list()
    my_list = [1, 2, None, False, 'hej']

.. code-block:: python

    >>> my_list = [1, 2, None, False, 'hej']
    >>> my_list[2]
    None

``set`` - Zbiór
---------------

.. code-block:: python

    >>> a = set([1, 3, 1])
    >>> a
    {1, 3}

``dict`` - Słownik
------------------

.. code-block:: python

    my_data = {
        "imie": "Mateusz",
        "nazwisko": 'Harasymczuk',
        'wiek': 10,
    }

    print(my_data['nazwisko'])

Dobieranie się do wartości elementów
====================================

``[...]`` i ``.get(...)``
-------------------------

.. code-block:: python

    >>> dane = {'imie': 'Jan', 'nazwisko': 'Kowalski'}

    >>> dane['nazwisko']
    'Kowalski'

    >>> dane.get('nazwisko')
    'Kowalski'

    >>> dane['wiek']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'wiek'

    >>> dane.get('wiek')

    >>> dane.get('wiek', 'n/d')
    'n/d'

Złożone typy danych
===================

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

.. code-block:: python

    array = [
        [0, 1, 2],
        [1, 2, 3],
    ]

Mieszane typy
-------------

.. code-block:: python

    array = [
        [0, 1, 2],
        (1, 2, 3),
        set([1, 3, 1]),
        {'imie': 'Jan', 'nazwisko': 'Kowalski'}
    ]

Jak inicjować poszczególne typy?
================================

- ``list()`` czy ``[]``
- ``tuple()`` czy ``()``
- ``dict()`` czy ``{}``
- ``set()`` czy ``{}``
