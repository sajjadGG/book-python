*************************
New and Old style classes
*************************


* https://docs.python.org/dev/tutorial/classes.html


New Style Class
===============
* Inherit from object
* Or from another new style class

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

Old Style classes
=================
* Don't inherit from ``object``

.. class:: python

    class SomeObject:
        pass

.. note:: In Python 3, there are no old-style classes, and this code will produce new style class


Python 2 vs 3
=============
* Old style classes are **only** in Python 2
* New style classes works in Python 2 (when inherit from object)
* In Python 3 all classes always inherit from object, hence they are new style classes
