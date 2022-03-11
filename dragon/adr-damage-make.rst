Dragon ADR Damage Make
======================


Rationale
---------
* ADR - Architecture Design Records
* Dragon makes damage


Problem
-------
.. code-block:: text

    dragon ---> enemy
    dragon -> enemy
    dragon <-> enemy
    dragon <- enemy
    dragon <--- enemy


Option 1
--------
>>> dragon.attack()
>>> dragon.hit()
>>> dragon.hurt()
>>> dragon.damage()
>>> dragon.wound()

* Bad: dragon <-> enemy


Option 2
--------
>>> dragon.damage(dragon)
>>> dragon.damage(enemy)


Option 2
--------
>>> dragon.deal_damage()
>>> dragon.hurt_someone()
>>> dragon.make_damage()  # good

* Good: dragon ---> enemy


Option 3
--------
>>> dragon.take_damage()

* Bad: dragon <--- enemy


Option 4
--------
>>> dragon.attack(enemy)
>>> dragon.hit(enemy)
>>> dragon.make_damage(enemy)
>>> dragon.take_damage(enemy)
>>> dragon.wound(enemy)

* Bad: MVC


Option 5
--------
>>> hero.health -= dragon.damage()

* Bad: enkapsulacja


Option 6
--------
>>> hero.wound(dragon.hit())


Option 7
--------
>>> dragon.get_damage()

* Bad: ``get`` is used as a getter of a field ``damage``


Decision
--------
