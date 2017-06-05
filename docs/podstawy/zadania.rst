*******
Zadania
*******

Przeliczenia trygonometryczne
=============================
Napisz program, który wczyta od użytkownika wielkość kąta w stopniach i wyświetli wartość czterech podstawowych funkcji trygonometrycznych (sin, cos, tg, ctg) o ile dla danego kąta jest to możliwe.

Lotto
=====
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
Napisz program, który obliczy pole trójkąta, pod warunkiem że użytkownik poda wysokość i długość podstawy tego trójkąta. Uwzględnij, że wysokość i długość podstawy mogą być liczbami niecałkowitymi. Wykorzystaj doctest do przetestowania funckji.

Konwersja liczby na zapis słowny
================================
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
:Zadanie 1:
    Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną.

:Zadanie 2:
    Zrób drugą funkcję, która dokona procesu odwrotnego.


