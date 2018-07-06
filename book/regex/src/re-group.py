import re

PATTERN = r'(?P<first_name>\w+) (?P<last_name>\w+)'
matches = re.match(PATTERN, 'José Jiménez')

matches.group('first_name')
# 'José'

matches.group('last_name')
# 'Jiménez'

matches.group()
# 'José Jiménez'

matches.group(0)
# 'José Jiménez'

matches.group(1)
# 'José'

matches.group(2)
# 'Jiménez'

matches.groups()
# ('José', 'Jiménez')

matches.groupdict()
# {'first_name': 'José', 'last_name': 'Jiménez'}