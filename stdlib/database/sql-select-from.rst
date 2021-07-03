Select From
===========


SQL Syntax
----------
.. code-block:: sql

    SELECT * FROM astronauts;

.. code-block:: sql

    SELECT firstname, lastname
    FROM astronauts;

.. code-block:: sql

    SELECT
        firstname AS fname,
        lastname AS lname
    FROM astronauts;

.. code-block:: sql

    SELECT
        firstname,
        lastname,
        previous_job as career
    FROM astronauts;
