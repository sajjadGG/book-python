*******************************
Function Decorator with Methods
*******************************


Syntax
======
* ``decorator`` is a decorator name
* ``method`` is a method name
* ``instance`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

Syntax:
    .. code-block:: python

        class MyClass:
            @decorator
            def my_method(self, *args, **kwargs):
                pass


        obj = MyClass()
        obj.my_method()

Is equivalent to:
    .. code-block:: python

        class MyClass:
            def my_method(self, *args, **kwargs):
                pass


        obj = MyClass()
        obj.my_method = decorator(obj.my_method)


Definition
==========
* ``decorator`` is a decorator name
* ``method`` is a method name
* ``instance`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

.. code-block:: python

    def decorator(method):
        def wrapper(instance, *args, **kwargs):
            return method(instance, *args, **kwargs)
        return wrapper


Usage
=====
.. code-block:: python

    def if_permitted(method):
        def wrapper(instance, *args, **kwargs):
            if instance.can_something:
                return method(instance, *args, **kwargs)
            else:
                print('Sorry, you cannot do anything')
        return wrapper


    class MyClass:
        def __init__(self):
            self.can_something = True

        @if_permitted
        def do_something(self):
            print('Doing...')

        @if_permitted
        def do_something_else(self):
            print('Doing something else...')


    my = MyClass()

    my.do_something()           # Doing...
    my.do_something_else()      # Doing something else...

    my.can_something = False

    my.do_something()           # Sorry, you cannot do anything
    my.do_something_else()      # Sorry, you cannot do anything


Examples
========

Make Paragraph
--------------
.. code-block:: python

    def make_paragraph(method):

        def wrapper(instance, *args, **kwargs):
            value = method(instance, *args, **kwargs)
            print(f'<p>{value}</p>')
            return value

        return wrapper


    class HTMLReport:

        @make_paragraph
        def first_method(self, *args, **kwargs):
            return 'First Method'

        @make_paragraph
        def second_method(self, *args, **kwargs):
            return 'Second Method'


    if __name__ == "__main__":
        x = HTMLReport()
        x.first_method()
        x.second_method()

    """
    <p>First Method</p>
    <p>Second Method</p>
    """
