numbers = (x for x in range(1, 34) if x % 3 == 0)
numbers = filter(lambda x: x%2, numbers)
numbers = map(lambda x: x**3, numbers)
numbers = list(numbers)
mean = sum(numbers) / len(numbers)

print(mean)
# 11502.0
