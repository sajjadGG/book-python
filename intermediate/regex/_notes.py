# Groups - wszystko będzie dotyczyło nawiasów () i tego co w nich
# (...) - positional group

result = re.finditer('([A-Z]\w+) ([A-Z]\w+)', TEXT)
match = next(result)

match.groups()
# ('Yuri', 'Gagarin')

match.group()
# 'Yuri Gagarin'
match.group(0)
# 'Yuri Gagarin'
match.group(1)
# 'Yuri'
match.group(2)
# 'Gagarin'

# (?P<nazwa>...) - name group


result = re.finditer('(?P<firstname>[A-Z]\w+) (?P<lastname>[A-Z]\w+)', TEXT)
match = next(result)

match.group()
# 'Yuri Gagarin'
match.group(0)
# 'Yuri Gagarin'
match.group(1)
# 'Yuri'
match.group(2)
# 'Gagarin'

match.group('firstname')
# 'Yuri'
match.group('lastname')
# 'Gagarin'

match.groups()
# ('Yuri', 'Gagarin')
match.groupdict()
# {'firstname': 'Yuri', 'lastname': 'Gagarin'}


line_of_code = 'myvar = 123'
assignment = '^(?P<variable>\w+)\s?=\s?(?P<value>.+)$'

result = re.finditer(assignment, line_of_code)
match = next(result)

match.groupdict()
{'variable': 'myvar', 'value': '123'}


# (?#...) - komentarz

# https://docs.python.org/3/reference/grammar.html
# https://github.com/python/cpython/blob/main/Grammar/python.gram
# https://www.youtube.com/watch?v=esZLCuWs_2Y


re.findall('[abc]', TEXT)
# ['a', 'a', 'a', 'c', 'a', 'c', 'a', 'a']
re.findall('[abc]', TEXT, flags=re.IGNORECASE)
# ['a', 'a', 'a', 'c', 'a', 'c', 'A', 'a', 'a']
re.findall('[abc]', TEXT, flags=re.I)
# ['a', 'a', 'a', 'c', 'a', 'c', 'A', 'a', 'a']

# 2. Wykorzystanie w Python
import re

re.findall(), re.finditer()


result = re.finditer(r'\d{1,4}', TEXT)
r = next(result)

r
# <re.Match object; span=(38, 40), match='12'>

r.span()
# (38, 40)
r.start()
# 38
r.end()
# 40
r.pos
# 0
r.endpos
# 60

r.group()
'12'
r.groups()
()
r.groupdict()
{}




re.match()   # służy do walidacji (dokładnego dopasowania)

email = 'mwatney@nasa.gov'
username = '[a-z][a-z0-9.-]+'
domain = '[a-z][a-z0-9.-]+'
tld = '(gov|int|com|pl)'
pattern = f'{username}@{domain}\.{tld}'
pattern
# '[a-z][a-z0-9.-]+@[a-z][a-z0-9.-]+\\.(gov|int|com|pl)'
pattern = f'^{username}@{domain}\.{tld}$'
re.match(pattern, email)
# <re.Match object; span=(0, 16), match='mwatney@nasa.gov'>
re.match(pattern, '123mwatney@nasa.gov')


def is_valid_email(email):
    if re.match(pattern, email):
        return True
    else:
        return False

is_valid_email('mwatney@nasa.gov')
# True
is_valid_email('123mwatney@nasa.gov')
# False
is_valid_email('mwatney@nasa.co.uk')
# False


re.search()  # czy w tekście jest znalezisko (da pierwsze wystąpienie, a później przestanie szukać)

TEXT
# 'Yuri Gagarin launched to space on Apr 12th, 1961 at 1:37 pm.'

firstname = '(?P<firstname>[A-Z][a-z]+)'
lastname = '(?P<lastname>[A-Z][a-z]+)'

re.search(f'{firstname} {lastname}', TEXT)
# <re.Match object; span=(0, 12), match='Yuri Gagarin'>


re.sub()

re.sub(r'\b[a-z]{2}\b', '\n', TEXT)
# 'Yuri Gagarin launched \n space \n Apr 12th, 1961 \n 1:37 \n.'

re.sub(r'\b[a-z]{2}\b', ',', TEXT)
# 'Yuri Gagarin launched , space , Apr 12th, 1961 , 1:37 ,.'

re.split()

re.split(r'[\s,.]', TEXT)
# ['Yuri', 'Gagarin', 'launched', 'to', 'space', 'on', 'Apr', '12th', '', '1961', 'at', '1:37', 'am', '']
re.split(r'[\s,.]', TEXT, maxsplit=2)
# ['Yuri', 'Gagarin', 'launched to space on Apr 12th, 1961 at 1:37 pm.']

re.compile()

print(pattern)
# ^[a-z][a-z0-9.-]+@[a-z][a-z0-9.-]+\.(gov|int|com|pl)$

def is_valid_email(email):
    if re.match(pattern, email):
        return True
    else:
        return False


DATA = [
    'mwatney@nasa.gov',
    'mwatney@nasa',
    'mwatney@esa.int',
    '123mwatney@nasa.gov',
]

for email in DATA:
    result = is_valid_email(email)
    print(f'{result=}, {email=}')

result=True, email='mwatney@nasa.gov'
result=False, email='mwatney@nasa'
result=True, email='mwatney@esa.int'
result=False, email='123mwatney@nasa.gov'



username = '[a-z][a-z0-9.-]+'
domain = '[a-z][a-z0-9.-]+'
tld = '(gov|int|com|pl)'
valid_email = re.compile(f'{username}@{domain}\.{tld}')

def is_valid_email(email):
    if valid_email.match(email):
        return True
    else:
        return False
