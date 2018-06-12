import re


PATTERN = r'[a-z]'
text = 'Lorem Ipsum'

re.findall(PATTERN, text)
# ['o', 'r', 'e', 'm', 'p', 's', 'u', 'm']

characters = re.compile(PATTERN)
characters.findall(text)
# ['o', 'r', 'e', 'm', 'p', 's', 'u', 'm']


for i in range(0, 1e6):
    # compiles at every loop iteration
    # and then finds
    re.findall(PATTERN, text)


for i in range(0, 1e6):
    # once compiled, now only searches
    characters.findall(text)