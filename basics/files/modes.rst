.. testsetup::

    from pathlib import Path
    Path('/tmp/myfile.txt').unlink(missing_ok=True)
    Path('/tmp/myfile.txt').touch()


File Modes
==========
* Text - easy to read and write
* Binary - Fast and efficient
* Read - Get data from file
* Write - Save data to file (overwrite existing data)
* Append - Add line to file
* Update - Read and Write (rarely used)

By type:

    * Text - easy to read and write
    * Binary - Fast and efficient

By operation:

    * Read - Get data from file
    * Write - Save data to file (overwrite existing data)
    * Append - Add line to file
    * Update - Read and Write (rarely used)

If mode is not specified it will read in text mode (``mode='rt'``)

>>> open('/tmp/myfile.txt')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='r' encoding='UTF-8'>


Modes
-----
* `r` - For reading – The file pointer is placed at the beginning of the file. This is the default mode.
* `r+` - Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
* `w` - Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
* `w+` - Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
* `rb` - Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.
* `rb+` - Opens a file for both reading and writing in binary format.
* `wb+` - Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
* `a` - Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
* `ab` - Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
* `a+` - Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
* `ab+` - Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
* `x` - Open for exclusive creation, failing if the file already exists (Python 3)

Source: [#ROHIT2020]_


Short Notation
--------------
* Most commonly used
* By default text mode is used
* ``mode='r'`` - read in text mode
* ``mode='w'`` - write in text mode
* ``mode='a'`` - append in text mode

>>> open('/tmp/myfile.txt', mode='r')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='r' encoding='UTF-8'>

>>> open('/tmp/myfile.txt', mode='w')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='w' encoding='UTF-8'>

>>> open('/tmp/myfile.txt', mode='a')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='a' encoding='UTF-8'>


Text Mode
---------
* Text - easy to read and write
* ``mode='rt'`` - read in text mode (default)
* ``mode='wt'`` - write in text mode
* ``mode='at'`` - append in text mode

>>> open('/tmp/myfile.txt', mode='rt')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='rt' encoding='UTF-8'>

>>> open('/tmp/myfile.txt', mode='wt')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='wt' encoding='UTF-8'>

>>> open('/tmp/myfile.txt', mode='at')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='at' encoding='UTF-8'>


Binary Mode
-----------
* Binary - Fast and efficient
* ``mode='rb'`` - read in binary mode
* ``mode='wb'`` - write in binary mode
* ``mode='ab'`` - append in binary mode

>>> open('/tmp/myfile.txt', mode='rb')
<_io.BufferedReader name='/tmp/myfile.txt'>

>>> open('/tmp/myfile.txt', mode='wb')
<_io.BufferedWriter name='/tmp/myfile.txt'>

>>> open('/tmp/myfile.txt', mode='ab')
<_io.BufferedWriter name='/tmp/myfile.txt'>


Update Mode
-----------
* Reading and Writing
* Text mode is used if not specified otherwise
* ``mode='r+'`` - read in text mode
* ``mode='w+'`` - write in text mode
* ``mode='a+'`` - append in text mode
* ``mode='rt+'`` - update in text mode
* ``mode='wt+'`` - update in text mode
* ``mode='at+'`` - update in text mode
* ``mode='rb+'`` - update in binary mode
* ``mode='wb+'`` - update in binary mode
* ``mode='ab+'`` - update in binary mode

>>> open('/tmp/myfile.txt', mode='r+')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='r+' encoding='UTF-8'>
>>>
>>> open('/tmp/myfile.txt', mode='w+')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='w+' encoding='UTF-8'>
>>>
>>> open('/tmp/myfile.txt', mode='a+')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='a+' encoding='UTF-8'>
>>>

>>> open('/tmp/myfile.txt', mode='rt+')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='rt+' encoding='UTF-8'>
>>>
>>> open('/tmp/myfile.txt', mode='wt+')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='wt+' encoding='UTF-8'>
>>>
>>> open('/tmp/myfile.txt', mode='at+')
<_io.TextIOWrapper name='/tmp/myfile.txt' mode='at+' encoding='UTF-8'>
>>>

>>> open('/tmp/myfile.txt', mode='rb+')
<_io.BufferedRandom name='/tmp/myfile.txt'>
>>>
>>> open('/tmp/myfile.txt', mode='wb+')
<_io.BufferedRandom name='/tmp/myfile.txt'>
>>>
>>> open('/tmp/myfile.txt', mode='ab+')
<_io.BufferedRandom name='/tmp/myfile.txt'>
>>>


Recap
-----
Most common (90% of time):

    * ``mode='r'`` - read in text mode
    * ``mode='w'`` - write in text mode
    * ``mode='a'`` - append in text mode

Text Mode:

    * ``mode='rt'`` - read in text mode (default)
    * ``mode='wt'`` - write in text mode
    * ``mode='at'`` - append in text mode

Binary Mode:

    * ``mode='rb'`` - read in binary mode
    * ``mode='wb'`` - write in binary mode
    * ``mode='ab'`` - append in binary mode

Update (rarely used):

    * ``mode='rb+'`` - update in binary mode
    * ``mode='wb+'`` - update in binary mode
    * ``mode='ab+'`` - update in binary mode
    * ``mode='r+'`` - read in text mode
    * ``mode='w+'`` - write in text mode
    * ``mode='a+'`` - append in text mode

* If mode is not specified it will read in text mode (``mode='rt'``)


References
----------
.. [#ROHIT2020] Rohit. Python file modes | Open, Write, append (r, r+, w, w+, x, etc). Year: 2020. URL: https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/


.. todo:: Assignments
