from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split


dataset = datasets.load_iris()
features_train, features_test, labels_train, labels_test = train_test_split(dataset.data, dataset.target, test_size=0.25, random_state=0)


model = KNeighborsClassifier()
scores = cross_val_score(model, features_train, labels_train, cv=5)
accuracy = scores.mean() * 100  # percent
stdev = scores.std() * 100  # percent

print(f'Accuracy: {accuracy:.2f}% (+/- {stdev:.2f}%)')
