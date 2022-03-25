.. testsetup::

    class Dragon:
        def __init__(*args, **kwargs):
            pass


Dragon ADR Init Name
====================
* ADR - Architecture Design Records


Problem
-------
* Create and name it "Wawelski"


Option 1
--------
>>> dragon = Dragon('Wawelski')

* Good: easy to use
* Bad: less verbose than keyword arguments


Option 2
--------
>>> dragon = Dragon(name='Wawelski')

* Good: easy to use
* Good: more verbose than positional arguments
* Bad: too verbose for such simple example


Decision
--------
>>> dragon = Dragon('Wawelski')

* Because: easy to use
* Because: verbose enough
