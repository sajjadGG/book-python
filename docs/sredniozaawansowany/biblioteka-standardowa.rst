**********************
Biblioteka standardowa
**********************

``datetime``
============

Tworzenie obiektu ``date`` i ``datetime``
-----------------------------------------

.. code-block:: python

    import datetime

    now = datetime.datetime.now()
    today = datetime.date.today()

    date = datetime.date(2017, 12, 15)
    dt = datetime.datetime(2017, 12, 15, 20, 13, 33)
    midnight = datetime.datetime(2017, 12, 15)


Różne formaty dat
-----------------
* '15.12.2017'
* '15/12/2017'
* '15 grudnia 2017'
* '15 grudzień 2017'
* '12/15/17'
* 'December 15, 2017'
* '2017-12-15'

.. code-block:: python

    import datetime

    now = datetime.datetime.now()
    now.strftime('%A, %B %d, %I:%M %p')

    print(f'{now:%Y-%m-%d}')

Przesunięcia czasu (dodawanie i odejmowanie)
--------------------------------------------

.. code-block:: python

    import datetime

    datetime.datetime.now() - datetime.timedelta(hours=3)
    datetime.date(2017, 12, 15) - datetime.timedelta(days=3)

Strefy czasowe
--------------

.. code-block:: python

    import datetime

    datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)

``time``
========


``os``
======

.. code-block:: python

    import os

    os.path
    os.walk
    os.path.join
    os.path.abspath
    os.path.dirname

.. code-block:: python

    import os

    for element in os.scandir('/etc'):
        print(element.name)

    script = os.path.basename(__file__)
    PWD = os.path.basename(os.getcwd())

    path = os.path.join(PWD, script)

    print(path)


``sys``
=======

.. code-block:: python

    import sys

    sys.path
    sys.path.append
    sys.platform


``warnings``
============

.. code-block:: python

    import warnings

    warnings.warn('Wersja API jest już nieaktualna', PendingDeprecationWarning)

.. code-block:: python

    import warnings

    def run_HTTP_server(*args, **kwargs):
        pass


    def runHTTPServer(*args, **kwargs):
        warnings.warn(PendingDeprecationWarning, 'You should use \'run_HTTP_server()\' instead.')
        return run_HTTP_server(*args, **kwargs)


``pprint``
==========

.. code-block:: python

    from pprint import pprint

    data = [
       {'first_name': 'Baked', 'last_name': 'Beans'},
       {'first_name': 'Lovely', 'last_name': 'Spam'},
       {'first_name': 'Wonderful', 'last_name': 'Spam'}
    ]

    pprint(data)

``csv``
=======

.. code-block:: python

    import csv

    csv.DictReader()
    csv.DictWriter()

``memoize``
===========

``json``
========

.. code-block:: python

    import json

    json.loads()
    json.dumps()

``sqlite``
==========

``re``
======

.. code-block:: python

    import re

    re.search()
    re.findall()
    re.match()
    re.compile()

``httplib``
===========

``urllib``
==========

``socket``
==========

``tempfile``
============

``io``
======

.. code-block:: python

    import io

    io.StringIO

``functools``
=============

``itertools``
=============

``math``
========

.. code-block:: python

    import math

    math.sin()
    math.cos()
    math.tan()
    math.pi

``statistics``
==============

.. code-block:: python

    import statistics

    statistics.avg()
    statistics.mean()
    statistics.stdev()

``random``
==========

.. code-block:: python

    import random

    random.sample()
    random.random()

``subprocess``
==============

.. code-block:: python

    import subprocess

    subprocess.Popen()

``doctest``
===========

.. code-block:: python

    import doctest

    doctest.testmod()


Collections
===========

================  ====================================================================
Name              Description
================  ====================================================================
``namedtuple()``  factory function for creating tuple subclasses with named fields
``deque``         list-like container with fast appends and pops on either end
``ChainMap``      dict-like class for creating a single view of multiple mappings
``Counter``       dict subclass for counting hashable objects
``OrderedDict``   dict subclass that remembers the order entries were added
``defaultdict``   dict subclass that calls a factory function to supply missing values
``UserDict``      wrapper around dictionary objects for easier dict subclassing
``UserList``      wrapper around list objects for easier list subclassing
``UserString``    wrapper around string objects for easier string subclassing
================  ====================================================================
