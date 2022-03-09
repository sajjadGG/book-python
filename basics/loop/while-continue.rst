Loop While Continue
===================


Skip Iteration
--------------
* if ``continue`` is encountered, it will jump to next loop iteration

>>> TEXT = ['# "Moon Speech" by John F. Kennedy, Rice Stadium, Houston, TX, 1962-09-12',
...         '# Source: http://er.jsc.nasa.gov/seh/ricetalk.htm',
...         'We choose to go to the Moon.',
...         'We choose to go to the Moon in this decade and do the other things.',
...         'Not because they are easy, but because they are hard.',
...         'Because that goal will serve to organize and measure the best of our energies a skills.',
...         'Because that challenge is one that we are willing to accept.',
...         'One we are unwilling to postpone.',
...         'And one we intend to win']
>>>
>>> i = 0
>>>
>>> while i < len(TEXT):
...     line = TEXT[i]
...     i += 1
...
...     if line.startswith('#'):
...         continue
...
...     print(line)
We choose to go to the Moon.
We choose to go to the Moon in this decade and do the other things.
Not because they are easy, but because they are hard.
Because that goal will serve to organize and measure the best of our energies a skills.
Because that challenge is one that we are willing to accept.
One we are unwilling to postpone.
And one we intend to win


.. todo:: Assignments
