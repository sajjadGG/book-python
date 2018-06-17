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

Variables vs. Constants
-----------------------
* Jedyną różnicą jest konwencja nazewnicza
* Stałe zapisujemy dużymi literami
* Zmienne zapisujemy małymi literami

Types
-----
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

Type inference
--------------
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

Numerical types
===============

``int``
-------
* Liczba całkowita
* Funkcja ``int()`` kowertuje argument na ``int``
* W Python 3 ``int`` nie ma maksymalnej wartości (dynamicznie się rozszerza)

.. code-block:: python

    age = 30
    age: int = 30

    int(10)  # 10
    int(10.0)  # 10
    int(10.9)  # 10

    milion = 1000000
    milion = 1_000_000
    milion = 1e6

``float``
---------
* Liczba zmiennoprzecinkowa
* Funkcja ``float()`` konwertuje argument na ``float``

.. code-block:: python

    float(10)  # 10.0

    float('+1.23')  # 1.23
    float('-1.23')  # -1.23
    float('   -123.45\n')  # -123.45

    float('1e-003')  # 0.001
    float('+1E6')  # 1000000.0

    float('-inf')  # -inf
    float('-Infinity')  # -inf
    float('inf')  # inf
    float('Infinity')  # inf

``complex``
-----------
* Liczba zespolona (część rzeczywista i urojona)
* Notacja inżynierska ``j`` a nie matematyczna ``i``
* W ciągu nie może być spacji

.. code-block:: python

    complex('1+2j')  # (1+2j)
    complex('1 + 2j')  # ValueError: complex() arg is a malformed string


Character types
===============

``str``
-------
* Ciąg (łańcuch) znaków
* Funkcja ``str()`` konwertuje argument na ``str``

.. code-block:: python

    name = 'José'  # 'José'
    name = "José"  # 'José'
    name: str = 'José'  # 'José'

    str(1969)  # '1969'
    str(13.37)  # '13.37'

    name = """
        José Jiménez
        Max Peck
        Ivan Ivanovic
    """  # '\nMax Peck\nMax Peck\nIvan Ivanovic'

Single or double quote?
-----------------------
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

Escape characters
-----------------
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
    \x1F680  # after \x goes hexadecimal number
    \u1F680  # after \u goes four hexadecimal numbers
    \b1010   # after \b goes bytes
    \t
    \'

Characters before strings
-------------------------
.. code-block:: python

    f'hello {first_name}, how are you?'  # since Python 3.6
    u'zażółć gęślą jaźń'  # Used in Python 2, now doesn't have any effect
    r'(?P<foo>)\n'  # escapes does not matters
    r'C:\Users\Admin\file.txt'  # without ``r`` this have problems with \Users (invalid hex for unicode character)
    b'this is text'

Wprowadzanie znaków od użytkownika
----------------------------------
* Spacja na końcu prompt
* ``input()`` zawsze zwraca ``str``

.. code-block:: python

    name = input('Type your name: ')

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