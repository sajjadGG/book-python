DATA = 'We choose to go to the Moon!'
REMOVE = 'to go to '

before_end = DATA.find(REMOVE)  # 23
after_start = before_end + len(REMOVE)  # 27

before = DATA[:before_end]  # 'We choose '
after = DATA[after_start:]  # 'the Moon!'

print(before + after)
# 'We choose the Moon!'
