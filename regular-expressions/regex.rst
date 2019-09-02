*******************
Regular Expressions
*******************


Most frequent used functions in ``re`` module
=============================================

``re.match()``
--------------
.. code-block:: python
    :caption: Usage of ``re.match()``

    import re

    PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'

    def is_valid_email(email: str) -> bool:
        if re.match(PATTERN, email):
            return True
        else:
            return False

    is_valid_email('jose.jimenez@nasa.gov')     # True
    is_valid_email('jose.jimenez@nasa.g')       # False

``re.search()``
---------------
.. code-block:: python
    :caption: Usage of ``re.search()``

    import re


    TEXT = "Issues #23919, #31337 removed obsolete comments"

    def contains(text, pattern)
        if re.search(pattern, text):
            return True
        else:
            return False


    contains(r'#[0-9]+', TEXT)      # True
    contains(r'#[a-z]+', TEXT)      # False

``re.findall()`` and ``re.finditer()``
--------------------------------------
.. code-block:: python
    :caption: Usage of ``re.findall()`` and ``re.finditer()``

    import re


    PATTERN = r'#[A-Z]{2,10}-[0-9]{1,6}'
    TEXT = "MYPROJ-1337 removed obsolete comments"

    re.findall(PATTERN, TEXT)
    # ['MYPROJ-1337']

``re.compile()``
----------------
.. code-block:: python
    :caption: Compiles at every loop iteration, and then matches
    :emphasize-lines: 15

    import re

    PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'
    DATA = [
        'jose.jimenez@nasa.gov',
        'Jose.Jimenez@nasa.gov',
        '+jose.jimenez@nasa.gov',
        'jose.jimenez+@nasa.gov',
        'jose.jimenez+newsletter@nasa.gov',
        'jose.jimenez@.gov',
        '@nasa.gov',
        'jose.jimenez@nasa.g']

    for email in DATA:
        re.match(PATTERN, email)

