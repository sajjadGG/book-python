OOP Methods
===========


Rationale
---------
* Methods are functions in the class
* First argument is always instance (``self``)
* While calling function you never pass ``self``
* Prevents copy-paste code
* Improves readability
* Improves refactoring
* Decomposes bigger problem into smaller chunks

.. glossary::

    method
        Functions in the class which takes instance as first argument (``self``)

Syntax:

.. code-block:: python

    class MyClass:
        def mymethod(self):
            ...

    my = MyClass()
    my.mymethod()


Methods Without Arguments
-------------------------
Methods without arguments:

.. code-block:: python

    class Astronaut:
        def say_hello(self):
            print('My name... José Jiménez')


    jose = Astronaut()
    jose.say_hello()
    # My name... José Jiménez


Methods With Required Argument
------------------------------
Methods with required argument:

.. code-block:: python

    class Astronaut:
        def say_hello(self, name):
            print(f'My name... {name}')


    jose = Astronaut()

    jose.say_hello(name='José Jiménez')
    # My name... José Jiménez

    jose.say_hello('José Jiménez')
    # My name... José Jiménez

    jose.say_hello()
    # Traceback (most recent call last):
    # TypeError: say_hello() missing 1 required positional argument: 'name'


Methods With Optional Argument
------------------------------
Methods with arguments with default value:

.. code-block:: python

    class Astronaut:
        def say_hello(self, name='Unknown'):
            print(f'My name... {name}')


    jose = Astronaut()

    jose.say_hello(name='José Jiménez')
    # My name... José Jiménez

    jose.say_hello('José Jiménez')
    # My name... José Jiménez

    jose.say_hello()
    # My name... Unknown


Assignments
-----------
.. literalinclude:: assignments/oop_method_syntax.py
    :caption: :download:`Solution <assignments/oop_method_syntax.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_method_mean.py
    :caption: :download:`Solution <assignments/oop_method_mean.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_method_call.py
    :caption: :download:`Solution <assignments/oop_method_call.py>`
    :end-before: # Solution
