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
        >>> hello('Иван Иванович')
        'Иван Иванович'

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
        >>> hello('Иван Иванович')
        Иван Иванович

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

Celsius to Kelvin temperature conversion
----------------------------------------
.. code-block:: python

    from typing import Union


    def celsius_to_kelvin(temperature_in_celsius: Union[int, float]) -> float:
        """
        >>> celsius_to_kelvin(0)
        273.15

        >>> celsius_to_kelvin(1)
        274.15

        >>> celsius_to_kelvin(-1)
        272.15

        >>> celsius_to_kelvin(-273.15)
        0.0

        >>> celsius_to_kelvin(-274.15)
        Traceback (most recent call last):
            ...
        ValueError: Argument must be greater than -273.15

        >>> celsius_to_kelvin([-1, 0, 1])
        Traceback (most recent call last):
            ...
        ValueError: Argument must be int or float

        >>> celsius_to_kelvin('one')
        Traceback (most recent call last):
            ...
        ValueError: Argument must be int or float
        """
        if not isinstance(temperature_in_celsius, (float, int)):
            raise ValueError('Argument must be int or float')

        if temperature_in_celsius < -273.15:
            raise ValueError('Argument must be greater than -273.15')

        return float(temperature_in_celsius + 273.15)

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

Distance conversion doctest
---------------------------
#. Napisz funkcję, która przeliczy dystans podany w metrach na kilometry
#. 1 km = 1000 m
#. Dystans nie może być ujemny
#. Zwracany dystans musi być zawsze float
#. Napisz testy do rozwiązania i pokryj przypadki:

    * dystans w metrach jest -1 (ujemny)
    * dystans w metrach jest 0 (zero)
    * dystans w metrach jest 1 (dodatni)
    * dystans w metrach jest ``float``
    * dystans w metrach jest ``int``
    * podano listę odległości
    * podany parametr to ``str``

:About:
    * Filename: ``doctest_temperature.py``
    * Lines of code to write: 5 lines of code + 16 lines of tests
    * Estimated time of completion: 5 min

