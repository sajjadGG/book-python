*************************
Match, search and Findall
*************************


``re.match()``
==============
.. code-block:: python
    :caption: Usage of ``re.match()``

    import re


    PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'

    def is_valid_email(email: str) -> bool:
        if re.match(PATTERN, email):
            return True
        else:
            return False

    is_valid_email('mark.watney@nasa.gov')     # True
    is_valid_email('mark.watney@nasa.g')       # False


``re.search()``
===============
.. code-block:: python
    :caption: Usage of ``re.search()``

    import re


    INPUT = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'

    def contains(pattern, text)
        if re.search(pattern, text):
            return True
        else:
            return False


    contains(r'[A-Z]{2,10}-[0-9]{1,6}', INPUT)      # True
    contains(r'#[0-9]+', INPUT)                     # False


``re.findall()`` and ``re.finditer()``
======================================
.. code-block:: python
    :caption: Usage of ``re.findall()`` and ``re.finditer()``

    import re


    PATTERN = r'[A-Z]{2,10}-[0-9]{1,6}'
    INPUT = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'

    re.findall(PATTERN, INPUT)
    # ['MYPROJ-1337', 'MYPROJ-997']


Comparision
===========
.. code-block:: python
    :caption: Comparision between ``re.match()``, ``re.search()`` and ``re.findall()``

    import re


    PATTERN = r'[A-Z]{2,10}-[0-9]{1,6}'
    INPUT = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'

    re.findall(PATTERN, INPUT)           # ['MYPROJ-1337', 'MYPROJ-997']
    re.search(PATTERN, INPUT).group()    # 'MYPROJ-1337'
    re.match(PATTERN, INPUT)             # None


Good practices
==============

Tests
-----
.. code-block:: python
    :caption: Usage of ``re.match()``

    import re

    PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'


    def is_valid_email(email: str) -> bool:
        """
        Function check email address against Regular Expression

        >>> is_valid_email('jose.jimenez@nasa.gov')
        True
        >>> is_valid_email('Jose.Jimenez@nasa.gov')
        True
        >>> is_valid_email('+jose.jimenez@nasa.gov')
        False
        >>> is_valid_email('jose.jimenez+@nasa.gov')
        True
        >>> is_valid_email('jose.jimenez+newsletter@nasa.gov')
        True
        >>> is_valid_email('jose.jimenez@.gov')
        False
        >>> is_valid_email('@nasa.gov')
        False
        >>> is_valid_email('jose.jimenez@nasa.g')
        False
        """
        if re.match(PATTERN, email):
            return True
        else:
            return False

Assignments
===========

PESEL Validation
----------------
* Complexity level: medium
* Lines of code to write: 0 lines
* Estimated time of completion: 10 min

:English:
    .. todo:: English translation

:Polish:
    #. Przeprowadź eksperyment myślowy (nie pisz kodu tylko pomyśl)
    #. Jak sprawdzić za pomocą wyrażeń regularnych czy:

        * czy pesel jest poprawny?
        * jaka jest data urodzenia? (podaj obiekt ``datetime.date``)
        * płeć użytkownika który podał PESEL

    #. Mając PESEL "69072101234"

        #. Jakie wyrażenie może być na pierwszym miejscu w PESEL?
        #. Jakie wyrażenie może być na drugim miejscu w PESEL?
        #. Jakie wyrażenie może być na trzecim miejscu w PESEL?
        #. Jakie wyrażenie może być na czwartym miejscu w PESEL?
        #. Jakie wyrażenie może być na piątym miejscu w PESEL?
        #. Jakie wyrażenie może być na szóstym miejscu w PESEL?

    #. Mając PESEL "18220801234"

        #. Jakie wyrażenie może być na pierwszym miejscu w PESEL?
        #. Jakie wyrażenie może być na drugim miejscu w PESEL?
        #. Jakie wyrażenie może być na trzecim miejscu w PESEL?
        #. Jakie wyrażenie może być na czwartym miejscu w PESEL?
        #. Jakie wyrażenie może być na piątym miejscu w PESEL?
        #. Jakie wyrażenie może być na szóstym miejscu w PESEL?

    #. Sprawdź sumę kontrolną
