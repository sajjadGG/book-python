************
Regexp Match
************


About
=====
* ``re.match()``
* Checks exact match
* Checking if user input is correct (email, url, NIP, VAT ID, PESEL)


Examples
========
.. code-block:: python
    :caption: Usage of ``re.match()``

    import re


    def is_valid_email(email: str) -> bool:
        PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'

        if re.match(PATTERN, email):
            return True
        else:
            return False


    is_valid_email('mark.watney@nasa.gov')     # True
    is_valid_email('mark.watney@nasa.g')       # False


Good Engineering Practices
==========================
* Doctests

.. code-block:: python

    import re

    email = r'^(?P<username>[a-z][a-z0-9._-]*)@(?P<domain>([a-z0-9-.]+)+)\.(?P<tld>[a-z]{2,10})$'

    def is_valid(data):
        if re.match(pattern, data):
            return True
        else:
            return False

.. code-block:: python

    import re

    username = r'[a-z][a-z0-9._-]*'
    domain   = r'([a-z0-9-.]+)+'
    tld      = r'[a-z]{2,10}'
    email    = f'{username}@{domain}.{tld}'

    def is_valid(data):
        if re.match(pattern, data):
            return True
        else:
            return False

.. code-block:: python

    import re

    username = r'^(?P<username>[a-z][a-z0-9._-]*)'
    domain   = r'(?P<domain>([a-z0-9-.]+)+)'
    tld      = r'(?P<tld>[a-z]{2,10})'
    email    = f'^{username}@{domain}.{tld}$'

    def is_valid(data):
        if re.match(pattern, data):
            return True
        else:
            return False

.. code-block:: python

    import re

    username = r'[a-z][a-z0-9._-]*'
    domain   = r'([a-z0-9-.]+)+'
    tld      = r'[a-z]{2,10}'
    email    = f'^(?P<username>{username})@(?P<domain>{domain}).(?P<tld>{tld})$'

    def is_valid(data):
        if re.match(pattern, data):
            return True
        else:
            return False

.. code-block:: python

    import re

    username = r'[a-z][a-z0-9._-]*'
    domain   = r'([a-z0-9-.]+)+'
    tld      = r'[a-z]{2,10}'
    email    = f'^(?P<username>{username})@(?P<domain>{domain}).(?P<tld>{tld})$'

    pattern = re.compile(email, flags=re.IGNORECASE)

    def is_valid(data):
        if re.match(pattern, data):
            return True
        else:
            return False

.. code-block:: python
    :caption: Doctests

    """
    >>> is_valid_email('mark.watney@nasa.gov')
    True
    >>> is_valid_email('Mark.Watney@nasa.gov')
    True
    >>> is_valid_email('+mark.watney@nasa.gov')
    False
    >>> is_valid_email('mark.watney+@nasa.gov')
    True
    >>> is_valid_email('mark.watney+newsletter@nasa.gov')
    True
    >>> is_valid_email('mark.watney@.gov')
    False
    >>> is_valid_email('@nasa.gov')
    False
    >>> is_valid_email('mark.watney@nasa.g')
    False
    """

    import re


    def is_valid_email(email: str) -> bool:
        """Function check email address against Regular Expression"""
        PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'

        if re.match(PATTERN, email):
            return True
        else:
            return False

.. code-block:: python

    """
    >>> is_valid('3ares@nasa.gov')
    False
    >>> is_valid('ares3@nasa.gov')
    True
    >>> is_valid('a3@nasa.gov')
    True
    >>> is_valid('3@nasa.gov')
    False
    >>> is_valid('m@nasa.gov')
    True
    >>> is_valid('m.watney@nasa.gov')
    True
    >>> is_valid('m_watney@nasa.gov')
    True
    >>> is_valid('m-watney@nasa.gov')
    True
    >>> is_valid('mark.watney@nasa.gov')
    True
    >>> is_valid('markwatney@nasa.gov')
    True
    >>> is_valid('jan.twardowski@polsa.gov.pl')
    True
    >>> is_valid('jan.twardowski@polsa24.gov.pl')
    True
    """

    import re

    username = r'^(?P<username>[a-z][a-z0-9._-]*)'
    domain   = r'(?P<domain>([a-z0-9-.]+)+)'
    tld      = r'(?P<tld>[a-z]{2,10})'
    email    = f'^{username}@{domain}.{tld}$'
    pattern = re.compile(email, flags=re.IGNORECASE)


    def is_valid(data):
        if pattern.match(data):
            return True
        else:
            return False


