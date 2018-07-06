*********
Metaclass
*********

A metaclass is the class of a class. Like a class defines how an instance of the class behaves, a metaclass defines how a class behaves. A class is an instance of a metaclass.

.. figure:: img/metaclass.png
    :scale: 75%
    :align: center

    A metaclass is the class of a class. Like a class defines how an instance of the class behaves, a metaclass defines how a class behaves. A class is an instance of a metaclass.

A metaclass is most commonly used as a class-factory. Like you create an instance of the class by calling the class, Python creates a new class (when it executes the 'class' statement) by calling the metaclass. Combined with the normal ``__init__`` and ``__new__`` methods, metaclasses therefore allow you to do 'extra things' when creating a class, like registering the new class with some registry, or even replace the class with something else entirely.

When the ``class`` statement is executed, Python first executes the body of the ``class`` statement as a normal block of code. The resulting namespace (a dict) holds the attributes of the class-to-be. The metaclass is determined by looking at the baseclasses of the class-to-be (metaclasses are inherited), at the ``__metaclass__`` attribute of the class-to-be (if any) or the ``__metaclass__`` global variable. The metaclass is then called with the name, bases and attributes of the class to instantiate it.

However, metaclasses actually define the *type* of a class, not just a factory for it, so you can do much more with them. You can, for instance, define normal methods on the metaclass. These metaclass-methods are like classmethods, in that they can be called on the class without an instance, but they are also not like classmethods in that they cannot be called on an instance of the class. ``type.__subclasses__()`` is an example of a method on the ``type`` metaclass. You can also define the normal 'magic' methods, like ``__add__``, ``__iter__`` and ``__getattr__``, to implement or change how the class behaves.


