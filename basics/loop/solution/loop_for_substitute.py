DATA = 'zażółć gęślą jaźń'

PL_ASCII = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ż': 'z',
    'ź': 'z',
}

result = []

for letter in DATA:
    letter = PL_ASCII.get(letter, letter)
    result.append(letter)

result = ''.join(result)
print(result)
# zazolc gesla jazn
