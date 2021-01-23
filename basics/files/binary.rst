Files Binary
============

.. testsetup::

    from pathlib import Path
    Path('/tmp/myfile.bin').unlink(missing_ok=True)
    Path('/tmp/myfile.pkl').unlink(missing_ok=True)


Rationale
---------
* Text I/O over a binary storage (such as a file) is significantly slower
  than binary I/O over the same storage
* It requires conversions between unicode and binary data using
  a character codec
* This can become noticeable handling huge amounts of text data like
  large log files
* Source: https://docs.python.org/3/library/io.html#id3


Append Binary
-------------
* ``mode='ab'`` - append in binary mode

    >>> FILE = r'/tmp/myfile.bin'
    >>> DATA = 'We choose to go to the Moon...'
    >>> data = DATA.encode()
    >>>
    >>> with open(FILE, mode='ab') as file:
    ...     file.write(data)
    30


Write Binary
------------
* ``mode='wb'`` - write in binary mode

    >>> FILE = r'/tmp/myfile.bin'
    >>> DATA = 'We choose to go to the Moon...'
    >>> data = DATA.encode()
    >>>
    >>> with open(FILE, mode='wb') as file:
    ...     file.write(data)
    30


Read Binary
-----------
* ``mode='rb'`` - read in binary mode

    >>> FILE = r'/tmp/myfile.bin'
    >>>
    >>> with open(FILE, mode='rb') as file:
    ...     data = file.read()
    ...
    >>> result = data.decode()
    >>> print(result)
    We choose to go to the Moon...


Pickle
------
* Works with any Python object (variables, functions, classes, nested objects)
* More information in `Serialization Pickle`

Write binary data to file:

    >>> import pickle
    >>>
    >>> FILE = r'/tmp/myfile.pkl'
    >>> data = [1, 2, 3]
    >>>
    >>> with open(FILE, mode='wb') as file:
    ...     pickle.dump(data, file)

Load binary data from file:

    >>> import pickle
    >>>
    >>> FILE = r'/tmp/myfile.pkl'
    >>>
    >>> with open(FILE, mode='rb') as file:
    ...    result = pickle.load(file)
    ...
    >>> print(result)
    [1, 2, 3]

Seek
----
* Go to the n-th byte in the file
* Supports negative index (from end of file)

    >>> FILE = r'/tmp/myfile.bin'
    >>> DATA = b'We choose to go to the Moon...'
    >>>
    >>>
    >>> with open(FILE, mode='wb') as file:
    ...    file.write(DATA)
    30
    >>>
    >>> file = open(FILE, mode='rb')
    >>>
    >>> file.seek(23)
    23
    >>> file.read(1)
    b'M'
    >>> file.read(1)
    b'o'
    >>> file.read(1)
    b'o'
    >>> file.read(1)
    b'n'
    >>>
    >>> file.seek(23)
    23
    >>> file.read(4)
    b'Moon'
    >>>
    >>> file.seek(-7, 2)
    23
    >>> file.read(4)
    b'Moon'
