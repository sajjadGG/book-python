.. _OOP Advanced:

************
OOP Advanced
************


``__new__()`` and ``__init__()``
================================
``__call__()`` method invokes the following:

    * ``__new__()``
    * ``__init__()``


``__new__()``
-------------
* the constructor
* solely for creating the object
* ``cls`` as it's first parameter
* when calling ``__new__()`` you actually don't have an instance yet, therefore no ``self`` exists at that moment

``__init__()``
--------------
* the initializer
* for initializing object with data
* ``self`` as it's first parameter
* ``__init__()`` is called after ``__new__()`` and the instance is in place, so you can use ``self`` with it
* it's purpose is just to alter the fresh state of the newly created instance

Example usage
-------------
.. code-block:: python
    :emphasize-lines: 3,4

    class A:
        def __new__(cls):
            print("A.__new__() called")
            return super().__new__(cls)

        def __init__(self):
            print("A.__init__() called")

    A()
    # A.__new__() called
    # A.__init__() called

Missing ``return`` from constructor
-----------------------------------
.. code-block:: python
    :emphasize-lines: 3

    class B:
        def __new__(cls):
            print("B.__new__() called")

        def __init__(self):
            print("B.__init__() called")  # -> is actually never called

    print B()
    # B.__new__() called
    # None

The instantiation is evaluated to ``None`` since we don't return anything from the constructor.

Return invalid from constructor
-------------------------------
.. code-block:: python
    :emphasize-lines: 4

    class C:
        def __new__(cls):
            print("C.__new__() called")
            return 29

    print C()
    # C.__new__() called
    # 29

Return invalid from initializer
-------------------------------
.. code-block:: python
    :emphasize-lines: 4

    class D:
        def __init__(self):
            print("C.__new__() called")
            return 33

    D()
    # TypeError: __init__ should return None

Why?
----
* Factory method
* Could be used to implement Singleton

.. code-block:: python

    class One:
        name = 'Twardowski'


    class Two:
        def __new__(cls):
            return One()


    a = Two()

    print(a)
    # <__main__.One object at 0x11ca09588>

    a.__class__.__name__
    # 'One'

``__slots__``
-------------
* faster attribute access
* space savings in memory

The proper use of __slots__ is to save space in objects. Instead of having a dynamic dict that allows adding attributes to objects at anytime, there is a static structure which does not allow additions after creation. This saves the overhead of one dict for every object that uses slots

Unfortunately there is a side effect to slots. They change the behavior of the objects that have slots in a way that can be abused by control freaks and static typing weenies. This is bad, because the control freaks should be abusing the metaclasses and the static typing weenies should be abusing decorators, since in Python, there should be only one obvious way of doing something.

The space savings is from:

    * Storing value references in slots instead of ``__dict__``.
    * Denying ``__dict__`` and ``__weakref__`` creation if parent classes deny them and you declare ``__slots__``.

.. code-block:: python

    class Base(object):
        __slots__ = ()

    b = Base()
    b.a = 'a'
    # Traceback (most recent call last):
    #   File "<pyshell#38>", line 1, in <module>
    #     b.a = 'a'
    # AttributeError: 'Base' object has no attribute 'a'

    class Child(Base):
        __slots__ = ('a',)

    c = Child()
    c.a = 'a'

    c.b = 'b'
    # Traceback (most recent call last):
    #   File "<pyshell#42>", line 1, in <module>
    #    c.b = 'b'
    # AttributeError: 'Child' object has no attribute 'b'

.. code-block:: python

    class Base:
        __slots__ = 'foo', 'bar'

    class Right(Base):
        __slots__ = 'baz',

    class Wrong(Base):
        __slots__ = 'foo', 'bar', 'baz'        # redundant foo and bar

Requirements:

    * To have attributes named in ``__slots__`` to actually be stored in slots instead of a ``__dict__``, a class must inherit from object
    * To prevent the creation of a ``__dict__``, you must inherit from object and all classes in the inheritance must declare ``__slots__`` and none of them can have a '``__dict__``' entry.

