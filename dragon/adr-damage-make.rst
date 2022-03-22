Dragon ADR Damage Make
======================
* ADR - Architecture Design Records


Problem
-------
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
>>> dragon.deal_damage()
>>> dragon.hurt_someone()
>>> dragon.make_damage()

* Good: dragon ---> enemy


Option 3
--------
>>> dragon.take_damage()

* Bad: dragon <--- enemy


Option 4
--------
>>> dragon.damage(enemy)
>>> dragon.attack(enemy)
>>> dragon.hit(enemy)
>>> dragon.wound(enemy)
>>> dragon.make_damage(enemy)
>>> dragon.take_damage(enemy)

* Good: dragon ---> enemy
* Bad: MVC

.. figure:: img/firkraag.jpeg

Problem:

>>> class BankAccount:
...     def transfer(destination_account):
...         amount = 1000
...         destination_account.deposit(1000)

* Bad: inny bank nie udostępni Ci swojego kodu źródłowego, tylko po to aby móc zrobić przelew


Option 5
--------
>>> hero.health -= dragon.damage()

* Bad: enkapsulacja


Option 6
--------
>>> hero.wound(dragon.hit())

* Bad: readibility

Option 7
--------
>>> dragon.get_damage()

* Bad: name ``get_damage()`` indicate a getter of ``damage`` field


Decision
--------
>>> dmg = dragon.make_damage()

* Good: dragon ---> enemy
