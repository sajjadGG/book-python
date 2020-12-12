.. _Dragon Beta:

*********************
Dragon (version beta)
*********************

.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

* Assignment: Dragon (version beta)
* Complexity: medium
* Lines of code: 120 lines
* Time: 60 min (±10 min), then 30 min live coding with instructor
* Filename: :download:`assignments/dragon_beta.py`
* Warning: Don't delete code, assignment will be continued

English:
    .. todo:: English Translation

Polish:
    1. Zaimportuj smoka z poprzedniej części zadania ("Part 1")
    2. Wykorzystaj mechanizm dziedziczenia dla Smoka
    3. Nie modyfikuj klasy smoka z poprzedniej części
    4. Smok nie może wyjść poza obszar ekranu (1024x768) + napisz ``doctest``
    5. Jeżeli dojdzie do granicy ekranu, to przesuwając dalej, pozycja będzie ustawiona na maks
    6. Zmień smokowi punkty życia na losowy ``int`` z zakresu 100 do 150
    7. Stwórz bohatera "Jan Twardowski":

        a. losowe punkty życia (200-250)
        b. zadaje losowe obrażenia (1-15)
        c. klasa postaci (domyślnie "Warrior")
        d. Bohater może przyjmować obrażenia
        e. Bohater może zginąć
        f. Bohater może poruszać się po planszy

    8. Wszystkie istoty mają statusy:

        a. "Full Health" - gdy punkty życia 100% (zastąp status "alive")
        b. "Injured" - gdy punkty życia 99% - 75%
        c. "Badly Wounded" - gdy punkty życia 74% - 25%
        d. "Near Death" - gdy punkty życia 24% - 1%
        e. "Dead" - gdy punkty życia poniżej lub równe 0%

    9. Bohater przejmuje złoto smoka, jeżeli go zabije
    10. Przeprowadź walkę, tak długo aż ktoś pierwszy nie zginie
    11. Jeżeli konieczne jest wprowadzenie nowej metody, klasy lub pól to należy to zrobić

Hints:
    * Aby zaimportować trzeba najpierw w katalogu stworzyć pusty plik ``__init__.py``
