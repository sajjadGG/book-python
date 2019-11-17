************
Polymorphism
************


Switch
======
.. code-block:: python
    :caption: Switch moves business logic to the execution place

    agency = 'NASA'

    if agency == 'NASA':
        print('Howdy from NASA')
    elif agency == 'Roscosmos':
        print('Privyet z Roscosmos')
    elif agency == 'ESA':
        print('Guten Tag aus ESA')
    else:
        raise NotImplementedError

.. code-block:: python

    def switch(key=None):
        return {
            'NASA': 'Howdy from NASA',
            'Roscosmos': 'Privyet z Roscosmos',
            'ESA': 'Guten Tag aus ESA',
        }.get(key, 'Default Value')


Polymorphism on Function
========================
.. code-block:: python
    :caption: Polymorphism on Function

    class Person:
        def __init__(self, name):
            self.name = name


    class Astronaut(Person):
        def say_hello(self):
            print('Howdy from NASA')

    class Cosmonaut(Person):
        def say_hello(self):
            print('Privyet z Roscosmos')


    def hello(spaceman):
        spaceman.say_hello()


    watney = Astronaut('Mark Watney')
    ivanovic = Cosmonaut('Ivan Ivanovic')

    hello(watney)
    # Howdy from NASA

    hello(ivanovic)
    # Privyet z Roscosmos


Polymorphism on Classes
=======================
.. code-block:: python
    :caption: Polymorphism on Classes

    class Person:
        def __init__(self, name):
            self.name = name


    class Astronaut(Person):
        def say_hello(self):
            print(f'Howdy from NASA')


    class Cosmonaut(Person):
        def say_hello(self):
            print(f'Privyet z Roscosmos')


    crew = [
        Astronaut('Mark Watney'),
        Cosmonaut('Иван Иванович'),
        Astronaut('Matt Kowalski'),
        Cosmonaut('Jan Twardowski'),
    ]

    for member in crew:
        member.say_hello()
        # Howdy from NASA
        # Privyet z Roscosmos
        # Howdy from NASA
        # Privyet z Roscosmos
