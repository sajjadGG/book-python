****
Apps
****

Reusability
===========

Location
========
.. literalinclude:: src/django-apps-location.py
    :language: python
    :caption: Django Apps Location

Create
======
.. code-block:: console

    $ cd addressbook
    $ django-admin startapp contact

.. code-block:: python

    # settings.py
    INSTALLED_APPS += ['addressbook.contact.apps.ContactConfig']

Structure
=========
.. literalinclude:: src/django-apps-structure.txt
    :language: python
    :caption: Django Apps Structure

Configuration
=============
.. literalinclude:: src/django-apps-config.py
    :language: python
    :caption: Django Apps Configuration