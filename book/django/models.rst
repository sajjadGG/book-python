******
Models
******

Model Fields
============

Text fields
-----------
- ``CharField``
- ``TextField``
- ``SlugField``
- ``URLField``

Numeric fields
--------------
- ``DecimalField``
- ``IntegerField``
- ``PositiveIntegerField``
- ``PositiveSmallIntegerField``

Logic fields
------------
- ``BooleanField``

Date and time fields
--------------------
- ``DateField``
- ``DateTimeField``
- ``DurationField``
- ``TimeField``

File fields
-----------
- ``FileField``
- ``ImageField``

Relations
---------
- ``ForeignKeyField``
- ``ManyToManyField``

Model field arguments
=====================

All
---
- ``verbose_name``
- ``max_length``
- ``choices``
- ``validators``
- ``help_text``
- ``null``
- ``blank``
- ``default``
- ``db_index``

Relations
---------
- ``to`` (ForeignKey, ManyToManyField)
- ``related_name`` (ForeignKey, ManyToManyField)
- ``on_delete`` (ForeignKey, ManyToManyField)

Date and time
-------------
- ``auto_add`` (DateField, DateTimeField)
- ``auto_add_now`` (DateField, DateTimeField)

Numeric
-------
- ``decimal_places`` (DecimalField)
- ``max_digits`` (DecimalField)

Abstract Models
===============
.. code-block:: python

    class Meta:
        abstract = True

Architecture
============
- Fat model architecture

Reverse engineering database
============================
- ``python manage.py inspectdb