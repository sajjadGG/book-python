File Append
===========

.. testsetup::

    from pathlib import Path
    Path('/tmp/myfile.txt').unlink(missing_ok=True)


Rationale
---------
* Appends data at the end of file
* Creates file if not exists
* Works with both relative and absolute path
* Fails when directory with file cannot be accessed
* ``mode`` parameter to ``open()`` function is required
* ``.writelines()`` does not add a line separator!!

>>> file = open(r'/tmp/myfile.txt', mode='a')
>>> file.write('hello')
5
>>> file.close()


Appending to File
-----------------
* Append to the end of file

    >>> FILE = r'/tmp/myfile.txt'
    >>> DATA = 'We choose to go to the Moon...'
    >>>
    >>> with open(FILE, mode='a') as file:
    ...    file.write(DATA)
    30
