a = [5.8, 2.7, 5.1, 1.9, 'virginica']
b = [5.1, 3.5, 1.4, 0.2, 'setosa']
c = [5.7, 2.8, 4.1, 1.3, 'versicolor']

a.insert(0, b[4])
b.append(a.pop())
del c[4]

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
