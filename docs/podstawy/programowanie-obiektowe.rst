***********************
Programowanie obiektowe
***********************


Paradygmat Obiektowy
====================

Dziedziczenie
-------------

Wielodziedziczenie
------------------

Kompozycja
----------

Dziedziczenie czy kompozycja?
-----------------------------

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


Polimorfizm
-----------

.. code-block:: python

    >>> class Pojazd:
    >>>    def zatrab(self):
    >>>        raise NotImplementedError
    >>>
    >>>
    >>> class Motor(Pojazd):
    >>>     def zatrab(self):
    >>>         print('bip')
    >>>
    >>>
    >>> class Samochod(Pojazd):
    >>>     def zatrab(self):
    >>>         print('biiiip')
    >>>
    >>>
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
