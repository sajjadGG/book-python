Doctesty
========

Niezwykle użytecznym sposobem komentowania są tzw. doctesty. W wielolinijkowym komentarzu wpisujemy sesję z interpreterem a po uruchomieniu doctestów otrzymujemy informację czy nasza funkcja poprawnie się wykonuje. Jest to bardzo proste narzędzie, które poza samym pokazaniem jak działa funkcja, jakie parametry przyjmuje i co zwraca daje możliwość weryfikacji poprawności działania kodu. W tych materiałach nieraz będziemy korzystać z tego rozwiązania.

.. code-block:: python

    def sumowanie_liczb(a, b):
        """Funkcja sumuje dwie liczby podane jako argumenty:

        >>> sumowanie_liczb(1, 2)
        3
        >>> sumowanie_liczb(-1, 1)
        0
        >>> sumowanie_liczb(0, 0)
        0
        """
        return a + b

Wykorzystując taki zapis natychmiast widzimy co dzieje się w danym rozwiązaniu. Doctesty bardzo przydają się przede wszystkim do zastosowań wykorzystujących wyrażenia regularne, których zrozumienie zapisu często wymaga chwili zastanowienia.
