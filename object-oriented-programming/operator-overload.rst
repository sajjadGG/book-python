*****************
Operator Overload
*****************


Why to use operator overload?
=============================
* Readable syntax
* Simpler operations

.. code-block:: python

    class Vector:
        def __init__(self, x=0.0, y=0.0):
            self.x = x
            self.y = y


    vector1 = Vector(x=1, y=2)
    vector2 = Vector(x=3, y=4)

    suma = vector1 + vector2
    # TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'

.. code-block:: python

    class Vector:
        def __init__(self, x=0.0, y=0.0):
            self.x = x
            self.y = y

        def __str__(self):
            return f'Vector(x={self.x}, y={self.y})'

        def __add__(self, other):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )

    vector1 = Vector(x=1, y=2)
    vector2 = Vector(x=3, y=4)
    vector3 = Vector(x=5, y=6)

    suma = vector1 + vector2
    print(suma)
    # Vector(x=4, y=6)

    suma = vector1 + vector2 + vector3
    print(suma)
    # Vector(x=9, y=12)


Operator Overload
=================

Numerical Operators
-------------------
.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``a + b``",        "``__add__()``"
    "``a += b``",       "``__iadd__()``"
    "``a - b``",        "``__sub__()``"
    "``a -= b``",       "``__isub__()``"
    "``a * b``",        "``__mul__()``"
    "``a *= b``",       "``__imul__()``"
    "``a / b``",        "``__div__()``"
    "``a /= b``",       "``__idiv__()``"
    "``a % b``",        "``__mod__()``"

Comparison Operators
--------------------
.. csv-table:: Comparison Operators Overload
    :header: "Operator", "Method"

    "``a == b``",       "``__eq__()``"
    "``a != b``",       "``__ne__()``"
    "``a < b``",        "``__lt__()``"
    "``a <= b``",       "``__le__()``"
    "``a > b``",        "``__gt__()``"
    "``a >= b``",       "``__ge__()``"

Boolean Operators
-----------------
.. csv-table:: Boolean Operators Overload
    :header: "Operator", "Method"

    "``-a``",           "``__neg__()``"
    "``+a``",           "``__pos__``"
    "``a & b``",        "``__and__()``"
    "``a | b``",        "``__or__()``"
    "``a ^ b``",        "``__xor__()``"
    "``a << b``",       "``__lshift__()``"
    "``a >> b``",       "``__rshift__()``"

Builtin Functions
-----------------
.. csv-table:: Builtin Functions Overload
    :header: "Function", "Method"

    "``abs(a)``",             "``__abs__()``"
    "``bool(a)``",            "``__bool__()``"
    "``divmod(a, b)``",       "``__divmod__()``"
    "``pow(a)``",             "``__pow__()``"
    "``round(a, prec)``",     "``__round__()``"
    "``dir(a)``",             "``__dir__()``"
    "``len(a)``",             "``__len__()``"
    "``delattr(cls, 'a')``",  "``__delattr__()``"
    "``complex(a)``",         "``__complex__()``"
    "``int(a)``",             "``__int__()``"
    "``float(a)``",           "``__float__()``"
    "``oct(a)``",             "``__oct__()``"
    "``hex(a)``",             "``__hex__()``"
    "``reversed()``",         "``__reversed__()``"

.. code-block:: python

    from math import sqrt


    class Vector:
        def __init__(self, x=0.0, y=0.0):
            self.x = x
            self.y = y

        def __abs__(self):
            return sqrt(self.x**2 + self.y**2)


    vector = Vector(x=3, y=4)
    abs(vector)
    # 5.0

Builtin keywords
----------------
.. csv-table:: Builtin Keywords Overload
    :header: "Keyword", "Method"

    "``del a``",              "``__delattr__()``"

Accessors Overload
------------------
.. csv-table:: Operator Overload
    :header: "Operator", "Description"

    "``a[b]``",                                 "``__getitem__()``"
    "``a[b] = 10``",                            "``__setitem__()``"
    "``a in b``",                               "``__contains__()``"
    "``a[b]`` (when ``b`` is not in ``a``)",    "``__missing__()``"


Example
=======

Modulo operator for ``int`` and ``str``
---------------------------------------
.. code-block:: python

    7 % 2               # 1
    'My number' % 2     # TypeError: not all arguments converted during string formatting
    'My number %s' % 2  # My number 2
    'My number %d' % 2  # My number 2
    'My number %f' % 2  # My number 2.0

.. note:: ``%s``, ``%d``, ``%f`` is currently deprecated in favor of ``f'...'`` string formatting. The topic will be continued in :ref:`Print Formatting` chapter.

Contains in ``numpy``
---------------------
.. code-block:: python

    import numpy as np

    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a[1][2]  # 6
    a[1,2]   # 6

.. code-block:: python
    :caption: Intuitive implementation of numpy ``array[row,col]`` accessor

    class array(list):
        def __getitem__(key):
            row = key[0]
            col = key[1]
            return super().__getitem__(row).__getitem__(col)

    # a[1,2]
    a.__getitem__(key=(1,2))


Assignment
==========

Address Book
------------
* Complexity level: Easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/operator_overload.py`

#. Dopisz odpowiednie metody do ``Contact`` i ``Address`` aby poniższy kod zadziałał poprawnie

.. code-block:: python

    class Contact:
        def __str__(self):
            return f'{self.__dict__}'


    class Address:
        def __repr__(self):
            return f'{self.__dict__}'


    contact = Contact(name='José Jiménez', addresses=[Address(location='JPL')])
    contact += Address(location='Houston')
    contact += Address(location='KSC')

    print(contact)
    # {'name': 'José Jiménez', 'addresses': [
    #       {'location': 'JPL'},
    #       {'location': 'Houston'},
    #       {'location': 'KSC'}
    # ]}

    if Address(location='Houston') in contact:
        print(True)
    else:
        print(False)
    # True