.. code-block:: python

    class SlottedWithDict(Child):
        __slots__ = ('__dict__', 'b')

    swd = SlottedWithDict()
    swd.a = 'a'
    swd.b = 'b'
    swd.c = 'c'

    swd.__dict__
    # {'c': 'c'}

    class NoSlots(Child):
        pass

    ns = NoSlots()
    ns.a = 'a'
    ns.b = 'b'

.. note:: More info: https://stackoverflow.com/questions/472000/usage-of-slots

Stringify objects
=================
* ``__repr__()`` jest dla developerów (być jednoznacznym)
* ``__str__()`` dla użytkowników (być czytelnym)
* ``__format__()`` - do zaawansowanego formatowania

``__str__()``
-------------
.. code-block:: python
    :caption: Using ``__str__()`` on a class
    :emphasize-lines: 6,7,11,12

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f'({self.x}, {self.y})'


     point = Point(2, 4)

     str(point)     # '(2, 4)'
     print(point)   # (2, 4)

``__repr__()``
--------------
.. code-block:: python
    :caption: Using ``__repr__()`` on a class
    :emphasize-lines: 6,7,11,12

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f'Point(x={self.x}, y={self.y})'

     point = Point(2, 4)

     repr(point)    # 'Point(x=2, y=4)'
     point          # 'Point(x=2, y=4)'

``__format__()``
----------------
.. code-block:: python
    :emphasize-lines: 7-13,17,18

    class Point:
        def __init__(self, x=0, y=0, z=0):
            self.x = x
            self.y = y
            self.z = z

        def __format__(self, style):
            if style == 'flat':
                return f"({self.x}, {self.y})"
            elif style == '3D':
                return f"({self.x}, {self.y}, {self.z})"
            else:
                raise ValueError

    p = Point(x=1, y=2)

    print(f'{p:flat}')    # (1, 2)
    print(f'{p:3D}')    # (1, 2, 3)

Use cases
---------
* ``__repr__``

    .. code-block:: python

        import datetime

        datetime.datetime.now()
        # datetime.datetime(2019, 1, 5, 20, 15, 0, 684972)

* ``__str__``

    .. code-block:: python

        import datetime

        print(datetime.datetime.now())
        # 2019-01-05 20:15:00.927387


What should be in the class and what not?
=========================================
* Jeżeli metoda w swoim ciele ma ``self`` i z niego korzysta to powinna być w klasie
* Jeżeli metoda nie ma w swoim ciele ``self`` to nie powinna być w klasie
* Jeżeli metoda nie ma w swoim ciele ``self`` ale wybitnie pasuje do klasy, to można ją tam zamieścić oraz dodać dekorator ``@staticmethod``

``@staticmethod``
-----------------
* Using class as namespace
* Will not pass instance as a first argument
* ``self`` is not required

.. code-block:: python
    :caption: Functions on a high level of a module lack namespace

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b


    add(1, 2)
    sub(8, 4)

.. code-block:: python
    :caption: When ``add`` and ``sub`` are in ``Calculator`` class (namespace) they get instance (``self``) as a first argument. Instantiating Calculator is not needed, as of functions do not read or write to instance variables.

    class Calculator:

        def add(self, a, b):
            return a + b

        def sub(self, a, b):
            return a - b


    Calculator.add(10, 20)  # TypeError: add() missing 1 required positional argument: 'b'
    Calculator.sub(8, 4)    # TypeError: add() missing 1 required positional argument: 'b'

    calc = Calculator()
    calc.add(1, 2)          # 3
    calc.sub(8, 4)          # 4

.. code-block:: python
    :caption: Class ``Calculator`` is a namespace for functions. ``@staticmethod`` remove instance (``self``) argument to method.

    class Calculator:

        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def sub(a, b):
            return a - b


    Calculator.add(1, 2)
    Calculator.sub(8, 4)

