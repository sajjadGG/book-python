TEXT = 'We choose to go to the Moon!'
REMOVE = 'to go to '

a = TEXT.find(REMOVE)   # 10
b = a + len(REMOVE)     # 19

first_part = TEXT[:a]   # 'We choose '
second_part = TEXT[b:]  # 'the Moon!'

print(first_part + second_part)
# 'We choose the Moon!'
