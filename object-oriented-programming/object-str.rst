*****************
Stringify objects
*****************


``__str__()``
=============
* ``__str__()`` dla użytkowników (być czytelnym)
* ``print`` converts it's arguments to ``str()`` before printing

.. code-block:: python
    :caption: Object without ``__str__()`` method overloaded prints their memory address

    class Iris:
        def __init__(self, species):
            self.species = species


    flower = Iris('setosa')

    str(flower)       # <__main__.Iris object at 0x112b366d8>
    print(flower)     # <__main__.Iris object at 0x112b366d8>

.. code-block:: python
    :caption: Objects can verbose print if ``__str__()`` method is present

    class Iris:
        def __init__(self, species):
            self.species = species

        def __str__(self):
            return f'Species: {self.species}'


    flower = Iris('setosa')

    str(flower)       # Species: setosa
    print(flower)     # Species: setosa


``__repr__()``
==============
* ``__repr__()`` jest dla developerów (być jednoznacznym)

.. code-block:: python
    :caption: Using ``__repr__()`` on a class

    class Iris:
        def __init__(self, species):
            self.species = species

        def __repr__(self):
            return f'Iris(species="{self.species}")'


     flower = Iris(species='setosa')

     repr(point)    # Iris(species="setosa")
     point          # Iris(species="setosa")


``__format__()``
================
* ``__format__()`` - do zaawansowanego formatowania

.. code-block:: python

    class Iris:
        def __init__(self, species):
            self.species = species

        def __format__(self, style):
            if style == 'flat':
                return f"({self.x}, {self.y})"
            elif style == '3D':
                return f"({self.x}, {self.y}, {self.z})"
            else:
                raise ValueError

    flower = Iris()

    print(f'{p:flat}')    # (1, 2)
    print(f'{p:3D}')    # (1, 2, 3)


Print formatting in classes
===========================
* Now f-string formatting is preferred

.. code-block:: python

    class Osoba:
        first_name = 'Jan'
        last_name = 'Twardowski'

        def __str__(self):
            return '{first_name} {last_name}'.format(first_name=self.first_name,
                                                     last_name=self.last_name)

.. code-block:: python

    class Osoba:
        first_name = 'Jan'
        last_name = 'Twardowski'

        def __str__(self):
            return '{first_name} {last_name}'.format(**self.__dict__)

.. code-block:: python

    class Osoba:
        first_name = 'Jan'
        last_name = 'Twardowski'

        def __str__(self):
            return f'{self.first_name} {self.last_name}'


Example
=======

Datetime
--------
.. code-block:: python
    :caption: ``__str__``

    import datetime

    print(datetime.datetime.now())
    # 2019-01-05 20:15:00.927387

.. code-block:: python
    :caption: ``__repr__``

    import datetime

    datetime.datetime.now()
    # datetime.datetime(2019, 1, 5, 20, 15, 0, 684972)

List Print
----------
.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name

    crew = [
        Astronaut(name='Jan Twardowski'),
        Astronaut(name='Mark Watney'),
        Astronaut(name='Melissa Lewis'),
    ]

    print(crew)
    # [
    #   <__main__.Astronaut object at 0x107871160>,
    #   <__main__.Astronaut object at 0x107c422e8>,
    #   <__main__.Astronaut object at 0x108156be0>
    # ]

.. code-block:: python

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f'{self.name}'

    crew = [
        Astronaut(name='Jan Twardowski'),
        Astronaut(name='Mark Watney'),
        Astronaut(name='Melissa Lewis'),
    ]

    print(crew)
    # [Jan Twardowski, Mark Watney, Melissa Lewis]
