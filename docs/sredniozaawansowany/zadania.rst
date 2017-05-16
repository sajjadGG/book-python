*******
Zadania
*******

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
