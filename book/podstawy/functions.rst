.. _Funkcje:

*******
Funkcje
*******

Funkcje pozwalają na wielokrotne używanie tego samego kodu. Znacznie poprawiają także czytelność kodu i go porządkują.

Definiowanie funkcji
====================
.. code-block:: python

    def hello():
        print('hello world')

Konwencja nazewnicza funkcji
============================
#. Nie robimy CamelCase
#. Używanie ``_`` w nazwach (snake_case)
#. Funkcje o nazwie zaczynającej się od ``_`` przez konwencję są traktowane jako prywatne (w Pythonie nie ma private/protected/public).
#. Funkcje o nazwie zaczynającej się od ``__`` i kończących się na ``__`` przez konwencję są traktowane jako systemowe.
#. Nazwy opisowe funkcji
#. ``print_()``
#. ``__nazwa_funkcji()``

Zwracanie wartości
==================
#. Słowo kluczowe ``return`` wskazuje funkcji jaką wartość ma dana funkcja zwrócić.
#. Wykonanie linii ze słowem kluczowym ``return`` kończy wykonywanie funkcji.

.. code-block:: python

    def sum(a, b):
        return a + b

    sum(2, 3)
    # 5

Zwracanie wartości prostych
---------------------------
.. code-block:: python

    def zwracanie_stringow():
        return 'José Jiménez'

    def zwracanie_bool():
        return True

    def zwracanie_wartosci_pustej():
        return None

    def zwracanie_niejawne():
        # Python always return something, in this case ``return None``
        pass

    def zwracanie_dict():
        return {'imie': 'José', 'nazwisko': 'Jiménez'}

    def zwracanie_tupli_1():
        return 1, 'foobar'

    def zwracanie_tupli_2():
        return (5, 10, 15, 'foobar')

    def zwracanie_listy():
        return [1, 2.5, 'foobar']

Zwracanie typów złożonych
-------------------------
.. code-block:: python

    def zwracanie_zlozone():
        return [
            {'imie': 'Max', 'nazwisko': 'Peck'},
            {'imie': 'Иван', 'nazwisko': 'Иванович'},
            {'imie': 'José', 'nazwisko': 'Jiménez'},
        ]

Zwracanie funkcji
-----------------
.. code-block:: python

    def returns_str():
        return 'José Jiménez'

    def returns_callable():
        return returns_str


    my_data = returns_callable()
    # <function __main__.returns_str()>

    my_data()
    # 'José Jiménez'

Przykład z życia:
.. code-block:: python

    import datetime

    print(datetime.datetime.now())

    now = datetime.datetime.now
    print(now())
    print(now())

    now = datetime.datetime.now()
    print(now)
    print(now)


Argumenty do funkcji
====================
Argumenty funkcji to wartości na których ta funkcja wykonuje operacje. W idealnym przypadku wartość wyjściowa funkcji powinna zależeć jedynie od jej argumentów.

.. code-block:: python

    def add(a, b):
        return a + b

    add(1, 2)
    # 3

Typowanie
---------
* Od Python 3.5

.. code-block:: python

    >>> def dodaj(a: int, b: float) -> float:
    ...    return float(a + b)

    >>> dodaj(1, 2.0)
    3.0

.. note:: więcej na ten temat w rozdziale dotyczącym :numref:`Type Annotation`

Nazwy argumentów
-----------------
Każdy argument ma swoją nazwę przez którą uzyskujemy dostęp do wartości argumentu w ciele funkcji. Ta nazwa może też być używana do przypisania wartości przy wywołaniu funkcji.

.. code-block:: python

    def substract(a, b):
        return a - b

    substract(a=0, b=1)
    # -1

    substract(0, b=1)
    # -1

    substract(b=1, a=0)
    # -1

    substract(1, 0)
    # 0

Argumenty z wartością domyślną
------------------------------
#. Argument funkcji może mieć wartość domyślną.
#. Funkcja przyjmie tą wartość jeżeli użytkownik nie zdefiniuje tego argumentu.
#. Argumenty z wartością domyślną muszą być skrajnie po prawej stronie.

.. code-block:: python

    def echo(text='default string'):
         print(text)

    echo('my string')
    # my string

    echo(text='my string')
    # my string

    echo()
    # default string

.. code-block:: python

    def server(username, password, host='127.0.0.1', port=80, ssl=True):
        print(f'host={host}, username={username}, password={password}, port={port}, ssl={ssl})


    # Kolejność ma znaczenie i łatwo się pomylić
    # Trudno również powiedzieć co znaczy ostatni parametr True
    server('admin', 'admin', 'localhost', 80, True)

    # argumenty definiowane są jawnie i trudniej się pomylić
    # kod jest bardziej przejrzysty
    # dla nazwanych argumentów kolejność nie ma znaczenia
    server(host='localhost', user='admin', password='admin', ssl=True)

    server(
        host='localhost',
        user='admin',
        password='admin',
        port=443,
        ssl=True,
    )

Rekurencja
==========
.. code-block:: python

    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

Zadania kontrolne
=================

Konwersja liczby na zapis słowny
--------------------------------
#. Napisz funkcję ``int_to_str``
#. Funkcja zamieni dowolego ``int`` lub ``float`` na formę tekstową.

    .. code-block:: python

        >>> int_to_str(1969)
        'one nine six nine'

        >>> int_to_str(31337)
        'three one three three seven'

        >>> int_to_str(13.37)
        'one three and three seven'

        >>> int_to_str(31.337)
        'three one and three three seven'

#. Wersja zaawansowana - pełne nazwy liczb

    .. code-block:: python

        >>> int_to_str(1969)
        'one thousand nine hundred sixty nine'

        >>> int_to_str(13.37)
        'thirteen and thirty seven hundredths'

:Założenia:
    * Nazwa pliku: ``functions-int-to-str.py``
    * Linii kodu do napisania: około 15 linii
    * Maksymalny czas na zadanie: 15 min

:Wymagania:
    * max 6 cyfr przed przecinkiem
    * max 5 cyfr po przecinku

:Co zadanie sprawdza?:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Przypadek zaawansowany: argumenty pozycyjne i domyślne
    * Rzutowanie i konwersja typów

Prosta memoizacja
-----------------
#. Napisz program, który obliczy silnię dla dowolnego ``int``
#. Program ma zapisać w ``dict`` o nazwie ``MEMOIZE`` wyniki funkcji dla poszczególnych parametrów (klucz to parametr, a wartość to wynik)
#. Przed uruchomieniem funkcji, musi sprawdzić czy wynik został już wcześniej obliczony

    - jeżeli tak, to zwraca dane z cache
    - jeżeli nie, to oblicza, aktualizuje cache a następnie zwraca wartość

#. Porównaj prędkość działania z obliczaniem na bieżąco dla parametru 500

:Założenia:
    * Nazwa pliku: ``functions-memoize.py``
    * Linii kodu do napisania: około 5 linii
    * Maksymalny czas na zadanie: 15 min

:Podpowiedź:
    .. code-block:: python

        def factorial(n: int) -> int:
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)

Rzymskie
--------
#. Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną.
#. Napisz drugą funkcję, która dokona procesu odwrotnego.

:Co zadanie sprawdza?:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Sprawdzanie czy element istnieje w ``dict``
    * Rzutowanie i konwersja typów

:Założenia:
    * Nazwa pliku: ``functions-roman.py``
    * Linii kodu do napisania: około 15 linii
    * Maksymalny czas na zadanie: 15 min