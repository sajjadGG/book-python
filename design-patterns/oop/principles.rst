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

    class KelvinTemperature:
        _value: float

        def set_value(self, value: float) -> None:
            if value >= 0:
                self._value = value

        def get_value(self) -> float:
            return self._value


    t = KelvinTemperature()
    t.set_value(1)
    t.set_value(0)
    t.set_value(-1)
    t.get_value()

.. code-block:: python

    class Astronaut:
        _firstname: str
        _lastname: str

        def set_name(self, name):
            fname, lname = name.split()
            self._firstname = fname
            self._lastname = lname

        def get_name(self):
            return f'{self._firstname} {self._lastname}'

    astro = Astronaut()
    astro.set_name('Mark Watney')
    astro.get_name()


Abstraction
-----------
* Reduce complexity by hiding unnecessary details
* User do not need what does it mean to send email, that you have to connect, auth and later disconnect

.. code-block:: python

    class MailService:
        def send_email(sender, rcpt, subject, body):
            self._connect()
            self._authenticate()
            self._disconnect()

        def _connect(self, timeout=1):
            print('Connect')

        def _authenticate(self):
            print('Authenticate')

        def _disconnect(self):
            print('Disconnect')


    if __name__ == '__main__':
        ms = MailService()
        ms.send_email(...)


Inheritance
-----------
.. code-block:: python

    class Person:
        _firstname: str
        _lastname: str

    class Astronaut(Person):
        pass


Polymorphism
------------
* Ability of an object to take many forms

.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class UIElement(metaclass=ABCMeta):
        @abstractmethod
        def draw(self):
            pass

    class TextBox(UIElement):
        def draw(self):
            print('Drawing text box')


    class CheckBox(UIElement):
        def draw(self):
            print('Drawing check box')


    def draw(element: UIElement):
        element.draw()


    if __name__ == '__main__':
        draw(TextBox())
        draw(CheckBox())

.. code-block:: python

    class Cache:
        def set(self, name: str, value: str) -> None: pass
        def get(self, name: str) -> str: pass
        def is_valid(self, name: str) -> bool: pass

    class DatabaseCache(Cache):
        pass

    class MemoryCache(Cache):
        pass

    class FilesystemCache(Cache):
        pass


    def get(cache: Cache, key):
        if not cache.is_valid(key):
            cache.set(key, '...')
        return cache.get(key)


    get(DatabaseCache(), 'name')
    get(FilesystemCache(), 'name')
    get(MemoryCache(), 'name')


Further Reading
---------------
* https://www.youtube.com/watch?v=NU_1StN5Tkk