``@classmethod``
----------------
.. code-block:: python
    :emphasize-lines: 14-17,25-29

    import json

    class User:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def __str__(self):
            return f'{self.first_name} {self.last_name}'

        def to_json(self):
            return json.dumps(self.__dict__)

        @classmethod
        def from_json(cls, data):
            data = json.loads(data)
            return cls(**data)

    class SuperUser(User):
        pass


    DATA = '{"first_name": "Jan", "last_name": "Twardowski"}'

    normal = User.from_json(DATA)
    root = SuperUser.from_json(DATA)

    type(normal)    # <class '__main__.User'>
    type(root)      # <class '__main__.SuperUser'>


Dynamically creating fields
===========================
.. code-block:: python
    :caption: Funkcja inicjalizującą, która automatycznie dodaje pola do naszej klasy w zależności od tego co zostanie podane przy tworzeniu obiektu

    class Astronaut:
        def __init__(self, last_name, **kwargs):
            self.last_name = last_name

            for key, value in kwargs.items():
                setattr(self, key, value)


    ivan = Astronaut(first_name='Иван', last_name='Иванович', agency='Roscosmos')
    jose = Astronaut(last_name='Jimenez', addresses=())

    print(ivan.first_name)  # Иван
    print(jose.last_name)   # Jimenez

    print(jose.__dict__)    # {'last_name': 'Jimenez', 'addresses': ()}
    print(ivan.__dict__)    # {'last_name': 'Иванович', 'first_name': 'Иван', 'agency': 'Roscosmos'}


Setter and Getter
=================

Accessing class fields
----------------------
.. code-block:: python
    :caption: Accessing class fields "Java way" -- don't do that in Python

    class Astronaut:
        name = ''

        def set_name(self, name):
            print('I can print some log messages')
            self.name = name

        def get_name(self):
            return self.name

    jose = Astronaut()
    jose.set_name('José Jiménez')

    print(jose.get_name())

.. code-block:: python
    :caption: Accessing class fields - "the Python way"

    class Astronaut:
        def __init__(self, name=''):
            self.name = name

    ivan = Astronaut()              # either put ``name`` as an argument for ``__init__()``
    ivan.name = 'Ivan Иванович'     # or create dynamic field in runtime

    print(ivan.name)


.. code-block:: python
    :caption: Use case uzasadnionego użycia gettera w kodzie
    :emphasize-lines: 9,14-20

    from django.contrib import admin
    from habitat._common.admin import HabitatAdmin
    from habitat.sensors.models import ZWaveSensor


    @admin.register(ZWaveSensor)
    class ZWaveSensorAdmin(HabitatAdmin):
        change_list_template = 'sensors/change_list_charts.html'
        list_display = ['date', 'time', 'type', 'device', 'value', 'unit']
        list_filter = ['created', 'type', 'unit', 'device']
        search_fields = ['^date', 'device']
        ordering = ['-datetime']

        def get_list_display(self, request):
            list_display = self.list_display

            if request.user.is_superuser:
                list_display = ['datetime'] + list_display

            return list_display

``@property``
-------------
* ``@property`` - for defining getters
* Przykład użycia:

    * Blokowanie możliwości edycji pola klasy
    * Dodawanie logowania przy ustawianiu wartości

.. code-block:: python
    :caption: Using ``@property`` as a getter

    class Temperature:
        def __init__(self, kelvin: float = 0.0):
            self.kelvin = kelvin

        @property
        def celsius(self):
            temp = self.kelvin - 273.15
            return round(temp, 2)


    temp = Temperature(kelvin=309.75)

    print(temp.celsius)
    # 36.6

``@x.setter``
-------------
* ``@x.setter`` - for defining setter for field ``x``
* Require field to be ``@property``

.. code-block:: python
    :caption: ``@x.setter``

    class Temperature:
        def __init__(self, kelvin: float = 0.0):
            self.kelvin = kelvin

        @property
        def celsius(self):
            temp = self.kelvin - 273.15
            return round(temp, 2)

        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError('Temperature below -273.15 is not possible')
            else:
                self.kelvin = value + 273.15

    temp = Temperature()

    print(temp.kelvin)
    # 0.0

    temp.celsius = 36.60
    print(temp.kelvin)
    # 309.75

    temp.celsius = -1000
    # ValueError: Temperature below -273.15 is not possible

