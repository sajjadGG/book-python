*************************
New and Old style classes
*************************


Rationale
---------
* https://docs.python.org/dev/tutorial/classes.html
* The major motivation for introducing new-style classes is to provide a unified object model with a full meta-model


New Style Class
===============
* Introduced in Python 2.2
* In Python 3 this is the only way
* Inherit from object or from another new style class
* Ability to subclass most built-in types
* ``super()`` added
* MRO changed
* descriptors added
* new style class objects cannot be raised unless derived from Exception
* ``__slots__`` added

.. code-block:: python
    :caption: New Style Class

    class MyClass(object):
        pass

.. code-block:: python
    :caption: New Style Class

    class MyClass(object):
        pass

    class OtherClass(MyClass):
        pass

.. code-block:: python
    :caption: In Python 3, there are no old-style classes, and this code will produce new style class

    class SomeObject:
        pass


Old Style classes
=================
* Not existing in Python 3
* Don't inherit from ``object``

.. code-block:: python

    class SomeObject:
        pass

.. note:: In Python 3, there are no old-style classes, and this code will produce new style class


Python 2 vs 3
=============
* Old style classes are **only** in Python 2
* New style classes works in Python 2 (when inherit from object)
* In Python 3 all classes always inherit from object, hence they are new style classes
