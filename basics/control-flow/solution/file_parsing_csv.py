FILE = r'../data/iris.csv'
features = []
labels = []


with open(FILE) as file:
    header = file.readline()

    for line in file:
        *measurements, species = line.strip().split(',')
        features.append(tuple(measurements))
        labels.append(species)


print(features)
print(labels)
