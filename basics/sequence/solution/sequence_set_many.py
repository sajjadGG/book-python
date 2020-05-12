result = {5.8, 2.7, 5.1, 1.9}

result.add(5.1)
result.add(3.5)
result.add(1.4)
result.add(0.2)

result.update({5.7, 2.8, 4.1, 1.3})
result.update((6.3, 2.9, 5.6, 1.8))
result.update([6.4, 3.2, 4.5, 1.5])

print(sorted(result))
# [0.2, 1.3, 1.4, 1.5, 1.8, 1.9, 2.7, 2.8, 2.9, 3.2, 3.5, 4.1, 4.5, 5.1, 5.6, 5.7, 5.8, 6.3, 6.4]
