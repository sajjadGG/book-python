Regex Flag
==========


Rationale
---------
* ``re.ASCII``
* ``re.IGNORECASE``
* ``re.LOCALE``
* ``re.MULTILINE``
* ``re.DOTALL``
* ``re.UNICODE``
* ``re.VERBOSE``


ASCII
-----
* Short: ``a``
* Long: ``re.ASCII``

Make ``\w``, ``\W``, ``\b``, ``\B``, ``\d``, ``\D``, ``\s`` and ``\S`` perform ASCII-only matching instead of full Unicode matching


IGNORECASE
----------
* Short: ``i``
* Long: ``re.IGNORECASE``

Case-insensitive (has Unicode support i.e. Ą and ą)


LOCALE
------
* Short: ``L``
* Long: ``re.LOCALE``

make ``\w``, ``\W``, ``\b``, ``\B`` and case-insensitive matching dependent on the current locale


MULTILINE
----------
* Short: ``m``
* Long: ``re.MULTILINE``

match can start in one line, and end in another: ``^`` - start of line, ``$`` - end of line


DOTALL
------
* Short: ``s``
* Long: ``re.DOTALL``

``.`` matches also newlines (default newlines are not matched by ``.``)


UNICODE
-------
* Short: ``u``
* Long: ``re.UNICODE``

turns on UNICODE mode


VERBOSE
-------
* Short: ``x``
* Long: ``re.VERBOSE``

ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``

>>> import re
>>>
>>> a = re.compile(r"""\d +  # the integral part
...                    \.    # the decimal point
...                    \d *  # some fractional digits""", re.VERBOSE)
>>>
>>> b = re.compile(r"\d+\.\d*")

The final piece of regex syntax that Python's regular expression engine offers is a means of setting the flags. Usually the flags are set by passing them as additional parameters when calling the re.compile() function, but sometimes it's more convenient to set them as part of the regex itself. The syntax is simply (?flags) where flags is one or more of the following:

If the flags are set this way, they should be put at the start of the regex; they match nothing, so their effect on the regex is only to set the flags.

The letters used for the flags are the same as the ones used by Perl's regex engine, which is why s is used for re.DOTALL and x is used for re.VERBOSE.

Source: [#Summerfield2008]_


References
----------
.. [#Summerfield2008] Summerfield, Mark. Programming in Python 3. Regular Expressions. Chapter: 12. Pages: 445-465. Year: 2008. Retrieved: 2021-04-11. Publisher: Addison-Wesley Professional. ISBN: 978-0-13-712929-4. URL: https://www.informit.com/articles/article.aspx?p=1278986
