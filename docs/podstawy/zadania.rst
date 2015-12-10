*******
Zadania
*******

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


Przeliczanie temperatury
========================

:Nazwa skryptu: ``bin/temperatura.py``
:Uruchamianie: ``python bin/temperatura.py``

:Zadanie:
    Woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach Fahrenheita. Napisz program, który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni). Pamiętaj o wyświetlaniu znaku plus/minus przy temperaturze. Oczywiście napisz testy do rozwiązania.

:Podpowiedź:
    * Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
    * Celsius to Fahrenheit: (°C * 1.8) + 32 = °F


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


``map()``, ``filter()`` i ``lambda``
====================================

:Nazwa skryptu: ``bin/funkcyjne.py``
:Uruchamianie: ``python bin/funkcyjne.py``

:Zadanie 1:
    Używając generatora zbuduj listę zawierającą wszystkie liczby podzielne przez 3 z zakresu od 1 do 33.

:Zadanie 2:
    * Używając funkcji ``filter()`` usuń z niej wszystkie liczby parzyste
    * Używając wyrażenia ``lambda`` i funkcji ``map()`` podnieś wszystkie elementy tak otrzymanej listy do sześcianu
    * Odpowiednio używając funkcji ``sum()``  i ``len()`` oblicz średnią arytmetyczną z elementów tak otrzymanej listy.


Zawartość pliku
===============

:Nazwa skryptu: ``bin/zawartosc-pliku.py``
:Uruchamianie: ``python bin/zawartosc-pliku.py``

:Zadanie 1:
    Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.

:Zadanie 2:
    Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.


Książka adresowa
================

:Nazwa skryptu: ``bin/ksiazka-adresowa.py``
:Uruchamianie: ``python bin/ksiazka-adresowa.py``

:Zadanie:
    Napisz książkę adresową, która będzie zapisywała dane do pliku w formacie json.
    Każdy z użytkowników jest reprezentowany przez:

    * imię
    * nazwisko
    * telefon
    * adres

     * ulica
     * miasto
     * kod_pocztowy
     * wojewodztwo
     * panstwo

    Wszystkie dane w książce muszą być reprezentowane przez typy proste.

:Zadanie 2:
    Bardzo często wykorzystywanym typem pliku jest CSV, czyli wartości oddzielone przecinkami. Zamień format pliku na ten typ. Zrób tak, aby dane trafiły do odpowiednich kolumn nawet po przesortowaniu. Użyj ``csv.DictWriter()``. Wszystkie pola muszą być zawsze w cudzysłowiach i oddzielone średnikami.

:Zadanie 3:
    Zmodyfikuj aby można było wpisywać wiele adresów.

:Zadanie 4:
    Zmodyfikuj program aby wykorzystywał klasy do reprezentowania wpisów w książce. Które podejście jest lepsze?

:Zadanie 5:
    Teraz wykorzystaj plik bazy danych sqlite aby trzymać informacje w tabeli. Które podejście jest lepsze?

:Zadanie 6:
    Wykorzystaj Django do stworzenia takiego modelu i wygeneruj panel administracyjny. Trudne?

:Pytanie:
    * Które podejście było najłatwiejsze?
    * W jakim formacie najlepiej przechowywać dane?
    * Które podejście jest najlepsze dla innych programistów, a które dla użytkowników?


Zbalansowanie nawiasów
======================

:Nazwa skryptu: ``bin/zbalansowanie-nawiasow.py``
:Uruchamianie: ``python bin/zbalansowanie-nawiasow.py``

:Zadanie 1:
    Napisz kod który sprawdzi zbalansowanie nawiasów, tzn. czy ilość otwieranych nawiasów jest równa ilości nawiasów zamykanych. Zwórć uwagę, że mogą być cztery typy nawiasów:

    * okrągłe: ``(`` i ``)``
    * kwadratowe: ``[`` i ``]``
    * klamrowe ``{`` i ``}``
    * trójkątne ``<`` i ``>``

:Zadanie 2:
    Rozbuduj poniższy zestaw testów i napisz funkcjonalność.

    .. code-block:: python

        >>> dane = "() [] () ([]()[])"
        >>> zbalansowanie_nawiasow(a)
        True
        >>> dane = "( (] ([)]"
        >>> zbalansowanie_nawiasow(a)
        False

:Zadanie 3:
    Spróbuj użyć rekurencji.
