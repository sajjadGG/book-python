Syntax Comments
===============


Rationale
---------
* Line Comments
* Multiline Comments
* Inline Comments


Line Comments
-------------
* :pep:`8` -- Style Guide for Python Code: for line comments: Hash (``#``), space and then comment

>>> # Mark thinks he is...
>>> print('Mark Watney: Space Pirate')
Mark Watney: Space Pirate


Multiline Comments
------------------
* There are no multiline comments in Python
* You can create many one line comments

>>> # Mark thinks...
>>> # he is...
>>> print('Mark Watney: Space Pirate')
Mark Watney: Space Pirate

People sometimes use multiline strings to achieve similar behavior as
multiline-comment. Unfortunately this requires Python to define string,
store it into the memory, and then remove it.

>>> # doctest: +SKIP
... """
... This is first line of a multiline comment
... This is second line of a multiline comment
... """


Inline Comments
---------------
* :pep:`8` -- Style Guide for Python Code: for inline comments: code, two spaces, hash (``#``), space and then comment

>>> print('Mark Watney: Space Pirate')  # This is who Mark Watney is
Mark Watney: Space Pirate


Docstring and Doctests
----------------------
* Docstring is a first multiline comment in: File/Module, Class, Method/Function
* Used for ``doctest``
* More information in `Function Doctest`
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters

>>> # doctest: +SKIP
... """
... This is my first Python script
...
... >>> result
... 12
... """
>>>
>>> result = 10 + 2


Good Practices
--------------
* If you need comments, you failed with writing clean code
* Instead of comments write more readable code
* Never commit commented out code
* Use Version Control System instead - e.g.: ``git blame``
* IDE has Local history (modifications) and you can compare file


Assignments
-----------
.. literalinclude:: assignments/syntax_comments_a.py
    :caption: :download:`assignments/syntax_comments_a.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_comments_b.py
    :caption: :download:`assignments/syntax_comments_b.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_comments_c.py
    :caption: :download:`assignments/syntax_comments_c.py`
    :end-before: # Solution
