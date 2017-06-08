*********
Operatory
*********

Lista operatorów
================

+------------+-------------------------+
| Operacja   | Znaczenie               |
+============+=========================+
| ``%``      | modulo (reszta)         |
+------------+-------------------------+
| ``**``     | potęga ``pow()``        |
+------------+-------------------------+
| ``\\``     | dzielenie bez reszty    |
+------------+-------------------------+
| ``<``      | mniejsze niż            |
+------------+-------------------------+
| ``+=``     | dodanie i przypisanie   |
+------------+-------------------------+
| ``<=``     | mniejsze lub równe      |
+------------+-------------------------+
| ``>``      | większe niż             |
+------------+-------------------------+
| ``>=``     | większe lub równe       |
+------------+-------------------------+
| ``==``     | równe                   |
+------------+-------------------------+
| ``!=``     | różne                   |
+------------+-------------------------+
| ``is``     | obiekty są tożsame      |
+------------+-------------------------+
| ``is not`` | obiekty nie są tożsame  |
+------------+-------------------------+
| ``in``     | obiekty są tożsame      |
+------------+-------------------------+
| ``not in`` | obiekty nie są tożsame  |
+------------+-------------------------+

Operacje na typach numerycznych
===============================

+---------------------+---------------------------------+
| Operacja            | Rezultat                        |
+=====================+=================================+
| ``x + y``           | suma *x* i *y*                  |
+---------------------+---------------------------------+
| ``x - y``           | różnica *x* i *y*               |
+---------------------+---------------------------------+
| ``x * y``           | iloczyn *x* i *y*               |
+---------------------+---------------------------------+
| ``x / y``           | iloraz *x* i *y*                |
+---------------------+---------------------------------+
| ``x // y``          | podłoga z ilorazu *x* i *y*     |
+---------------------+---------------------------------+
| ``x % y``           | reszta z dzielenia ``x / y``    |
+---------------------+---------------------------------+
| ``-x``              | *x* negacja                     |
+---------------------+---------------------------------+
| ``+x``              | *x* bez zmiany                  |
+---------------------+---------------------------------+
| ``abs(x)``          | wartość bezwzględna *x*         |
+---------------------+---------------------------------+
| ``int(x)``          | *x* przekonwertowane do int     |
+---------------------+---------------------------------+
| ``float(x)``        | *x* przekonwertowane do float   |
+---------------------+---------------------------------+
| ``complex(re, im)`` | liczba zespolona:               |
|                     | *re* - część rzeczywista        |
|                     | *im* - część urojona            |
+---------------------+---------------------------------+
| ``divmod(x, y)``    | para ``(x // y, x % y)``        |
+---------------------+---------------------------------+
| ``pow(x, y)``       | *x* podniesione do potęgi *y*   |
+---------------------+---------------------------------+
| ``x ** y``          | *x* do potęgi *y*               |
+---------------------+---------------------------------+


Kolejność operatorów
====================

* modulo
* ``//`` i ``**``
* przypisania i porównania
* ``+=``
* ``in`` i ``not in``





Zadania kontrolne
=================

Parzystość
----------

:Zadanie:
    * napisz program, który wczyta od użytkownika ciąg znaków
    * zweryfikuje czy wprowadzony ciąg jest liczbą (``int`` lub ``float``)
    * sprawdzi czy jest to liczba parzysta, czy nieparzysta

:Podpowiedź:
    * Liczba parzysta, to taka, która po podzieleniu przez dwa nie ma reszty
    * Użyj dzielenia modulo ``%`` lub ``divmod()``
    * Zwróć uwagę, że operator ``%`` działa modulo tylko na ``int`` oraz na ``float``. Przy ``str`` ma zupełnie inne znaczenie.

Przeliczenia trygonometryczne
-----------------------------
Napisz program, który wczyta od użytkownika wielkość kąta w stopniach i wyświetli wartość czterech podstawowych funkcji trygonometrycznych (sin, cos, tg, ctg) o ile dla danego kąta jest to możliwe.

Lotto
-----
Napisz program, który wyświetli 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.

:Podpowiedź:
    * ``random.randrange()``
    * ``random.sample()``

:Pytania:
    * Czym sa liczby pseudolosowe?
    * Czy da się stworzyć program czysto losowy?
    * Dlaczego?


Pole trójkąta
-------------
Napisz program, który obliczy pole trójkąta, pod warunkiem że użytkownik poda wysokość i długość podstawy tego trójkąta. Uwzględnij, że wysokość i długość podstawy mogą być liczbami niecałkowitymi. Wykorzystaj doctest do przetestowania funckji.


