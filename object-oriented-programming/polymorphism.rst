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


Polymorphism on Function
========================
.. code-block:: python
    :caption: Polymorphism on Function

    class Astronaut:
        def say_hello(self):
            print('Howdy from NASA')

    class Cosmonaut:
        def say_hello(self):
            print('Privyet z Roscosmos')


    def hello(spaceman):
        spaceman.say_hello()


    watney = Astronaut()
    ivanovic = Cosmonaut()


    hello(watney)
    # Howdy from NASA

    hello(ivanovic)
    # Privyet z Roscosmos


Polymorphism on Classes
=======================
.. code-block:: python
    :caption: Polymorphism on Classes

    class Spaceman:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            raise NotImplementedError


    class Astronaut(Spaceman):
        def say_hello(self):
            print(f'Howdy from NASA')


    class Cosmonaut(Spaceman):
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
