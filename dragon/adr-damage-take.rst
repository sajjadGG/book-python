Dragon ADR Damage Take
======================


Rationale
---------
* ADR - Architecture Design Records
* Make DMG points damage to the dragon


Possibilities
-------------
>>> dragon.take_damage(DMG)  # good

>>> dragon.receive_damage(DMG)

>>> dragon.wound(DMG)

>>> dragon.hurt(DMG)

>>> dragon.hit(DMG)

>>> dragon.damage(DMG)

>>> dragon.hurt_self(DMG)

>>> dragon.receive_damage(DMG)

>>> dragon - DMG
>>> dragon -= DMG

>>> dragon.health - DMG
>>> dragon.health -= DMG

>>> dragon.__sub__(DMG)
>>> dragon.__isub__(DMG)


Option 7
--------
>>> dragon.set_damage()

* Bad: ``set`` is used as a setter of a field ``damage``
