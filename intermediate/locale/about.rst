Locale About
============
* i18n = internationalization
* l10n = localization
* https://en.wikipedia.org/wiki/Indian_numbering_system

.. code-block:: text

    $100
    100 zł

.. code-block:: text

    100.00
    100,00

.. code-block:: text

    1 000 000
    1.000.000
    1,000,000
    1'000'000

.. code-block:: text

    1.000.000
    10.00.000


Syntax
------
* language
* variant
* encoding

.. code-block:: text

    en_US.UTF-8
    en_GB.UTF-8
    en_AU.UTF-8
    en_NZ.UTF-8

.. code-block:: text

    pl_PL.UTF-8
    pl_PL.ISO-8859-2
    pl_PL.CP1250


Get Locale
----------
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
----------
.. code-block:: console

    $ echo 'export LC_ALL=en_US.UTF-8' >> ~/.profile

.. code-block:: console

    ls -R /etc/locale*


Locale in Python
----------------
.. code-block:: python

    import locale


Further Reading
---------------
* https://github.com/django/django/blob/master/django/utils/formats.py
* https://github.com/django/django/blob/master/django/conf/locale/pl/formats.py
* https://github.com/django/django/blob/master/django/conf/locale/en/formats.py
* https://github.com/django/django/blob/main/django/conf/locale/hi/formats.py
