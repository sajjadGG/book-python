************
Trigonometry
************


.. glossary::

    Universal Functions
    ufunc
        Mathematical operations optimized to work on ``np.array()``:

            .. code-block:: python

                import numpy as np


                 a = np.array([1, 2, 3])

                 np.sin(a)
                 # array([0.84147098, 0.90929743, 0.14112001])

Unit conversion
===============

Degrees
-------
* ``np.deg2rad()``
* ``np.degrees()``

Radians
-------
* ``np.rad2deg()``
* ``np.radians()``


Trigonometric functions
=======================

Basic functions
---------------
* ``np.sin()``
* ``np.cos()``
* ``np.tan()``

Arcus functions
---------------
* ``np.arcsin()``
* ``np.arccos()``
* ``np.arctan()``

Hyperbolic functions
--------------------
* ``np.sinh()``
* ``np.cosh()``
* ``np.tanh()``

Arcus hyperbolic functions
--------------------------
* ``np.arcsinh()``
* ``np.arccosh()``
* ``np.arctanh()``


Assignments
===========

Numpy Trigonometry
------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/numpy_trigonometry.py`

:English:
    #. Read input (angle in degrees) from user
    #. User will type ``int`` or ``float``
    #. Print all trigonometric functions (sin, cos, tg, ctg)
    #. Ctg for 180 degrees does not exists
    #. If there is no value for this angle, raise an exception

:Polish:
    #. Program wczytuje od użytkownika wielkość kąta w stopniach
    #. Użytkownik zawsze podaje ``int`` albo ``float``
    #. Wyświetl wartość funkcji trygonometrycznych (sin, cos, tg, ctg)
    #. Ctg dla wartości 180 stopni nie istnieje
    #. Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta podnieś stosowny wyjątek

:Hint:
    * ``input('Type angle [deg]: ')``
