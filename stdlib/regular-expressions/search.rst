*************
Regexp Search
*************


About
=====
* ``re.search()``
* Searches if pattern contains a string


Examples
========
.. code-block:: python
    :caption: Usage of ``re.search()``

    import re


    def contains(pattern, text)
        if re.search(pattern, text):
            return True
        else:
            return False


    COMMIT_MESSAGE = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'
    JIRA_ISSUEKEY = r'[A-Z]{2,10}-[0-9]{1,6}'
    REDMINE_NUMBER = r'#[0-9]+'

    contains(JIRA_ISSUEKEY, COMMIT_MESSAGE)      # True
    contains(REDMINE_NUMBER, COMMIT_MESSAGE)     # False


Assignments
===========

Regexp Search
-------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/search_astronauts.py`
* References: First paragraph from Apollo 11 Wikipedia entry :cite:`RegexpWikipediaApollo11`

:English:
    #. Download :download:`data/apollo11-header.txt` and save as ``search_astronauts.txt``
    #. Use ``re.search()`` to check if Astronaut first and last names are in the text
    #. Astronauts to find:

        * Neil Armstrong
        * Buzz Aldrin
        * Michael Collins
        * Jan Twardowski
        * Mark Watney

:Polish:
    #. Pobierz :download:`data/apollo11-header.txt` i zapisz jako ``search_astronauts.txt``
    #. Użyj ``re.search()`` do sprawdzenia czy imiona i nazwiska Astronautów występują w tekście
    #. Astronauts do znalezienia:

        * Neil Armstrong
        * Buzz Aldrin
        * Michael Collins
        * Jan Twardowski
        * Mark Watney

Moon Speech (search)
--------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/search_moon_speech.py`
* References: "Moon Speech" by John F. Kennedy at Rice Stadium, Houston, TX on 1962-09-12 :cite:`RegexpKennedy1962`

:English:
    #. Download "Moon Speech" text :download:`data/moon_speech.html`
    #. Save as ``moon_speech.html``
    #. Using ``re.search()`` split text by paragraphs
    #. Print paragraph starting with "We choose to go to the moon"

:Polish:
    #. Pobierz tekst przemówienia "Moon Speech" :download:`data/moon_speech.html`
    #. Zapisz jako ``moon_speech.html``
    #. Za pomocą ``re.search()`` podziel tekst na paragrafy
    #. Wyświetl paragraf zaczynający się od słów "We choose to go to the moon"

Search for Any Time
-------------------
* Complexity level: medium
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/search_time_any.py`
* References: First paragraph from Apollo 11 Wikipedia entry :cite:`RegexpWikipediaApollo11`

:English:
    #. Download :download:`data/apollo11-header.txt` and save as ``search_astronauts.txt``
    #. Use regular expressions to check text contains time in UTC (format: ``%H:%M UTC``)
    #. Use simplified checking: ``##:## UTC``, where ``#`` is a digit
    #. Print found time

:Polish:
    #. Pobierz :download:`data/apollo11-header.txt` i zapisz jako ``search_astronauts.txt``
    #. Użyj wyrażeń regularnych do sprawdzenia czy tekst zawiera godzinę w UTC (format: ``%H:%M UTC``)
    #. Użyj uproszczonego sprawdzania: ``##:## UTC``, gdzie ``#`` to dowolna cyfra
    #. Print found time

Search for Valid Time
---------------------
* Complexity level: hard
* Lines of code to write: 4 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/search_time_valid.py`
* References: (modified) First paragraph from Apollo 11 Wikipedia entry :cite:`RegexpWikipediaApollo11`

:English:
    #. Use data from "Input" section (see below)
    #. Use regular expressions to check text contains time in UTC (format: ``%H:%M UTC``)
    #. Note, that this is slightly modified text than previously
    #. Check if text contains time in UTC (format: ``%H:%M UTC``)
    #. Found match must be a valid time
    #. Print found time

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Użyj wyrażeń regularnych do sprawdzenia czy tekst zawiera godzinę w UTC (format: ``%H:%M UTC``)
    #. Zwróć uwagę, że to lekko zmodyfikowany tekst niż poprzednio
    #. Sprawdź czy tekst zawiera godzinę w UTC (format: ``%H:%M UTC``)
    #. Znalezisko musi być poprawnym czasem
    #. Wyświetl znaleziony czas

:Input:
    .. code-block:: text
        :caption: (modified) First paragraph from Apollo 11 Wikipedia entry :cite:`RegexpWikipediaApollo11`

        Apollo 11 was the spaceflight that first landed humans on the Moon. Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed the American crew that landed the Apollo Lunar Module Eagle on July 20, 1969, at 20:67 UTC. Armstrong became the first person to step onto the lunar surface six hours and 39 minutes later on July 21 at 02:56 UTC; Aldrin joined him 19 minutes later. They spent about two and a quarter hours together outside the spacecraft, and they collected 47.5 pounds (21.5 kg) of lunar material to bring back to Earth. Command module pilot Michael Collins flew the command module Columbia alone in lunar orbit while they were on the Moon's surface. Armstrong and Aldrin spent 21 hours, 36 minutes on the lunar surface at a site they named Tranquility Base before lifting off to rejoin Columbia in lunar orbit.
