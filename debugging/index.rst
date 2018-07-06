*********
Debugging
*********

Run in the console
==================
* Execute cell
* Run File in the console

``print``
=========
.. code-block:: python

    DATA = ['a', 'b', 'c', [1, 2, 3]]
    for element in DATA:
        print(element)
    # a
    # b
    # c
    # [1, 2, 3]

.. code-block:: python

    USERNAMES = ('José')

    for user in USERNAMES:
        print(user)
    # J
    # o
    # s
    # é

``pprint``
==========
.. code-block:: python

    from pprint import pprint

    pprint(...)

.. code-block:: python

    import json
    from pprint import pprint

    DANE = '{"contacts": [{"id": 1, "created": "2018-06-13T09:57:55.405Z", "modified": "2018-06-13T10:16:13.975Z", "reporter_id": 1, "is_deleted": false, "first_name": "José", "last_name": "Jiménez", "date_of_birth": "1969-07-24", "email": "jose.jimenez@nasa.gov", "bio": "", "image": "33950257662_d7561fb140_o.jpg", "status": null, "gender": null}, {"id": 2, "created": "2018-06-13T10:26:46.948Z", "modified": "2018-06-13T10:26:46.948Z", "reporter_id": 1, "is_deleted": false, "first_name": "Max", "last_name": "Peck", "date_of_birth": null, "email": null, "bio": "", "image": "", "status": null, "gender": null}, {"id": 3, "created": "2018-06-13T10:26:55.820Z", "modified": "2018-06-13T10:26:55.820Z", "reporter_id": 1, "is_deleted": false, "first_name": "Ivan", "last_name": "Ivanovich", "date_of_birth": null, "email": null, "bio": "", "image": "", "status": null, "gender": null}, {"id": 15, "created": "2018-06-13T14:34:42.353Z", "modified": "2018-06-13T14:34:43.638Z", "reporter_id": null, "is_deleted": false, "first_name": "Matt", "last_name": "Harasymczuk", "date_of_birth": null, "email": null, "bio": null, "image": "", "status": null, "gender": null}]}'

    dane = json.loads(DANE)
    pprint(dane)

.. code-block:: python

    pprint(globals())

.. code-block:: python

    from pprint import pprint

    print(globals())
    pprint(globals())

    def hello(a, b, text='My name'):
        first_name = 'José'
        last_name = 'Jiménez'
        pprint(locals())
        return locals()


    hello(1, 2)

``locals()``
============
.. code-block:: python

    def hello(a, b, text='My name'):
        first_name = 'José'
        last_name = 'Jiménez'
        my_vars = locals()
        del my_vars['text']
        return my_vars

``help`` and docstring ``__doc__``
==================================
.. code-block:: python

    help(str)

.. code-block:: python

    def hello(name='José Jiménez'):
        """
        Function displays greeting
        """
        print(f'My name {name}')

    help(hello)

.. literalinclude:: src/debugging-docstring.py
    :language: python
    :caption: Debugging with docstring

``object.__dict__``
===================
.. code-block:: python

    >>> class Astronaut():
    ...    def __init__(self):
    ...        self.first_name = 'José'
    ...        self.last_name = 'Jiménez'

    >>> jose = Astronaut()

    >>> jose.__dict__
    {'first_name': 'José', 'last_name': 'Jiménez'}


``dir()`` i ``object.__dict__``
===============================
* Więcej w :ref:`Introspection`.

.. code-block:: python

    >>> class Astronaut():
    ...    def __init__(self):
    ...        self.first_name = 'José'
    ...        self.last_name = 'Jiménez'

    >>> jose = Astronaut()

    >>> dir(jose)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'first_name', 'last_name']

``json.tool``
=============
.. code-block:: console

    $ curl -s http://localhost:8000/contact/api/
    {"contacts": [{"id": 1, "created": "2018-06-13T09:57:55.405Z", "modified": "2018-06-13T10:16:13.975Z", "reporter_id": 1, "is_deleted": false, "first_name": "José", "last_name": "Jiménez", "date_of_birth": "1969-07-24", "email": "jose.jimenez@nasa.gov", "bio": "", "image": "33950257662_d7561fb140_o.jpg", "status": null, "gender": null}, {"id": 2, "created": "2018-06-13T10:26:46.948Z", "modified": "2018-06-13T10:26:46.948Z", "reporter_id": 1, "is_deleted": false, "first_name": "Max", "last_name": "Peck", "date_of_birth": null, "email": null, "bio": "", "image": "", "status": null, "gender": null}, {"id": 3, "created": "2018-06-13T10:26:55.820Z", "modified": "2018-06-13T10:26:55.820Z", "reporter_id": 1, "is_deleted": false, "first_name": "Ivan", "last_name": "Ivanovich", "date_of_birth": null, "email": null, "bio": "", "image": "", "status": null, "gender": null}]}

