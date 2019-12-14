*************
Regexp Syntax
*************


About Regular Expressions
=========================
* Also known as ``regexp``
* Also known as ``regex``
* Also known as ``re``


Pattern Matching
================
* ``\`` - Escapes special characters (allows matching ``*``, ``?``, etc)

.. csv-table:: Regular Expression Pattern Matching
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``[a-z]``", "One small letter form ``a`` to ``z``"
    "``[A-Z]``", "One capital letter form ``A`` to ``Z``"
    "``[0-9]``", "One digit from ``0`` to ``9``"
    "``[a-zA-Z0-9]``", "One of the following: small or capital letter or digit"
    "``[abc]``", "One of the following: ``a``, ``b`` or ``c``"
    "``A|B``", "One of either A or B patterns"


Negation
========
.. csv-table:: Regular Expression Pattern Negation
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``[^abc]``", "None of the following: ``a``, ``b`` or ``c``"
    "``^(?!.*word).*$``", "Not containing ``word``"


Unicode Patterns
================
* ``\w`` - Includes most characters that can be part of a word in any language, as well as numbers and the underscore

.. csv-table:: Regular Expression Patterns
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``\w``", "Unicode word character"
    "``\d``", "Unicode decimal digit ``[0-9]``, and many other digit characters"
    "``\s``", "Unicode whitespace characters ``[\t\n\r\f\v]`` and non-breaking spaces"


Qualifiers
==========
.. csv-table:: Regular Expression Qualifiers
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``.``", "Any character except a newline"
    "``^``", "Start of the string"
    "``$``", "End of the string"
    "``*``", "Zero or more repetitions of the preceding pattern (as many as possible)"
    "``+``", "One or more repetitions of the preceding pattern"
    "``?``", "Zero or one repetitions of the preceding pattern"


Quantifiers
===========
.. csv-table:: Regular Expression Quantifiers
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``{m}``", "Exactly ``m`` copies of the previous RE should be matched"
    "``{m,}``", "At least ``m`` repetitions"
    "``{,n}``", "At most ``n`` repetitions"
    "``{m,n}``", "Match from ``m`` to ``n`` repetitions of the preceding RE (as many as possible)"
    "``{m,n}?``", "Match from ``m`` to ``n`` repetitions of the preceding RE (as few as possible)"


Greedy and Non-Greedy
=====================
``...?`` - as few repetitions as possible

.. csv-table:: Regular Expression Greedy and Non-Greedy Qualifiers
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``??``", "zero or one (non greedy)"
    "``*?``", "zero or more (non greedy)"
    "``+?``", "one or more (non greedy)"


Flags
=====
.. csv-table:: Regular Expression Flags
    :widths: 15, 85
    :header: "Flag", "Description"

    "``re.IGNORECASE``", "Case-insensitive (Unicode support i.e. Ü and ü)"
    "``re.MULTILINE``",  "``^`` matches beginning of the string and each line"
    "``re.MULTILINE``",  "``$`` matches end of the string and each line"
    "``re.DOTALL``",     "``.`` matches newlines"


Multiline
=========
* ``re.MULTILINE`` - Flag turns on Multiline search
* ``^`` - Matches the start of the string, and immediately after each newline
* ``$`` - Matches the end of the string or just before the newline at the end of the string also matches before a newline


Groups
======
* ``(?P<name>...)``- Define named group
* ``(?P=name)``- Backreferencing by group name
* ``\number`` - Backreferencing by group number

.. csv-table:: Regular Expression Groups
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``(...)``", "Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group"
    "``(?P<name>...)``", "substring matched by the group is accessible via the symbolic group name name"
    "``(?P=name)``", "A backreference to a named group"
    "``\number``", "Matches the contents of the group of the same number"

Example:

    * ``(?P<tag><.*?>)text(?P=tag)``
    * ``(?P<tag><.*?>)text\1``
    * ``(.+) \1`` matches ``the the`` or ``55 55``
    * ``(.+) \1`` not matches ``thethe`` (note the space after the group)


Example
=======
* ``r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'``


Visualizing RegExps
===================
* https://regexper.com/
* https://regex101.com/

.. figure:: img/regexp-vizualization.png
    :scale: 100%
    :align: center

    Visualization for pattern ``r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'``
