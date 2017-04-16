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
        kierowca = {'imie': 'Matt', 'nazwisko': 'Harasymczuk'}

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
        kierowca = {'imie': 'Matt', 'nazwisko': 'Harasymczuk'}

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

Konstruktor
-----------

``super()``
-----------

.. code-block:: python

    class Human:
        def __init__(name='human')
            self.name = name

        def my_name(self):
            print(self.name)

    class Man(Human):
        def __init__(name='man')
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

``__str__()`` i ``__repr__()``
------------------------------

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
    print(str(auto))

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

Klasa per plik?
---------------
