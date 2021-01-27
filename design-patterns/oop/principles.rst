OOP Principles
==============


Rationale
---------
* Encapsulation
* Abstraction
* Inheritance
* Polymorphism


Encapsulation
-------------
* Do not allow to modify attributes directly
* Hide them behind setters and getters
* Prevents objects to get to an invalid state

.. code-block:: python

    position_x = 0
    position_y = 0

    def position_set(x, y):
        global position_x
        global position_y
        position_x = x
        position_y = y

    def position_get():
        return position_x, position_y

    position_set(1, 2)
    position_get()
    # (1, 2)

.. code-block:: python

    class Position:
        x: int = 0
        y: int = 0

        def set(self, x, y):
            self.x = x
            self.y = y

        def get(self):
            return self.x, self.y

    position = Position()
    position.set(1, 2)
    position.get()
    # (1, 2)


Abstraction
-----------
* Reduce complexity by hiding unnecessary details
* User do not need what does it mean to send email, that you have to connect, auth and later disconnect

.. code-block:: python

    class MailService:
        def send_email(sender, rcpt, subject, body):
            self._connect()
            self._authenticate()
            self._send(sender, rcpt, subject, body)
            self._disconnect()

        def _connect(self, timeout=1):
            print('Connect')

        def _authenticate(self):
            print('Authenticate')

        def _send(sender, rcpt, subject, body):
            print('Sending')

        def _disconnect(self):
            print('Disconnect')


    if __name__ == '__main__':
        ms = MailService()
        ms.send_email(...)

.. todo:: Make example space related MarsMission and Astronauts


Inheritance
-----------
.. code-block:: python

    class Person:
        firstname: str
        lastname: str

        def say_hello(self):
            print(f'Hello {self.firstname} {self.lastname}')


    class Astronaut(Person):
        pass


    astro = Astronaut()
    astro.firstname = 'Mark'
    astro.lastname = 'Watney'
    astro.say_hello()
    # Hello Mark Watney


Polymorphism
------------
* Ability of an object to take many forms

.. code-block:: python

    class Person:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            pass

    class Astronaut(Person):
        def say_hello(self):
            return f'Hello {self.name}'

    class Cosmonaut(Person):
        def say_hello(self):
            return f'Привет {self.name}'


    def hello(crew: list[Person]) -> None:
        for member in crew:
            print(member.say_hello())


    if __name__ == '__main__':
        crew = [Astronaut('Mark Watney'),
                Cosmonaut('Иван Иванович'),
                Astronaut('Melissa Lewis'),
                Cosmonaut('Jan Twardowski')]

        hello(crew)
    # Hello Mark Watney
    # Привет Иван Иванович
    # Hello Melissa Lewis
    # Привет Jan Twardowski


Further Reading
---------------
* https://www.youtube.com/watch?v=NU_1StN5Tkk
