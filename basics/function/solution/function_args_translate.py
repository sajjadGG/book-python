PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

DATA = 'zażółć gęślą jaźń'


def translate(text):
    return ''.join(PL.get(x, x) for x in text)


result = translate(DATA)

print(result)
# zazolc gesla jazn
