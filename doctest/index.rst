*******
Doctest
*******


* używane jako zawsze aktualna dokumentacja kodu
* sprawdzają poprawność działania funkcji
* niezwykle przydatne przy tworzeniu regexpów
* można przetykać tekst pomiędzy testami


Test for ``bool`` return values
===============================
.. code-block:: python

    AGE_ADULT = 18

    def is_adult(age):
        """
        Function checks if person is adult.
        Adult person is over 18 years old.

        >>> is_adult(18)
        True

        >>> is_adult(17.9)
        False
        """
        if age >= AGE_ADULT:
            return True
        else:
            return False


Test for ``int`` return values
==============================
.. code-block:: python

    def sumowanie_liczb(a, b):
        """
        >>> sumowanie_liczb(1, 2)
        3

        >>> sumowanie_liczb(-1, 1)
        0

        >>> sumowanie_liczb(0, 0)
        0
        """
        return a + b


Test for ``str`` return values
==============================

Returning ``str``
-----------------
.. code-block:: python

    def hello(name='José Jiménez'):
        """
        Function returns the name of the astronaut
        >>> hello('Ivan Ivanovich')
        'Ivan Ivanovich'

        Default value is 'José Jiménez'
        >>> hello()
        'José Jiménez'
        """
        return name

Printing ``str``
----------------
.. code-block:: python

    def hello(name='José Jiménez'):
        """
        Function prints on the screen the name of the astronaut
        >>> hello('Ivan Ivanovich')
        Ivan Ivanovich

        Default value is 'José Jiménez'
        >>> hello()
        José Jiménez
        """
        print(name)

Printing ``str`` with newlines
------------------------------
.. code-block:: python

    def hello(name='José Jiménez'):
        """
        >>> hello()
        José Jiménez
        José Jiménez
        José Jiménez
        <BLANKLINE>
        """
        print(f'{name}\n' * 3)

Testing for exceptions
======================
.. code-block:: python

    def add(a, b):
        """
        >>> add(1, 2)
        3

        >>> add(-1, 1)
        0

        >>> add(0, 0)
        0

        Function should do:
            - one thing
            - one thing only
            - one thing good

        Adding list elements is not a business of this function.

        >>> add([1, 2])
        Traceback (most recent call last):
            ...
        TypeError: Argument must be int or float
        """
        if not isinstance(a, (int, float)):
            raise TypeError('Argument must be int or float')

        if not isinstance(b, (int, float)):
            raise TypeError('Argument must be int or float')

        return a + b


Using python statements in ``doctest``
======================================
.. code-block:: python

    def when(date):
        """
        >>> import datetime
        >>> moon = datetime.date(1969, 7, 20)
        >>> hello(moon)
        '1969-07-20'
        """
        print(f'{date:%Y-%m-%d}')


Running doctest from standalone scripts
=======================================
* Testy dla wszystkich funkcji aktualnie zdefiniowanych w przestrzeni nazw

.. code-block:: python

    def add(a, b):
        """
        >>> add(1, 2)
        3

        >>> add(-1, 1)
        0

        >>> add(0, 0)
        0
        """
        return a + b


    if __name__ == '__main__':
        import doctest
        doctest.testmod()


Practical example
=================

Non negative distances
----------------------
.. code-block:: python

    from typing import Union


    def kilometers_from_meters(km: Union[int, float]) -> float:
        """
        >>> kilometers_from_meters(1)
        1000.0

        >>> kilometers_from_meters(0)
        0.0

        >>> kilometers_from_meters(-1)
        Traceback (most recent call last):
            ...
        ValueError: Argument must be positive

        >>> kilometers_from_meters([1, 2])
        Traceback (most recent call last):
            ...
        ValueError: Invalid Argument

        >>> kilometers_from_meters('one')
        Traceback (most recent call last):
            ...
        ValueError: Invalid Argument

        >>> kilometers_from_meters(1.5)
        1500.0
        """
        if not isinstance(km, (int, float)):
            raise ValueError('Invalid Argument')

        if km < 0:
            raise ValueError('Argument must be positive')

        return float(1000 * km)

Email regex
-----------
.. code-block:: python

    import re

    VALID_EMAIL = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'


    def is_valid_email(email: str) -> bool:
        """
        Function check email address against Regular Expression

        >>> is_valid_email('jose.jimenez@nasa.gov')
        True
        >>> is_valid_email('Jose.Jimenez@nasa.gov')
        True
        >>> is_valid_email('+jose.jimenez@nasa.gov')
        False
        >>> is_valid_email('jose.jimenez+@nasa.gov')
        True
        >>> is_valid_email('jose.jimenez+newsletter@nasa.gov')
        True
        >>> is_valid_email('jose.jimenez@.gov')
        False
        >>> is_valid_email('@nasa.gov')
        False
        >>> is_valid_email('jose.jimenez@nasa.g')
        False
        """
        if re.match(VALID_EMAIL, email):
            return True
        else:
            return False


Assignments
===========

Konwersja temperatury
---------------------
#. Napisz funkcję, która przeliczy temperaturę podaną w Fahrenheit na Kelviny
#. Napisz testy do rozwiązania i pokryj przypadki:

    * temperatura ujemna
    * temperatura zero
    * temperatura dodatnia
    * temperatura ``float``
    * temperatura ``int``
    * lista temperatur
    * podany parametr to ``str``

:Podpowiedź:
    * Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
    * Celsius to Fahrenheit: (°C * 1.8) + 32 = °F
    * Jeden stopień Celsiusza odpowiada jednemu stopniowi w skali Kelvina
    * -273,15 °C = 0 K

:About assignment:
    * Filename: ``doctest_temperature.py``
    * Lines of code to write: 6 linii
    * Estimated time of completion: 5 min
