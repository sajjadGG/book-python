.. testsetup::

    # doctest: +SKIP_FILE


Dragon ADR Damage Take
======================
* ADR - Architecture Design Records


Problem
-------
* Make DMG points damage to the dragon


Option 1
--------
>>> dragon.set_damage(DMG)

* Good: easy to use
* Good: clear intent
* Good: encapsulation
* Bad: ``set_damage()`` indicates setter of ``damage`` field
* Bad: not Pythonic way


Option 2
--------
>>> dragon.wound(DMG)
>>> dragon.hurt(DMG)
>>> dragon.hit(DMG)
>>> dragon.damage(DMG)

* Bad: Indication of direction is too weak ``dragon <-> enemy``

Rationale:

.. code-block:: text

    dragon ---> enemy
    dragon -> enemy
    dragon <-> enemy
    dragon <- enemy
    dragon <--- enemy


Option 3
--------
>>> dragon.hurt_self(DMG)
>>> dragon.receive_damage(DMG)

* Good: Explicit relation ``dragon ---> enemy``
* Bad: ``hurt_self()`` is to colloquial
* Bad: Inconsistent with ``make_damage()``


Option 4
--------
>>> dragon.take_damage(DMG)

* Good: Explicit relation ``dragon ---> enemy``
* Good: Consistent with ``make_damage()``


Option 5
--------
>>> dragon.health - DMG
>>> dragon.health -= DMG

* Good: simple
* Good: can use ``@property`` for validation if needed
* Bad: requires knowledge of API
* Bad: encapsulation


Option 6
--------
>>> dragon.health - Damage(20)
>>> dragon.health -= Damage(20)

* Good: simple
* Good: can use ``@property`` for validation if needed
* Bad: requires knowledge of API
* Bad: encapsulation


Option 7
--------
>>> dragon - DMG
>>> dragon -= DMG

* Good: simple
* Good: can use ``.__sub__()`` for validation if needed
* Bad: requires knowledge of API


Option 8
--------
>>> dragon - Damage(20)
>>> dragon -= Damage(20)

* Good: simple
* Good: can use ``.__sub__()`` for validation if needed
* Bad: requires knowledge of API


Option 9
--------
>>> dragon < Damage(20)
>>> dragon <= Damage(20)

* Good: simple
* Good: can use ``.__lt__()``, ``.__le__()`` for validation if needed
* Bad: requires knowledge of API


Option 9
--------
>>> dragon.__sub__(DMG)
>>> dragon.__isub__(DMG)

* Good: encapsulation
* Bad: not Pythonic way
* Bad: not simple
* Bad: requires knowledge of API


Decision
--------
>>> dragon.take_damage(DMG)

* Good: encapsulation
* Good: easy
* Good: Explicit relation ``dragon ---> enemy``
