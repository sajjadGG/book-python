*******
Zadania
*******

Przeliczenia trygonometryczne
=============================

:Nazwa skryptu: ``bin/trygonometria.py``
:Uruchamianie: ``python bin/trygonometria.py``

:Zadanie:
    Napisz program, który wczyta od użytkownika wielkość kąta w stopniach i wyświetli wartość czterech podstawowych funkcji trygonometrycznych (sin, cos, tg, ctg) o ile dla danego kąta jest to możliwe.

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

Konwersja liczby na zapis słowny
================================

:Nazwa skryptu: ``bin/konwersja-liczby.py``
:Uruchamianie: ``python bin/konwersja-liczby.py``

:Zadanie 1:
    Napisz program ``numer.py``, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:

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


