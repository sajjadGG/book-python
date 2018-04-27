python3 -m timeit '"-".join(str(n) for n in range(100))'
# 10000 loops, best of 3: 30.2 usec per loop

python3 -m timeit '"-".join([str(n) for n in range(100)])'
# 10000 loops, best of 3: 27.5 usec per loop

python3 -m timeit '"-".join(map(str, range(100)))'
# 10000 loops, best of 3: 23.2 usec per loop
