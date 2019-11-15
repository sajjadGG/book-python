*************
Regexp Syntax
*************


What are Regular Expressions?
=============================
.. glossary::

    pattern
        * ``[a-z]``
        * ``[0-9]``
        * ``[a-zA-Z0-9]``
        * ``\w+``

    group
        ``(...)``

    newline
        ``^``

    endline
        ``$``

    qualifier
        * ``?`` - 0 or 1
        * ``*`` - 0 or many
        * ``+`` - 1 or many

    greedy
        * ``??`` - 0 or 1 (non greedy)
        * ``*?`` - 0 or many (non greedy)
        * ``+?`` - 1 or many (non greedy)

    flags
        * ``re.IGNORECASE``
        * ``re.MULTILINE``
        * ``re.MULTILINE``
        * ``re.DOTALL``

    multiline
        ...

    match
        ...


Constructing
================================
* ``r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'``


Visualizing RegExps
===================
* https://regexper.com/
* https://regex101.com/

.. figure:: img/regexp-vizualization.png
    :scale: 100%
    :align: center

    Visualization for pattern ``r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'``


Qualifiers
==========
.. csv-table:: Regular Expression Syntax
    :header-rows: 1
    :widths: 25, 75

    "Syntax", "Description"
    "``.``", "(Dot.) In default mode, matches any character except a newline"
    "``^``", "(Caret.) Matches the start of the string, and in ``MULTILINE`` mode also matches immediately after each newline"
    "``$``", "Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline"
    "``*``", "Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible"
    "``+``", "Causes the resulting RE to match 1 or more repetitions of the preceding RE"
    "``?``", "Causes the resulting RE to match 0 or 1 repetitions of the preceding RE"
    "``*?``, ``+?``, ``??``", " Adding ``?`` after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched"
    "``{m}``", "Specifies that exactly m copies of the previous RE should be matched; fewer matches cause the entire RE not to match."
    "``{m,n}``", "Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible."
    "``{m,n}?``", "Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible."
    "``\``", "Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a special sequence"
    "``[a-z]``", "any character from ``a`` to ``z``"
    "``[A-Z]``", "any character from ``A`` to ``Z``"
    "``[0-9]``", "any digit from ``0`` to ``9``"
    "``[abc]``", "will match ``a``, ``b`` or ``c``"
    "``|``", "``A|B``, where A and B can be arbitrary REs, creates a regular expression that will match either A or B."
    "``(...)``", "Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group"
    "``(?P<name>...)``", "substring matched by the group is accessible via the symbolic group name name"
    "``(?P=name)``", "A backreference to a named group; it matches whatever text was matched by the earlier group named name. ``(?P<tag><.*?>)text(?P=tag)`` or ``(?P<tag><.*?>)text\1``"
    "``\number``", "Matches the contents of the group of the same number. Groups are numbered starting from 1. For example, ``(.+) \1`` matches ``the the`` or ``55 55``, but not ``thethe`` (note the space after the group)."
    "``\d``", "Unicode decimal digit ``[0-9]``, and many other digit characters"
    "``\s``", "Unicode whitespace characters ``[\t\n\r\f\v]`` and non-breaking spaces"
    "``\w``", "Unicode word characters; this includes most characters that can be part of a word in any language, as well as numbers and the underscore"

Flags
=====
.. csv-table:: Regular Expression Flags
    :header-rows: 1
    :widths: 25, 75

    "Flag", "Description"
    "``re.IGNORECASE``", "Case-insensitive (Unicode support i.e. Ü and ü)"
    "``re.MULTILINE``", "``^`` matches beginning of the string and each line"
    "``re.MULTILINE``", "``$`` matches end of the string and each line"
    "``re.DOTALL``", "``.`` matches newlines"
