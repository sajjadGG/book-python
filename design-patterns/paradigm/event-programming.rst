Event Programming
=================



Rationale
---------
* EN: Callback Design
* PL:


Metaclass
---------
>>> class EventListener(type):
...     listeners: dict[str, list[callable]] = {}
...
...     @classmethod
...     def register(cls, *clsnames):
...         def wrapper(func):
...             for clsname in clsnames:
...                 if clsname not in cls.listeners:
...                     cls.listeners[clsname] = []
...                 cls.listeners[clsname] += [func]
...         return wrapper
...
...     def __new__(mcs, classname, bases, attrs):
...         for listener in mcs.listeners.get(classname, []):
...             listener.__call__(classname, bases, attrs)
...         return type(classname, bases, attrs)
>>>
>>>
>>> @EventListener.register('Astronaut')
... def hello_class(clsname, bases, attrs):
...     print(f'\n\nHello new class {clsname}\n')
>>>
>>>
>>> @EventListener.register('Astronaut', 'Person')
... def print_name(clsname, bases, attrs):
...     print('\nNew class created')
...     print('Classname:', clsname)
...     print('Bases:', bases)
...     print('Attrs:', attrs)
>>>
>>>
>>> class Person(metaclass=EventListener):
...     pass
<BLANKLINE>
New class created
Classname: Person
Bases: ()
Attrs: {'__module__': 'builtins', '__qualname__': 'Person'}
>>>
>>> class Astronaut(Person, metaclass=EventListener):
...     pass
<BLANKLINE>
<BLANKLINE>
Hello new class Astronaut
<BLANKLINE>
<BLANKLINE>
New class created
Classname: Astronaut
Bases: (<class 'Person'>,)
Attrs: {'__module__': 'builtins', '__qualname__': 'Astronaut'}


Implementation
--------------
.. code-block:: python

    class event:
        __slots__ = ('__subscribers', )

        def __init__(self):
            self.__subscribers = set()

        def call(self, *args, **kwargs):
            for subscriber in self.__subscribers:
                subscriber(*args, **kwargs)
        __call__ = call

        def register(self, function):
            self.__subscribers.add(function)
            return self
        __add__ = __iadd__ = register

        def unregister(self, function):
            self.__subscribers.remove(function)
            return self
        __sub__ = __isub__ = unregister

    class EventManager:
        @staticmethod
        def register(name):
            if not hasattr(EventManager, name):
                setattr(EventManager, name, event())
            return getattr(EventManager, name).register


Usage:

.. code-block:: python

    @EventManager.register('on_foo')
    def foo(*args, **kwargs):
        print('Args: ' + str(args), 'Kwargs: ' + str(kwargs))

    def call_on_foo():
        EventManager.on_foo()
        EventManager.on_foo(1, 2, 3)
        EventManager.on_foo(a=1, b=2, c=3)
        EventManager.on_foo(1, 2, 3, a=1, b=2, c=3)

    @EventManager.register('on_bar')
    def bar():
        call_on_foo()

    EventManager.on_bar()

Use:

.. code-block:: python

    EventManager.on_bar + funkcja

.. code-block:: python

    EventManager.on_bar += funkcja


Assignments
-----------
.. literalinclude:: assignments/paradigm_event_a.py
    :caption: :download:`Solution <assignments/paradigm_event_a.py>`
    :end-before: # Solution
