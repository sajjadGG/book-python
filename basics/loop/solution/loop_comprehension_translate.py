PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

DATA = 'zażółć gęślą jaźń'

result = ''.join(PL.get(x, x) for x in DATA)

print(result)
# zazolc gesla jazn