.. code-block:: console

    $ curl -s http://localhost:8000/contact/api/ |python -m json.tool
    {
        "contacts": [
            {
                "id": 1,
                "created": "2018-06-13T09:57:55.405Z",
                "modified": "2018-06-13T10:16:13.975Z",
                "reporter_id": 1,
                "is_deleted": false,
                "first_name": "José",
                "last_name": "Jiménez",
                "date_of_birth": "1969-07-24",
                "email": "jose.jimenez@nasa.gov",
                "bio": "",
                "image": "33950257662_d7561fb140_o.jpg",
                "status": null,
                "gender": null
            },
            {
                "id": 2,
                "created": "2018-06-13T10:26:46.948Z",
                "modified": "2018-06-13T10:26:46.948Z",
                "reporter_id": 1,
                "is_deleted": false,
                "first_name": "Max",
                "last_name": "Peck",
                "date_of_birth": null,
                "email": null,
                "bio": "",
                "image": "",
                "status": null,
                "gender": null
            },
            {
                "id": 3,
                "created": "2018-06-13T10:26:55.820Z",
                "modified": "2018-06-13T10:26:55.820Z",
                "reporter_id": 1,
                "is_deleted": false,
                "first_name": "Ivan",
                "last_name": "Ivanovich",
                "date_of_birth": null,
                "email": null,
                "bio": "",
                "image": "",
                "status": null,
                "gender": null
            },
        ]
    }

Using ``pdb``
=============
.. code-block:: python

    print('Jose Jimenez')
    import pdb; pdb.set_trace()
    print('Max Peck')

``breakpoint()``
================
.. code-block:: python

    print('Jose Jimenez')
    breakpoint()
    print('Max Peck')

* ``sys.breakpointhook()``
* ``sys.__breakpointhook__``
* By default, ``sys.breakpointhook()`` implements the actual importing and entry into ``pdb.set_trace()``.
* It can be set to a different function to change the debugger that ``breakpoint()`` enters.

.. code-block:: python

    os.environ['PYTHONBREAKPOINT'] = 'foo.bar.baz'
    breakpoint()    # Imports foo.bar and calls foo.bar.baz()


Using debugger in IDE
=====================

Break Point
-----------

View Breakpoints
~~~~~~~~~~~~~~~~

Mute Breakpoints
~~~~~~~~~~~~~~~~

Poruszanie się
--------------

Step Over
~~~~~~~~~

Step Into My Code
~~~~~~~~~~~~~~~~~

Force Step Into
~~~~~~~~~~~~~~~

Show Execution Point
~~~~~~~~~~~~~~~~~~~~

Step Out
~~~~~~~~

Run to Cursor
~~~~~~~~~~~~~

Resume Program
~~~~~~~~~~~~~~

New Watch
~~~~~~~~~

Frames
------

Previous Frame
~~~~~~~~~~~~~~

Next Frame
~~~~~~~~~~

Threads
~~~~~~~

Scope
-----

Special Variables
~~~~~~~~~~~~~~~~~

* ``__file__``
* ``__name__``
* ``__builtins__``
* ``__doc__``
* ``__loader__``
* ``__spec__``
* ``__package__``

Moduły
~~~~~~

Stałe
~~~~~

Zmienne
~~~~~~~

Wartości funkcji
~~~~~~~~~~~~~~~~

Debugging i Wątki
-----------------

Debugging i Procesy
-------------------

Debugging aplikacji sieciowych
------------------------------
.. code-block:: python

    import logging

    logging.getLogger('requests').setLevel(logging.DEBUG)

Wyciszanie logowania
--------------------
.. code-block:: python

    import logging

    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime).19s] [%(levelname)s] %(message)s')

    logging.getLogger('requests').setLevel(logging.WARNING)
    log = logging.getLogger(__name__)

    log.debug('to jest moja debugowa wiadomosc')

