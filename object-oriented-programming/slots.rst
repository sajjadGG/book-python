*************
``__slots__``
*************


* faster attribute access
* space savings in memory

Instead of having a dynamic dict that allows adding attributes to objects at anytime, there is a static structure which does not allow additions after creation. This saves the overhead of one dict for every object that uses slots

Unfortunately there is a side effect to slots. They change the behavior of the objects that have slots in a way that can be abused by control freaks and static typing weenies. This is bad, because the control freaks should be abusing the metaclasses and the static typing weenies should be abusing decorators, since in Python, there should be only one obvious way of doing something.

The space savings is from:

    * Storing value references in slots instead of ``__dict__``.
    * Denying ``__dict__`` and ``__weakref__`` creation if parent classes deny them and you declare ``__slots__``.

Using
=====
.. code-block:: python

    class Iris:
        __slots__ = ()

    flower = Iris()

    flower.species = 'setosa'
    # AttributeError: 'Iris' object has no attribute 'species'

.. code-block:: python

    class Iris:
        __slots__ = ('species',)

    flower = Iris()

    flower.species = 'setosa'
    flower.kingdom = 'plantae'
    # AttributeError: 'Iris' object has no attribute 'kingdom'


``__slots__`` and ``__dict__``
==============================
.. code-block:: python
    :caption: Using ``__slots__`` will prevent from creating ``__dict__``

    class Iris:
        __slots__ = ('species', 'kingdom')

    flower = Iris()

    flower.species = 'setosa'
    flower.kingdom = 'plantae'

    flower.__dict__
    # AttributeError: 'Iris' object has no attribute '__dict__'

.. code-block:: python

    class Iris:
        __slots__ = ('__dict__', 'species')

    flower = Iris()

    flower.species = 'setosa'   # will use slots
    flower.kingdom = 'plantae'  # not in __slots__, will use __dict__

    flower.__dict__
    # {'kingdom': 'plantae'}


Inheritance
===========
.. code-block:: python

    class Iris:
        __slots__ = 'species', 'kingdom'

    class Setosa(Iris):
        __slots__ = 'name',

    class Virginica(Iris):
        __slots__ = 'species', 'kingdom', 'name'  # redundant species and kingdom


More info
=========
.. note:: More info: https://stackoverflow.com/questions/472000/usage-of-slots
