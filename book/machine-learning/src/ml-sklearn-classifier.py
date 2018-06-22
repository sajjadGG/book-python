from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics, datasets


dataset = datasets.load_iris()
features_train, features_test, labels_train, labels_test = train_test_split(dataset.data, dataset.target, test_size=0.25, random_state=0)


model = KNeighborsClassifier(n_neighbors=5)
model.fit(features_train, labels_train)
labels_predicted = model.predict(features_test)

accuracy = metrics.accuracy_score(labels_test, labels_predicted)
print(accuracy)
# 0.9736842105263158