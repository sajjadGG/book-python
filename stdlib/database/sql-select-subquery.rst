SQL Select Subquery
===================


Rationale
---------
* ``IN (SELECT ...)`` - subquery


Subqueries
----------
.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE agency IN (
        SELECT name FROM agencies);

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE career IN (
        SELECT name FROM job_names);
