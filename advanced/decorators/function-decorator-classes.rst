*******************************
Function Decorator with Classes
*******************************


Syntax
======
* ``decorator`` is a decorator name
* ``MyClass`` is a class name

Syntax:
    .. code-block:: python

        @decorator
        class MyClass:
            pass

Is equivalent to:
    .. code-block:: python

        MyClass = decorator(MyClass)


Definition
==========
* ``decorator`` is decorator name
* ``cls`` is a pointer to class which is being decorated (``MyClass`` in this case)
* Decorator must return pointer to ``Wrapper``
* ``Wrapper`` is a closure class
* ``Wrapper`` name is a convention, but you can name it anyhow
* ``Wrapper`` inherits from ``MyClass`` so it is almost identical
* decorator must return pointer to ``Wrapper``

.. code-block:: python

    def decorator(cls):
        class Wrapper(cls):
            attribute = 'some value...'
        return Wrapper


Usage
=====
.. code-block:: python

    def decorator(cls):
        class Wrapper(cls):
            attribute = 'some value...'
        return Wrapper


    @decorator
    class MyClass:
        pass


    print(MyClass.attribute)
    # some value...


Examples
========

Singleton
---------
.. code-block:: python

    def singleton(cls):

        class Wrapper(cls):
            def __new__(cls, *args, **kwargs):

                if not hasattr(cls, '_instance'):
                    print('First use, creating instance')
                    instance = object.__new__(cls, *args, **kwargs)
                    setattr(cls, '_instance', instance)
                else:
                    print('Reusing instance')
                return getattr(cls, '_instance')

        return Wrapper


    @singleton
    class DatabaseConnection:
        def connect(self):
            print(f'Connecting... using {self._instance}')


    a = DatabaseConnection()    # First use, creating instance
    a.connect()                 # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x10372d310>

    b = DatabaseConnection()    # Reusing instance
    b.connect()                 # Connecting... using <__main__.singleton.<locals>.Wrapper object at 0x10372d310>
