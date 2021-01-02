File Modes
==========


Rationale
---------
By type:

    * Text - easy to read and write
    * Binary - Fast and efficient

By operation:

    * Read - Get data from file
    * Write - Save data to file (overwrite existing data)
    * Append - Add line to file
    * Update - Read and Write (rarely used)

If mode is not specified it will read in text mode (``mode='rt'``)

.. code-block:: python

    open('myfile.txt')


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

.. code-block:: python

    open('myfile.txt', mode='r')
    open('myfile.txt', mode='w')
    open('myfile.txt', mode='a')


Text Mode
---------
* Text - easy to read and write
* ``mode='rt'`` - read in text mode (default)
* ``mode='wt'`` - write in text mode
* ``mode='at'`` - append in text mode

.. code-block:: python

    open('myfile.txt', mode='rt')
    open('myfile.txt', mode='wt')
    open('myfile.txt', mode='at')


Binary Mode
-----------
* Binary - Fast and efficient
* ``mode='rb'`` - read in binary mode
* ``mode='wb'`` - write in binary mode
* ``mode='ab'`` - append in binary mode

.. code-block:: python

    open('myfile.txt', mode='rb')
    open('myfile.txt', mode='wb')
    open('myfile.txt', mode='ab')


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

.. code-block:: python

    open('myfile.txt', mode='r+')
    open('myfile.txt', mode='w+')
    open('myfile.txt', mode='a+')

    open('myfile.txt', mode='rt+')
    open('myfile.txt', mode='wt+')
    open('myfile.txt', mode='at+')

    open('myfile.txt', mode='rb+')
    open('myfile.txt', mode='wb+')
    open('myfile.txt', mode='ab+')


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


Assignments
-----------
.. todo:: Create assignments


References
----------
.. [#ROHIT2020] Rohit. Python file modes | Open, Write, append (r, r+, w, w+, x, etc). Year: 2020. URL: https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/
