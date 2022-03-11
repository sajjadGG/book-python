Dragon ADR Damage Make
======================


Rationale
---------
* ADR - Architecture Design Records
* Dragon makes damage

.. code-block:: text

    dragon ---> enemy
    dragon -> enemy
    dragon <-> enemy
    dragon <- enemy
    dragon <--- enemy


Possibilities
-------------
>>> dragon.take_damage()

>>> dragon.hit()

>>> dragon.wound()

>>> dragon.make_damage()  # good

>>> dragon.attack()

>>> dragon.take_damage(enemy)

>>> dragon.hit(enemy)

>>> dragon.attack(enemy)

>>> dragon.wound(enemy)

>>> dragon.make_damage(enemy)

>>> dragon.hurt()

>>> dragon.damage()

>>> dragon.hurt_someone()

>>> dragon.deal_damage()
