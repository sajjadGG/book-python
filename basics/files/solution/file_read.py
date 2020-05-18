FILE = r'../data/iris.csv'
features = []
labels = []


with open(FILE) as file:
    header = file.readline().strip()

    for line in file:
        *measurements, species = line.strip().split(',')
        measurements = tuple(float(x) for x in measurements)

        features.append(measurements)
        labels.append(species)


print(features)
print(labels)
