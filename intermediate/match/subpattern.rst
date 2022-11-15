Match Subpatterns
=================


Use Case - 0x01
---------------
* Game Controller

Test Setup:

>>> class Hero:
...     def walk(self, direction, value): ...
...     def run(self, direction): ...
>>>
>>> hero = Hero()

Use Case:

>>> action = ['walk', 'left', 10]
>>>
>>> match action:
...     case ['walk', ('up'|'down'|'left'|'right') as direction, value]:
...         hero.walk(direction, value)
...     case ['run', direction] if direction in ['up','down','left','right']:
...         hero.run(direction)
