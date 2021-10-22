"""
* Assignment: Loop While GuessGame1
* Required: yes
* Complexity: medium
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Use `input` in `while True` loop to ask user about number
    2. Compare user's number with `HIDDEN`:
       a. If number is greater, print `Above`
       b. If number is lower, print `Below`
       c. If number is equal, print `Exactly` and break game
    3. Run doctests - all must succeed

Polish:
    1. Użyj `input` w pętli `while True` do pytania użytkownika o liczbę
    2. Porównaj liczbę wprowadzoną przez użytkownika z `HIDDEN`:
       a. Jeżeli jest większa, to wypisz `Above`
       b. Jeżeli jest mniejsza, to wypisz `Below`
       c. Jeżeli jest taka sama, to wypisz `Exactly` i zakończ grę
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop

Tests:
    >>> import sys; sys.tracebacklimit = 0
"""

HIDDEN = 6

while True:
    guess = input('\nType number: ')

    if int(guess) > HIDDEN:
        print('Above')
    elif int(guess) < HIDDEN:
        print('Below')
    else:
        print('Exactly')
        break
