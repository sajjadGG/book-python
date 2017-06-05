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

.. code-block:: python

    def ehlo_world():
        """
        >>> ehlo_world()
        'ehlo world'
        """
        napis = 'ehlo world'
        return napis

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

.. code-block:: python

    WIEK_PELNOLETNOSCI = 21


    def pelnoletni(wiek):
        """
        >>> pelnoletni(2)
        False

        >>> pelnoletni(30)
        True
        """
        if wiek < WIEK_PELNOLETNOSCI:
            return False
        else:
            return True


.. code-block:: python

    def wyswietl(tekst):
        """
        >>> wyswietl('hej')
        hej

        >>> wyswietl('hej hej')
        hej hej
        """
        print(tekst)


.. code-block:: python

    def wyswietl(tekst):
        """
        >>> wyswietl('hej')
        hej
        hej
        hej
        hej
        hej
        <BLANKLINE>
        """
        print(f'{tekst}\n' * 5)


.. code-block:: python

    def sumowanie_liczb(a, b):
        """Funkcja sumuje dwie liczby podane jako argumenty:

        >>> sumowanie_liczb(1, 2)
        3

        >>> sumowanie_liczb(-1, 1)
        0

        >>> sumowanie_liczb(0, 0)
        0

        >>> sumowanie_liczb([1, 2])
        Traceback (most recent call last):
            ...
        TypeError: sumowanie_liczb() missing 1 required positional argument: 'b'
        """
        return a + b
