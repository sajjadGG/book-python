***************************
Object Oriented Programming
***************************

Everything is an object
=======================
* W Pythonie wszystkie rzeczy są obiektem.
* Każdy element posiada swoje metody, które możemy na nim uruchomić.
* W dalszej części tych materiałów będziemy korzystali z polecenia ``help()`` aby zobaczyć jakiego z jakiego typu obiektem mamy okazję pracować oraz co możemy z nim zrobić.


Objects and instances
=====================
.. literalinclude:: src/oop-objects-and-instances.py
    :language: python
    :caption: Objects and instances


Duck typing
===========
.. literalinclude:: src/oop-duck-typing.py
    :language: python
    :caption: Duck typing


Accessors
=========

Accessing class fields
----------------------
.. literalinclude:: src/oop-accessor-fields.py
    :language: python
    :caption: Accessing class fields

.. literalinclude:: src/oop-getter.py
    :language: python
    :caption: Case Study uzasadnionego użycia gettera w kodzie

``@property``, ``@x.setter``, ``@x.deleter``
--------------------------------------------
* ``@propery`` - for defining getters
* ``@kola.setter`` - for defining setter
* ``@kola.deleter`` - for defining deleter
* Blokowanie możliwości edycji pola klasy
* Dodawanie logowania przy ustawianiu wartości

.. literalinclude:: src/oop-property.py
    :language: python
    :caption: ``@property``, ``@x.setter``, ``@x.deleter``


``@staticmethod``
=================
* Using class as namespace
* Will not pass instance as a first argument
* ``self`` is not required

.. literalinclude:: src/oop-staticmethod.py
    :language: python
    :caption: Using ``@staticmethod``


Method Resolution Order
=======================
.. literalinclude:: src/oop-mro.py
    :language: python
    :caption: Method Resolution Order


Hash
====
* ``set()`` można zrobić z dowolnego hashowalnego obiektu

.. code-block:: python

    class Adres:
        def __init__(self, miasto):
            self.miasto = miasto

    {1, 1, 2}
    # {1, 2}

    a = Adres(miasto='Gwiezdne')
    data = {a, a}
    len(data)
    # 1

    data = {Adres(miasto='Gwiezdne'), Adres(miasto='Gwiezdne')}
    len(data)
    # 2

.. code-block:: python

    key = 'last_name'

    my_dict = {
        'fist_name': 'José',
        key: 'Jiménez',
        1: 'id',
    }


.. code-block:: python

    class Adres:
        def __init__(self, ulica, miasto):
            self.ulica = ulica
            self.miasto = miasto

        def __hash__(self, *args, **kwargs):
            """
            __hash__ should return the same value for objects that are equal.
            It also shouldn't change over the lifetime of the object;
            generally you only implement it for immutable objects.
            """
            return hash(self.ulica) + hash(self.miasto)

        def __eq__(self, other):
            if self.ulica == other.ulica and self.miasto == other.miasto:
                return True
            else:
                return False


Polymorphism
============
.. literalinclude:: src/oop-polymorphism.py
    :language: python
    :caption: Polymorphism


Interfaces
==========
* Nie można tworzyć instancji
* Wszystkie metody muszą być zaimplementowane przez potomków
* Tylko deklaracje metod
* Metody nie mogą mieć implementacji

.. literalinclude:: src/oop-interface.py
    :language: python
    :caption: Interfaces


Abstract Classes
================
* Nie można tworzyć instancji
* Można tworzyć implementację metod

.. literalinclude:: src/oop-abstract-class.py
    :language: python
    :caption: Abstract Class


Good Engineering Practises
==========================

Tell - don't ask
----------------
* Tell-Don't-Ask is a principle that helps people remember that object-orientation is about bundling data with the functions that operate on that data.
* It reminds us that rather than asking an object for data and acting on that data, we should instead tell an object what to do.
* This encourages to move behavior into an object to go with the data.

.. literalinclude:: src/oop-tell-dont-ask.py
    :language: python
    :caption: Tell - don't ask

Do not run methods in ``__init__()``
------------------------------------
* Nie powinniśmy uruchamiać innych metod na obiekcie.
* Obiekt nie jest jeszcze w pełni zainicjalizowany!
* Konstruktor się nie wykonał do końca.
* Dopiero jak się skończy ``__init__`` to możemy uruchamiać metody obiektu

.. literalinclude:: src/oop-init-calls.py
    :language: python
    :caption: Do not run methods in ``__init__()``


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


Metaclass
=========
* Można zmienić, że obiekt nie dziedziczy po ``object``
* Każdy obiekt klasy jest instancją tej klasy
* Każda napisana klasa jest instancją obiektu, który nazywa się metaklasą
* Na 99.999% tego nie potrzebujesz

.. literalinclude:: src/oop-metaclass.py
    :language: python
    :caption: Metaclass