.. code-block:: python
    :caption: Compiling before loop, hence matching only inside
    :emphasize-lines: 15

    import re

    PATTERN = re.compile(r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$')
    DATA = [
        'jose.jimenez@nasa.gov',
        'Jose.Jimenez@nasa.gov',
        '+jose.jimenez@nasa.gov',
        'jose.jimenez+@nasa.gov',
        'jose.jimenez+newsletter@nasa.gov',
        'jose.jimenez@.gov',
        '@nasa.gov',
        'jose.jimenez@nasa.g']

    for email in DATA:
        PATTERN.match(email)

``re.sub()``
------------
.. code-block:: python
    :caption: Usage of ``re.sub()``

    import re


    PATTERN = r'\s[a-z]{3}\s'
    TEXT = 'Baked Beans And Spam'

    re.sub(PATTERN, ' & ', TEXT, flags=re.IGNORECASE)
    # 'Baked Beans & Spam'

``re.split()``
--------------
.. code-block:: python
    :caption: Usage of ``re.split()``

    import re

    PATTERN = r'\s[a-z]{3}\s'
    TEXT = 'Baked Beans And Spam'

    re.split(PATTERN, TEXT, flags=re.IGNORECASE)
    # ['Baked Beans', 'Spam']

Comparision between ``re.match()``, ``re.search()`` and ``re.findall()``
------------------------------------------------------------------------
.. code-block:: python
    :caption: Comparision between ``re.match()``, ``re.search()`` and ``re.findall()``

    import re


    PATTERN = r'#[0-9]+'
    TEXT = "Issues #23919, #31337 removed obsolete comments"

    re.findall(PATTERN, TEXT)           # ['#23919', '#31337']
    re.search(PATTERN, TEXT).group()    # '#23919'
    re.match(PATTERN, TEXT)             # None


RegEx parameters (variables)
============================
.. code-block:: python
    :caption: Usage of group in ``re.match()``

    import re

    PATTERN = r'(?P<first_name>\w+) (?P<last_name>\w+)'
    TEXT = 'Jan Twardowski'

    matches = re.match(PATTERN, TEXT)

    matches.group('first_name')     # 'Jan'
    matches.group('last_name')      # 'Twardowski'
    matches.group(1)                # 'Jan'
    matches.group(2)                # 'Twardowski'
    matches.groups()                # ('Jan', 'Twardowski')
    matches.groupdict()             # {'first_name': 'Jan', 'last_name': 'Twardowski'}


Multi line searches
===================
.. code-block:: python
    :caption: Usage of regexp

    import re

    PATTERN = r'^#[0-9]+'
    TEXT = """
    #27533 Fixed inspectdb crash;
    #31337 Remove commented out code
    """

    re.findall(PATTERN, TEXT)
    # []

    re.findall(PATTERN, TEXT, flags=re.MULTILINE)
    # ['#27533', '#31337']


Greedy and non-greedy search
============================
* greedy qualifiers: ``*``, ``+``, ``?``
* they match as much text as possible
* Adding ``?`` after the qualifier makes it non-greedy

.. code-block:: python
    :caption: Usage of greedy and non-greedy search in ``re.findall()``

    import re

    TEXT = '<strong>Ehlo World</strong>'

    re.findall(r'<.*>', TEXT)         # ['<strong>Ehlo World</strong>']
    re.findall(r'<.*?>', TEXT)        # ['<strong>', '</strong>']

.. code-block:: python
    :caption: Usage of greedy and non-greedy search with groups

    re.findall(r'<(.*)>', TEXT)       # ['strong>Ehlo World</strong']
    re.findall(r'<(.*?)>', TEXT)      # ['strong', '/strong']
    re.findall(r'</?(.*?)>', TEXT)    # ['strong', 'strong']


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

Parsing text from webpage
-------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/regex_html.py`

:English:
    #. Write input data to ``regex_html.html`` file
    #. Using regexp split text by paragraphs
    #. Print on the screen paragraph starting with "We choose to go to the moon"

:Polish:
    #. Zapisz dane wejściowe do pliku ``regex_html.html``
    #. Za pomocą regexpów podziel tekst na paragrafy
    #. Wyświetl paragraf zaczynający się od słów "We choose to go to the moon"

:Input:
    .. code-block:: text
        :caption: "Moon Speech" by John F. Kennedy, Rice Stadium, Houston, TX, 1962-09-12 :cite:`Kennedy1962`

        <html><body><bgsound src="jfktalk.wav" loop="2"><p></p><center><h3>John F. Kennedy Moon Speech - Rice Stadium</h3><img src="jfkrice.jpg"><h3>September 12, 1962</h3></center><p></p><hr><p></p><center>Movie clips of JFK speaking at Rice University: <a href="JFKatRice.mov">(.mov)</a> or <a href="jfkrice.avi">(.avi)</a> (833K)</center><p><a href="jfkru56k.asf">See and hear</a> the entire speech for 56K modem download [8.7 megabytes in a .asf movie format which requires Windows Media Player 7 (speech lasts about 33 minutes)].<br><a href="jfkru100.asf">See and hear</a> the entire speech for higher speed access [25.3 megabytes in .asf movie format which requires Windows Media Player 7].<br><a href="jfkslide.asf">See and hear</a> a five minute audio version of the speech with accompanying slides and music. This is a most inspirational presentation of, perhaps, the most famous space speech ever given. The file is a streaming video Windows Media Player 7 format. [11 megabytes in .asf movie format which requires Windows Media Player 7]. <br><a href="jfk_rice_speech.mpg">See and hear</a> the 17 minute 48 second speech in the .mpg format. This is a very large file of 189 megabytes and only suggested for those with DSL, ASDL, or cable modem access as the download time on a 28.8K or 56K modem would be many hours duration. </p><p></p><hr><p></p><center><h4>TEXT OF PRESIDENT JOHN KENNEDY'S RICE STADIUM MOON SPEECH</h4></center><p>President Pitzer, Mr. Vice President, Governor, CongressmanThomas, Senator Wiley, and Congressman Miller, Mr. Webb, Mr.Bell, scientists, distinguished guests, and ladies and gentlemen:</p><p>We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organize and measure the best of our energies and skills,because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win,and the others, too. </p><p>It is for these reasons that I regard the decision last year to shift our efforts in space from low to high gear as among the most important decisions that will be made during my incumbency in the office of the Presidency. </p><p>In the last 24 hours we have seen facilities now being created for the greatest and most complex exploration in man's history.We have felt the ground shake and the air shattered by the testing of a Saturn C-1 booster rocket, many times as powerful as the Atlas which launched John Glenn, generating power equivalent to 10,000 automobiles with their accelerators on the floor.We have seen the site where the F-1 rocket engines, each one as powerful as all eight engines of the Saturn combined, will be clustered together to make the advanced Saturn missile, assembled in a new building to be built at Cape Canaveral as tall as a48 story structure, as wide as a city block, and as long as two lengths of this field.</p><p></p><hr><p></p><center><a href="movies.html">Return to Space Movies Cinema</a></center></body></html>

PESEL Validation
----------------
* Complexity level: medium
* Lines of code to write: 0 lines
* Estimated time of completion: 10 min

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
