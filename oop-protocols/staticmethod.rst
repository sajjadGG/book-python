****************
``staticmethod``
****************


Rationale
=========
* Should **not** be in a class: method which don't use ``self`` in its body
* Should be in class: if method takes ``self`` and use it (it requires instances to work)
* If a method don't use ``self`` but uses class as a namespace use ``@staticmethod`` decorator


Application
===========
* Using class as namespace
* No need to create a class instance
* Will not pass instance (``self``) as a first method argument


Implementation
==============
.. code-block:: python

    class MyClass:

        @staticmethod
        def say_hello():
            print('hello')


     MyClass.say_hello()


Use case
========
.. code-block:: python
    :caption: Functions on a high level of a module lack namespace

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b


    add(1, 2)
    sub(8, 4)

.. code-block:: python
    :caption: When ``add`` and ``sub`` are in ``Calculator`` class (namespace) they get instance (``self``) as a first argument. Instantiating Calculator is not needed, as of functions do not read or write to instance variables.

    class Calculator:

        def add(self, a, b):
            return a + b

        def sub(self, a, b):
            return a - b


    Calculator.add(10, 20)  # TypeError: add() missing 1 required positional argument: 'b'
    Calculator.sub(8, 4)    # TypeError: add() missing 1 required positional argument: 'b'

    calc = Calculator()
    calc.add(1, 2)          # 3
    calc.sub(8, 4)          # 4

.. code-block:: python
    :caption: Class ``Calculator`` is a namespace for functions. ``@staticmethod`` remove instance (``self``) argument to method.

    class Calculator:

        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def sub(a, b):
            return a - b


    Calculator.add(1, 2)
    Calculator.sub(8, 4)
