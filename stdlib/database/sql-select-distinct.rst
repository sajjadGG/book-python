Select Distinct
===============


SQL Syntax - Distinct
---------------------
.. code-block:: sql

    SELECT DISTINCT agency
    FROM astronauts;

.. code-block:: sql

    SELECT DISTINCT agency
    FROM astronauts
    WHERE location = 'Europe';

.. code-block:: sql

    SELECT DISTINCT agency AS ag
    FROM astronauts
