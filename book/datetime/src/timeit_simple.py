import timeit


duration = timeit.timeit(stmt='a = 1 + 2', number=10000)
print(duration)
# 0.000547270999999995

