def is_odd(x):
    if x % 2:
        return True
    else:
        return False


def cube(x):
    return x ** 3


numbers = (x for x in range(1, 34) if x % 3 == 0)
numbers = filter(is_odd, numbers)
numbers = map(cube, numbers)
numbers = list(numbers)
mean = sum(numbers) / len(numbers)
print(mean)
# 11502.0
