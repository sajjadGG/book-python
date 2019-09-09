
NUMBERS = range(1, 34)

out = [x for x in NUMBERS if x % 3 == 0]
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]

out = filter(lambda x: not x % 2 == 0, out)
# <filter object at 0x117c639d0>
# [3, 9, 15, 21, 27, 33]

out = map(lambda x: pow(x, 3), out)
# <map object at 0x117c7ac10>
# [3, 9, 15, 21, 27, 33]

numbers = list(out)
# [27, 729, 3375, 9261, 19683, 35937]

mean = sum(numbers) / len(numbers)
# 11502.0
