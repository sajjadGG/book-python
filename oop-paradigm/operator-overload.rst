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

    "``a + b``",        "``a.__add__(b)``"
    "``a += b``",       "``a.__iadd__(b)``"
    "``a - b``",        "``a.__sub__(b)``"
    "``a -= b``",       "``a.__isub__(b)``"
    "``a * b``",        "``a.__mul__(b)``"
    "``a *= b``",       "``a.__imul__(b)``"
    "``a / b``",        "``a.__div__(b)``"
    "``a /= b``",       "``a.__idiv__(b)``"
    "``a % b``",        "``a.__mod__(b)``"

.. code-block:: python
    :caption: Modulo operator for ``int`` and ``str``

    7 % 2               # 1
    'My number' % 2     # TypeError: not all arguments converted during string formatting
    'My number %s' % 2  # My number 2
    'My number %d' % 2  # My number 2
    'My number %f' % 2  # My number 2.0

.. note:: ``%s``, ``%d``, ``%f`` is currently deprecated in favor of ``f'...'`` string formatting. The topic will be continued in :ref:`Print Formatting` chapter.

Comparison Operators
--------------------
.. csv-table:: Comparison Operators Overload
    :header: "Operator", "Method"

    "``a == b``",       "``a.__eq__(b)``"
    "``a != b``",       "``a.__ne__(b)``"
    "``a < b``",        "``a.__lt__(b)``"
    "``a <= b``",       "``a.__le__(b)``"
    "``a > b``",        "``a.__gt__(b)``"
    "``a >= b``",       "``a.__ge__(b)``"

Boolean Operators
-----------------
.. csv-table:: Boolean Operators Overload
    :header: "Operator", "Method"

    "``-a``",           "``a.__neg__(b)``"
    "``+a``",           "``a.__pos__(b)``"
    "``a & b``",        "``a.__and__(b)``"
    "``a | b``",        "``a.__or__(b)``"
    "``a ^ b``",        "``a.__xor__(b)``"
    "``a << b``",       "``a.__lshift__(b)``"
    "``a >> b``",       "``a.__rshift__(b)``"

Builtin Functions and Keywords
------------------------------
.. csv-table:: Builtin Functions Overload
    :header: "Function", "Method"

    "``abs(a)``",             "``a.__abs__()``"
    "``bool(a)``",            "``a.__bool__()``"
    "``divmod(a, b)``",       "``a.__divmod__(b)``"
    "``pow(a)``",             "``a.__pow__()``"
    "``round(a, prec)``",     "``a.__round__(prec)``"
    "``dir(a)``",             "``a.__dir__()``"
    "``len(a)``",             "``a.__len__()``"
    "``complex(a)``",         "``a.__complex__()``"
    "``int(a)``",             "``a.__int__()``"
    "``float(a)``",           "``a.__float__()``"
    "``oct(a)``",             "``a.__oct__()``"
    "``hex(a)``",             "``a.__hex__()``"
    "``reversed(a)``",        "``a.__reversed__()``"
    "``delattr(a, attr)``",   "``a.__delattr__(attr)``"
    "``del a``",              "``a.__del__()``"

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

Accessors Overload
------------------
.. csv-table:: Operator Overload
    :header: "Operator", "Description"

    "``a(b)``",                                 "``a.__call__(b)``"
    "``a[b]``",                                 "``a.__getitem__(b)``"
    "``a[b] = 10``",                            "``a.__setitem__(b, 10)``"
    "``a in b``",                               "``a.__contains__(b)``"
    "``a[b]`` (when ``b`` is not in ``a``)",    "``a.__missing__(b)``"

.. code-block:: python
    :caption: Contains in ``numpy``

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
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/operator_overload.py`

:English:
    #. Use the code from listing below
    #. Override operators of ``Contact`` and ``Address`` for code to work correctly

:Polish:
    #. Użyj kodu z listingu poniżej
    #. Nadpisz operatory ``Contact`` i ``Address`` aby poniższy kod zadziałał poprawnie

.. code-block:: python

    class Astronaut:
        def __str__(self):
            return f'{self.name}, {self.locations}'


    class Location:
        def __repr__(self):
            return f'\n\t{self.name}'


    astro = Astronaut('Jan Twardowski', locations=(
        Location('Armstrong Flight Research Center'),
        Location('Kennedy Space Center'),
    ))

    astro += Location('Jet Propulsion Laboratory')
    astro += Location('Johnson Space Center')

    print(astro)
    # Jan Twardowski, [
    #     Armstrong Flight Research Center,
    #     Kennedy Space Center,
    #     Jet Propulsion Laboratory,
    #     Johnson Space Center]

    if Location('Johnson Space Center') in astro:
        print(True)
    else:
        print(False)
    # True
