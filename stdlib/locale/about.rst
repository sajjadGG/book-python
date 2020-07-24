************
Locale About
************


Rationale
=========
* i18n = internationalization
* l10n = localization


Syntax
======
* language
* variant
* encoding

.. code-block:: text

    en_US.UTF-8


Get Locale
==========
.. code-block:: console

    $ locale
    LANG=""
    LC_COLLATE="en_US.UTF-8"
    LC_CTYPE="en_US.UTF-8"
    LC_MESSAGES="en_US.UTF-8"
    LC_MONETARY="en_US.UTF-8"
    LC_NUMERIC="en_US.UTF-8"
    LC_TIME="en_US.UTF-8"
    LC_ALL="en_US.UTF-8"

.. code-block:: console

    $ env |grep LC_
    LC_ALL=en_US.UTF-8
    LC_CTYPE=UTF-8


Set Locale
==========
.. code-block:: console

    $ echo 'export LC_ALL=en_US.UTF-8' >> ~/.profile

.. code-block:: console

    ls -R /etc/locale*


Locale in Python
================
.. code-block:: python

    import locale


Further Reading
===============
* https://github.com/django/django/blob/master/django/utils/formats.py
* https://github.com/django/django/blob/master/django/conf/locale/pl/formats.py
* https://github.com/django/django/blob/master/django/conf/locale/en/formats.py

