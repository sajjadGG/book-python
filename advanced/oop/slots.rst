OOP Slots
=========


Rationale
---------
* Faster attribute access
* Space savings in memory (overhead of dict for every object)
* Prevents from adding new attributes
* The space savings is from:
* Store value references in slots instead of ``__dict__``
* Denying ``__dict__`` and ``__weakref__`` creation if parent classes deny them and you declare ``__slots__``

.. code-block:: python

    class Astronaut:
        __slots__ = ('firstname', 'lastname')


    astro = Astronaut()

    astro.firstname = 'Mark'
    astro.lastname = 'Watney'

    astro.mission = 'Ares 3'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


Example
-------
.. code-block:: python

    class Astronaut:
        __slots__ = ()


    astro = Astronaut()

    astro.name = 'Mark Watney'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'name'

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)


    astro = Astronaut()

    astro.name = 'Mark Watney'
    astro.mission = 'Ares 3'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


``__slots__`` and ``__dict__``
------------------------------
* Using ``__slots__`` will prevent from creating ``__dict__``

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)


    astro = Astronaut()
    astro.name = 'Mark Watney'

    print(astro.__slots__)
    # ('name',)

    print(astro.__dict__)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__dict__'

.. code-block:: python

    class Astronaut:
        __slots__ = ('__dict__', 'name')


    astro = Astronaut()
    astro.name = 'Mark Watney'   # will use __slots__
    astro.mission = 'Ares 3'     # will use __dict__

    print(astro.__slots__)
    # ('__dict__', 'name')

    print(astro.__dict__)
    # {'mission': 'Ares 3'}


Slots and Methods
-----------------
.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def say_hello(self):
            print(f'My name... {self.name}')


    astro = Astronaut()
    astro.name = 'Mark Watney'
    astro.say_hello()


Slots and Init
--------------
.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def __init__(self, name)
            self.name = name


    astro = Astronaut('Mark Watney')
    print(astro.name)
    # Mark Watney

.. code-block:: python

    class Astronaut:
        __slots__ = ('name',)

        def __init__(self, name, mission):
            self.name = name
            self.mission = mission


    astro = Astronaut('Mark Watney', 'Ares 3')
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'mission'


Inheritance
-----------
* Slots do not inherit, unless they are specified in subclass
* Slots are added on inheritance

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)

    class Astronaut(Pilot):
        pass


    astro = Astronaut()
    astro.name = 'Mark Watney'
    astro.mission = 'Ares 3'

    print(astro.mission)
    # Ares 3

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)

    class Astronaut(Pilot):
        __slots__ = ('name', 'mission')


    astro = Astronaut()
    astro.firstname = 'Mark Watney'
    astro.mission = 'Ares 3'
    astro.rank = 'Senior'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'rank'

.. code-block:: python

    class Pilot:
        __slots__ = ('name',)


    class Astronaut(Pilot):
        __slots__ = ('mission',)


    astro = Astronaut()
    astro.name = 'Mark Watney'
    astro.mission = 'Ares 3'
    astro.rank = 'Senior'
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute 'rank'


Use Cases
---------
.. code-block:: python

    class Astronaut:
        __slots__ = ('firstname', 'lastname')


    astro = Astronaut()
    astro.firstname = 'Mark'
    astro.lastname = 'Watney'

    print(astro.firstname)
    # Mark

    print(astro.lastname)
    # Watney

    print(astro.__slots__)
    # ('firstname', 'lastname')

    print(astro.__dict__)
    # Traceback (most recent call last):
    # AttributeError: 'Astronaut' object has no attribute '__dict__'

    result = {attr: getattr(astro, attr)
              for attr in astro.__slots__}

    print(result)
    # {'firstname': 'Mark', 'lastname': 'Watney'}

Use Case - Deep Size
--------------------
.. code-block:: python

    from sys import getsizeof, stderr
    from itertools import chain
    from collections import deque
    import logging


    logging.basicConfig(
        level='DEBUG')
    log = logging.getLogger('sizeof')


    def total_size(o, handlers={}):
        """
        Returns the approximate memory footprint an object and all of its contents.

        Automatically finds the contents of the following builtin containers and
        their subclasses: tuple, list, deque, dict, set and frozenset
        """
        dict_handler = lambda d: chain.from_iterable(d.items())
        all_handlers = {tuple: iter,
                        list: iter,
                        deque: iter,
                        dict: dict_handler,
                        set: iter,
                        frozenset: iter}
        all_handlers.update(handlers)     # user handlers take precedence
        seen = set()                      # track which object id's have already been seen
        default_size = getsizeof(0)       # estimate sizeof object without __sizeof__

        def sizeof(o):
            if id(o) in seen:       # do not double count the same object
                return 0
            seen.add(id(o))
            s = getsizeof(o, default_size)

            log.debug('Size: %s, Type: %s, Repr: %s', s, type(o), repr(o))

            for typ, handler in all_handlers.items():
                if isinstance(o, typ):
                    s += sum(map(sizeof, handler(o)))
                    break
            else:
                if not hasattr(o.__class__, '__slots__'):
                    if hasattr(o, '__dict__'):
                        # no __slots__ *usually* means a
                        # __dict__, but some special builtin classes (such
                        # as `type(None)`) have neither
                        # else, `o` has no attributes at all, so sys.getsizeof()
                        # actually returned the correct value
                        s += sizeof(o.__dict__)
                else:
                    s += sum(
                        sizeof(getattr(o, x))
                               for x in o.__class__.__slots__
                               if hasattr(o, x))
            return s
        return sizeof(o)


    if __name__ == '__main__':
        # d = dict(a=1, b=2, c=3, d=[4,5,6,7], e='a string of chars')
        # print(total_size(d, verbose=True))
        # print(getsizeof(d))

        class Astronaut:
            __slots__ = ('firstname', 'lastname')

        class Cosmonaut:
            pass

        a = Astronaut()
        a.firstname = 'Mark'
        a.lastname = 'Watney'

        c = Cosmonaut()
        c.firstname = 'Mark'
        c.lastname = 'Watney'

        # DEBUG:sizeof:Size: 48, Type: <class '__main__.Astronaut'>, Repr: <__main__.Astronaut object at 0x10790b940>
        # DEBUG:sizeof:Size: 53, Type: <class 'str'>, Repr: 'Mark'
        # DEBUG:sizeof:Size: 55, Type: <class 'str'>, Repr: 'Watney'
        # DEBUG:sizeof:Size: 48, Type: <class '__main__.Cosmonaut'>, Repr: <__main__.Cosmonaut object at 0x10790b9d0>
        # DEBUG:sizeof:Size: 104, Type: <class 'dict'>, Repr: {'firstname': 'Mark', 'lastname': 'Watney'}
        # DEBUG:sizeof:Size: 58, Type: <class 'str'>, Repr: 'firstname'
        # DEBUG:sizeof:Size: 53, Type: <class 'str'>, Repr: 'Mark'
        # DEBUG:sizeof:Size: 57, Type: <class 'str'>, Repr: 'lastname'
        # DEBUG:sizeof:Size: 55, Type: <class 'str'>, Repr: 'Watney'
        # Astronaut 156
        # Cosmonaut 375

        print('Astronaut', total_size(a))
        # Astronaut 156

        print('Cosmonaut', total_size(c))
        # Cosmonaut 375




Assignments
-----------
.. literalinclude:: assignments/oop_slots_define.py
    :caption: :download:`Solution <assignments/oop_slots_define.py>`
    :end-before: # Solution
