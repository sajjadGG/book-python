from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split


dataset = datasets.load_iris()
features_train, features_test, labels_train, labels_test = train_test_split(dataset.data, dataset.target, test_size=0.25, random_state=0)


model = KNeighborsClassifier()
model.fit(features_train, labels_train)
model.predict(features_test)

score = model.score(features_test, labels_test)
accuracy = score * 100  # in percent

print(f'Accuracy: {accuracy:.2f}%')
