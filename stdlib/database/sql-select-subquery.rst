Select Subquery
===============


SQL Syntax
----------
* ``IN (SELECT ...)`` - subquery

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE agency IN (
        SELECT name FROM agencies
    );

.. code-block:: sql

    SELECT *
    FROM astronauts
    WHERE career IN (
        SELECT name FROM job_names);
