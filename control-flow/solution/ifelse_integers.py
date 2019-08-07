number = input('What is your number?: ')

if int(number) % 1:
    print(False)
else:
    print(True)


# '50' % 1  -> TypeError: not all arguments converted during string formatting
# '50 %s' % 1 -> 50 1
# 50 % 1 -> 0
