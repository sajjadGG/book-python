number = input('What is your number?: ')

if number % 2:
    print('Odd')
else:
    print('Even')

# '50' % 1  -> TypeError: not all arguments converted during string formatting
# '50 %s' % 1 -> 50 1
# 50 % 1 -> 0
