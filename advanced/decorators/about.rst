****************
About Decorators
****************


What are decorators?
====================
* Decorator is an object, which takes another object as it's argument
* Decorators can:

    * Do things before call
    * Do things after call
    * Modify arguments
    * Modify returned value
    * Avoid calling
    * Modify globals
    * Add or change metadata


Types of decorators
===================
By type:

    * Function Decorators
    * Class Decorators

By decorated object:

    * Decorating function
    * Decorating class
    * Decorating methods

By number of arguments:

    * Without arguments
    * With arguments


Function Decorate Function
==========================
.. code-block:: python

    @decorator
    def my_function(*args, **kwargs):
        pass


Function Decorate Method
========================
.. code-block:: python

    class MyClass:
        @decorator
        def my_method(self, *args, **kwargs):
            pass


Function Decorate Class
=======================
.. code-block:: python

    @decorator
    class MyClass:
        pass


Class Decorate Function
=======================
.. code-block:: python

    @Decorator
    def my_function(*args, **kwargs):
        pass


Decorator with arguments
========================
.. code-block:: python
    :caption: Decorator with arguments

    @decorator(a, b)
    def my_function(*args, **kwargs):
        pass


Decorator library
=================
* https://wiki.python.org/moin/PythonDecoratorLibrary
