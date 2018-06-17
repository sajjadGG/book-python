***************
Primitive types
***************

Variables and Constants
=======================

Declaring variables
-------------------
.. code-block:: python

    my_variable = 10
    my_variable = 'ehlo world'

Declaring constants
-------------------
.. code-block:: python

    MY_CONSTANT = 10
    MY_CONSTANT = 'ehlo world'

Różnica między stałymi i zmiennymi
----------------------------------
* Jedyną różnicą jest konwencja nazewnicza
* Stałe zapisujemy dużymi literami
* Zmienne zapisujemy małymi literami

Typy
----
* Od Python 3.5 wprowadzono nową składnię
* Nowa składnia nie jest wymagana (ale jest dobrą praktyką)
* Nowa składnia uruchomiona w Python przed 3.5 rzuci SyntaxError
* Twórcy języka mówą, że typy nigdy nie będą wymagane
* Aby sprawdzić poprawność trzeba użyć bibliotek zewnętrznych tj: ``mypy`` lub ``pyre``
* Typy można znaleźć w wielu funkcjach w bibliotece standardowej
* Dobre IDE podpowiada typy i informuje o błędach

.. code-block:: python

    name: str = 'José Jiménez'
    age: int = 30

Inferencja typów
----------------
* Static Typing (Java, C++, Swift)

.. code-block:: java

    String name = new String("Jose Jimenez")

* Dynamic Typing (Python, PHP, Ruby)

.. code-block:: python

    name: str = str('Jose Jimenez')  # Type annotations
    name = str()

    # Type annotations (type hinting not forcing)
    # this will work, but IDE should warn
    name: str = 10

Numeryczne typy danych
======================

``int`` - Liczba całkowita
--------------------------
Jednym z najbardziej podstawowych typów danych jest ``int``.
``int()`` jest funkcją wbudowaną, która zamieni swój argument na liczbę całkowitą.

.. code-block:: python

    age = 10
    int(10)
    # 10

    int(10.0)
    # 10

    int(10.9)
    # 10

    my_int = 1000000
    my_int = 1_000_000
    my_int = 1e6

Minimum and maximum values for integers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:Python 3:
    In Python 3, this question doesn't apply. The plain int type is unbounded.

    However, you might actually be looking for the machine's word size. That's still available in Python 3 as ``sys.maxsize``.

    .. code-block:: python

        >>> import sys
        >>> sys.maxsize

:Python 2:
    In Python 2, the maximum value for plain int values is available as sys.maxint:

    .. code-block:: python

        >>> import sys
        >>> sys.maxint
        9223372036854775807

    You can calculate the minimum value with -sys.maxint - 1 as shown here.

Python seamlessly switches from plain to long integers once you exceed this value. So most of the time, you won't need to know what is the maximum value for ``int``.

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
.. code-block:: text

    \n
    \r
    \r\n

.. figure:: img/type-machine.jpg
    :scale: 50%
    :align: center

    Why we have '\\r\\n' on Windows?

.. code-block:: text

    🚀
    \x1F680
    \u1F680
    \b123
    \t
    \'

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

    name = 'José'
    name += 'Jiménez'
    print(name)
    # José Jiménez

Pojedynczy czy podwójny cudzysłów
---------------------------------
* Python nie rozróżnia czy stosujemy pojedyncze znaki cudzysłowiu czy podwójne.
* Ważne jest aby wybrać jedną konwencję i się jej konsekwentnie trzymać.
* Interpreter Pythona domyślnie stosuje pojedyncze znaki cudzysłowia.
* Z tego powodu w tej książce będziemy trzymać się powyższej konwencji.
* Ma to znaczenie przy ``doctest``, który zawsze korzysta z pojedynczych i rzuca errorem jak są podwójne

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
        print('user does not')


Assignments
===========

.. note:: Pobaw się opcjami w IDE:

    * Run in console
    * Run...
    * Debug...
    * Python Console

Zmienne i typy
--------------
#. Wczytaj od użytkownika imię
#. Użytkownik wprowadza tylko dane typu ``str``
#. Wyświetl na ekranie ``'My name "IMIE".\nI hope you\'re ok!'``, gdzie IMIE to wartość którą podał
#. Zwróć uwagę na cudzysłowia i nową linię
#. Podmień wszystkie spacje na ``_``
#. Nie korzystaj z dodawania stringów ``str + str``

:Założenia:
    * Nazwa pliku: ``type-print.py``
    * Linii kodu do napisania: około 2 linie
    * Maksymalny czas na zadanie: 5 min

:Podpowiedź:
    * Użyj podawania stringów po przecinku ``print(str, str)`` oraz parametru ``sep``
    * Użyj f-string formatting dla Python >= 3.6

User input and type casting
---------------------------
#. Użytkownik za pomocą wprowadza odległości w metrach
#. Użytkownik wprowadza tylko dane typu ``int`` lub ``float``
#. Napisz program który przekonwertuje odległości i wyświetli je w formacie ``dict`` zgodnie z szablonem:

.. code-block:: python

    print({
        'kilometers': int,
        'miles': float,
        'nautical miles': float,
        'all': [int, float, float]
    })

:Założenia:
    * Nazwa pliku: ``types-casting.py``
    * Linii kodu do napisania: około 3 linie
    * Maksymalny czas na zadanie: 5 min

:Podpowiedź:
    * 1000 m = 1 km
    * 1608 m = 1 mila
    * 1852 m = 1 mila morska

Wyrazy
------
#. Napisz program, który na podstawie paragrafu tekstu "Lorem Ipsum" podzieli go na zdania
#. Kropka rozdziela zdania
#. Spacja oddziela wyrazy w zdaniu
#. Dla każdego zdania wyświetli ile jest w nim wyrazów::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

:Założenia:
    * Nazwa pliku: ``type-split-text.py``
    * Linii kodu do napisania: około 3 linie
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza:
    * dzielenie stringów
    * sprawdzanie długości linii
    * iterowanie po elementach w tablicy

:Podpowiedź:
    * ``len(...)`` - Length of the list
    * .. code-block:: python

        lista = ['Element 1', 'Element 2']

        for element in lista:
            print(element)