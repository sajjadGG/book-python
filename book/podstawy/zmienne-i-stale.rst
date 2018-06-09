.. _Stałe, zmienne i typy danych:

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

    >>> int(10.9)
    10

    >>> my_int = 1000000
    >>> my_int = 1_000_000
    >>> my_int = 1e6


``float`` - Liczba zmiennoprzecinkowa
-------------------------------------
``float`` w Pythonie reprezentuje liczbę zmiennoprzecinkową. Ciekawą własnością tego typu jest możliwość reprezentacji nieskończoności za pomocą ``Infinity`` oraz minus nieskończoności ``-Infinity``. Więcej szczegółów dostępnych jest w dokumentacji dla tego `typu <https://docs.python.org/3/library/functions.html#grammar-token-infinity>`_

Podobnie jak pozostałe typy ``float()`` jest funkcją, która konwertuje swój argument na liczbę zmiennoprzecinkową.

.. code-block:: python

    >>> float(10)
    10.0

    >>> float('+1.23')
    1.23

    >>> float('-1.23')
    -1.23

    >>> float('   -12345\n')
    -12345.0

    >>> float('1e-003')
    0.001

    >>> float('+1E6')
    1000000.0

    >>> float('-inf')
    >>> float('-Infinity')
    -inf

    >>> float('inf')
    >>> float('Infinity')
    inf

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

    >>> name1 = 'José'
    'José'

    >>> name2 = "Ivan"
    'Ivan'

    >>> print("""
    ... Max Peck
    ... """)
    '\nMax Peck\n'

    >>> str(10)
    '10'


Wprowadzanie znaków od użytkownika
----------------------------------
* Spacja na końcu prompt

.. code-block:: python

    name = input('Type your name: ')
    print(name)


Escape'owanie znaków
--------------------
.. code-block:: python

    '\n'
    '\r'
    '\r\n'

.. figure:: img/type-machine.jpg
    :scale: 50%
    :align: center

    Why we have '\r\n' on Windows?

.. code-block:: python

    """
    \xac
    \u7723
    \b123
    \t
    \'
    """

Znaki przed stringiem
---------------------
.. code-block:: python

    u'zażółć gęślą jaźń'
    r'(?P<foo>)\n' # escapes does not matters
    r'C:\Users\Admin\Desktop\foobar.txt'
    f'hello {first_name}, how are you?'
    b'this is text'


Niemutowalność
--------------
* Ważną cechą ciągów znakowych jest tzw. niemutowalność.
* Gdy wykonujemy operację na stringu tworzona jest jego nowa kopia.
* Zwóć uwagę ile stringów jest przechowywanych w pamięci

.. code-block:: python

    >>> name = 'José'
    >>> name += 'Jiménez'
    >>> print(name)
    José Jiménez


Pojedynczy czy podwójny cudzysłów
---------------------------------
* Python nie rozróżnia czy stosujemy pojedyncze znaki cudzysłowiu czy podwójne.
* Ważne jest aby wybrać jedną konwencję i się jej konsekwentnie trzymać.
* Interpreter Pythona domyślnie stosuje pojedyncze znaki cudzysłowia.
* Z tego powodu w tej książce będziemy trzymać się powyższej konwencji.

.. code-block:: python

    print('it\'s José\'s book')
    print("it's José's book")

.. code-block:: python

    print('<a href="http://python.astrotech.io">Python and Machine Learning</a>')

Operacje na stringach
---------------------
* ``split()``

.. code-block:: python

    >>> 'ehlo world'.split()
    ['ehlo', 'world']

    >>> text = 'ehlo,world'
    >>> text.split(',')
    ['ehlo', 'world']


* ``strip()``, ``lstrip()``, ``rstrip()``
    .. code-block:: python

        >>> name = '    Max Peck    '
        >>> name.strip()
        'Max Peck'
        >>> name.lstrip()
        'Max Peck    '
        >>> name.rstrip()
        '    Max Peck'

* ``startswith()``
    .. code-block:: python

        name = 'José Jiménez'

        if name.startswith('José'):
            print('My name José Jiménez')
        else:
            print('Noname')

* ``join()``
    .. code-block:: python

        >>> names = ['José', 'Max', 'Ivan', str(1961), '1969']
        >>> ';'.join(names)
        'José;Max;Ivan;1961;1969'


* ``title()``, ``lower()``, ``upper()``
    .. code-block:: python

        >>> name = 'joSé jiMénEz'

        >>> name.title()
        'José Jiménez'

        >>> name.upper()
        'JOSÉ JIMÉNEZ'

        >>> name.lower()
        'josé jiménez'
.. note:: bardzo przydatne do czyszczenia danych przed analizą lub Machine Learning

* ``replace()``
    .. code-block:: python

        >>> name = 'José Jiménez'
        >>> name.replace('J', 'j')
        'josé jiménez'


Wykonywanie operacji na obiekcie
--------------------------------
.. code-block:: python

    >>> text = 'Ehlo,world'

    >>> text.split(',')
    ['Ehlo', 'world']

    >>> str.split(text, ',')
    ['Ehlo', 'world']

    >>> str.split('Ehlo,world', ',')
    ['Ehlo', 'world']

Wycinanie części stringów
-------------------------
.. code-block:: python

    >>> text = 'Lorem ipsum'

    >>> text[2]
    'r'

    >>> text[:2]
    'Lo'

    >>> text[0:3]
    'Lor'

    >>> text[1:4]
    'ore'

    >>> text[-3]
    's'

    >>> text[-3:]
    'sum'

    >>> text[-3:-1]
    'su'

    >>> text[:-2]
    'Lorem ips'

``io``
------

``io`` to biblioteka do obsługi strumienia wejściowego i wyjściowego. StringIO jest wtedy traktowany jak plik wejściowy.

.. code-block:: python

    import io

    io.StringIO


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

    if wiek is None:
        print('użytkownik nie podał wieku')

    if not wiek:
        print('user does not ')


Zadania kontrolne
=================

Zmienne i typy
--------------
#. Napisz program, który poprosi użytkownika o imie i ładnie go przywita wyświetlając 'hello IMIE'.
#. Zamiast spacji użyj przecinka

:Podpowiedź:
    * Użyj podawania stringów po przecinku ``print(str, str)`` oraz parametru ``sep``
    * Użyj f-string formatting dla Python >= 3.6

.. note:: Pobaw się opcją w IDE:
    * Run in console
    * Debugger