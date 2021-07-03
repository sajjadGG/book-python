Database Delete
---------------

Rationale
---------
* Removes data from table
* Can be narrowed down by a ``WHERE``
* Leaves table structure intact
* Write your statement starting with ``--`` after you're done, make sure
  there is no mistake, then remove comment and execute


SQL Syntax
----------
.. code-block:: sql

    DELETE FROM astronauts
    WHERE id = 1;

.. code-block:: sql

    DELETE FROM astronauts
    WHERE agency = 'NASA';

.. code-block:: sql

    DELETE FROM astronauts
    WHERE firstname = 'Mark'
    AND lastname = 'Watney';
