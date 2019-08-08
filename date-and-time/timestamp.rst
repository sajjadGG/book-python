*********
Timestamp
*********

What is timestamp?
==================
* Also called "epoch"
* Unix era
* Seconds since 1970-01-01T00:00:00.000000+0000
* max 32-bit integer is 2,147,483,647
* If you add +1 to that, you get -2,147,483,647
* 2,147,483,647 seconds from 01-01-1970 00:00:00 is January 19, 2038
* If you add one more second, you get a date somewhere in 1902


``datetime``
============

Get timestamp
-------------
.. code-block:: python
    :caption: Get timestamp

    from datetime import datetime

    datetime.now().timestamp()
    # 1544116827.618863

From epoch timestamp
--------------------
.. code-block:: python
    :caption: From epoch timestamp

    from datetime import datetime

    ts = 267809220

    datetime.fromtimestamp(ts)
    # datetime.datetime(1978, 6, 27, 15, 27)

From Java Script timestamp
--------------------------
* JavaScript has timestamp in milliseconds
* To convert from milliseconds we have to divide by 1000

.. code-block:: python
    :caption: From Java Script timestamp

    from datetime import datetime

    MILLISECONDS = 1000
    ts = 267809220000

    datetime.fromtimestamp(ts / MILLISECONDS)
    # datetime.datetime(1978, 6, 27, 17, 27)


``time``
========

Timestamp with precision
------------------------
.. code-block:: python
    :caption: Get timestamp

    import time

    time.time()
    # 1496737953.0712671


Assignments
===========

Create ``datetime`` object
--------------------------
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/datetime_timestamp.py`

#. Stwórz obiekt ``datetime`` z datą "1970-01-01T00:00:00.000000+0000"
#. Przedstaw datę jako timestamp
#. Co wyszło?
#. Co to za data?
