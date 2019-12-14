def total(sequence):
    return sum(x for x in sequence if x % 2 == 0)


print(total([1, 2, 3, 4]))
# 6

print(total([1, 1, 2]))
# 2

print(total([0, 2, 4, 9]))
# 6
