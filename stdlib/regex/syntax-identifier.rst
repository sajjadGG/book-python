Syntax Identifier
=================


Rationale
---------
Identifiers specifies what to find.
They are also called Character Classes.


Numeric
-------
* ``\d`` - digit
* ``\D`` - anything but digit


String
------
* ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
* ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)


Whitespaces
-----------
* ``\s`` - whitespace (space, tab, newline, non-breaking space)
* ``\S`` - anything but whitespace
* ``\n`` - newline
* ``\r\n`` - windows newline
* ``\r`` - carriage return
* ``\b`` - backspace
* ``\t`` - tab
* ``\v`` - vertical space
* ``\f`` - form feed


Anchors
-------
* ``\b`` - word boundary
* ``\B`` - anything but word boundary

Examples:

    * ``\babc\b`` - performs a "whole words only" search
    * ``\Babc\B`` - pattern is fully surrounded by word characters