``@x.deleter``
--------------
* ``@x.deleter`` - for defining deleter for field ``x``
* Require field to be ``@property``

.. code-block:: python
    :caption: ``@x.deleter``

    class Temperature:
        def __init__(self, kelvin: float = 0.0):
            self.kelvin = kelvin

        @property
        def celsius(self):
            temp = self.kelvin - 273.15
            return round(temp, 2)

        @celsius.deleter
        def celsius(self):
            self.kelvin = 0.0

    temp = Temperature(kelvin=100)

    print(temp.celsius)
    # -173.15

    del temp.celsius

    print(temp.celsius)
    # -273.15

Hash
====
* Funkcja hash zwraca ``int``
* ``set()`` można zrobić z dowolnego hashowalnego obiektu
* ``dict()`` może mieć klucze, które są dowolnym hashowalnym obiektem

* User-defined classes have ``__eq__()`` and ``__hash__()`` methods by default.
* All objects compare unequal (except with themselves)
* ``x.__hash__()`` returns an appropriate value such that ``x == y`` implies both that ``x is y`` and ``hash(x) == hash(y)``


.. code-block:: python
    :caption: ``dict()`` może mieć klucze, które są dowolnym hashowalnym obiektem

    key = 'last_name'

    my_dict = {
        'fist_name': 'key can be ``str``',
        key: 'key can be ``str``',
        1: 'key can be ``int``',
        1.5: 'key can be ``float``',
        (1, 2): 'key can be ``tuple``',
    }

.. code-block:: python
    :caption: ``set()`` można zrobić z dowolnego hashowalnego obiektu

    class Astronaut:
        def __init__(self, name):
            self.name = name


    {1, 1, 2}
    # {1, 2}

    jose = Astronaut(name='Jose Jimenez')
    data = {jose, jose}
    len(data)
    # 1

    data = {Astronaut(name='Jose Jimenez'), Astronaut(name='Jose Jimenez')}
    len(data)
    # 2

.. literalinclude:: src/oop-hash-generate-bad.py
    :language: python
    :caption: Generating hash and object comparision

.. literalinclude:: src/oop-hash-generate-good.py
    :language: python
    :caption: Generating hash and object comparision

.. note:: Since Python 3.7 ``dict`` has fixed order and using ``OrderedDict`` is not necessary

``is``
======
* ``is`` porównuje czy dwa obiekty są tożsame
* Sprawdzenie odbywa się przez porównanie wartości ``id()`` dla obiektu
* Najczęściej służy do sprawdzania czy coś jest ``None``

Good
----
.. code-block:: python

    if name is None:
        print('Name is not set')
    else:
        print('You have set your name')

Not good
--------
 .. code-block:: python

     if name is 'Mark Watney':
        print('You are Space Pirate!')
     else:
        print('You are not pirate at all!')

Using ``is`` in script
----------------------
* ``id()`` will change every time you execute script
* both objects has the same ``id``.

 .. code-block:: python
    :caption: Using this code in script.

    a = 'Jan Twardowski'
    b = 'Jan Twardowski'

    print(a)        # Jan Twardowski
    print(b)        # Jan Twardowski

    print(a == b)   # True
    print(a is b)   # True

    print(id(a))    # 4430933296
    print(id(b))    # 4430933296

Using ``is`` in REPL (evaluated line by line)
---------------------------------------------
.. code-block:: python
    :caption: Evaluated in REPL line by line.

    a = 'Jan Twardowski'
    b = 'Jan Twardowski'

    print(a)        # Jan Twardowski
    print(b)        # Jan Twardowski

    print(a == b)   # True
    print(a is b)   # False

    print(id(a))    # 4784790960
    print(id(b))    # 4784791408

