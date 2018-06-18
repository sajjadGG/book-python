import re

text = '<strong>Ehlo World</strong>'

re.findall(r'<.*>', text)
# ['<strong>Ehlo World</strong>']

re.findall(r'<.*?>', text)
# ['<strong>', '</strong>']