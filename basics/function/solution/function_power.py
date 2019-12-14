def power(a, b=None):
    if b is None:
        b = a

    return a ** b


print(power(10, 2))
# 100

print(power(3))
# 27
