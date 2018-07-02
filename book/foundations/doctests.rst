*******
Doctest
*******

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

Testy dla wszystkich funkcji aktualnie zdefiniowanych w przestrzeni nazw wykonujemy wywołując funckję ``doctest.testmod()``.

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

.. code-block:: python

    def km_na_m(km: float) -> float:
        """
        >>> km_na_m(1)
        1000.0

        >>> km_na_m(2)
        2000.0

        >>> km_na_m(0)
        0.0

        >>> km_na_m(-1)
        1000.0

        >>> km_na_m("jeden")
        Traceback (most recent call last):
            ...
        ValueError: Argument must be int or float

        >>> km_na_m([0, 1, 2, 3])
        Traceback (most recent call last):
            ...
        ValueError: Argument must be int or float

        >>> km_na_m(object)
        Traceback (most recent call last):
            ...
        ValueError: Argument must be int or float

        >>> km_na_m(1.5)
        1500.0

        >>> km_na_m(-0.5)
        500.0

        >>> km_na_m(0.0)
        0.0
        """
        if not isinstance(km, (int, float)):
            raise ValueError('Argument must be int or float')

        return abs(km * 1000.0)

.. code-block:: python

    def say_hello(dt):
        """
        ta funkcja wypisuje hello na ekranie

        >>> import datetime
        >>> dt = datetime.datetime.now()
        >>> say_hello(dt)
        'hello'

        a gdyby uruchomić ją...
        """
        print('hello')


Assignments
===========

Konwersja temperatury
---------------------
#. Napisz funkcję, która przeliczy temperaturę podaną w Fahrenheit na Kelviny
#. Napisz testy do rozwiązania i pokryj przypadki:

    * temperatura ujemna
    * temperatura zero
    * temperatura dodatnia
    * temperatura ``float``
    * temperatura ``int``
    * lista temperatur
    * podany parametr to ``str``

:Podpowiedź:
    * Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
    * Celsius to Fahrenheit: (°C * 1.8) + 32 = °F
    * Jeden stopień Celsiusza odpowiada jednemu stopniowi w skali Kelvina
    * -273,15 °C = 0 K

:Założenia:
    * Nazwa pliku: ``doctest_temperature.py``
    * Szacunkowa długość kodu: około 6 linii
    * Maksymalny czas na zadanie: 5 min
