.. testsetup::

    # doctest: +SKIP_FILE


Dragon ADR Damage Take
======================
* ADR - Architecture Design Records


Problem
-------
* Make DMG points damage to the dragon

.. code-block:: text

    dragon ---> enemy
    dragon -> enemy
    dragon <-> enemy
    dragon <- enemy
    dragon <--- enemy


Option 1
--------
>>> dragon.take_damage(DMG)
>>> dragon.hurt_self(DMG)
>>> dragon.receive_damage(DMG)

* Good: dragon ---> enemy


Option 2
--------
>>> dragon.wound(DMG)
>>> dragon.hurt(DMG)
>>> dragon.hit(DMG)
>>> dragon.damage(DMG)

* Good: dragon -> enemy
* Bad: dragon -> enemy


Option 3
--------
>>> dragon - DMG
>>> dragon -= DMG

* Good: simple
* Good: can use ``.__sub__()`` for validation if needed
* Bad: requires knowledge of API


Option 4
--------
>>> dragon - Damage(20)
>>> dragon -= Damage(20)

* Good: simple
* Good: can use ``.__sub__()`` for validation if needed
* Bad: requires knowledge of API


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
>>> dragon.__sub__(DMG)
>>> dragon.__isub__(DMG)

* Good: encapsulation
* Bad: not Pythonic way
* Bad: not simple
* Bad: requires knowledge of API


Option 8
--------
>>> dragon.set_damage(DMG)

* Good: encapsulation
* Bad: not Pythonic way
* Bad: ``set_damage()`` indicates setter of ``damage`` field


Decision
--------
>>> dragon.take_damage(DMG)

* Good: easy
* Good: dragon ---> enemy
