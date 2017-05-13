*******
Zadania
*******

Zmienne i typy
==============

:Nazwa skryptu: ``bin/zmienne.py``
:Uruchamianie: ``python bin/zmienne.py``

:Zadanie:
    Napisz program, który poprosi użytkownika o imie i ładnie go przywita.

:Podpowiedź:
    * Użyj podawania stringów po przecinku ``print(str, str)``
    * Użyj f-string formatting z Python >= 3.6


Zmienne i wczytywanie ciągu od użytkownika
==========================================

:Nazwa skryptu: ``bin/pelnoletnosc.py``
:Uruchamianie: ``python bin/pelnoletnosc.py``

:Zadanie:
    Napisz program, który poprosi użytkownika o wiek i wyświetli wartość. Następnie sprawdzi pełnoletność i wyświetli informację czy osoba jest "dorosła" czy "niepełnoletnia".

Powielanie napisów
==================

:Nazwa skryptu: ``bin/zadanie1-powielanie-napisow.py``
:Uruchamianie: ``python bin/zadanie1-powielanie-napisow.py``

:Zadanie 1:
    Napisz program, który wczyta od użytkownika pewien napis, a następnie wyświetli 30 kopii tego napisu, każda w osobnej linii.

:Zadanie 2:
    Napisz trzy wersje tego programu:

    * wykorzystując ``range()``
    * wykorzystując pętlę ``while``
    * wykorzystując właściwości mnożenia stringów

:Zadanie 3:
    Napisz doctest do takiej funkcji.

:Podpowiedź:
    * ``print('ciag znakow' * 30)``


Przeliczanie temperatury
========================

:Nazwa skryptu: ``bin/temperatura.py``
:Uruchamianie: ``python bin/temperatura.py``

:Zadanie:
    Woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach Fahrenheita. Napisz program, który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni). Pamiętaj o wyświetlaniu znaku plus/minus przy temperaturze. Oczywiście napisz testy do rozwiązania.

:Podpowiedź:
    * Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
    * Celsius to Fahrenheit: (°C * 1.8) + 32 = °F
    * skorzystaj z funkcji ``range()``


Przeliczanie odległości
=======================

:Nazwa skryptu: ``bin/odleglosci.py``
:Uruchamianie: ``python bin/odleglosci.py``

:Zadanie:
    Napisz program który przekonwertuje odległości (podane w metrach) i zwróci ``dict``, zgodnie z szablonem:

    .. code-block:: python

        {
            'kilometers': int(),
            'miles': float(),
            'nautical miles': float(),
        }

:Podpowiedź:
    * 1000 m = 1 km
    * 1608 m = 1 mila
    * 1852 m = 1 mila morska


Parzystość
==========

:Nazwa skryptu: ``bin/zadanie2-parzystosc.py``
:Uruchamianie: ``python bin/zadanie2-parzystosc.py``

:Zadanie:
    * napisz program, który wczyta od użytkownika ciąg znaków
    * zweryfikuje czy wprowadzony ciąg jest liczbą (``int`` lub ``float``)
    * sprawdzi czy jest to liczba parzysta, czy nieparzysta

:Podpowiedź:
    * Liczba parzysta, to taka, która po podzieleniu przez dwa nie ma reszty
    * Użyj dzielenia modulo ``%`` lub ``divmod()``
    * Zwróć uwagę, że operator ``%`` działa modulo tylko na ``int`` oraz na ``float``. Przy ``str`` ma zupełnie inne znaczenie.


Liczby całkowite
================

:Nazwa skryptu: ``bin/zadanie3-calkowite.py``
:Uruchamianie: ``python bin/zadanie3-calkowite.py``

:Zadanie:
    Napisz program, który wczyta od użytkownika liczbę i wyświetli informację, czy jest to liczba całkowita, czy niecałkowita.

:Podpowiedź:
    Liczba całkowita to taka, której część dziesiętna nie występuje (``int``) lub jest równa zero ``float``.


Dzienniczek ucznia
==================

:Nazwa skryptu: ``bin/oceny.py``
:Uruchamianie: ``python bin/oceny.py``

:Zadanie:
    Napisz program, który wczytuje od użytkownika kolejne oceny i:

    * sprawdza czy wprowadzona ocena jest na liście dopuszczalnych na wydziale ocen
    * jeżeli ocena jest na liście dopuszczalnych na wydziale ocen, dodaje ją do dzienniczka
    * jeżeli wpisano cyfrę nie znjadującą się na liście dopuszczalnych ocen, wyświetl informację i zakończ wpisywanie
    * wyświetla wyliczoną dla dzienniczka ocen średnią arytmetyczną
    * jeżeli wciśnięto sam Enter, oznacza to koniec wpisywania do dzienniczka
    * wykorzystaj moduł statistics do wyliczania średniej