Assignments
===========

.. todo:: Convert assignments to literalinclude

Regexp Match Phones
-------------------
* Assignment: Regexp Match Phones
* Filename: :download:`assignments/regexp_match_phones.py`
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Use regular expressions to validate phone numbers
    3. Check all given numbers (see input section)
    4. Valid phone number formats:

        a. Easy version: ``+## ### ### ###``
        b. Harder version: ``+## ### ### ###`` or ``+## ## ### ####``

    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj wyrażeń regularnych do walidacji numeru telefonu
    3. Sprawdź wszystkie podane numery (patrz sekcja input)
    4. Poprawne formaty numeru:

        a. Wersja łatwa: ``+## ### ### ###``
        b. Wersja trudniejsza: ``+## ### ### ###`` lub ``+## ## ### ####``

    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> is_valid_phone('+48 (12) 355 5678')
    False
    >>> is_valid_phone('+48 123 555 678')
    True
    >>> is_valid_phone('123 555 678')
    False
    >>> is_valid_phone('+48 12 355 5678')
    True
    >>> is_valid_phone('+48 123-555-678')
    False
    >>> is_valid_phone('+48 123 555 6789')
    False
    >>> is_valid_phone('+1 (123) 555-6789')
    False
    >>> is_valid_phone('+1 (123).555.6789')
    False
    >>> is_valid_phone('+1 800-python')
    False
    >>> is_valid_phone('+48123555678')
    False
    >>> is_valid_phone('+48 123 555 678 wew. 1337')
    False
    >>> is_valid_phone('+48 123555678,1')
    False
    >>> is_valid_phone('+48 123555678,1,2,3')
    False

Regexp Match Git Flow
---------------------
* Assignment: Regexp Match Git Flow
* Filename: :download:`assignments/regexp_match_gitflow.py`
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Use regular expressions to validate Git branch names
    2. Check all given branch names (see input section)
    3. Branch names should comply with Git Flow convention:

        a. ``release/major.minor`` - major and minor are unsigned integers
        b. ``feature/``, ``bugfix/``, ``hotfix/`` - branch prefixes
        c. ``prefix/ISSUEKEY-NUMBER-summary``
        d. ``ISSUEKEY`` - uppercase, only ASCII letters, minimum 2 characters, not longer than 10
        e. ``NUMBER`` - positive integer, maximal 5 digits
        f. ``summary`` - lowercase, ASCII letters and numbers, dashes instead whitespaces, not longer than 30
        g. ``pull-request/NUMBER`` - positive integer, maximal 5 digits

    4. Example of valid branches:

        a. ``master``
        b. ``develop``
        c. ``release/1.0``
        d. ``feature/ID-1337-some-new-feature``
        e. ``bugfix/ID-1337-fixing-old-bug``
        f. ``hotfix/ID-1337-bug-on-production``
        g. ``pull-request/42``


Polish:
    1. Użyj wyrażeń regularnych do walidacji nazwy gałęzi w Git
    2. Sprawdź wszystkie dane nazwy gałęzi (patrz sekcja input)
    3. Nazwy gałęzi powinny stosować się do konwencji Git Flow:

        a. ``release/major.minor`` - major i minor nieujemne liczby całkowite
        b. ``feature/``, ``bugfix/``, ``hotfix/`` - prefiks nazwy gałęzi
        c. ``prefix/ISSUEKEY-NUMBER-summary``
        d. ``ISSUEKEY`` - duże litery, tylko litery ASCII, minimum 2 znaki, nie więcej niż 10
        e. ``NUMBER`` - dodatnia liczba całkowita, maksymalnie 5 cyfr
        f. ``summary`` - małe litery, litery ASCII i liczby, myślniki zamiast białych spacji, nie dłuższa niż 30
        g. ``pull-request/NUMBER`` - dodatnia liczba całkowita, maksymalnie 5 cyfr

    4. Przykład poprawnych gałęzi:

        a. ``master``
        b. ``develop``
        c. ``release/1.0``
        d. ``feature/ID-1337-some-new-feature``
        e. ``bugfix/ID-1337-fixing-old-bug``
        f. ``hotfix/ID-1337-bug-on-production``
        g. ``pull-request/42``

