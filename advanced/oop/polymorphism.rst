************
Polymorphism
************


Switch
======
.. code-block:: python
    :caption: Switch moves business logic to the execution place

    watney = 'Astronaut'

    if watney == 'Astronaut':
        print('Hello')
    elif watney == 'Cosmonaut':
        print('Привет!')
    elif watney == 'Taikonaut':
        print('你好')
    else:
        print('Default Value')

    # Hello

.. code-block:: python

    def say_hello(key=None):
        return {
            'Astronaut': 'Hello',
            'Cosmonaut': 'Привет!',
            'Taikonaut': '你好',
        }.get(key, 'Default Value')


    watney = 'Astronaut'
    ivanovic = 'Cosmonaut'
    twardowski = 'Sorcerer'

    say_hello(watney)
    # Hello

    say_hello(ivanovic)
    # Привет!

    say_hello(twardowski):
    # 'Default Value'


Polymorphism in a Function
==========================
.. code-block:: python
    :caption: Polymorphism on Function

    class Sorcerer:
        pass

    class Astronaut:
        def say_hello(self):
            return 'Hello'

    class Cosmonaut:
        def say_hello(self):
            return 'Привет!'


    def say_hello(spaceman):
        if hasattr(spaceman, 'say_hello')
            return spaceman.say_hello()
        else:
            return 'Default Value'


    watney = Astronaut()
    ivanovic = Cosmonaut()
    twardowski = Sorcerer()

    say_hello(watney)
    # Hello

    say_hello(ivanovic)
    # Привет!

    say_hello(twardowski)
    # 'Default Value'


Polymorphism on a Class
=======================
.. code-block:: python
    :caption: Polymorphism on Classes

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            return 'Hello'


    class Cosmonaut:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            return 'Привет!'


    crew = [
        Astronaut('Mark Watney'),
        Cosmonaut('Иван Иванович'),
        Astronaut('Matt Kowalski'),
        Cosmonaut('Jan Twardowski'),
    ]

    for member in crew:
        print(member.say_hello())
    # Hello
    # Привет!
    # Hello
    # Привет!


Assignments
===========
.. todo:: Create Assignments
