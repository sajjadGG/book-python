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

:settings.py:
    .. code-block:: python

        INSTALLED_APPS += ['addressbook.contact.apps.ContactConfig']

Structure
=========
.. literalinclude:: src/django-apps-structure.py
    :language: python
    :caption: Django Apps Structure

Installation
============
.. literalinclude:: src/django-apps-installation.py
    :language: python
    :caption: Django Apps Installation

Configuration
=============
.. literalinclude:: src/django-apps-config.py
    :language: python
    :caption: Django Apps Configuration