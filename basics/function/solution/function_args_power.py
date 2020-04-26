def power(a, b=None):
    if b is None:
        b = a

    return a ** b


print(power(4, 3))
# 64

print(power(3))
# 27
