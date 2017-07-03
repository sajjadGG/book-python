.. _Programowanie obiektowe:

***********************
Programowanie obiektowe
***********************

Paradygmat Obiektowy
====================

Dziedziczenie
-------------

.. code-block:: python

    class Pojazd:
        marka = None
        kierowca = None
        kola = 4

    class Samochod(Pojazd):
        marka = None
        kierowca = {'imie': 'José', 'nazwisko': 'Jiménez'}

    class Motor(Pojazd):
        marka = 'honda'
        kola = 2

Wielodziedziczenie
------------------

.. code-block:: python

    class Pojazd:
        marka = None

    class Samochod(Pojazd):
        marka = None
        kierowca = {'imie': 'José', 'nazwisko': 'Jiménez'}

    class Jeep(Samochod):
        marka = 'jeep'

    class Star(Samochod):
        marka = 'star'

Kompozycja
----------

.. code-block:: python

    class OtwieralneSzyby:
        def otworz_szyby(self):
            raise NotImplementedError


    class OtwieralnyDach:
        def otorz_dach(self):
            raise NotImplementedError


    class UmieTrabic:
        def zatrab(self):
            print('\bbiip')


    class Pojazd:
        kola = None


    class Samochod(Pojazd, UmieTrabic, OtwieralneSzyby):
        kola = 4

        def wlacz_swiatla(self, *args, **kwargs):
            print('włączam światła')


    class Cabrio(Samochod, OtwieralnyDach):
        def wlacz_swiatla(self, *args, **kwargs):
            print('Podnieś obudowę lamp')
            print('Puść muzyzkę')
            super(Cabrio, self).wlacz_swiatla(*args, **kwargs)
            print('Zatrąb')


    class Motor(Pojazd, UmieTrabic):
        kola = 2


    c = Cabrio()
    c.wlacz_swiatla()


.. code-block:: python


    class OtwieralnyDach:
        def otworz_dach(self):
            pass

        def zamknij_dach(self):
            pass


    class Trabi:
        def zatrab(self):
            raise NotImplementedError



    class Pojazd:
        kola = None


    class Samochod(Pojazd):
        kola = 4


    class Motor(Pojazd, Trabi):
        kola = 2

        def zatrab(self):
            print('biip')


    class Cabriolet(Samochod, OtwieralnyDach, Trabi):
        def zatrab(self):
            print('tru tu tu tu')


    class Mercedes(Samochod, OtwieralnyDach, Trabi):
        pass


    class Maluch(Samochod, Trabi):
        pass





Dziedziczenie czy kompozycja?
-----------------------------

* Kompozycja ponad dziedziczenie!

Polimorfizm
-----------

.. code-block:: python

    >>> class Pojazd:
    ...    def zatrab(self):
    ...        raise NotImplementedError
    ...
    >>> class Motor(Pojazd):
    ...     def zatrab(self):
    ...         print('bip')
    ...
    >>> class Samochod(Pojazd):
    ...     def zatrab(self):
    ...         print('biiiip')
    ...
    >>> obj = Motor()
    >>> obj.zatrab()
    >>>
    >>> obj = Samochod()
    >>> obj.zatrab()


Klasy abstrakcyjne
------------------

Składnia
========

Klasy
-----

.. code-block:: python

    class Samochod:
        def __init__(self, marka, kola=4):
            self.marka = marka
            self.kola = kola

    auto = Samochod(marka='mercedes', kola=3)
    print(auto.kola)


Metody
------

``self``
--------

Pola klasy
----------

.. code-block:: python

    import logging


    class Samochod:
        kola = 4
        marka = None

        def set_marka(self, marka):
            logging.warning('Ustawiamy marke')
            self.marka = marka

        def get_marka(self):
            return self.marka


    mercedes = Samochod()
    mercedes.set_marka('Mercedes')
    print(mercedes.get_marka())


    maluch = Samochod()
    maluch.marka = 'Maluch'
    print(maluch.marka)


    maluch = Samochod(marka='Maluch')
    print(maluch.marka)


Konstruktor
-----------

.. code-block:: python

    import logging


    class Samochod:
        kierowca = None

        def __init__(self, marka, kola=4):
            logging.warning('inicjalizujemy obiekt %s', marka)
            self.marka = marka
            self.kola = kola


    sam1 = Samochod(marka='Maluch')
    print(sam1.marka)
    print(sam1.kola)

    print(dir(sam1))
    print(sam1.__dict__)


    sam2 = Samochod(marka='Merc')
    print(sam2.marka)
    print(sam2.kola)




``super()``
-----------

.. code-block:: python

    class Human:
        def __init__(self, name='human'):
            self.name = name

        def my_name(self):
            print(self.name)


    class Man(Human):
        def __init__(self, name='man'):
            self.name = name

        def my_parent(self):
            name = super().name
            print(name)


