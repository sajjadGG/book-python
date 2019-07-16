.. _OOP Basic:

*********
OOP Basic
*********


Access modifiers
================
* No protected i private
* All fields are always public
* ``_nazwa`` - private fields (by convention)
* ``__nazwa__`` - system methods
* ``nazwa_`` - used while name collision

.. code-block:: python
    :caption: ``_`` and ``__`` - Private, protected, public?!

    class Astronaut:
        first_name = ''     # public
        last_name = ''      # public
        _agency = None      # private

        def print_(self):   # avoid name collision with print
            print(self.__str__())

        def __str__(self):  # system function
            return f'My name... {self.name}'


``__dict__`` - Getting dynamic fields and values
================================================
.. code-block:: python
    :caption: ``__dict__`` - Getting dynamic fields and values

    class Iris:
        def __init__(self, sepal_length, sepal_width,
                     petal_length, petal_width, species):

            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

    flower = Iris(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2,
        species='setosa'
    )

    flower.__dict__
    # {'sepal_length': 5.1,
    # 'sepal_width': 3.5,
    # 'petal_length': 1.4,
    # 'petal_width': 0.2,
    # 'species': 'setosa'}


One class per file?
===================
* Osobne pliki - gdy klasy są duże
* Jeden plik - gdy klasy są małe i czytelne

.. code-block:: python
    :caption: Classes and Objects

    class IrisSetosa:
        pass

    class IrisVersicolor:
        pass

    class IrisVirginica:
        pass


    setosa = IrisSetosa()
    versicolor = IrisVersicolor()
    virginica = IrisVirginica()



Assignments
===========

Dragon (version alpha)
----------------------
* Filename: :download:`solution/basic_dragon_foundation.py` or :download:`solution/basic_dragon_advanced.py`
* Lines of code to write: 120 lines
* Estimated time of completion: 60 min (±15 min), then 60 min live coding with instructor
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif
    :scale: 100%
    :align: center

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

#. Zadanie jest specyfikacją wymagań biznesowych, a nie dokumentacją techniczną. tj. "co Smok ma robić, a nie jak to ma robić"
#. Smok ma:

    * nazwę
    * pozycję ``x`` na ekranie
    * pozycję ``y`` na ekranie
    * nazwę pliku tekstury, domyślnie ``img/dragon/alive.png``
    * punkty życia, domyślnie losowy ``int`` z zakresu od 50 do 100

#. Smok może:

    * być ustawiony w dowolne miejsce ekranu
    * zadawać komuś losowe obrażenia z przedziału od 5 do 20
    * otrzymywać obrażenia
    * być przesuwany o zadaną liczbę punktów w którymś z kierunków

#. Przyjmij górny lewy róg ekranu za punkt początkowy:

    * idąc w prawo dodajesz ``x``
    * idąc w lewo odejmujesz ``x``
    * idąc w górę odejmujesz ``y``
    * idąc w dół dodajesz ``y``

#. Jest to wersja ``alpha`` więc bez dodatkowych funkcjonalności
#. Przy każdym obrażeniu wypisz na ekranie nazwę Smoka, ilość obrażeń i pozostałe punkty życia
#. Kiedy punkty życia Smoka spadną do, lub poniżej zera:

    * Smok jest martwy
    * ustaw status obiektu na ``dead``
    * na ekranie ma pojawić się napis ``XXX is dead`` gdzie XXX to nazwa smoka
    * zmień nazwę pliku tekstury na ``img/dragon/dead.png``
    * na ekranie pojawi się informacja ile złota smok wyrzucił (losowa 1-100)
    * na ekranie pojawi się informacja o pozycji gdzie smok zginął
    * Nie można zadawać mu obrażeń
    * Smok nie może zadawać obrażeń
    * Smok nie może się poruszać

#. Przeprowadź grę:

    * Stwórz smoka w pozycji x=50, y=120 i nazwij go Wawelski
    * Ustaw nową pozycję na x=10, y=20
    * Przesuń smoka o 10 w lewo i 20 w dół
    * Przesuń smoka o 10 w lewo i 15 w prawo
    * Przesuń smoka o 15 w prawo i 5 w górę
    * Przesuń smoka o 5 w dół
    * Zadaj 10 obrażeń smokowi
    * Zadaj 5 obrażeń smokowi
    * Zadaj 3 obrażeń smokowi
    * Zadaj 2 obrażeń smokowi
    * Zadaj 15 obrażeń smokowi
    * Zadaj 25 obrażeń smokowi
    * Zadaj 75 obrażeń smokowi

#. Pozycja Smoka na końcu powinna być x=20, y=40
#. Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stały, klasy, obiekty, co tylko chcesz
#. Nie musisz trzymać się kolejności punktów i podpunktów w zadaniu
#. Nie przeglądaj kolejnych (przyszłych) części zadania. Zadanie jest symulacją pewnego procesu. Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę.

:The whys and wherefores:
    * "Smok" jest tylko narracją do demonstracji praktyk
    * myślenie obiektowe i odwzorowanie struktury w programie
    * tworzenie i praca z obiektami
    * zagnieżdżanie obiektów
    * specyfikacja interfejsów klas
    * interakcja między obiektami
    * podział aplikacji na warstwy
    * dobre praktyki programistyczne

:Hint:
    * ``from random import randint``
    * ``logging.debug()``

Bank i Bankomaty
----------------
* Filename: :download:`solution/basic_bank.py`
* Lines of code to write: 60 lines
* Estimated time of completion: 20 min

#. Klient może otworzyć konto w banku
#. Bank może mieć wiele kont dla różnych klientów
#. Każde konto ma unikalny numer, który jest generowany przy zakładaniu
#. Klient może odpytać o swój numer
#. Klient może wpłacić pieniądze na swoje konto
#. Klient może wybrać pieniądze z bankomatu
