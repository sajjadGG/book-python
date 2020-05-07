from timeit import timeit


setup = """name = 'Jose Jimenez'"""
stmt = """result = f'My name... {name}'"""

duration = timeit(stmt, setup, number=10000)

print(duration)
# 0.0005737080000000061