Using ``is`` in REPL (evaluated at once)
----------------------------------------
.. code-block:: python
    :caption: Evaluated in REPL at once.

    a = 'Jan Twardowski'
    b = 'Jan Twardowski'

    print(a)        # Jan Twardowski
    print(b)        # Jan Twardowski

    print(a == b)   # True
    print(a is b)   # True

    print(id(a))    # 4784833072
    print(id(b))    # 4784833072


Monkey Patching
===============
.. literalinclude:: src/oop-monkey-patching-1.py
    :language: python
    :caption: Monkey Patching

.. literalinclude:: src/oop-monkey-patching-2.py
    :language: python
    :caption: Monkey Patching

.. literalinclude:: src/oop-monkey-patching-3.py
    :language: python
    :caption: Monkey Patching


Inheritance Method Resolution
=============================

Method Resolution Order
-----------------------

.. code-block:: python
    :caption: Method Resolution Order

    class A:
        def show(self):
            print('a')

    class B:
        def show(self):
            print('b')

    class C:
        def show(self):
            print('c')

    class D(A, B, C):
        pass


    obj = D()

    obj.show()
    # a

    print(D.__mro__)
    # (<class '__main__.D'>,
    #  <class '__main__.A'>,
    #  <class '__main__.B'>,
    #  <class '__main__.C'>,
    #  <class 'object'>)

Inheritance Diamond
-------------------
.. figure:: img/inheritance-diamond-1.jpg
    :scale: 75%
    :align: center

    Inheritance Diamond

.. figure:: img/inheritance-diamond-2.jpg
    :scale: 75%
    :align: center

    Inheritance Diamond

.. code-block:: python
    :caption: Inheritance Diamond

    class A:
        def show(self):
            print('a')


    class B(A):
        def show(self):
            print('b')


    class C(A):
        def show(self):
            print('c')


    class D(B, C):
        pass


    obj = D()

    obj.show()
    # b

    print(D.__mro__)
    # (<class '__main__.D'>,
    #  <class '__main__.B'>,
    #  <class '__main__.C'>,
    #  <class '__main__.A'>,
    #  <class 'object'>)


Objects and instances
=====================
.. code-block:: python
    :caption: Implicit passing instance to class as ``self``.

    text = 'Jan,Twardowski'

    text.split(',')                     # ['Jan', 'Twardowski']

.. code-block:: python
    :caption: Explicit passing instance to class overriding ``self``.

    text = 'Jan,Twardowski'

    str.split(text, ',')                # ['Jan', 'Twardowski']

.. code-block:: python
    :caption: Passing anonymous objects as instances.

    'Jan,Twardowski'.split(',')         # ['Jan', 'Twardowski']
    str.split('Jan,Twardowski', ',')    # ['Jan', 'Twardowski']

Assignments
===========

Dragon (Part 3)
---------------
* Filename: ``oop_dragon_3.py``
* Lines of code to write: 50 lines
* Estimated time of completion: 30 min

.. figure:: img/dragon.gif
    :scale: 100%
    :align: center

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

#. Dodaj możliwość poruszania się smoka i bohatera w 3 wymiarach
#. Bohater może należeć do drużyny, który może składać się maks z 6 postaci (różnych klas)
#. Żadna z istot na planszy nie może wyjść poza zakres ekranu
#. Bohater może dodatkowo założyć ekwipunek i może być to wiele obiektów na raz
#. Każdy z przedmiotów ma swoją nazwę, typ oraz modyfikator

    * zbroję (dodatkowe punkty obrony, np. +10%)
    * tarczę (dodatkowe punkty obrony, np. +5%)
    * miecz (dodatkowe punkty ataku, np. +5%)

#. Zbroja i tarcza chroni przed uderzeniami obniżając ilość obrażeń o wartość obrony
#. Miecz zwiększa ilość zadawanych obrażeń
#. Obrażenia smoka maleją z sześcianem odległości (zianie ogniem)
#. Bohater nie może zadawać obrażeń jak jest dalej niż 50 punktów od przeciwnika
#. Wszystkie istoty mogą levelować a bazowe punty życia i obrażeń się zmieniają z poziomem
#. Przeprowadź symulację walki. Kto zginie pierwszy?
