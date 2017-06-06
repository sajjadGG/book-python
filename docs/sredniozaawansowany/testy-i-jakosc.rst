**************
Testy i Jakość
**************

Doctest
=======

.. code-block:: python

    def km_na_metry(ile):
        """
        >>> km_na_metry(1)
        1000

        >>> km_na_metry(0)
        0

        >>> km_na_metry(-1)
        Traceback (most recent call last):
            ...
        ValueError

        >>> km_na_metry('adas')
        Traceback (most recent call last):
            ...
        TypeError
        """
        return ile * 1000


    if __name__ == "__main__":
        import doctest

        doctest.testmod()


.. code-block:: python


    MINIMALNA_TEMPERATURA = -273.15


    def przelicz_celsius_na_kelvin(temperatura):
        """
        >>> przelicz_celsius_na_kelvin(1)
        274.15

        >>> przelicz_celsius_na_kelvin(0)
        273.15

        >>> przelicz_celsius_na_kelvin(-300)
        Traceback (most recent call last):
            ...
        ValueError: Nie może być mniejsze niż minimalna temperatura

        >>> przelicz_celsius_na_kelvin('jeden')
        Traceback (most recent call last):
            ...
        ValueError: Temperatura musi być float

        >>> przelicz_celsius_na_kelvin([1.0, 1, 0])
        Traceback (most recent call last):
            ...
        TypeError: Nie obsługiwany typ argumentu
        """

        try:
            temperatura = float(temperatura)
        except ValueError:
            raise ValueError('Temperatura musi być float')
        except TypeError:
            raise TypeError('Nie obsługiwany typ argumentu')

        if temperatura < MINIMALNA_TEMPERATURA:
            raise ValueError('Nie może być mniejsze niż minimalna temperatura')
        else:
            return temperatura - MINIMALNA_TEMPERATURA


Unit Test
=========

.. code-block:: python

    class Prostokat:
        def __init__(self, a, b):
            if not isinstance(a, (float, int)) or a <= 0:
                raise ValueError('Długość boku A musi być więszka od 0')

            if not isinstance(b, (float, int)) or b <= 0:
                raise ValueError('Długość boku B musi być więszka od 0')

            self.bok_a = float(a)
            self.bok_b = float(a)

        def pole(self):
            return self.bok_a * self.bok_b

        def obwod(self):
            return 2 * (self.bok_a + self.bok_b)

        def __str__(self):
            return f'Prostokat(a={self.bok_a}, b={self.bok_b})'

.. code-block:: python

    class ProstokatTest(unittest.TestCase):

        def setUp(self):
            self.prostokat = Prostokat(a=10, b=20)

        def test_prostokata_bok_nieprawidlowy(self):
            with self.assertRaises(ValueError):
                Prostokat(a='a', b=20)

            with self.assertRaises(ValueError):
                Prostokat(a=20, b='b')

        def test_prostokata_bok_zero(self):
            with self.assertRaises(ValueError):
                Prostokat(a=0, b=20)

            with self.assertRaises(ValueError):
                Prostokat(a=20, b=0)

        def test_prostokata_bok_ujemny(self):
            with self.assertRaises(ValueError):
                Prostokat(a=-3, b=20)

            with self.assertRaises(ValueError):
                Prostokat(a=20, b=-3)

        def test_ustawienia_bokow(self):
            with self.assertRaises(TypeError):
                Prostokat(a=0)

            with self.assertRaises(TypeError):
                Prostokat(b=0)

        def test_tworzenie_prostokata(self):
            self.assertEqual(self.prostokat.bok_a, 10)
            self.assertEqual(self.prostokat.bok_b, 20)

        def test_pole(self):
            self.assertEqual(self.prostokat.pole(), 200)

        def test_obwod(self):
            self.assertEqual(self.prostokat.obwod(), 60)

        def test_prostokat_to_string(self):
            self.assertEqual(str(self.prostokat), 'Prostokat(a=5.0, b=10.0)')


    if __name__ == '__main__':
        unittest.main()


``selenium``
============

Mock
====

Stub
====

Wykorzystanie debuggera w IDE
=============================

Break Point
-----------

View Breakpoints
~~~~~~~~~~~~~~~~

Mute Breakpoints
~~~~~~~~~~~~~~~~

Poruszanie się
--------------

Step Over
~~~~~~~~~

Step Into My Code
~~~~~~~~~~~~~~~~~

Force Step Into
~~~~~~~~~~~~~~~

Show Execution Point
~~~~~~~~~~~~~~~~~~~~

Step Out
~~~~~~~~

Run to Cursor
~~~~~~~~~~~~~

Resume Program
~~~~~~~~~~~~~~

New Watch
~~~~~~~~~

Frames
------

Previous Frame
~~~~~~~~~~~~~~

Next Frame
~~~~~~~~~~

Threads
~~~~~~~

Scope
-----

Special Variables
~~~~~~~~~~~~~~~~~

* __file__
* __name__
* __builtins__
* __doc__
* __loader__
* __spec__
* __package__

Moduły
~~~~~~

Stałe
~~~~~

Zmienne
~~~~~~~

Wartości funkcji
~~~~~~~~~~~~~~~~

Debugging i Wątki
-----------------

Debugging i Procesy
-------------------

Debugging aplikacji sieciowych
------------------------------

Wyciszanie logowania
--------------------

Static Code Analysis
====================

pychecker
---------

pylint
------
Coding Standard:

- checking line-code's length,
- checking if variable names are well-formed according to your coding standard
- checking if imported modules are used

Error detection:

- checking if declared interfaces are truly implemented
- checking if modules are imported and much more (see the complete check list)

Pylint is shipped with Pyreverse which creates UML diagrams for python code.

.. code-block:: console

    $ pip install pylint

PyFlakes
--------
A simple program which checks Python source files for errors.

Pyflakes analyzes programs and detects various errors. It works by parsing the source file, not importing it, so it is safe to use on modules with side effects. It’s also much faster.

.. code-block:: console

    $ pip install --upgrade pyflakes

.. code-block:: console

    $ python2 -m pyflakes .

    $ python3 -m pyflakes .

Coverage
--------

Use coverage run to run your program and gather data:

.. code-block:: console

    $ coverage run my_program.py arg1 arg2
    blah blah ..your program's output.. blah blah

Use coverage report to report on the results:

.. code-block:: console

    $ coverage report -m
    Name                      Stmts   Miss  Cover   Missing
    -------------------------------------------------------
    my_program.py                20      4    80%   33-35, 39
    my_other_module.py           56      6    89%   17-23
    -------------------------------------------------------
    TOTAL                        76     10    87%

For a nicer presentation, use ``coverage html`` to get annotated HTML listings detailing missed lines:

.. code-block:: console

    $ coverage html

PEP8
----

.. code-block:: shell

    pip install pep8

    pep8 my_program.py

    pep8 my_module/

setup.cfg
~~~~~~~~~

.. code-block:: ini

    [pep8]
    max-line-length = 150
    ignore = E402,W391


Testy Mutacyjne
===============

* https://pypi.python.org/pypi/MutPy/0.4.0
* https://github.com/sixty-north/cosmic-ray
* https://hackernoon.com/mutmut-a-python-mutation-testing-system-9b9639356c78
* https://www.youtube.com/watch?v=jwB3Nn4hR1o
* http://cosmic-ray.readthedocs.io/en/latest/
* https://github.com/sk-/elcap



