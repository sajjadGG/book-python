.. _Files Write:

**********
File Write
**********


Rationale
=========
* Creates file if not exists
* Truncate the file before writing
* Works with both relative and absolute path
* Fails when directory with file cannot be accessed
* ``mode`` parameter to ``open()`` function is required


Line
====
* File must end with a newline ``\n`` character

Line Definition by POSIX [1]_:

    Line: A sequence of zero or more non- <newline> characters plus a terminating <newline> character.

Line definition by ANSI C89 and ISO C99 language standards [2]_, [3]_, [4]_:

    A source file that is not empty shall end in a new-line character, which shall not be immediately preceded by a backslash character.


Write to File
=============
* Always remember to close file

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = 'We choose to go to the Moon...'

    file = open(FILE, mode='w')
    file.write(DATA)
    file.close()


Write One Line
==============
.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = 'We choose to go to the Moon...'

    with open(FILE, mode='w') as file:
        file.write(DATA)


Write Multiple Lines
====================
* Write a list of lines to the file.
* ``.writelines()`` does not add a line separator (``\n``)!!
*  Each line must add a separator at the end.

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = ['We choose to go to the Moon.',
            'We choose to go to the Moon in this decade and do the other things.',
            'Not because they are easy, but because they are hard.']

    result = '\n'.join(DATA)

    with open(FILE, mode='w') as file:
        file.write(result)

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = ['We choose to go to the Moon.',
            'We choose to go to the Moon in this decade and do the other things.',
            'Not because they are easy, but because they are hard.']

    result = [line+'\n' for line in DATA]

    with open(FILE, mode='w') as file:
        file.writelines(result)


Write Non-Str Data
==================
* Join works only for strings
* Conversion to ``str`` must be performed before adding a separator and writing to file.

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    DATA = [1, 2, 3]

    result = ','.join(str(x) for x in DATA) + '\n'

    with open(FILE, mode='w') as file:
        file.write(result)

    # 1,2,3

.. note:: When writing output to the stream, if newline is ``None``, any ``'\n'`` characters written are translated to the system default line separator, ``os.linesep``. If newline is ``''`` or ``'\n'``, no translation takes place. If newline is any of the other legal values, any ``'\n'`` characters written are translated to the given string. Source: https://docs.python.org/3/library/io.html#io.TextIOWrapper


Reading From One File and Writing to Another
============================================
.. code-block:: python

    FILE_READ = r'/tmp/my-infile.txt'
    FILE_WRITE = r'/tmp/my-outfile.txt'

    with open(FILE_READ) as infile, \
         open(FILE_WRITE, mode='w') as outfile:

        for line in infile:
            outfile.write(line)

References
==========
.. [1] Section 3.206 IEEE Std 1003.1-2017 (Revision of IEEE Std 1003.1-2008). Open Group Base Specifications Issue 7, 2018 edition. URL: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206 Accessed Date: 2020-12-17s
.. [2] Section 2.1.1.2 of the ANSI C 1989 standard
.. [3] Section 5.1.1.2 of the ISO C 1999 standard
.. [4] https://gcc.gnu.org/legacy-ml/gcc/2003-11/msg01568.html


Assignments
===========

.. literalinclude:: assignments/file_write_str.py
    :caption: :download:`Solution <assignments/file_write_str.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_write_multiline.py
    :caption: :download:`Solution <assignments/file_write_multiline.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_write_list.py
    :caption: :download:`Solution <assignments/file_write_list.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_write_nonstr.py
    :caption: :download:`Solution <assignments/file_write_nonstr.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_write_iris.py
    :caption: :download:`Solution <assignments/file_write_iris.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_write_csv.py
    :caption: :download:`Solution <assignments/file_write_csv.py>`
    :end-before: # Solution
