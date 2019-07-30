FILE = r'../data/iris.csv'
X = []
y = []


with open(FILE) as file:
    header, *data = file.readlines()

    for line in data:
        *features, label = line.strip().split(',')
        X.append(tuple(features))
        y.append(label)


print(X)
print(y)
