.. _Files Encoding:

*************
File Encoding
*************


Rationale
=========
* ``utf-8`` - a.k.a. Unicode - international standard (should be always used!)
* ``iso-8859-1`` - ISO standard for Western Europe and USA
* ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
* ``cp1250`` or ``windows-1250`` - Polish encoding on Windows
* ``cp1251`` or ``windows-1251`` - Russian encoding on Windows
* ``cp1252`` or ``windows-1252`` - Western European encoding on Windows
* ``ASCII`` - ASCII characters only

.. figure:: img/files-windows2000-notepad-saveas.png

    Windows 2000 Notepad "Save As" window with possibility to select encoding. UTF-8 is not selected by default... Source: [1]_

.. figure:: img/files-windows10-notepad-saveas.png

    Windows 10 Notepad "Save As" window with possibility to select encoding. Since Windows 10.1903 (May 2019) notepad writes files in UTF-8 by default! Source: [2]_ [3]_

.. figure:: img/files-encoding-ascii2.jpg

    ASCII table. Source: [4]_

.. figure:: img/files-encoding-unicode2.png

    Unicode. Source: [5]_

.. figure:: img/files-encoding-unicode3.png

    Unicode. Source: [6]_


UTF-8
=====
.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE, mode='w', encoding='utf-8') as file:
        file.write('Иван Иванович')

    with open(FILE, encoding='utf-8') as file:
        print(file.read())
    # Иван Иванович


.. figure:: img/files-encoding-utf.png

    UTF-8. Source: [7]_

.. figure:: img/files-encoding-utf2.jpg

    UTF-8. Source: [8]_


Unicode Encode Error
====================
.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE, mode='w', encoding='cp1250') as file:
        file.write('Иван Иванович')
    # Traceback (most recent call last):
    # UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-3: character maps to <undefined>


Unicode Decode Error
====================
.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE, mode='w', encoding='utf-8') as file:
        file.write('Иван Иванович')

    with open(FILE, encoding='cp1250') as file:
        print(file.read())
    # Traceback (most recent call last):
    # UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1: character maps to <undefined>


Escape Characters
=================
* ``\r\n`` - is used on windows
* ``\n`` - is used everywhere else

.. figure:: img/type-machine.jpg

    Why we have '\\r\\n' on Windows?

Frequently used escape characters:

    * ``\n`` - New line (ENTER)
    * ``\t`` - Horizontal Tab (TAB)
    * ``\'`` - Single quote ``'`` (escape in single quoted strings)
    * ``\"`` - Double quote ``"`` (escape in double quoted strings)
    * ``\\`` - Backslash ``\`` (to indicate, that this is not escape char)

Less frequently used escape characters:

    * ``\a`` - Bell (BEL)
    * ``\b`` - Backspace (BS)
    * ``\f`` - New page (FF - Form Feed)
    * ``\v`` - Vertical Tab (VT)
    * ``\uF680`` - Character with 16-bit (2 bytes) hex value ``F680``
    * ``\U0001F680`` - Character with 32-bit (4 bytes) hex value ``0001F680``
    * ``\o755`` - ASCII character with octal value ``755``
    * ``\x1F680`` - ASCII character with hex value ``1F680``

Emoticons:

    >>> print('\U0001F680')
    🚀

    >>> a = '\U0001F9D1'  # 🧑
    >>> b = '\U0000200D'  # ''
    >>> c = '\U0001F680'  # 🚀
    >>>
    >>> astronaut = a + b + c
    >>> print(astronaut)
    🧑‍🚀

More information in :ref:`Builtin Printing` and https://en.wikipedia.org/wiki/List_of_Unicode_characters


References
==========
.. [1] redhotwords.com. Windows 2000 Notepad. http://redhotwords.com/assets/Uninotepadunicode.png

.. [2] digitalcitizen.life. Windows 10 Notepad. https://www.digitalcitizen.life/sites/default/files/gdrive/windows_notepad/notepad_10.png

.. [3] https://docs.microsoft.com/en-us/windows/whats-new/whats-new-windows-10-version-1903

.. [4] Briana Spinall. Better Ascii Table. 2015. http://brianaspinall.com/wp-content/uploads/2015/11/better_ascii_table.jpg

.. [5] http://www.gammon.com.au/unicode/gbk.svg.png

.. [6] http://cdn.ilovefreesoftware.com/wp-content/uploads/2016/10/unicode-Character-list-1.png

.. [7] https://camo.githubusercontent.com/7806142e30089cac76da9fe9fb1c5bbd0521cde6/68747470733a2f2f692e696d6775722e636f6d2f7a414d74436a622e706e67

.. [8] https://i.pinimg.com/736x/12/e2/37/12e237271c063313762fcafa1cf58e39--web-development-tools.jpg
