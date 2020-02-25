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


How decorator works
===================

Without arguments
-----------------
Decorator:
    .. code-block:: python

        @my_decorator
        def my_function(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        my_function = my_decorator(my_function)

With arguments
--------------
Decorator:
    .. code-block:: python

        @my_decorator(a, b)
        def my_function(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        my_function = my_decorator(a, b)(my_function)


Decorator library
=================
* https://wiki.python.org/moin/PythonDecoratorLibrary