:Warunek:
    * Zastosuj akademicką skalę ocen ``[2, 3, 3.5, 4, 4.5, 5]``

:Podpowiedź:
    * dla ułatwienia wszystkie oceny mogą być typu ``float``
    * ``len()`` ``sum()``
    * ``in``
    * ``import statistics`` ``statistics.mean()``


Przeliczenia trygonometryczne
=============================

:Nazwa skryptu: ``bin/trygonometria.py``
:Uruchamianie: ``python bin/trygonometria.py``

:Zadanie:
    Napisz program, który wczyta od użytkownika wielkość kąta w stopniach i wyświetli wartość czterech podstawowych funkcji trygonometrycznych (sin, cos, tg, ctg) o ile dla danego kąta jest to możliwe.


Wyrazy
======

:Nazwa skryptu: ``bin/podzial-wyrazow.py``
:Uruchamianie: ``python bin/podzial-wyrazow.py``

:Zadanie:
    Napisz program, który wczyta od użytkownika pewien tekst, a następnie podzieli go na zdania (zakładamy, że jednoznacznie kropka rozdziela zdania) i dla każdego zdania wyświetli ile jest w nim wyrazów (zakładamy, że spacja oddziela wyrazy w zdaniu).

:Podpowiedź:

    * ``str.split()``
    * ``len()``

Lotto
=====

:Nazwa skryptu: ``bin/lotto.py``
:Uruchamianie: ``python bin/lotto.py``

:Zadanie:
    Napisz program, który wyświetli 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.

:Podpowiedź:
    * ``random.randrange()``
    * ``random.sample()``

:Pytania:
    * Czym sa liczby pseudolosowe?
    * Czy da się stworzyć program czysto losowy?
    * Dlaczego?


Pole trójkąta
=============

:Nazwa skryptu: ``bin/pole-trojkata.py``
:Uruchamianie: ``python bin/pole-trojkata.py``

:Zadanie:
    Napisz program, który obliczy pole trójkąta, pod warunkiem że użytkownik poda wysokość i długość podstawy tego trójkąta. Uwzględnij, że wysokość i długość podstawy mogą być liczbami niecałkowitymi. Wykorzystaj doctest do przetestowania funckji.


Wyliczanie średniej dla parametrów
==================================

:Nazwa skryptu: ``bin/srednia.py``
:Uruchamianie: ``python bin/srednia.py``

:Zadanie 1:
    Zdefiniuj funkcję ``avg()``, która dla dowolnej liczby parametrów zwróci ich średnią arytmetyczną (lub 0 dla 0 parametrów).

:Zadanie 2:
    Dowolna liczba parametrów podanych z linii poleceń.

:Podpowiedź:
    * ``getopt``
    * ``argparse``
    * ``docopt``

:Uruchamianie: ``python bin/srednia.py 5 10 100 32 -90 27.5``


Konwersja liczby na zapis słowny
================================

:Nazwa skryptu: ``bin/konwersja-liczby.py``
:Uruchamianie: ``python bin/konwersja-liczby.py``

:Zadanie 1:
    Napisz program "numer.py``", który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:

    * znaki nie będące cyframi mają być ignorowane
    * konwertujemy cyfry, nie liczby, a zatem:
      * 911 to "dziewięć jeden jeden"
      * 1100 to "jeden jeden zero zero"

:Zadanie 2:
    Napisz program, który przekonwertuje liczbę na zapis słowny, np.:

    .. code-block:: python

        >>> int_to_str(999)
        'dziewiećset dziewięćdziesiąt dziewięć'
        >>> int_to_str(127.32)
        'sto dwadzieścia siedem i trzydzieści dwa setne'

:Zakres:
    * 6 cyfr przed przecinkiem
    * 5 cyfr po przecinku

:Zadanie 3:
    Napisz testy sprawdzające przypadki brzegowe.


Rzymskie
========

:Nazwa skryptu: ``bin/rzymskie.py``
:Uruchamianie: ``python bin/rzymskie.py``

:Zadanie 1:
    Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną.

:Zadanie 2:
    Zrób drugą funkcję, która dokona procesu odwrotnego.


Zawartość pliku
===============

:Nazwa skryptu: ``bin/zawartosc-pliku.py``
:Uruchamianie: ``python bin/zawartosc-pliku.py``

:Zadanie 1:
    Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.

:Zadanie 2:
    Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.
