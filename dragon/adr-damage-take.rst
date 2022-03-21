Dragon ADR Damage Take
======================


Important
---------
* ADR - Architecture Design Records
* Make DMG points damage to the dragon

Problem
-------
.. code-block:: text

    dragon ---> enemy
    dragon -> enemy
    dragon <-> enemy
    dragon <- enemy
    dragon <--- enemy


Possibilities
-------------


Option 1
--------
>>> dragon.take_damage(DMG)
>>> dragon.hurt_self(DMG)
>>> dragon.receive_damage(DMG)


Option 2
--------
>>> dragon.wound(DMG)
>>> dragon.hurt(DMG)
>>> dragon.hit(DMG)
>>> dragon.damage(DMG)


Option 3
--------
>>> dragon - DMG
>>> dragon -= DMG


Option 4
--------
>>> dragon - Damage(20)
>>> dragon -= Damage(20)


Option 5
--------
>>> dragon.health - DMG
>>> dragon.health -= DMG


Option 6
--------
>>> dragon.health - Damage(20)
>>> dragon.health -= Damage(20)


Option 7
--------
>>> dragon.__sub__(DMG)
>>> dragon.__isub__(DMG)


Option 8
--------
>>> dragon.set_damage()

* Bad: ``set_damage()`` indicates setter of ``damage`` field


Decision
--------
>>> dragon.take_damage(DMG)

* Good: easy
* Good: dragon ---> enemy
