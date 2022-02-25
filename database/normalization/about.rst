Normalization About
===================

.. important::

    * Entities - rows in database
    * Attributes - columns in database
    * Normalization is what gives data meaning
    * NF - Normal Form
    * In order to be in 3rd normal form, you need to be in 1st and 2nd NF
    * Core basics: 1st, 2nd, 3rd
    * Exceptions: 4th, 5th
    * 1st: atomic values, unique identifiers (PK), columns with same type
    * 2nd: all data must depend on the Primary Key
    * 3rd: PK define all Non-Key columns, those can't depend on any other Key
    * 4th: No multi-valued dependencies


Rationale
---------
.. glossary::

    normalization
        Database normalization is the process of structuring a database,
        usually a relational database, in accordance with a series of
        so-called normal forms in order to reduce data redundancy and
        improve data integrity. Normalization entails organizing the columns
        (attributes) and tables (relations) of a database to ensure that
        their dependencies are properly enforced by database integrity
        constraints. It is accomplished by applying some formal rules either
        by a process of synthesis (creating a new database design) or
        decomposition (improving an existing database design). A relational
        database relation is often described as 'normalized' if it meets
        third normal form. [#WikipediaDatabaseNormalization]_ [#Codd1972]_

    NF
        Normal Form

    Entity
    Entities
        Rows in database

    Attributes
        Columns in database

    Table
        Database Table


Recap
-----
.. figure:: img/normalform-1st,2nd,3rd.png
