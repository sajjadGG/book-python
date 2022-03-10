AsyncIO 3rd Party
=================


Unsync
------
* 3rd Party Library
* Library decides which to run, thread, asyncio or sync

.. code-block:: console

    $ pip install unsync

.. code-block:: python

    @unsync
    def my_function():
        pass
