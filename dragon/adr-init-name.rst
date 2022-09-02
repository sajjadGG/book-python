.. testsetup::

    # doctest: +SKIP_FILE


Dragon ADR Init Name
====================
* ADR - Architecture Design Records


Problem
-------
* Create Dragon and name it "Wawelski"


Option 1
--------
>>> dragon = Dragon('Wawelski')

* Good: easy to use
* Bad: less verbose than keyword arguments
* Verdict: candidate


Option 2
--------
>>> dragon = Dragon(name='Wawelski')

* Good: easy to use
* Good: more verbose than positional arguments
* Bad: too verbose for such simple example
* Verdict: rejected, too verbose for such simple example


Decision
--------
>>> dragon = Dragon('Wawelski')

* Because: easy to use
* Because: verbose enough for now
