PL_ASCII = {'ą': 'a', 'ć': 'c', 'ę': 'e',
            'ł': 'l', 'ń': 'n', 'ó': 'o',
            'ś': 's', 'ż': 'z', 'ź': 'z'}

DATA = 'zażółć gęślą jaźń'

result = []
i = 0

while i < len(DATA):
    letter = DATA[i]
    letter = PL_ASCII.get(letter, letter)
    result.append(letter)
    i += 1

result = ''.join(result)
print(result)
# zazolc gesla jazn
