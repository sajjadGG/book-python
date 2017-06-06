*****************
Logowanie zdarzeń
*****************

Poziomy logowania
=================

* Critical
* Error
* Warning
* Info
* Debug

Korzystanie z ``logging``
=========================

Konfiguracja logowania
----------------------

.. code-block:: python

    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(format='[%(asctime).19s] [%(levelname)s] %(message)s')

    log = logging.getLogger()

.. code-block:: python

    import logging

    logging.basicConfig(
        level=logging.DEBUG,
        filename='/tmp/python.log',
        format='"%(asctime).19s", "%(levelname)s", "%(message)s"'
    )

    logging.warning('hej')

.. code-block:: python

    logging.critical('Błąd krytyczny, kończę.')
    logging.error('Błąd, ale kontynuuję.')
    logging.warning('Uwaga będę coś robił')
    logging.info('Będę coś robił')
    logging.debug('Robię to tak')

Logowanie zdarzeń
-----------------

.. code-block:: python

    import logging
    log = logging.getLogger(__name__)

    >>> def sum(a, b):
    ...     log.debug('Function `sum()` executed with: %s', locals())
    ...     value = a + b
    ...     log.debug(f'Will produce "{value}" as result')
    ...     return value
    ...
    >>> sum(1, 2)
    Function `sum()` executed with: {'b': 2, 'a': 1}
    Will produce "3" as result
    3


Konfiguracja formatowania logów
===============================

+-------------------------+-----------------------------------------------+
| Format                  | Description                                   |
+=========================+===============================================+
| args                    | The tuple of arguments merged into ``msg`` to |
|                         | produce ``message``, or a dict whose values   |
|                         | are used for the merge (when there is only one|
|                         | argument, and it is a dictionary).            |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(asctime)s``         | Human-readable time when the                  |
|                         | `LogRecord` was created.  By default          |
|                         | this is of the form '2003-07-08 16:49:45,896' |
|                         | (the numbers after the comma are millisecond  |
|                         | portion of the time).                         |
+-------------------------+-----------------------------------------------+
| ``%(created)f``         | Time when the `LogRecord` was created         |
|                         | (as returned by `time.time`).                 |
+-------------------------+-----------------------------------------------+
| exc_info                | Exception tuple (à la ``sys.exc_info``) or,   |
|                         | if no exception has occurred, ``None``.       |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(filename)s``        | Filename portion of ``pathname``.             |
+-------------------------+-----------------------------------------------+
| ``%(funcName)s``        | Name of function containing the logging call. |
+-------------------------+-----------------------------------------------+
| ``%(levelname)s``       | Text logging level for the message            |
|                         | (``'DEBUG'``, ``'INFO'``, ``'WARNING'``,      |
|                         | ``'ERROR'``, ``'CRITICAL'``).                 |
+-------------------------+-----------------------------------------------+
| ``%(levelno)s``         | Numeric logging level for the message         |
|                         | (`DEBUG`, `INFO`,                             |
|                         | `WARNING`, `ERROR`,                           |
|                         | `CRITICAL`).                                  |
+-------------------------+-----------------------------------------------+
| ``%(lineno)d``          | Source line number where the logging call was |
|                         | issued (if available).                        |
+-------------------------+-----------------------------------------------+
| ``%(module)s``          | Module (name portion of ``filename``).        |
+-------------------------+-----------------------------------------------+
| ``%(msecs)d``           | Millisecond portion of the time when the      |
|                         | `LogRecord` was created.                      |
+-------------------------+-----------------------------------------------+
| ``%(message)s``         | The logged message, computed as ``msg %       |
|                         | args``. This is set when                      |
|                         | `Formatter.format` is invoked.                |
+-------------------------+-----------------------------------------------+
| msg                     | The format string passed in the original      |
|                         | logging call. Merged with ``args`` to         |
|                         | produce ``message``, or an arbitrary object   |
|                         | (see `arbitrary-object-messages`).            |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(name)s``            | Name of the logger used to log the call.      |
+-------------------------+-----------------------------------------------+
| ``%(pathname)s``        | Full pathname of the source file where the    |
|                         | logging call was issued (if available).       |
+-------------------------+-----------------------------------------------+
| ``%(process)d``         | Process ID (if available).                    |
+-------------------------+-----------------------------------------------+
| ``%(processName)s``     | Process name (if available).                  |
+-------------------------+-----------------------------------------------+
| ``%(relativeCreated)d`` | Time in milliseconds when the LogRecord was   |
|                         | created, relative to the time the logging     |
|                         | module was loaded.                            |
+-------------------------+-----------------------------------------------+
| stack_info              | Stack frame information (where available)     |
|                         | from the bottom of the stack in the current   |
|                         | thread, up to and including the stack frame   |
|                         | of the logging call which resulted in the     |
|                         | creation of this record.                      |
|                         | You shouldn't need to format this yourself.   |
+-------------------------+-----------------------------------------------+
| ``%(thread)d``          | Thread ID (if available).                     |
+-------------------------+-----------------------------------------------+
| ``%(threadName)s``      | Thread name (if available).                   |
+-------------------------+-----------------------------------------------+


``warnings``
============

.. code-block:: python

    import warnings

    warnings.warn('Wersja API jest już nieaktualna', PendingDeprecationWarning)

.. code-block:: python

    import warnings

    def run_HTTP_server(*args, **kwargs):
        pass


    def runHTTPServer(*args, **kwargs):
        warnings.warn(PendingDeprecationWarning, 'You should use \'run_HTTP_server()\' instead.')
        return run_HTTP_server(*args, **kwargs)
