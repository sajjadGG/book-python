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

* CamelCase? Nie?! Używanie ``_`` w nazwach (snake_case)
* Funkcje o nazwie zaczynającej się od ``_`` przez konwencję są traktowane jako prywatne (w Pythonie nie ma private/protected/public).
* Funkcje o nazwie zaczynającej się od ``__`` i kończących się na ``__`` przez konwencję są traktowane jako systemowe.
* Nazwy opisowe funkcji
* ``nazwa_funkcji_()``
* ``__nazwa_funkcji()``

Argumenty do funkcji
====================
Argumenty funkcji to wartości na których ta funkcja wykonuje operacje. W idealnym przypadku wartość wyjściowa funkcji powinna zależeć jedynie od jej argumentów.

.. code-block:: python

    >>> def dodaj(a, b):
    ...    return a + b

    >>> dodaj(1, 2)
    3

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

    >>> def podziel(a, b):
    ...     return a / b

    >>> podziel(a=1, b=2)
    0.5

    >>> podziel(b=2, a=1)
    0.5


Argumenty z wartością domyślną
------------------------------
Argument funkcji może mieć także wartość domyślną, z której funkcja skorzysta jeżeli użytkownik nie zdefiniuje tego argumentu. Argumenty z wartością domyślną muszą być skrajnie po prawej stronie.

.. code-block:: python

    >>> def hello(tekst='hello world'):
    ...     print(tekst)

    >>> hello(tekst='ehlo')
    ehlo

    >>> hello()
    hello world

.. code-block:: python

    def server(host, user, password, port=1337):
        print(locals())


    # kolejność ma znaczenie
    # łatwo się pomylić
    server('localhost', 'admin', 'admin')

    # argumenty definiowane są jawnie
    # trudniej się pomylić
    # kod jest bardziej przejrzysty
    # dla nazwanych argumentów kolejność nie ma znaczenia
    server(host='localhost', user='admin', password='admin')

    server(
        host='localhost',
        user='admin',
        password='admin',
        port=31337,
    )

.. code-block:: python

    jira = Jira(
        url='http://localhost:8080',
        username='admin',
        password='admin',
        ssl_verify=False)

    # Zdecydowanie mniej czytelny zapis
    # Szczególnie nie wiadomo co False na koncu znaczy
    jira = Jira('http://localhost:8080', 'admin', 'admin', False)

Zwracanie wartości
==================

Zwracanie wartości prostych
---------------------------

.. code-block:: python

    def zwracanie_stringow():
        return 'Иван Иванович'

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
        return 10, 20.6, 30, 5, 'foobar'

    def zwracanie_tupli_2():
        return (10, 20.6, 30, 5, 'foobar')

    def zwracanie_listy():
        return [10, 20.6, 'foobar']

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

    def zwracanie_stringow():
        return 'Иван Иванович'

    def zwracanie_funkcji():
        return zwracanie_stringow

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