``@property`` i ``@x.setter``
-----------------------------

.. code-block:: python

    class Cls:
        def __init__(self):
            self._x = None

        @property
        def x(self):
            """I'm the 'x' property."""
            return self._x

        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self):
            del self._x

``@staticmethod``
-----------------

``__str__()``
-------------

.. code-block:: python

    class Samochod:
        def __init__(self, marka, kola=4):
            self.marka = marka
            self.kola = kola

        def __str__(self):
            return f'Marka: {self.marka} i ma {self.kola} koła'

            # For Python < 3.6
            # return 'Marka: {marka} i ma {kola} koła'.format(**self.__dict__)


    auto = Samochod(marka='mercedes', kola=3)
    print(auto)

``__repr__()``
--------------
.. code-block:: python

    class Samochod:
        def __init__(self, marka, kola=4):
            self.marka = marka
            self.kola = kola

        def __repr__(self):
            return f'Marka: {self.marka} i ma {self.kola} koła'


    auta = [
        Samochod(marka='mercedes', kola=3),
        Samochod(marka='maluch', kola=4),
        Samochod(marka='fiat', kola=4),
    ]

    print(auta)


Metaclass
---------


Przeciążanie operatorów
=======================

``__eq__()``
------------

``__ne__()``
------------

``__lt__()``
------------

``__le__()``
------------

``__gt__()``
------------

``__ge__()``
------------


Dobre praktyki
==============

Ask don't tell
--------------

Inicjalizacja parametrów
------------------------

Private, public? konwencja ``_`` i ``__``
-----------------------------------------

Co powinno być w klasie a co nie?
---------------------------------

.. code-block:: python

    class Osoba:
        wiek = 10

        def __init__(self, imie):
            self.imie = imie

        @staticmethod
        def powiedz_hello():
            print('hello')


    Osoba.powiedz_hello()
    print(Osoba.wiek)


    o = Osoba(imie='Ivan')
    o.powiedz_hello()
    print(Osoba.wiek)


Klasa per plik?
---------------

Przykłady praktyczne
====================

.. code-block:: python

    >>> class Osoba:
    ...    nazwisko = 'Jiménez'
    ...
    ...    def __init__(self, imie):
    ...        self.imie = imie

    >>> o1 = Osoba('Jose')
    >>> o2 = Osoba('Ivan')


    >>> print(o1.nazwisko)
    Jiménez

    >>> print(o2.nazwisko)
    Jiménez



    >>> o1.nazwisko = 'Ivanovic'

    >>> print(o1.nazwisko)
    Ivanovic

    >>> print(o2.nazwisko)
    Jiménez



    >>> Osoba.nazwisko = 'Peck'

    >>> print(o1.nazwisko)
    Ivanovic

    >>> print(o2.nazwisko)
    Peck



Zadania kontrolne
=================

Książka adresowa
----------------

:Zadanie 1:
    Zmień swój kod zadania z książką adresową, aby każdy z kontaktów był reprezentowany przez:

        * imię
        * nazwisko
        * telefon
        * adresy:

            * ulica
            * miasto
            * kod_pocztowy
            * wojewodztwo
            * panstwo

    * Wszystkie dane w książce muszą być reprezentowane przez klasy.
    * Klasa osoba powinna wykorzystywać domyślne argumenty w ``__init__``.
    * Użytkownik może mieć wiele adresów.
    * Klasa adres powinna mieć zmienną liczbę argumentów za pomocą ``**kwargs`` z domyślnymi wartościami.
    * Zrób tak, aby się ładnie wyświetlało. Zarówno dla jednego wyniku (``print(adres)``, ``print(osoba)`` jak i dla wszystkich w książce ``print(ksiazka_adresowa)``.
    * API programu powinno być tak jak na listingu poniżej

    .. code-block:: python

        ksiazka_adresowa = [
            Kontakt(imie='Max', nazwisko='Peck', adresy=[
                Adres(ulica='...', miasto='...'),
                Adres(ulica='...', miasto='...'),
                Adres(ulica='...', miasto='...'),
            ]),
            Kontakt(imie='José', nazwisko='Jiménez'),
            Kontakt(imie='Иван', nazwisko='Иванович', adresy=[]),
        ]

:Zadanie 2:
    Napisz książkę adresową, która będzie zapisywała a później odczyta i sparsuje dane do pliku w formacie Pickle.

:Zadanie 3:
    Napisz książkę adresową, która będzie zapisywała a później odczyta i sparsuje dane do pliku w formacie JSON.

:Podpowiedź:
    * Dane w formacie Pickle muszą być zapisane do pliku binarnie
    * ``pickle.loads()`` przyjmuje uchwyt do pliku, a nie jego zawartość
