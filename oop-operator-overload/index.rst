*****************
Operator Overload
*****************

Przeciążanie operatorów
=======================
Python implementuje kilka funkcji systemowych (magic methods), zaczynających się od podwójnego podkreślnika. Są to funkcje wywoływane m.in podczas inicjalizacji obiektu (``__init__``). Innym przykładem może być funkcja ``obiekt1.__add__(obiekt2)``, która jest wywoływana gdy wykonamy operację ``obiekt1 + obiekt2``.

Poniżej przedstawiono kilka przykładów metod magicznych w Pythonie.

``__add__()``
-------------
.. code-block:: python

    class Vector:
        def __init__(self, x=0.0, y=0.0):
            self.x = x
            self.y = y

        def __str__(self):
            return f"Vector(x={self.x}, y={self.y})"

        def __add__(self, other):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )

    vector1 = Vector(x=1, y=2)
    vector2 = Vector(x=3, y=4)

    suma = vector1 + vector2
    print(suma)
    # wyświetli: Vector(x=4, y=6)

``__sub__()``
-------------
Return the difference of another ``Transaction`` object, or another class object that also has the ``val`` property.
.. code-block:: python

    class Transaction:

        def __init__(self, val):
            self.val = val

        def __sub__(self, other):
            return self.val - other.val


    buy = Transaction(10.00)
    sell = Transaction(7.00)
    print(buy - sell)
    # 3.0

Return a Transaction object with ``val`` as the difference of this ``Transaction.val`` property and another object with a ``val`` property.

.. code-block:: python

    class Transaction:

        def __init__(self, val):
            self.val = val

        def __sub__(self, other):
            return Transaction(self.val - other.val)


    buy = Transaction(20.00)
    sell = Transaction(5.00)
    result = buy - sell
    print(result.val)
    # 15

Return difference of this Transaction.val property and an integer.

.. code-block:: python

    class Transaction:

        def __init__(self, val):
            self.val = val

        def __sub__(self, other):
            return self.val - other


    buy = Transaction(8.00)
    print(buy - 6.00)
    # 2

``__abs__()``
-------------
.. code-block:: python

    class Vector:
        def __init__(self, x=0.0, y=0.0):
            self.x = x
            self.y = y

        def __abs__(self):
            return (self.x**2 + self.y**2)**0.5


``__iadd__()``
--------------
'+='

``__isub__()``
--------------

``__mul__()`` and ``__imul__()``
--------------------------------

``__div__()`` and ``__idiv__()``
--------------------------------

``__eq__()``
------------
.. code-block:: python

    vector1 == vector2  # ``urchamia __eq__``

``__ne__()``
------------
'!='

``__lt__()``
------------


``__le__()``
------------

``__gt__()``
------------

``__ge__()``
------------

``__contains__()``
------------------
* ``a in b``

``__dir__()``
-------------

``__len__()``
-------------

``__delattr__()``
-----------------

``__getattribute__()``
----------------------

``__getitem__()``
-----------------

``__mod__()``
-------------

``__setattr__()``
-----------------

``__divmod__()``
----------------

``__bool__()``
--------------

``__neg__()``
-------------

``__and__()``, ``__rand__()``
-----------------------------

``__or__()``, ``__ror__()``
---------------------------

``__xor__()``, ``__rxor__()``
-----------------------------

``__lshift__()``, ``__rshift__()``
----------------------------------


Assignment
==========

Address Book
------------
#. Dopisz odpowiednie metody do ``Contact`` i ``Address`` aby poniższy kod zadziałał poprawnie

:Założenia:
    * Nazwa pliku: ``oop_addressbook_operators.py``
    * Szacunkowa długość kodu: około 10 linii
    * Maksymalny czas na zadanie: 15 min

.. code-block:: python

    class Contact:
        def __str__(self):
            return f'{self.__dict__}'


    class Address:
        def __repr__(self):
            return f'{self.__dict__}'


    contact = Contact(name='Jose Jimenez')
    address = Address(city='Houston')

    contact + address
    print(contact)
    # {'name': 'Jose Jimenez', 'addresses': [{'city': 'Houston'}]}

    if address in contact:
        print(True)
    else:
        print(False)
    # True
